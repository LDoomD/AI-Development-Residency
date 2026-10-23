# EXAMPLES-Mode Tooling Search — Open Source Candidates

> **RESEARCH TIER.** Date: 2026-08-10.
> Scope: find open-source tooling for the **EXAMPLES mode gap** — shuffled, high-volume
> recognition practice (interval/chord ear training, listening comprehension, synthesis
> sound recognition, UX pattern recognition, dog-behavior recognition, ad/marketing
> pattern recognition, comedy timing judgment). Explicitly **not** re-litigating Anki,
> Gemini Notebook, or Obsidian as the base stack — those are locked (`DECISIONS.md` §1, §8).
> Every repo below was checked live via `curl`/GitHub API for stars, license, and last-push
> date, not taken from search-result prose. Two AnkiWeb add-on pages returned JavaScript
> shells and could not be scraped directly — their descriptions below come from Anki
> Forums / search-result text, **flagged UNVERIFIED** where the source page itself
> couldn't be read.

---

## The gap, restated

Nine of twenty subjects need **EXAMPLES**: volume + deliberate shuffle + recognition
feedback, not single-item spaced recall (Anki's job) and not "read about it" (MAP's job).
Concretely: music ear training (intervals/chords/FM bell tones), Italian/Spanish
listening comprehension, synthesis sound recognition (subtractive/additive/wavetable/FM),
comedy/charisma timing, UX/UI pattern recognition, dog training/psychology pattern
recognition, Meta Ads pattern recognition, agentic-marketing pattern recognition.
Nothing in the locked stack treats "shuffled recognition drilling" as a first-class mode.

---

## Candidates by search angle

### 1. Ear-training tools (interval / chord recognition)

