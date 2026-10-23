# Adversarial Review of Design Claims

> **Status: RESEARCH TIER — NOT MERGED INTO THE DESIGN DOC.**
> Read, decide, then amend `specs/adhd-learning-system-design.md` deliberately.
>
> **Date:** 2026-08-08
> **Method:** an agent tasked to *refute*, not confirm, six load-bearing claims.
> **Verification:** every citation confirmed via PubMed, Crossref, or publisher record.
> **28 candidate sources were discarded for failing verification** — 11 commercial/SEO
> neuroscience pages with no primary citation, 7 blogs, 5 advocacy/aggregator pages,
> 3 non-peer-reviewed items, 1 dissertation index entry, 1 unconfirmable ERIC PDF.
> 5 publisher pages returned HTTP 403 and were re-verified via PubMed/Crossref instead.

---

## Verdict summary

| # | Claim | Verdict | Grade |
|---|---|---|---|
| 1 | 40–60% load band; DMN / fronto-parietal thresholds | **UNSUPPORTED** — mechanism inverted | Not covered |
| 2 | 15-min sprints hold prefrontal BOLD | **CONTRADICTED** (length); no evidence (BOLD) | Not covered |
| 3 | Functional colour coding via N2pc | **PARTIALLY SUPPORTED** — right rule, wrong reason | Moderate (colour) / Not covered (N2pc) |
| 4 | Repeated failure suppresses plasticity | **CONTRADICTED** as stated | High (errors+feedback help) / Extrapolated (unchanged retry) |
| 5 | Retro-cueing intact in ADHD adults | **PARTIALLY SUPPORTED** — children only, 1 study | Extrapolated |
| 6 | Match method to neurotype | **PARTIALLY SUPPORTED** — learning-styles-shaped risk | Not covered (matching) / Moderate (supports) |

---

## Claim 1 — The 40–60% load band

**UNSUPPORTED. Grade: Not covered.**

**(a) The numbers do not exist.** No primary source states a 40–60% or 75% band. Cognitive
load is not measured as a percentage of working-memory capacity by anyone, because it
cannot be. De Jong (2010) documents that CLT's load types are not separably measurable and
that germane load is a post-hoc construct with no independent operationalization — the
theory verges on unfalsifiable as a result. **You cannot compute a percentage of a quantity
nobody can measure.**

**(b) The closest real finding is much weaker.** Callicott et al. (1999) found an
**inverted-U** dorsolateral prefrontal BOLD response as WM load rises. That supports
"there is a middle zone" and nothing more. The inflection is defined by task level relative
to individual performance breakdown, not a percentage; it is a BOLD signal, not
neuroplasticity; and it says nothing about learning outcomes.

**(c) The >75% mechanism is stated backwards.** High WM load is associated with *increased*
fronto-parietal synchronization. Desynchronization is what experimenters **induce** (tACS)
in order to **impair** working memory — Alekseichuk et al. (2017). The design inverts cause
and effect. Anyone with an EEG background will spot this immediately.

The DMN half is also loose: task engagement *suppresses* the DMN; the real low-load
phenomenon is mind-wandering, which has no 40% threshold attached anywhere.

> **Recommendation:** delete the numbers. Keep *"aim for challenging-but-achievable, adapt
> difficulty to performance."* Defensible, measurable, operationally identical.

---

## Claim 2 — 15-minute micro-sprints

**CONTRADICTED for the 15-minute optimum. No evidence either way for the BOLD mechanism.
Grade: Not covered.**

The 10–15 minute attention limit is **a documented myth.** Bradbury (2016) traced the
"attention declines 10–15 min in" consensus to its sources and found the primary data do
not support it — the most-cited source barely discusses attention at all. Institutions had
already shortened lectures on this basis.

Two RCTs test fixed sprints directly; neither finds an optimum:

- **Biwer et al. (2023)**, N=87. Compared self-regulated breaks · 24-min/6-min ·
  **12-min/3-min**. Systematic breaks beat self-regulated on fatigue, distraction,
  concentration and motivation — but **no difference between the 12- and 24-minute blocks**
  on mental effort or task completion. This is the closest existing test of your number,
  and it says block length does not matter.
- **Smits et al. (2025)**, N=94. Pomodoro vs Flowtime vs self-regulated over authentic
  2-hour sessions. No differences in completion or flow. Pomodoro showed *faster* fatigue
  increase and *faster* motivation decrease. Authors: no technique should be recommended
  over the others.

Note these two **disagree** on subjective measures — itself informative. The effect is not robust.

> **Recommendation:** keep structured, pre-committed breaks (Biwer supports this against
> self-regulated). Drop "15 minutes" as a scientific claim; make it a user-adjustable
> default. Delete the BOLD sentence.

---

