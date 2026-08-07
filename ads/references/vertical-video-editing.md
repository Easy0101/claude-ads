# Vertical Video Editing — Retention Playbook

<!-- Updated: 2026-08-07 -->
<!-- Sources: Retensis, Strategia-X, CapCut, Kapwing, Krotos, Socialync, Later, Metricool (2026 research) -->
<!-- Used by: ads-video (all modes), audit-creative agent -->

## Purpose

Editing techniques that maximize watch time, completion, and rewatch — the
three heaviest algorithm signals in 2026. Applies after the hook works (see
`vertical-video-hooks.md`).

## Pacing Rules

| Rule | Cadence |
|------|---------|
| Meaningful visual change (cut, zoom, text, b-roll, graphic) | Every **2-3 seconds** |
| Bigger "beat change" (location, concept, tone) | Every **5-8 seconds** |
| B-roll cutaway in talking-head content | Every **2-4 seconds**; never >5s static |
| Micro open-loop tease ("but here's where it gets weird") | Every ~10 seconds |
| Jump cuts | Remove ALL dead air, breaths, fillers — any silence >0.5s is a swipe opportunity |

High-energy DTC ads run up to 5 cuts/second; organic content needs a *pattern
refresh* every 2-3s, not necessarily a hard cut.

## Zoom Techniques (talking head)

- **Progressive zoom**: continuous slow zoom medium (~60% frame) → close-up
  (80-85%) at **1.5-2% per second** — imperceptible, kills static-frame
  fatigue. Single most effective retention technique for talking-head video.
- **Punch-ins**: hard 10-15% scale jumps on emphasis words — replaces a second
  camera angle. Shoot 4K to allow 10-30% punch-in without quality loss.
- Alternate: progressive zoom between punch-ins, reset on beat changes.

## Loop Engineering (rewatch = heaviest multiplier)

Looped videos can exceed 100% average-percentage-viewed; rewatch rate
**>15-20%** is a strong push signal.

1. **Record the ending first**, continue into the opening in the same take
2. In the edit, move the ending clip to the end — last frame connects to first
3. Cut the final line mid-word or mid-motion so it flows into the opening
4. Verify: watch the video twice in a row — the seam should be invisible

## Open Loops / Curiosity Gaps

- Promise in the hook, payoff in the final 20% ("…and the third one is the
  reason I quit my job")
- Number the listicle DOWN toward the teased best item, or hold #1 for last
- Keep the knowledge gap open the entire video; close it only at the payoff

## Retention Benchmarks (completion rate by length, TikTok)

| Length | Avg completion | Verdict |
|--------|---------------|---------|
| <15s | 92% | Loop-friendly, low follow conversion |
| 16-30s | 84% | Viral sweet spot (24-38s TikTok) |
| 31-60s | 68% | Needs mid-video re-hooks |

- **~75%+ completion** triggers significant algorithmic push
- % watched beats total seconds: a 30s video at 80% beats a 60s video at 40%
- Right length = shortest cut that fully delivers the payoff

## Captions (85% watch muted)

- ~85% of social video is watched on mute; captions raise completion up to 80%
  and are a confirmed Reels ranking factor
- **Style**: word-by-word / karaoke — 1-4 words on screen, active word pops
  (~110% scale) or changes color; never full sentences
- **Fonts**: bold high-x-height sans — Inter, Montserrat, Proxima Nova
  (running captions); Bebas Neue / Anton (hook words only)
- **Legibility**: heavy weight + black outline or shadow/box; ~5-8% of frame
  height per line
- **Accent color** on keywords: yellow/green are the de facto standards
- **Position**: center or slightly below center — never bottom 400px (UI),
  never right edge (action buttons)

## Audio Mix

| Element | Level |
|---------|-------|
| Voiceover | 100% — recorded close, denoised, normalized (~-14 LUFS) |
| Background/trending music | ~10-20% under VO; duck 3-6 dB under speech with ~1s recovery |
| SFX | ≥6 dB below voice |

Sound design vocabulary:
- **Whoosh** on transitions/punch-ins (signals content change, adds momentum)
- **Bass hit** on reveals — max 1-2 per video
- **Pop** on text reveals and listicle bullets
- Cut ON the music beat — on-beat cuts feel invisible, off-beat feels jarring

Trending audio: use within the **first 24h of a sound's rise** (~3x views vs
post-peak). Caveat: a voiceover layered over a trending track may prevent the
platform from associating the video with the trend — pick one priority.

## Structures That Work

1. **Hook → Context → Payoff → Loop** — the 4-beat retention spine
2. **Hook (0-3s) → Value drop (4-15s) → Story/payoff (16-45s) → CTA (last 5s)**
   — value BEFORE any ask; a hook with no payoff reads as bait
3. **Listicle** with on-screen counters (pop SFX per item), best item last
4. **PAS** — Problem → Agitate → Solution
5. **Before → After → Bridge** — show result, flash back, explain

## 12-Point Retention Edit Checklist (Audit mode scoring)

| # | Check |
|---|-------|
| R1 | Hook passes H1-H6 (see `vertical-video-hooks.md`) |
| R2 | First pattern interrupt before second 5-6 |
| R3 | Visual change every ≤3s (count them) |
| R4 | Zero dead air / silences >0.5s |
| R5 | Talking head never static >5s (zoom, punch-in, or b-roll) |
| R6 | Word-by-word captions, styled, inside safe zone |
| R7 | Audio mixed: VO dominant, music ducked, SFX on transitions |
| R8 | One idea only — no detours |
| R9 | Payoff delivers the hook's promise |
| R10 | Ending loops to opening OR hard-stops after payoff (no outro rambling) |
| R11 | Length = shortest cut that delivers payoff (in platform sweet spot) |
| R12 | CTA earns its place (part 2 exists, or question that drives comments) |

Score: 10-12 PASS = ship it · 7-9 = fix FAILs, re-cut · <7 = re-edit from raw

## Algorithm Signals Reference (2026)

| Platform | Heaviest signals | Cadence |
|----------|-----------------|---------|
| TikTok | Completion + watch time, rewatches, **DM shares (~3x likes)**, saves | 2-5x/week |
| Reels | Watch time incl. replays, likes/reach, **sends/reach (3-5x likes)** | 3-5x/week |
| Shorts | First-2s swipe-away, completion, rewatch | 3-5x/week |

Consistency beats bursts: 3x/week for 6 months outperforms 7x/week for 2
weeks then silence. Watermarked cross-posts are demoted everywhere.