| Repo | What it does | Last push | Stars | License | Fit |
|---|---|---|---|---|---|
| [birdears/birdears](https://github.com/birdears/birdears) | CLI functional ear trainer — plays a tonal context then random scale degrees/intervals/chords, terminal-based | 2026-02-16 | 77 | AGPL-3.0 | **Best-maintained candidate.** Actively pushed this year. CLI-only — no GUI, would need wrapping for casual use, but the drill loop (context → random probe → answer → next) is exactly the EXAMPLES shape |
| [abeage1/earwise](https://github.com/abeage1/earwise) | Static HTML/JS interval + chord (maj/min/dim/aug/dom7/maj7/min7 + inversions) trainer, adaptive, no backend | 2026-02-27 | 0 | **None declared** | Most recently pushed of all candidates, zero-install (single HTML file), but 0 stars/no community — likely a personal project. No LICENSE file = technically all-rights-reserved by default; **do not redistribute/fork without asking**, though running the static file locally is low-risk |
| [DimitriosLisenko/fet](https://github.com/DimitriosLisenko/fet) | "Functional Ear Trainer" — key established via chord progression, then random scale-degree probes | 2024-05-16 | 5 | MIT | Same functional-ear-training method as birdears; smaller, less active |
| [pianosnake/ear-training-buddy](https://github.com/pianosnake/ear-training-buddy) | Web app, real piano samples (University of Iowa, public domain), random or diatonic interval/chord playback | 2018-11-29 | 5 | **None declared** | Stale (7+ years). Real piano timbre is a plus over synth tones but staleness is a real risk |
| [mia-riezebos/eartip](https://github.com/mia-riezebos/eartip) | PureData (Pd) patch for interval/chord/key/tempo training | 2020-05-19 | 1 | MIT | Requires PureData installed — friction. Stale. Not recommended over the above |
| [tomcookedeveloper/solfetta](https://github.com/tomcookedeveloper/solfetta) | Small web app for practicing playing/singing by ear on phone/tablet | 2023-10-21 | 6 | MIT | Different focus (production/singing practice, not pure recognition) — lower fit |
| [DodecaCourse/DodecaCourse](https://github.com/DodecaCourse/DodecaCourse) | Full CC-licensed *course* in functional ear training (not just a drill tool) | 2024-09-29 | 5 | GPL-3.0 | Curriculum, not a drill engine — useful as **content**, not as the tool |

**Read:** `birdears` is the strongest single pick if a CLI is acceptable (it very likely
is, given the rest of this system already lives in Claude Code / terminal workflows).
`earwise` is the best if a zero-friction browser tool is preferred, with the caveat that
it has no visible community and no declared license.

### 2. Language listening-drill tools (not vocabulary SRS)

| Repo | What it does | Last push | Stars | License | Fit |
|---|---|---|---|---|---|
| [omnilingo/omnilingo](https://github.com/omnilingo/omnilingo) | Listening-first drills built on Mozilla Common Voice audio: fill-in-blank, drag-and-drop sentence building, multiple choice, audio word-spotting, batches of 5 random tasks per session | last release activity noted, 43 open issues (moderate ongoing interest, not fast-moving) | 70 | AGPL-3.0 | **Closest direct match to "shuffled listening comprehension" for a whole language**, not single vocab items. Supports any Common Voice language — includes Italian and Spanish. Requires downloading a Common Voice corpus and running a Flask app locally — real setup effort, not install-and-go |
| [kgurniak91/yall-mp](https://github.com/kgurniak91/yall-mp) ("Yet Another Language Learning Media Player") | Media player built for sentence mining, shadowing, and listening-comprehension training against your own audio/video/subtitle files | 2026-04-26 | 33 | GPL-3.0 | Actively maintained (pushed this year). Works against **your own content** (podcasts, shows) rather than a fixed corpus — good fit if Italian/Spanish listening material is self-sourced audio/video rather than a dataset |
| [Dthurow/SpeechShadowing](https://github.com/Dthurow/SpeechShadowing) | Python GUI for shadowing practice: play native-speaker clip, record yourself, play back both, auto-splits long audio (podcasts) into sentence-level clips by silence detection | 2020-06-25 | 16 | MIT | Good fit for the REPS-adjacent "speaking" side, not pure recognition — flagged for reference even though it's slightly outside EXAMPLES proper. Stale (5+ years, no recent commits) |
| [5uru/Discute](https://github.com/5uru/Discute) | Open-source app for speaking practice in a target language | 2025-06-20 | 80 | Apache-2.0 | Speaking-focused (REPS), not listening recognition — lower fit for this specific gap |
| [Kuuuube/minimal-pairs](https://github.com/Kuuuube/minimal-pairs) | Minimal-pairs listening discrimination test | 2025-11-16 | 16 | GPL-3.0 | **Japanese-specific** (a backup of a Japanese "コツ" test) — not directly reusable for Italian/Spanish without rebuilding the pair database. Cite as a pattern (minimal-pair discrimination testing), not a ready tool |

**Read:** `omnilingo` is the most direct hit but has real setup cost (corpus download,
local Flask server) — worth trying once before committing. `yall-mp` is the better fit
if the actual listening material will be self-chosen podcasts/shows rather than a
crowdsourced sentence corpus, which is plausible for adult Italian/Spanish study.

### 3. General "shuffled example quiz" engine (audio/image/video, pure recognition, reusable across subjects)

**This is the important question — a single reusable engine beats nine bespoke tools.**
Direct web search for "flashcard app, no spaced repetition, random order, image/audio
recognition, generic" turned up **no purpose-built open-source project matching that
description.** Every general flashcard OSS project found (Echo, KWordQuiz, Yokatta, etc.)
is built around SM-2/SRS scheduling as the core loop, not shuffled-recognition-only
practice. This confirms the gap is real, not just unsearched.

The closest thing to a generic reusable engine is **Anki itself, repurposed** — see
section below. No third-party tool was found that does this more directly than Anki's
own filtered-deck feature.

### 4. Sound-design / synthesis ear-training tools (subtractive/FM/wavetable)

**Confirmed: no open-source tool exists for this.** Searches for "ear training" +
"wavetable"/"FM"/"subtractive" + "site:github.com"-equivalent queries returned only:

- **Syntorial** — the commercial, closed-source, paid ($) product that does exactly
  this (train your ear to hear a sound and reproduce it on a subtractive/wavetable
  synth). Explicitly **not open source**, cannot be adopted under the "open-source
  research" scope of this brief, listed here only to confirm the niche is real and
  someone already found it commercially viable.
- Research-grade repos ([spiegelib/spiegelib](https://github.com/spiegelib/spiegelib)
  MIT, 61 stars, last push 2023-07-06; [aisynth/diffmoog](https://github.com/aisynth/diffmoog)
  MIT, 114 stars, last push 2024-06-18; [jorshi/synthml](https://github.com/jorshi/synthml),
  no license, last push 2021) — these are **automatic synthesizer programming /
  parameter-inference ML research code**, built for training neural nets to match
  synth patches, not for training a human ear. Wrong audience entirely; not
  adaptable without building a UI, a drill loop, and a grading mechanism from
  scratch, i.e. building a new app, not adopting one.

**Verdict: real gap, no ready tool.** This is the one area of the nine where "no
good single tool exists" is the honest answer, not a research gap on my end.

### 5. Can Anki's own add-on ecosystem cover this instead of adopting a new tool?

**This is the single most important finding, since it reuses the locked stack.**

**Yes — Anki can do this natively, no add-on required, via Filtered Decks.**
Verified against the official Anki manual (`docs.ankiweb.net/filtered-decks.html`):

- Filtered decks support **`Random`: "Randomize the order of all cards that match the
  filter criteria (use no set order)"** — the shuffle requirement, built in.
- Filtered decks support turning **"Reschedule cards based on my answers" OFF**, which
  puts cards into **preview mode**: *"cards are shown in a simple 'preview mode', and
  when they are returned to their original deck, they are returned exactly as they
  started."* Answering does not touch FSRS stability/difficulty/interval at all.

**Combined, this is precisely EXAMPLES mode: pull a filtered subset (e.g. all cards
tagged `music::intervals`), shuffle them, drill them, and the drilling has zero effect
on the spaced-recall schedule of the underlying cards.** No plugin needed — this is a
core Anki feature that predates add-ons entirely, and it works with audio/image/video
already embedded in card fields exactly as DRILL-mode cards would.

**One added-value add-on, if more variety than plain Q/A is wanted:** the AnkiWeb-listed
add-on **"Interactive and Randomized Cards"** (ankiweb.net/shared/info/171015247)
ships note-type templates for Match Pairs, Shuffled Cloze, Click Words, Sort Cards,
Randomized Basic/Cloze, etc. — media-capable (audio/image/text, pipe-delimited option
lists), explicitly pitched at "concepts that are hard to differentiate." **UNVERIFIED
in detail** — the AnkiWeb page is a JavaScript SPA that couldn't be scraped directly for
this brief, so maintenance status, exact author, and source-code location are taken from
Anki Forums search-result text only, not read first-hand. Confirm directly in-app
before relying on it; it is optional polish on top of the filtered-deck mechanism, not
a requirement — filtered decks alone already solve the core need.

**What was explicitly checked and ruled out:** the "No Scheduler – Review Order by
Long-term Knowledge Gain" add-on (`nekomaki/anki-no-scheduler`, GitHub, last push
2025-12-28, no declared license) reorders the *existing* FSRS queue by expected
knowledge gain — it is still spaced recall, just re-prioritized. **Not a fit** for
EXAMPLES mode; it optimizes DRILL, not shuffled recognition practice.

---

## Recommended approach

**Use Anki filtered decks (Random order + Reschedule OFF) as the default EXAMPLES
engine for every subject where the recognition material is audio/image and can live
on a card face** — this is zero new tooling, reuses the already-decided stack exactly
as the "reuse before adopt" instruction asked, and is a documented, stable, core Anki
feature (not an add-on someone could abandon).

This covers, directly, with just card content changes and a tag-based filtered deck:

- Music theory ear training (intervals/chords/FM bell tones as audio-embedded cards)
- Italian/Spanish listening comprehension, at the clip-recognition level (a Spanish
  audio clip → meaning/word recognition, shuffled) — **though this does not replace
  a corpus-driven, sentence-generation tool like `omnilingo` for open-ended listening
  practice; Anki cards work for "recognize this clip" not "produce/complete this
  sentence from audio."** If listening-comprehension work outgrows recognition-only
  cards, `omnilingo` (self-hosted, AGPL, supports Italian and Spanish via Common Voice)
  or `yall-mp` (self-content shadowing/listening player, actively maintained) are the
  two next steps, in that order of directness.
- UX/UI pattern recognition (screenshot on front, "good/bad + why" on back, shuffled)
- Dog training/psychology pattern recognition (photo/video-of-body-language on front)
- Meta Ads and agentic-marketing pattern recognition (ad screenshot/example on front)
- Comedy/charisma timing judgment, to the extent it can be captured as short audio/video
  clips with a judgment prompt

**For the two subjects where Anki-card recognition genuinely doesn't fit:**

- **Synthesis ear training (subtractive/additive/wavetable/FM):** no ready open-source
  tool exists (confirmed above). Least-bad path: **build the card content by hand as
  audio-embedded Anki cards anyway** (record short patch renders, tag by synthesis
  type, ask "which technique made this sound") — this repurposes the exact same
  filtered-deck mechanism rather than building or adopting new software, at the cost
  of manually producing the audio examples yourself (a real content-authoring burden,
  not a tooling one).
- **Music ear training, if CLI drilling is preferred over authoring Anki audio cards:**
  `birdears` (AGPL-3.0, actively maintained, pushed 2026-02) is a genuine standalone
  option, since interval/chord *generation* (not just playback of pre-recorded clips)
  is something a dedicated ear-trainer does better than a static Anki card can — it can
  play truly novel random combinations each session rather than cycling a fixed card
  pool.

**Bottom line ranking:**
1. Anki filtered decks (native) — zero new tooling, covers 6–7 of 9 subjects directly.
2. `birdears` — optional standalone add for music ear training specifically, if
   procedurally-generated (not pre-recorded) intervals/chords matter.
3. `omnilingo` / `yall-mp` — optional standalone add for listening comprehension
   specifically, if recognition-only Anki cards prove too thin for that subject.
4. Synthesis ear training — no tool; author raw audio examples into Anki cards by hand.

---

## Explicitly unverified / could not confirm

- **AnkiWeb "Interactive and Randomized Cards" add-on** (id `171015247`): page is a
  JavaScript SPA shell, could not be fetched directly; description above comes from
  search-result text quoting the page, not a first-hand read. Maintenance status and
  exact author unknown. Verify in-app before depending on it.
- **AnkiWeb "No Scheduler" add-on** (id `215758055`): same JS-shell fetch failure;
  description reconstructed from search-result text and the linked GitHub mirror
  (`nekomaki/anki-no-scheduler`, unlicensed). Ruled out as a fit regardless (see above),
  so this gap doesn't affect the recommendation.
- **`abeage1/earwise`**: no LICENSE file in the repo as of this check — legally
  all-rights-reserved by default despite being public on GitHub. Fine to run locally
  for personal study; do not redistribute or fork publicly without asking the author.
- **`omnilingo`'s actual current maintenance cadence**: GitHub API gave a last-push
  date but the "43 open issues, 1 open PR" figure came from a WebFetch summary of the
  repo page, not a direct issue-tracker query — treat as approximate, re-check before
  investing setup time.
- **No controlled evidence was sought or found** that shuffled-recognition drilling
  (EXAMPLES mode) outperforms alternatives for any of these nine subjects specifically —
  this brief is tooling-availability research only, not an efficacy review. The
  EXAMPLES-mode design rationale itself (`subjects.md`) is not re-litigated here.