## Claim 3 — Functional colour coding

**PARTIALLY SUPPORTED — right conclusion, wrong reason.**
**Grade: colour coding — Moderate, directional. N2pc — Not covered.**

The design rule survives, on completely different evidence:

- **Ozcelik et al. (2009)** — eye-tracking; colour-coded materials outperformed no-signal
  controls on matching and transfer.
- **Schneider et al. (2018)**, meta-analysis of signaling — small-to-medium positive effect
  on transfer and comprehension, **moderated by prior knowledge**: helps novices more, can
  wash out or reverse for experts.

This is the **signaling/cueing principle** of multimedia learning — universal instructional
design, not neurotype-matching. It applies to everyone, which is a point *in its favour*.

The N2pc justification fails. Eimer & Kiss (2008) showed N2pc is **gated by top-down task
set** — maximal for targets, attenuated for non-target singletons, absent for irrelevant
dimensions. Colour does not amplify selection by being colour; it does so only when the
learner is already looking for it. And no verified study links N2pc amplitude to any
learning outcome.

**Is this learning-styles thinking?** No — *provided* consistent functional colour is
applied to all users. It becomes learning-styles thinking the moment it is offered as a
"visual learner" option.

> **Recommendation:** keep the rule; cite Ozcelik/Schneider; delete N2pc. Add the
> prior-knowledge moderator — heavy signaling for beginners, tapering as competence grows.

---

## Claim 4 — "Repeated failure is actively harmful"

**CONTRADICTED as stated. A narrower version is defensible.**
**Grade: errors+feedback help — High. Unchanged retry — Extrapolated. Plasticity suppression — Not covered.**

The desirable-difficulties literature runs the other way, and it is strong:

- **Metcalfe (2017)**, *Annual Review of Psychology* — errorful learning followed by
  corrective feedback **benefits** learning, most strongly when the learner was confident
  in the wrong answer (hypercorrection). Low-stakes error-making beats error-avoidance.
- **Kornell, Hays & Bjork (2009)** — failing, then studying, beats studying alone.

> **"Failure is harmful to learning" is the opposite of the consensus.** A system that
> routes learners *away* from material they failed would forfeit one of the largest,
> best-replicated effects in the learning literature.

**Two genuine caveats:**

1. **The word "unchanged" does real work.** Metcalfe's benefit is conditional on
   *corrective feedback*. An identical retry with no feedback and no scaffolding is exactly
   the condition where the error benefit does not appear. So *"re-serving the same failed
   lesson with nothing added is a waste"* is defensible. *"Actively harmful to plasticity"*
   is not.
2. **There is a real motivational cost.** Moore et al. (2010) — WM overload produced
   subsequent performance decline, predicted by task failure and amygdala activation. A
   within-session affective cost, not plasticity suppression, with no threshold percentage.
   Milich & Okazaki (1991) — ADHD boys solved fewer puzzles after unsolvable ones, gave up
   more, reported more frustration. *Caveats: children, n=23 vs 22, 1991, no verified replication.*

> **Recommendation:** rewrite as a **motivational** rule, not a neural one:
> *"Never re-serve a failed item identically — always add feedback, scaffolding, or a
> decomposition step, and cap consecutive failures to protect motivation."*
> Keeps the useful behaviour, aligns with Metcalfe instead of fighting him.

---

## Claim 5 — Retro-cueing in ADHD adults

**PARTIALLY SUPPORTED — supported in children, zero adult evidence. Grade: Extrapolated.**

A PubMed search for `retro-cue AND ADHD` returns exactly **one** study:
Superbia-Guimarães, Bader & Camos (2022). Strong pre- and retro-cueing benefits in **both**
ADHD and typically-developing groups, no significant group difference; authors conclude
ADHD is not characterized by orienting deficits.

**Ages 10–16. No adults.** A broader search surfaced no adult ADHD study.

Directionally right with a good on-point study, but: single study, children, and the
group-equivalence conclusion rests on a **null result**, which small samples produce
easily. Extrapolating to adults is reasonable — retro-cue benefits are robust across young
adults and survive aging — but label it as extrapolation.

---

## Claim 6 — "Match the method to the neurotype"

**PARTIALLY SUPPORTED — and this is the real risk. As literally worded, it is structurally
the meshing hypothesis.**
**Grade: matching — Not covered. ADHD-targeted supports — Moderate, directional.**

**Why it is a genuine risk.** Pashler et al. (2008) found virtually no evidence for the
crossover interaction that matching requires; several adequate studies flatly contradicted
it. Kirschner (2017) reached the same verdict a decade later.

