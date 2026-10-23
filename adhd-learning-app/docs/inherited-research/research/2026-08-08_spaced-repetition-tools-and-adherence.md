# Spaced Repetition Tools & Adherence — Evidence Review

> **RESEARCH TIER — NOT MERGED INTO THE DESIGN DOC.**
> **Date:** 2026-08-08 · **50 candidate sources discarded** for failing verification.
> Licences read from `LICENSE` files, not prose claims. Benchmark numbers extracted from
> raw `README.md` at pinned commits, not summaries.

---

## ⚠️ THE HEADLINE — and it is not about algorithms

**Settles & Meeder (ACL 2016)**, `10.18653/v1/P16-1174`. Universally cited as *"spaced
repetition improved Duolingo engagement 12%."* **Table 4, extracted from the publisher PDF:**

| Experiment | Any activity | New lesson | Practice |
|---|---|---|---|
| **I. HLR vs Leitner** (6 wks, ~1M students) | +0.3 n.s. | +0.3 n.s. | **−7.3%** (p<0.001) |
| **II. HLR-lex vs HLR** (2 wks, 3.3M students) | **+12.0%** (p<0.001) | +1.7% | +9.5% |

**Replacing a naive scheduler with a well-fit memory model produced no significant
engagement gain and a 7.3% DROP in practice retention.**

The famous +12% came from Experiment II — a **simplified** model beating the **more
accurate** one. The trigger, in the authors' words: students complained certain words
*"would decay rapidly, regardless of how often they practiced"* — traced to overfit
per-item weights. Removing them removed the punishing behaviour and won +12%.

> **The lesson: a card that keeps coming back no matter how well you do is THE adherence
> killer, and fixing that beats fixing accuracy.** In the only large randomized test that
> exists, prediction accuracy and engagement moved in **opposite directions.**

**Grade: High — rely on as-is.** Anyone citing this paper as "better scheduling → +12%
engagement" is miciting it.

---

## ⚠️ CORRECTION: FSRS has no learning-outcome evidence

**This corrects an earlier overstatement in this project's notes, which graded FSRS
"High — rely on as-is" as the best mechanism to steal.**

| Claim | Verified? |
|---|---|
| FSRS predicts recall better than SM-2 | **Yes — High.** 349,923,850 reviews, 10k collections, 99.0% per-user superiority |
| FSRS produces better **learning outcomes** | **NOT COVERED.** No RCT, no field trial, no A/B test exists |
| FSRS reduces review time for equal retention | **No.** The Anki manual makes no percentage claim |
| "Backed by academic literature" | **Partly.** Both DOIs real and peer-reviewed — but they describe **SSP-MMC/DHP at MaiMemo**, not FSRS. **No peer-reviewed evaluation of FSRS exists** |

The benchmark measures **calibration on retrospective logs**, not learning. The maintainers'
own caveat: *"SM-2 wasn't designed to predict probabilities, and the only reason it does
that in this benchmark is because extra formulas… were added on top of it."*

**And the surprise** — current benchmark, log loss:

| Algorithm | Params | Log Loss ↓ |
|---|---|---|
| RWKV-P | 2,762,884 | 0.2773 |
| **MOVING-AVG** | **0** | **0.3369** |
| Logistic Regression | 34 | 0.3393 |
| FSRS-7 recency | 35 | 0.3414 |
| FSRS-6 | 21 | 0.3460 |
| HLR (Duolingo) | 3 | 0.4694 |

**A zero-parameter moving average beats every shipping FSRS version on log loss.** FSRS wins
decisively against *classical* schedulers (SM-2, HLR, Ebisu, ACT-R) but sits mid-table
against trivial baselines.

> **Practical read: FSRS-6 (21 params, MIT/BSD-3) is the sane stopping point.** Gains past
> it are small, costs climb steeply, and none has ever been shown to affect a learning outcome.

### What IS worth stealing from FSRS

1. **Separate stability from difficulty.** SM-2 collapses both into one `EF` multiplier.
   This is what structurally eliminates ease hell.
2. **`I(r,S) = 9S(1/r − 1)` — retention as a user-facing dial.** Scheduling becomes a
   *policy choice* rather than an emergent property of accumulated penalties. **Most
   portable idea in the survey; costs almost nothing.**
3. **Mean reversion on difficulty** — makes a bad week non-permanent. Directly relevant to
   ADHD-pattern usage.
4. **Post-lapse stability is a function, not a reset.** A lapsed card retains stability
   proportional to what it had.

**Failure mode:** the "Hard" button. Anki manual: *"When you press 'Hard', FSRS assumes you
have recalled the information correctly."* Users who press Hard when they actually forgot
get unreasonably long intervals. **A 4-button scale is a silent correctness dependency —
consider two buttons.**

---

## ⚠️ ADHERENCE — the part that matters most

