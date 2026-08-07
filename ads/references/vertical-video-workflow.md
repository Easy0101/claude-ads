# Vertical Video Workflow — Tools, Batch Production, Repurposing

<!-- Updated: 2026-08-07 -->
<!-- Sources: BIGVU, Unstar, Ssemble, Streamlabs, Cutback, OpusClip, Slidy, Digital Applied (2026 research) -->
<!-- Used by: ads-video (Batch mode), creative-strategist agent -->

## Tool Selection (2026)

| Tool | Cost | Best for |
|------|------|----------|
| **CapCut** | Free / Pro $19.99/mo | Default short-form editor: auto captions (100+ langs, word-by-word presets), keyframes, velocity/speed ramping, trend-synced templates, auto-reframe 16:9→9:16 |
| **VN** | Free, no watermark | Best free CapCut escape hatch: multi-track, keyframes, speed curves, LUTs |
| **InShot** | Free / ~$19.99/yr | Fast casual edits, excellent multi-platform resizing |
| **DaVinci Resolve** | Free (Studio $295 once) | Best free pro option: vertical timeline preset, superior color (fixes log/HDR), Speed Warp |
| **Premiere Pro** | $22.99+/mo | Agency/team workflows, Auto Reframe, Speech-to-Text |

CapCut 2026 note: free tier now caps usage; Pro price rose ~130% vs 2025.
VN or Resolve cover most needs free.

### AI tools

| Category | Leader | Notes |
|----------|--------|-------|
| Auto-clipping (long → shorts) | **Opus Clip** (~$15/mo) | Virality score 0-100 per clip, speaker-tracking reframe, auto-post |
| Cheapest clipping for podcasts | **Ssemble** ($7.50/mo) | Per-VIDEO pricing — 50-70% cheaper than per-minute tools on 20min+ sources |
| One-click simplicity | **Klap** | Paste YouTube URL → clips |
| Caption styling | **Submagic** ($12-23/mo) | Viral animated presets + auto b-roll, zooms, SFX |
| AI voiceover | **ElevenLabs** (free 10k credits/mo; Creator ~$22/mo) | Standard for faceless channels; 70+ languages |
| Silence removal | **Timebolt / Descript** | Auto-cut dead air before editing; text-based editing |

Standard faceless pipeline: script → ElevenLabs VO → CapCut/Resolve assembly →
Submagic captions → master export.

## Batch Production System (daily posting)

Batch filming saves ~40% of weekly production time:

| Day | Block |
|-----|-------|
| 1 | Ideation + scripting — write ALL hooks first (see `vertical-video-hooks.md`) |
| 2 | Batch film 7-15 videos in one session — change shirt + angle between takes to simulate different days; target 10 posts → record 12-15 |
| 3-4 | Batch edit in ONE editor, one pass: template to all → auto-caption all → export queue |
| 5 | Schedule everything; log hooks in the content calendar |

**Per-pillar template**: lock caption style, fonts, colors, and intro pattern
once per content pillar; reuse always. A one-page style guide (fonts, colors,
caption style, CTAs, liked/disliked examples) kills most revision cycles when
delegating to an editor.

### File organization

```
/Content/YYYY-MM/
  01_RAW/        # camera dumps: YYYYMMDD_topic_take
  02_SELECTS/    # usable takes only
  03_PROJECTS/   # editor project files
  04_ASSETS/     # music, SFX, b-roll, brand overlays, caption presets
  05_EXPORTS/
    master/      # clean 1080x1920 watermark-free H.264 masters
    tiktok/ reels/ shorts/   # per-platform variants if they differ
  06_POSTED/     # archive + performance notes
```

Naming: `2026-08-07_hook-keyword_v2_MASTER.mp4` (date + topic + version + role).

## Cross-Platform Repurposing

**Golden rule: one clean watermark-free master, uploaded natively in each app.**
Never "save from TikTok, repost to Reels" — Instagram suppresses
TikTok-watermarked Reels (no Explore; ~300% engagement gap vs clean uploads),
YouTube deprioritizes/demonetizes watermarked Shorts, TikTok limits rival marks.

Same footage, different packaging per platform:

| Platform | Adjust |
|----------|--------|
| **TikTok** | Trend-native: trending sound, raw/lo-fi OK, casual caption + 3-5 hashtags, hook in first 1-1.5s, 21-38s cut. Pure watch-time discovery (300-500-user test pools; followers irrelevant) |
| **Reels** | More polished; b-roll open outperforms talking-head open; loopable ending (auto-replay doubles watch time); pick licensed audio natively in-app; distribution starts from followers — sends + saves weigh most |
| **Shorts** | Search-first: keyword title + description (Shorts keep search life for weeks-months); drives subscriber conversion; can link long-form |
| **Facebook Reels** | Crosspost via Meta tools; older audience; keep ≤90s |

Change per platform: first 1.5s of the hook, on-screen text style,
caption/hashtags, title (Shorts), and audio (licensing differs per app —
trend sounds are never licensed for ads).

Scheduling tools that upload natively via official APIs (count as native):
Repurpose.io, Metricool, Buffer, Later, Opus Clip auto-post.

## Weekly Feedback Loop

1. Pull per-video metrics: 3s hold, avg % watched, completion, saves, shares
2. Compute the account's median watch time
3. **Kill** formats below median for 2 consecutive weeks
4. **Double down** on the top 20% (make direct sequels/variations)
5. Feed one learning into next week's scripts (single-variable changes)

## Posting Cadence (2026)

- TikTok 2-5x/week · Reels 3-5x/week · Shorts 3-5x/week
- Consistency beats bursts: 3x/week sustained for 6 months outperforms
  7x/week for 2 weeks then silence
- Post when your audience is active; native schedulers are fine everywhere