**The best pro-matching evidence, found deliberately:** Clinton-Lisell & Litzinger (2024),
meta-analysis of 21 studies, 101 effect sizes, N=1,712, reporting **g = 0.31** favouring
matched instruction. But the authors' own reading is deflationary: only **26%** of outcome
measures showed the crossover interaction that would validate matching, and they conclude
benefits are *"too small and too infrequent to warrant widespread adoption,"* recommending
**multimodal instruction for everyone** instead.

> That is the most favourable verified evidence in existence, and it still says do not build
> on matching.

**Why the design is not doomed.** ADHD is not a self-reported style preference — it is a
diagnosed condition with documented executive-function impairment, and aptitude-treatment
interactions for genuine deficits are a different logical animal from meshing.

Verified ADHD-intervention evidence is real but modest: Yegencik, Bell & Deniz (2025),
26 school-based RCTs — academic performance **d = 0.37**, inattention **d = −0.33**,
hyperactivity/impulsivity **d = −0.09 (n.s.)**. But I² = 48–61%, only **8 of 26** studies at
low risk of bias, mostly subjective measures, and **significant reporter bias** — parents and
teachers reported far less improvement than children self-reported. *That last detail matters
for a self-report-driven system.*

Critically: none of this shows ADHD learners **learn by different mechanisms.** It shows they
benefit from **external structure, immediate feedback, and reduced distraction** — supports
that help most learners and help this population more.

### The safe reframe

> Universal evidence-based instructional design (retrieval practice, spacing, signaling,
> corrective feedback, adaptive difficulty), delivered with ADHD-specific **supports** —
> externalized structure, immediate feedback, distraction reduction, and motivational
> scaffolding after failure.

Defensible, keeps essentially every concrete feature, and avoids the claim that would get the
design dismissed by anyone who knows the literature.

---

## The structural problem underneath all of this

Claims 1, 2, and part of 4 share a signature: **neural mechanisms the system cannot measure.**

This system cannot measure percentage-of-working-memory-capacity, prefrontal BOLD,
fronto-parietal coherence, or plasticity. Those claims therefore **cannot be validated,
falsified, or tuned by anything built here** — they are unfalsifiable decoration generating
specific-sounding numbers (40, 60, 75, 15) with no way to check them.

They also carry asymmetric reputational risk: the fronto-parietal desynchronization claim is
**backwards**, and one reviewer with an EEG background will notice and discount the entire design.

> **Replace each with the behavioural variable you can actually observe** — accuracy, response
> latency, abandonment rate, self-reported effort, session completion. Every one of the six
> claims has a behavioural restatement that is better evidenced, operationally identical, and
> adaptively tunable.

---

## Verified sources

| Source | Identifier |
|---|---|
| de Jong 2010, *Instructional Science* — CLT critique | `10.1007/s11251-009-9110-0` |
| Callicott et al. 1999, *Cerebral Cortex* — inverted-U PFC | PMID 10022492 |
| Alekseichuk et al. 2017 — FP desync impairs WM | `10.3233/RNN-160714` |
| Jenkins 2019, *Trends Cogn Sci* — DMN perspective on load | `10.1016/j.tics.2019.04.008` *(metadata only; 403)* |
| Bradbury 2016, *Adv Physiol Educ* — attention-span myth | `10.1152/advan.00109.2016` |
| Biwer et al. 2023, *Br J Educ Psychol* — break RCT | PMID 36859717 |
| Smits et al. 2025, *Behav Sci* — Pomodoro/Flowtime RCT | PMID 40723645 |
| Ozcelik et al. 2009, *Computers & Education* — colour coding | `10.1016/j.compedu.2009.03.002` |
| Schneider et al. 2018, *Educ Res Rev* — signaling meta-analysis | `10.1016/j.edurev.2017.11.001` |
| Eimer & Kiss 2008 — N2pc gated by task set | PMID 18801016 |
| Metcalfe 2017, *Annu Rev Psychol* — Learning from Errors | PMID 27648988 |
| Kornell, Hays & Bjork 2009, *JEP:LMC* | `10.1037/a0015729` |
| Moore et al. 2010, *Brain Imaging Behav* — WM overload | PMID 20503117 |
| Milich & Okazaki 1991, *J Abnorm Child Psychol* | PMID 1770188 |
| Superbia-Guimarães et al. 2022, *Dev Neuropsychol* | PMID 36514838 |
| Pashler et al. 2008, *PSPI* — Learning Styles | `10.1111/j.1539-6053.2009.01038.x` |
| Kirschner 2017, *Computers & Education* | `10.1016/j.compedu.2016.12.006` |
| Clinton-Lisell & Litzinger 2024, *Front Psychol* — matching meta-analysis | `10.3389/fpsyg.2024.1428732` |
| Yegencik, Bell & Deniz 2025, *Front Psychol* — ADHD RCT meta-analysis | `10.3389/fpsyg.2025.1611145` |