### The long-horizon picture

**Grad et al. (2021)**, *Adv Health Sci Educ*, `10.1007/s10459-020-10020-z` — cluster RCT,
12 programs, **634 residents, 67 weeks**:

- **20% of the intervention arm completed ZERO cases**
- Extreme bimodality: **27% did >80 cases · 27% did 1–15 · ~20% did nothing**
- **No significant effect on the certification exam** (73.9% vs 73.1%)

**Grade: High.** Over >1 year, voluntary spaced repetition splits into heavy users and
never-starters, and the learning benefit can vanish entirely.

### The Anki decay curve

**Gilbert et al. (2023)**, *Med Sci Educ*, `10.1007/s40670-023-01826-8`, N=130. Active users
across sequential exams: **61.5% → 50% → 29.5% → 12.8%.** A **~80% relative decay in one
academic year.** Users outperformed non-users at every point (+6.4% to +10.7%, all p<0.011)
— but self-selection is uncontrolled.

**Nour & Harris (2025)**, *Cureus*, `10.7759/cureus.95674`, N=89:
- **75% "never or rarely" maintained reviews from previous modules** — they abandon *old
  cards*, not the app
- **82.1% found it overwhelming · 67.9% reported anxiety · 34.5% lost sleep**

**Deng et al. (2015)**: mean **5,086 cards (SD 5,719)** over **24.5 weeks (SD 22.5)**.
**SD exceeds mean on both dimensions — there is no typical user to design for.**

### What predicts dropout

| Predictor | Grade |
|---|---|
| **Punishing scheduling** (cards that decay regardless of effort) — randomized, n=3.3M | **High** |
| Program duration — 1 mo → 88%/49% · 20–27 wks → 71–83% · 67 wks → 20% never start | Moderate |
| **Module/unit boundaries as abandonment triggers** — two independent cohorts | Moderate |
| Perceived overwhelm | Moderate |
| **Review debt / backlog size** | **NOT COVERED — zero peer-reviewed evidence** |
| Desired-retention → workload → dropout | Extrapolated |

> ⚠️ **"Review debt causes abandonment" is the most confidently repeated claim in SRS
> folklore and has NO verified empirical support.** Every quantitative version traced to SEO
> blogs and was discarded. Treat as a hypothesis to instrument, not a constant to inherit.

### ⚠️ Reminders do NOT work — including in an ADHD RCT

**Nordby et al. (2022)**, *Front Digit Health*, `10.3389/fdgth.2022.821031`,
**N=109 adults with ADHD:**

> *"SMS reminders do not improve number of logins, module completion rates or practice of
> coping strategies."*

Grad (2021) similarly found no significant difference from its alert intervention over 67 weeks.

**Grade: High — negative result. Reminders shift *timing*, not *volume*. Do not budget
adherence gains to notifications.**

### ✅ What DOES work — team competition

**Scales, … Kerfoot (2016)**, *Int J Qual Health Care*, `10.1093/intqhc/mzw008`,
**N=422 randomized:**

- Questions attempted: **79% vs 68%** (p=0.03)
- Response time significantly faster (p=0.006)
- **The gap WIDENED over time (p<0.001)** — the effect compounded rather than decayed

Design detail that matters: teams grouped by specialty, **de-identifying aliases to remove
individual shaming.** **Grade: High.**

### ⚠️ Zero ADHD evidence

**No study of spaced repetition, SRS apps, or retrieval-practice adherence in an ADHD
population exists.** Every adherence number above comes from medical students and residents
— populations under board-exam pressure with unusually high baseline conscientiousness.

> **Assume the ADHD adherence floor sits BELOW every figure quoted here.**

### Adherence is systematically not measured

**Martinengo et al. (2024)**, *JMIR*, `10.2196/57760` — 23 studies, 3,371 participants:

> **"No studies reported adverse events or dropout rates systematically."**

And: *"none of the studies provided a rationale"* for their chosen spacing intervals.

**Two consequences:** pooled effect sizes are computed on **completers** and are therefore
**upper bounds**; and any adherence model must be instrumented yourself.

**Never measure adherence by asking.** SpacED POCUS: 81% completed the *survey*, mean case
completion **38.6%**, only **27% finished**. Nour: 87.8% said Anki contributed significantly;
82.1% found it overwhelming. **The gap is 40+ points.**

---

## 🏆 Incremental Reading — the most transferable idea here

The load-bearing distinction: **topics** (things to read) and **items** (things to remember)
live in the **same scheduling queue**. Reading and reviewing are not separate modes.

Pipeline: import → **topic** → *extract* passage (becomes independently-scheduled topic,
parent keeps a bookmark) → recurse → *cloze* a keyword → **item** → normal SR.

