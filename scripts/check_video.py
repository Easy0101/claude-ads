#!/usr/bin/env python3
"""
Validate a vertical video file against short-form platform specifications.

Uses ffprobe (bundled with ffmpeg) to inspect resolution, aspect ratio,
duration, fps, codecs, bitrate, and audio presence, then scores the file
against TikTok, Instagram Reels, and YouTube Shorts upload requirements
and viral best-practice thresholds used by the ads-video sub-skill.

Usage:
    python check_video.py video.mp4
    python check_video.py video.mp4 --platform tiktok
    python check_video.py video.mp4 --json

Requires: ffmpeg/ffprobe on PATH (https://ffmpeg.org).
"""

import argparse
import json
import shutil
import subprocess
import sys

# Upload limits and best-practice targets per platform (2026).
PLATFORM_SPECS = {
    "tiktok": {
        "max_duration": 600,
        "best_duration": (24, 38),
        "max_file_mb": 500,
        "min_bitrate_kbps": 6000,
    },
    "reels": {
        "max_duration": 180,
        "best_duration": (7, 30),
        "max_file_mb": 4096,
        "min_bitrate_kbps": 5000,
    },
    "shorts": {
        "max_duration": 180,
        "best_duration": (20, 45),
        "max_file_mb": 2048,
        "min_bitrate_kbps": 8000,
    },
}


def ffprobe(path: str) -> dict:
    """Run ffprobe and return parsed stream/format metadata."""
    cmd = [
        "ffprobe", "-v", "error", "-print_format", "json",
        "-show_format", "-show_streams", path,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"ffprobe failed: {result.stderr.strip()}")
    return json.loads(result.stdout)


def parse_fps(rate: str) -> float:
    """Convert ffprobe rational frame rate ('30000/1001') to float."""
    try:
        num, _, den = rate.partition("/")
        return round(float(num) / float(den or 1), 2)
    except (ValueError, ZeroDivisionError):
        return 0.0


def analyze(path: str, platform: str) -> dict:
    """Inspect the video and evaluate it against platform specs."""
    meta = ffprobe(path)
    video = next((s for s in meta["streams"] if s["codec_type"] == "video"), None)
    audio = next((s for s in meta["streams"] if s["codec_type"] == "audio"), None)
    if video is None:
        raise RuntimeError("no video stream found")

    fmt = meta.get("format", {})
    width = int(video.get("width", 0))
    height = int(video.get("height", 0))
    duration = float(fmt.get("duration", 0))
    size_mb = round(int(fmt.get("size", 0)) / (1024 * 1024), 1)
    bitrate_kbps = round(int(fmt.get("bit_rate", 0)) / 1000)
    fps = parse_fps(video.get("avg_frame_rate", "0/1"))
    spec = PLATFORM_SPECS[platform]

    checks = []

    def check(check_id, label, passed, detail, severity="high"):
        checks.append({
            "id": check_id, "label": label, "pass": bool(passed),
            "detail": detail, "severity": severity,
        })

    ratio = round(width / height, 4) if height else 0
    check("V01", "Vertical 9:16 aspect ratio", abs(ratio - 9 / 16) < 0.01,
          f"{width}x{height} (ratio {ratio}, target 0.5625)", "critical")
    check("V02", "Resolution >= 1080x1920", width >= 1080 and height >= 1920,
          f"{width}x{height}")
    check("V03", "H.264/H.265 video codec",
          video.get("codec_name") in ("h264", "hevc"),
          f"codec: {video.get('codec_name')}")
    check("V04", "Frame rate 24-60 fps", 23.9 <= fps <= 60.1, f"{fps} fps")
    check("V05", "Audio track present (sound-on platforms)", audio is not None,
          f"audio codec: {audio.get('codec_name') if audio else 'MISSING'}",
          "critical")
    check("V06", "AAC audio codec",
          audio is not None and audio.get("codec_name") == "aac",
          f"codec: {audio.get('codec_name') if audio else 'none'}", "medium")
    check("V07", f"Duration <= {spec['max_duration']}s upload limit",
          duration <= spec["max_duration"], f"{round(duration, 1)}s")
    lo, hi = spec["best_duration"]
    check("V08", f"Duration in viral sweet spot ({lo}-{hi}s)",
          lo <= duration <= hi, f"{round(duration, 1)}s", "medium")
    check("V09", f"File size <= {spec['max_file_mb']}MB",
          size_mb <= spec["max_file_mb"], f"{size_mb}MB")
    check("V10", f"Bitrate >= {spec['min_bitrate_kbps']}kbps (survives recompression)",
          bitrate_kbps >= spec["min_bitrate_kbps"], f"{bitrate_kbps}kbps", "medium")
    check("V11", "SDR color (HDR washes out on non-HDR screens)",
          video.get("color_transfer", "bt709") not in ("smpte2084", "arib-std-b67"),
          f"transfer: {video.get('color_transfer', 'unknown')}", "medium")

    weights = {"critical": 3, "high": 2, "medium": 1}
    total = sum(weights[c["severity"]] for c in checks)
    earned = sum(weights[c["severity"]] for c in checks if c["pass"])

    return {
        "file": path,
        "platform": platform,
        "properties": {
            "width": width, "height": height, "duration_s": round(duration, 1),
            "fps": fps, "size_mb": size_mb, "bitrate_kbps": bitrate_kbps,
            "video_codec": video.get("codec_name"),
            "audio_codec": audio.get("codec_name") if audio else None,
        },
        "score": round(100 * earned / total),
        "checks": checks,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Validate vertical video against short-form platform specs")
    parser.add_argument("video", help="Path to video file")
    parser.add_argument("--platform", choices=sorted(PLATFORM_SPECS),
                        default="tiktok", help="Target platform (default: tiktok)")
    parser.add_argument("--json", action="store_true", help="JSON output only")
    args = parser.parse_args()

    if shutil.which("ffprobe") is None:
        print(json.dumps({"error": "ffprobe not found — install ffmpeg (https://ffmpeg.org)"}))
        sys.exit(1)

    try:
        report = analyze(args.video, args.platform)
    except (RuntimeError, OSError, json.JSONDecodeError, KeyError) as exc:
        print(json.dumps({"error": str(exc)}))
        sys.exit(1)

    if args.json:
        print(json.dumps(report, indent=2))
        return

    props = report["properties"]
    print(f"\n{report['file']} — {report['platform']} — Score: {report['score']}/100")
    print(f"{props['width']}x{props['height']} @ {props['fps']}fps, "
          f"{props['duration_s']}s, {props['size_mb']}MB, {props['bitrate_kbps']}kbps\n")
    for c in report["checks"]:
        mark = "PASS" if c["pass"] else "FAIL"
        print(f"  [{mark}] {c['id']} {c['label']} — {c['detail']}")
    print()


if __name__ == "__main__":
    main()
