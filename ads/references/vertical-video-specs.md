# Vertical Video Specs — TikTok / Reels / Shorts (2026)

<!-- Updated: 2026-08-07 -->
<!-- Sources: Fliki, GhostShorts, HeyOrca, vidIQ, Kreatli, Postplanify, Meta Engineering (2026 research) -->
<!-- Used by: ads-video (Validate + Edit Plan modes), scripts/check_video.py, format-adapter agent -->

## Master Export Spec (works everywhere)

**1080×1920 px, 9:16, MP4 (H.264 High profile + AAC 48 kHz), 30 fps,
10-15 Mbps VBR (or CRF 17-18), Rec.709/SDR, 4:2:0 8-bit, keyframe every 2s,
`-movflags +faststart`.** Export one clean watermark-free master, upload
natively to each platform.

## Per-Platform Limits

| Spec | TikTok | Instagram Reels | YouTube Shorts |
|------|--------|-----------------|----------------|
| Resolution | 1080×1920 | 1080×1920 | 1080×1920 (4K accepted, played at 1080p) |
| Duration | 3s-10min app (60min via Studio) | 3s-20min (>3min = limited non-follower reach) | max 3min (180s) |
| Viral sweet spot | **21-38s** (≥60s for Creator Rewards) | **7-30s**, loopable ending | **20-45s** (50-60s = highest watch-through) |
| File size | 287MB iOS / 72MB Android app; 4GB web | 4GB (keep <50MB — avoids harsher compression tier) | 256GB |
| Bitrate floor | ~516 kbps min; upload 10-15 Mbps | 3,500 kbps min; upload 10-15 Mbps | 8 Mbps @30fps / 12 @60fps; upload ≥10 |
| FPS | 23.976-60 | Normalized to 30 — **export 30fps** | 24-60 |
| Cover | 1080×1920; grid crops to ~3:4 center | 1080×1920; key elements inside central 1080×1080 square | Frame select or 1080×1920 upload |
| Quality toggle | "Allow high-quality uploads" ON | "Upload at highest quality" ON | n/a |

Platforms serve back at ~2-4 Mbps — the high-bitrate upload exists so only ONE
compression generation is added. Judge final quality 1-24h after posting (the
first minutes serve a fast low-quality rendition).

## Safe Zones (1080×1920 canvas — keep clear)

| Margin | TikTok | Reels | Shorts |
|--------|--------|-------|--------|
| Top | 130-150px | 210-250px | 250-290px |
| Bottom | ~484px (caption/handle/sound) | 320-420px | 250-320px |
| Right | 140-180px (action stack) | 110-140px | 120-140px |
| Left | 44-60px | ~60px | 48-60px |

- **Universal safe box: ~900×1290px, upper-center biased** — content inside is
  safe on all three platforms
- Treat the bottom ~420px and right ~150px as dead zones everywhere
- TikTok ADS official zone is stricter: top 130 / bottom 484 / left 44 / right 140
- UI margins drift several times a year — treat these as minimums, not exact

## Quality-Loss Prevention

1. **Never re-export compressed files** — compounding generations = mush
2. **Never upload 4K to TikTok/IG** — their downscale adds artifacts (4K only
   benefits YouTube)
3. **HDR washout (#1 modern complaint)**: iPhone records HLG/Dolby Vision
   10-bit by default; platform HDR→SDR tonemap looks gray and flat. Fix:
   iPhone Settings → Camera → Record Video → **HDR Video OFF**, or tonemap to
   Rec.709 before export. Never export Rec.2020/HLG to TikTok
4. **Noise kills bitrate**: low-light sensor noise eats the platform's bitrate
   budget. Light well; denoise before export
5. Upload on Wi-Fi (some apps compress harder on cellular)

## FFmpeg Recipes

Baseline flags for all commands:
```
-c:v libx264 -profile:v high -level 4.2 -pix_fmt yuv420p -crf 18 -preset slow \
-g 60 -r 30 -c:a aac -b:a 320k -ar 48000 -movflags +faststart
```

**Center-crop 16:9 → 9:16:**
```bash
ffmpeg -i in.mp4 -vf "crop=ih*9/16:ih,scale=1080:1920" [baseline flags] out.mp4
# subject off-center: crop=ih*9/16:ih:(iw-ih*9/16)*0.3:0
```

**Fit 16:9 inside 9:16 with blurred background:**
```bash
ffmpeg -i in.mp4 -filter_complex \
"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=20:5[bg];\
 [0:v]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2" [baseline flags] out.mp4
```

**Burn TikTok-style captions from .srt:**
```bash
ffmpeg -i in.mp4 -vf "subtitles=subs.srt:force_style='FontName=Montserrat ExtraBold,\
FontSize=15,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,Outline=2,Bold=1,\
Alignment=2,MarginV=90'" [baseline flags] out.mp4
# MarginV 90-110 clears bottom platform UI
```

**Tonemap HDR (iPhone) → SDR Rec.709:**
```bash
ffmpeg -i hdr.mov -vf "zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,\
tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p" [baseline flags] sdr.mp4
```

**Final master (normalize + strip metadata):**
```bash
ffmpeg -i edit.mov -vf "scale=1080:1920:flags=lanczos,fps=30,format=yuv420p" \
  -c:v libx264 -profile:v high -crf 18 -preset slow -g 60 \
  -colorspace bt709 -color_primaries bt709 -color_trc bt709 \
  -c:a aac -b:a 320k -ar 48000 -map_metadata -1 -movflags +faststart MASTER.mp4
```

**Loudness-normalize to -14 LUFS:**
```bash
ffmpeg -i in.mp4 -af "loudnorm=I=-14:TP=-1.5:LRA=11" -c:v copy -c:a aac -b:a 320k out.mp4
```

## Validation

Run `scripts/check_video.py <file> --platform tiktok|reels|shorts --json` to
score a local file against these specs (requires ffprobe on PATH).