Supporting machinery:
- **Priority queue** 0–100% (0 = highest), auto-sorted
- **A-Factor for topics** — reading pace tuned independently of item scheduling
- **Postpone** — *"reschedule outstanding repetitions to later dates with minimum cost to
  the retention of high-priority material"*
- **Dismiss** — removes a topic while preserving everything extracted from it

> **Why this matters most for an ADHD system:** incremental reading is the **only** system
> surveyed where falling behind is a **designed, first-class state with a graceful
> degradation path**, not an error condition. Every other tool treats a backlog as overdue
> debt. `Postpone` is the *intended* response to overload.

Given that module boundaries and overwhelm dominate dropout, **priority-ordered-stream +
postpone is more valuable than any scheduler refinement in this report.**

SuperMemo's implementation is proprietary and Windows-only, but the *pattern* is unencumbered.

---

## Other mechanisms worth stealing

| Source | Mechanism | Grade |
|---|---|---|
| **Anki** | **Leech circuit-breaker** — auto-suspend after N lapses. Given the Duolingo finding, arguably the highest-value mechanism in the report. **Trigger far earlier than Anki's 8** | High |
| **Anki** | Burying siblings + interval fuzz; separate new/review limits as first-class primitives | High |
| **SM-18** | `ItemDiff[i] := f·RepDiff[i] + (1−f)·ItemDiff[i−1]`, `f` decaying 0.8→0.1. **Best value-per-line in the report** — fixes ease hell more simply than FSRS's mean-reversion | High |
| **SM-11+** | Per-**element** forgetting-index targets (FSRS's desired retention, invented ~15 yrs earlier, but per-item) | High |
| **Mnemosyne** | **Interval fuzz** — two lines; prevents review clumping and workload spikes | High |
| **SM-2** | ~15 lines, no training data — a legitimate bootstrap while you accumulate logs | High |

**Ease hell, confirmed in Anki's own manual:** *"repeatedly failing a card after it has
graduated… could reduce its ease a lot, leading to what some people called 'ease hell.'"*

---

## Licences and cost

| Tool | Licence | Cost |
|---|---|---|
| FSRS (py/ts/anki) | **MIT** | Free |
| fsrs-rs, fsrs-optimizer | BSD-3-Clause | Free |
| Anki desktop | **AGPL-3.0** ⚠️ viral over a network | Free |
| AnkiMobile iOS | — | **$24.99** |
| Mnemosyne | **AGPL-3.0 + named-attribution clause** | Free |
| **SuperMemo 19** | **Proprietary, Windows-only** | **$34.00** |
| srs-benchmark | **No LICENSE file** (404) | — |
| anki-revlogs-10k dataset | Custom, **gated** | — |

FSRS's decisive advantage over SuperMemo: **you can vendor it into a commercial product
today with no legal work.** ⚠️ Anki's AGPL is viral over a network — serving a derivative
obliges you to publish source.

---

## Contradictions, surfaced

1. **The Duolingo "12%" is systematically miscited** — better prediction and better
   engagement moved in *opposite* directions.
2. **SuperMemo and FSRS publish contradictory rankings using the same metric.** SuperMemo's
   self-published table: SM-17 = 1.1, FSRS = 16.43. Independent repo using Wozniak's own
   metric: FSRS-6 = 0.0287, SM-17 = 0.0435. **Absolute scales are irreconcilable. Neither
   ranking should be relied on.** SuperMemo's is scored on logs generated by SuperMemo's own
   scheduling — a home-field advantage competitors never had.
3. **FSRS vs SM-18 has never been run** — SM-18 cannot export predictions.
4. **Efficacy vs real-world effectiveness diverge sharply.** Kerfoot's RCTs show reliable
   gains; Grad 2021 — longest and most pragmatic — found **no exam benefit** with 20% never
   starting.
5. **Anki users outperform non-users by 6–11 points — while 40% never used it and usage
   decayed 80% in a year.** The causal arrow is not identified in any verified study.

---

## What to actually build — ordered by evidence strength, not sophistication

1. **Leech circuit-breaker, triggered far earlier than 8 lapses.** *(High)*
2. **Priority-ordered stream + Postpone, not an overdue queue.** *(High mechanism / Moderate adherence link)*
3. **Retention as an explicit user-facing dial** — `I(r,S) = 9S(1/r − 1)`. *(High)*
4. **FSRS-6 as the scheduler; stop there.** Bootstrap on SM-2 until logs exist.
5. **SM-18's difficulty estimator.** *(High)*
6. **Mnemosyne's interval fuzz.** *(High)*
7. **Team competition with de-identifying aliases**, if a social layer is plausible. *(High)*
8. **Do NOT build a notification strategy and expect adherence from it.** *(High, negative)*
9. **Instrument adherence from day one — never measure it by asking.**
10. **Design for the observed shape:** ~20–30% never-starters, ~80% decay in a year without
    external pressure, SD > mean. **There is no typical user.**
