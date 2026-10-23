# Learning how to learn — self-regulation as the system's actual foundational goal

Prompted by Orlando naming the deepest motivation for this whole project: he wants the system to explicitly teach him HOW to learn, not just deliver study techniques — because he never developed that skill growing up. Context: immigrant, English as a second language, took on family caretaker/translator responsibilities as the oldest child during formative school years, on top of ADHD (already extensively researched elsewhere in this project). Three parallel research passes, 2026-08-13.

**Correction (same day, same session):** Orlando completed high school and community college coursework (English, social sciences, humanities) — schooling was **not** disrupted or incomplete. The "first-generation college student" and "language brokering" literature cited below is used as an evidence proxy for *never developing explicit self-regulated-learning strategies*, not as a claim about interrupted formal education — that distinction matters and the original draft blurred it. The specific, concrete symptom he named: math, which he was good at as a kid, atrophied and needs rebuilding — now added to `subjects.md` as subject #21, explicitly tied to systems thinking and his AI/UX-engineering career direction.

## The core finding: this is a real, currently-unaddressed gap — not already covered

An architectural fit-check against the fully locked design (`specs/DECISIONS.md` §1–§12) found the current ADHD-supports layer is **compensatory, not skill-building**:

- `adhd-learning-system-design.md:35` — "never require the learner to hold progress in working memory" — externalizes state *for* him by design.
- `DECISIONS.md:181` — `tracker.md` is "the sole durable state. Not conversational memory" — same pattern.
- The Paas effort scale looks like self-monitoring, but the *system* acts on the number, not Orlando: "an effort reading 7–9 → reduce scope, add scaffold. Never press on" (`DECISIONS.md:73`). He reports; the system regulates.
- Mapped against the three functions this project's own AI-assisted-learning research (`2026-08-10_ai-assisted-learning-practices.md`) already names as offload-risk (goal-setting, error monitoring, strategy selection): the router owns goal-setting (which mode a lesson dispatches to), the Examiner owns error-monitoring exclusively ("Claude decides whether you know it" — §8), and failed-gate strategy selection is automatic (3-fail auto-park). **All three currently sit with the AI, not Orlando.**

This isn't a diplomatic "it depends" — the fit-check found nothing locked or queued in `DECISIONS.md` §1–§12 currently builds Orlando's own planning/monitoring/evaluating capacity. The tool-boundary rule (§8) and the ADHD-supports layer solve different problems than this one.

## What the evidence says explicit self-regulation instruction should look like

- **Metacognitive strategy instruction is one of the best-evidenced levers in learning science** — d≈0.69 (~25 percentile points) in one synthesis, g=.50 immediate / g=.63 at follow-up in a 2017 meta-analysis (48 interventions). A dedicated meta-analysis (56 effect sizes, N=7,667) found it specifically improves *monitoring calibration accuracy*. **Grade: High.**
- **It has to be explicit** — not "be aware of your thinking," but concrete teaching of *when, why, and how* to use a specific strategy (Dignath & Büttner 2008). This is the exact layer missing: the system currently teaches retrieval/spacing *techniques* without teaching the planning→monitoring→reflecting cycle itself as its own skill.
- **Zimmerman's cyclical model** (forethought/planning → performance/monitoring → self-reflection) is the dominant framework, but evidence is skewed toward K-12/undergrad classroom settings. The strongest adult/workplace evidence (Sitzmann & Ely 2011, meta-analysis, k=430, N=90,380) identifies goal level, persistence, effort, and self-efficacy as the constructs that actually predict adult learning outcomes. **Grade: Moderate-high** for the constructs mattering; **low-moderate** for "explicitly teaching the cycle to an adult who lacks it," which is thin as a direct intervention literature.
- **First-generation college students** (the closest real proxy for "never explicitly taught how to learn," found independently in two research passes) consistently self-report lower self-regulated learning, and the deficit does **not** close through mere exposure to more schooling — it requires explicit, intentional instruction. Explicit strategy instruction (spacing, retrieval/self-testing, generative strategies — the exact mechanisms already used in this project) measurably improves outcomes for this population. **Grade: Moderate**, real and relevant, though "first-gen college student" isn't a perfect match for "adult remediating decades later."
- **Honest caveat, stated plainly in that literature:** knowledge gain from strategy instruction is easier to produce than durable behavior change — students learn what good strategies are, then revert to old habits (rereading, highlighting) under time pressure. **This is a maintenance problem, not a one-time-lesson problem** — and it matches this project's existing spaced-retrieval design far better than a single "how to study" lesson would. The meta-skill needs the same spaced-reinforcement treatment the content already gets.

## The AI-dependency risk, and the concrete fix

This project's own prior research already names "metacognitive laziness" (Fan et al. 2025, Dizon et al. 2026) — AI offloading of goal-setting, error-monitoring, and strategy-selection — as a real, moderate-to-high-graded risk. New material this pass adds the concrete design answer:

- **"Bounded autonomy"** (Frontiers in Education, 2026, "The regulation paradox") — AI scaffolding with deliberately limited scope/timing/duration, withdrawn on a schedule, returning regulatory responsibility to the learner over time.
- Load-bearing mechanism: "within-platform improvement may not transfer... once dashboards/metrics disappear" — i.e., skill built *while* an AI/dashboard is doing the monitoring evaporates when that support is removed. This is direct evidence for a **fading scaffold**, not a permanent one.

## On the ESL/immigrant-caretaker context specifically

- **"Language brokering"** (children translating/handling family paperwork) is a real, established construct in immigrant-family research since the 1990s — not a term this project invented. Effects on academic outcomes are genuinely mixed, not uniformly negative: "high-stakes" brokering (legal/medical/financial) correlates with worse outcomes and more stress; "everyday" brokering correlates with better outcomes; a strong sense of family obligation buffers stress and is linked to higher achievement. **No paper directly tests whether brokering suppressed formal study-skill acquisition specifically** — that exact causal claim is plausible and adjacent, not proven. Treat as a real, respected contributing factor, not a deficit diagnosis.
- **Directly reassuring finding:** metacognitive strategy use is *more* predictive of success in a second language than a first language (2024 structural-equation study on L2 writing), and strategies transfer across languages. ESL background does not make explicit strategy instruction less likely to work — the evidence points the opposite direction.
- **Andragogy (Malcolm Knowles' adult-learning theory) has weak evidentiary standing** — worth flagging since it's cited everywhere in adult-learning content. It wasn't derived from empirical research; multiple reviews call it "atheoretical" and note the child/adult distinction it rests on doesn't actually hold. Use as a descriptive frame if useful, never as validated science, and don't build a locked decision on it alone.

## Proposed new decision (not yet locked — for sign-off)

Add an explicit, separate self-regulation layer to the architecture — distinct from MAP/DRILL/EXAMPLES/REPS, which are content-delivery modes, not the planning/monitoring/reflecting cycle itself:

1. **An explicit "plan → monitor → reflect" scaffold** as its own mechanism, teaching *when, why, and how* to choose a study approach — not folded silently into existing modes.
2. **AI support that fades on a schedule** (bounded autonomy) rather than persisting indefinitely — early sessions may have more AI-driven prompting of "what's your plan today / how do you think that went," later sessions hand more of that back to Orlando explicitly.
3. **Spaced reinforcement of the meta-skill itself**, not just lesson content — matching the existing retrieval/spacing design, since the evidence says durable behavior change (not just knowledge of good strategies) is the actual hard part.

This is a candidate for `DECISIONS.md`, pending explicit sign-off — it's a genuine addition to a locked file, not something to apply silently.
