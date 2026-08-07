---
name: ads-video
description: >
  Viral vertical video editing and optimization for TikTok, Instagram Reels,
  and YouTube Shorts. Covers hook engineering, retention editing, captions,
  audio strategy, safe zones, export settings, and high-volume posting
  workflows. Use when user says "vertical video", "viral video", "TikTok
  video", "Reels", "Shorts", "video editing", "hooks", "retention", or wants
  to plan, script, edit, audit, or batch-produce short-form video content.
---

# Viral Vertical Video Editing & Optimization

Plan, script, edit, and audit short-form vertical video (9:16) engineered for
retention and shareability across TikTok, Instagram Reels, and YouTube Shorts.

## Modes

Detect intent and run the matching mode:

| Mode | Trigger | Output |
|------|---------|--------|
| **Script** | "write/plan a video", topic given | Shot-by-shot script with hook variants |
| **Edit Plan** | Raw footage or rough cut described | Timestamped edit decision list |
| **Audit** | Existing video/metrics shared | Retention diagnosis + fix list |
| **Batch** | "posting daily", "many videos" | Production system + content calendar |
| **Validate** | Video file available locally | Run `scripts/check_video.py` |

## Process

1. Collect context: niche/topic, target platform(s), goal (followers, views,
   traffic, sales), current metrics if any (avg watch time, retention curve,
   completion %), editing tool used (CapCut, Premiere, DaVinci, phone-only)
2. Read `ads/references/vertical-video-hooks.md` for hook formulas
3. Read `ads/references/vertical-video-editing.md` for retention techniques
4. Read `ads/references/vertical-video-specs.md` for platform specs and export
5. Read `ads/references/vertical-video-workflow.md` for tools and batch systems
6. Execute the detected mode
7. Always end with: 3 hook variants to test + one measurable retention target

## The Retention Hierarchy (edit priority order)

Fix in this order — each layer is worthless without the one above it:

1. **Hook (0-3s)** — decides ~80% of the video's fate; >70% of viewers must
   survive the first 3 seconds
2. **Pacing** — a visual or informational change every 2-4 seconds; no dead air
3. **Payoff** — deliver what the hook promised, hold the best moment for the end
4. **Loop** — ending that feeds back into the start drives rewatches
5. **Polish** — captions, SFX, color; matters only after 1-4 work

## Script Mode

Structure every script on the proven skeleton:

```
0-1s   VISUAL HOOK    Motion, unexpected frame, or mid-action start
0-3s   VERBAL HOOK    One line that creates an open question
3-8s   RE-HOOK        Raise stakes / context in one sentence, cut the intro
8-Ns   BODY           One idea per 3-5s beat; b-roll or angle change per beat
last 2s PAYOFF+LOOP   Resolve the open question; final frame matches frame 1
```

Rules:
- Never open with "Hi guys", intros, or logos — start mid-action
- Write the hook LAST, write 5+ variants, pick 3 to test
- One video = one idea; split multi-idea scripts into a series
- Script for sound-off too: key words must appear as on-screen text
- CTA: engagement-bait CTAs ("follow for part 2") only when a part 2 exists;
  otherwise ask a question that generates comments

## Audit Mode

Diagnose from the retention curve (or estimate from avg watch time):

| Symptom | Diagnosis | Fix |
|---------|-----------|-----|
| Cliff drop 0-3s (>40% loss) | Weak hook | New hook variants; start mid-action |
| Steady bleed 3s+ | Pacing too slow | Cut 20-30% of runtime; beat every 3s |
| Drop at a specific timestamp | Dead segment | Delete or replace that beat |
| Low completion, good hold | Too long | Trim to sweet spot for the platform |
| Good retention, low reach | Weak share/save triggers | Add save-worthy value or shareable emotion |
| Good views, no follows | No serialization | Series format, consistent visual identity |

Score the video with the 12-point checklist in
`ads/references/vertical-video-editing.md` and report PASS/FAIL per item.

## Quality Gates

Hard rules — never violate:
- 9:16 (1080×1920) only; never letterboxed 16:9 in a vertical frame
- Hook visible AND audible within 3 seconds — no exceptions
- Captions always on, inside safe zones, never covered by platform UI
- Never post with another platform's watermark (TikTok logo on Reels =
  suppressed distribution)
- Sound-on required for TikTok; design for sound-off comprehension everywhere
- Export per-platform settings from `vertical-video-specs.md` — never one
  file re-uploaded everywhere without checking safe zones
- Trend audio: use for reach on TikTok/Reels; on ads swap to licensed/commercial
  audio (trend sounds are NOT licensed for ad use)

## Batch Mode (high-volume creators)

For users posting daily/near-daily, deliver a production system:

1. **Pillars**: 3-4 repeatable content formats (series) mapped to goals
2. **Batching**: record 1 day/week (5-10 videos), edit in a second block
3. **Template**: per-pillar CapCut/editor template — caption style, fonts,
   colors, intro pattern locked once, reused always
4. **Calendar**: 7-day grid with pillar, hook, status per slot
5. **Feedback loop**: weekly review — kill formats below the account's median
   watch time, double down on the top 20%
6. **Repurposing map**: native re-upload per platform with per-platform tweaks
   (see `vertical-video-workflow.md`)

## Output

### Deliverables by mode
- Script mode → `VIDEO-SCRIPT.md` — shot list, 3 hook variants, caption text
- Audit mode → `VIDEO-AUDIT-REPORT.md` — retention diagnosis, prioritized fixes
- Batch mode → `VIDEO-PRODUCTION-SYSTEM.md` — pillars, calendar, templates
- Validate mode → JSON report from `scripts/check_video.py`

### Always include
- 3 testable hook variants (never one)
- One measurable target (e.g. "3-second hold rate >75%", "completion >40%")
- Next experiment to run (single variable)
