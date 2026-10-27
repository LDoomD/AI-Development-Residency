# External Framework Review — Eero Alvar's Agent Harness + Indie/OSS Learning Systems Catalog

**Source 1:** Eero Alvar (YouTube, @EeroAlvar), three videos reviewed in full (transcripts
read directly, not summarized from memory): "How I Use AI to Learn Things," "How I Learn
Difficult Things," "Agent Harness for Learning Things." A fourth, free, open-source desktop
app, demoed in the third video.

**Source 2:** 17 smaller open-source/indie projects found across two research sweeps
(GitHub, Hacker News/Show HN, Indie Hackers). Full links in the table below.

**Reviewed:** 2026-10-26.

**Evidence grade of both sources: None — practitioner workflows and shipped software, not
research.** Same standing rule as the Tina Huang review
(`docs/inherited-research/research/2026-08-09_lonely-octopus-4-part-workflow.md`): nothing
here may be cited in `DECISIONS.md` as support for a claim. These are reviewed because they
are well-built and because some of them independently reinvent mechanisms this project
already locked — which is a useful signal about design, not about efficacy.

Per `CLAUDE.md`, the inherited research was grepped first
(`eero|agent harness|probe.*plan.*teach|reasoning chain|knowledge graph|deeptutor|forgetting
curve|ebbinghaus`). Result: DeepTutor gets one passing mention in
`2026-08-09_ai-tutor-landscape-2026.md` as an academic prototype; "agent harness" and
"knowledge graph" are discussed only as general orchestration-engineering terms in
`2026-08-10_graph-engineering-best-practices.md`. None of the specific mechanisms below
(probe/plan/teach, the thinking field, the reasoning-chain graph, forgetting-curve decay)
were already covered. External research was justified.

---

## Executive summary

Eero Alvar's system solves the **same problem** this project solves — not planning and
follow-through like Tina Huang's framework, but encoding and retention. This makes it a much
closer comparison than the Tina Huang review, and the right read of it is **convergent
validation**, not new direction. Three of his four core mechanisms are things this project
already locked independently, under different names, for different cited reasons. That is
weak evidence on its own (two practitioners agreeing is still not a controlled trial), but it
is a second independent data point in a project whose own standing caveat says no study
proves any of this works — worth recording for exactly that reason.

One piece is genuinely new and not yet in this project's design: the **raw "thinking"
capture field**, present on nearly every interaction, not just at the gate. The project's
Examiner already forces evidence-before-verdict at the mastery gate (`DECISIONS.md` §8–9).
Eero's system captures *how the learner is reasoning* continuously, before any verdict is
needed — closer to what the queued "note-taking coaching" idea in `HANDOFF.md` would need
as input.

The indie/OSS catalog turned up one further new idea worth flagging: applying forgetting-curve
decay to a knowledge graph itself, not just to flashcards. This project already has a
forgetting-curve mechanism (FSRS, via the Anki-equivalent review queue, `DECISIONS.md` §1) —
but nothing in the current design decays the *router's* or any planning artifact's state the
same way. Noted as a queued idea, not a recommendation to rebuild the review queue.

---

## Eero Alvar's system, as built

| Phase | What it does | Closest existing decision |
|---|---|---|
| **Probe** | Adaptive multiple-choice quiz that binary-searches the exact edge of the learner's understanding across every dependency a lesson needs, before teaching anything | No direct equivalent. Closest is the router reading a `modes:` tag (§10a) — but that classifies the *content*, not the *learner's* current state |
| **Plan** | AI reasons out a minimal dependency tree from what the learner already knows to the goal, and renders it as a graph — partly so the learner can see what's coming, partly (Eero's stated real reason) to force the planning agent to actually reason instead of winging it | Resembles the queued "Phase 0 — plan intake" (§11, item 4), but Eero's plan is re-derived per learner per topic, not a static study plan generated once |
| **Teach** | Walks the dependency tree one step at a time. Each step: **predict** (learner guesses the next move before being told), **teach** (one reasoning step, kept deliberately slow), **check** (quiz to confirm the step actually landed) | The predict-before-teach piece is new. The check piece is what the Examiner already does, just moved earlier and made lower-stakes (per-step, not per-lesson) |
| **Practice** (separate mode, added in the third video) | Adaptive problem stream targeting weak spots, difficulty scaled by how many ideas a problem combines and how unfamiliar the cues are | This is functionally what DRILL + EXAMPLES already do via Anki/FSRS (§1, §10b) |
| **Thinking field** | A raw, unfiltered "type your reasoning" box on nearly every interaction — not just the final answer. Eero's stated reason: two people can give the same wrong answer for completely different reasons, and only the reasoning trace tells them apart | **New.** No equivalent currently in this project's design |
| **Persistent memory** | Sessions get distilled into propositions and reasoning chains, rendered as a navigable graph across sessions — not a transcript, a compressed structure | `tracker.md` is already the sole durable state (§9), but it tracks lesson status, not a graph of reasoning connections between lessons |

Video links, for reference: ["How I Use AI to Learn
Things"](https://www.youtube.com/watch?v=kzcI5F4tGiU), ["How I Learn Difficult
Things"](https://www.youtube.com/watch?v=ciC6ffUqI8k), ["Agent Harness for Learning
Things"](https://www.youtube.com/watch?v=nfTDljFG2g0).

---

## Findings

### 1. Convergent validation: separating understanding from recall

Eero's system treats **teaching** (installs understanding) and **practice** (broadens the
cues that bring it back to mind under pressure) as two different jobs with two different
mechanisms. This is, independently, exactly this project's MAP (structure, installs the
model) vs. DRILL/EXAMPLES/REPS (recall under varying conditions) split, already locked in
`DECISIONS.md` §2.

Worth recording as a second data point, worth **not overweighting** — same caveat as the
Obsidian convergence in the Tina Huang review. Two practitioners landing on the same split is
weak evidence next to zero controlled studies either project cites for it.

### 2. Convergent validation: evidence-before-verdict grading

Eero's "check" step and this project's Examiner (`DECISIONS.md` §8, §9) both refuse to accept
a holistic "that seems right" judgment. The Examiner forces quote-per-criterion evidence;
Eero's system quizzes on the specific reasoning step just taught, not a vague recap. Same
underlying principle — a grader has to point at the specific thing that proves
understanding, not pattern-match on fluency — arrived at separately.

### 3. Convergent validation: the plan should force the agent to actually reason

Eero states explicitly that rendering the teaching plan as a graph isn't mainly for the
learner — it's to stop the planning agent from skipping steps. This is the same logic behind
this project's drift-checker and tracker-writer design
(`docs/inherited-research/research/2026-08-09_agentic-tutoring-workflow-design.md`): don't
trust a reasoning agent's free-form output where a structured, checkable artifact can be
forced instead.

### 4. New idea: continuous raw-thinking capture, not just at the gate

This is the one piece of Eero's system genuinely absent from the current design. The Examiner
captures evidence at the mastery gate. Nothing currently captures *how* the learner is
reasoning during MAP or DRILL, before any gate is reached.

This connects directly to the queued, not-yet-researched idea in
`adhd-learning-app/HANDOFF.md` (2026-10-24 session): note-taking coaching, where the system
looks at *how* notes are taken, not just what's in them. A lightweight raw-thinking field
during MAP mode would be the input that idea needs. Flagging here as a design input for that
future research pass — not proposing a build now, since `HANDOFF.md` already correctly notes
no prior research exists on this and it isn't locked.

**Caution carried over from this project's own tool-boundary rule (§8):** "Gemini helps you
learn it, Claude decides whether you know it" exists precisely because an always-available,
always-explaining AI erodes unassisted performance (Bastani et al., PNAS 2025, already
cited). A thinking-capture field that also *responds* to what's typed would reopen that risk.
If built, it should capture only — the same evidence-before-verdict discipline the Examiner
already uses, applied earlier in the loop, not a running conversation.

### 5. New idea from the indie catalog: forgetting-curve decay on structure, not just cards

One project out of the 17 found —
[`sachitrafa/YourMemory`](https://github.com/sachitrafa/yourmemory) ([Show
HN](https://news.ycombinator.com/item?id=47914367), 98 points, 17 comments) — applies
Ebbinghaus forgetting-curve decay to an agent's knowledge graph itself: each recall
strengthens a node, unused ones fade, a graph layer catches related nodes a pure
similarity-search would miss.

This project already has forgetting-curve logic, via FSRS on individual cards
(`DECISIONS.md` §1). What's different about this idea is applying decay to *structure* —
which lessons/topics are going stale as a whole, not just which flashcards are due. No
current mechanism in this project does that at the lesson/tracker level.

**Not recommended for adoption now.** This is a single indie project with no outcome data,
and it would mean tracker.md carrying decay state on top of its already-defined status
transitions (§10c's tracker-writer is explicitly a validated tool call with a fixed
transition table, not a place for new inferred logic). Logged as a queued idea for later, the
same way item 8 in §11 ("True Recall — second SRS system") is logged: a standalone decision,
not a default.

### 6. The rest of the indie catalog: mostly re-confirms existing decisions, nothing else new

| Project | What it does | Relevance |
|---|---|---|
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) (43.7k★) | Multi-agent tutoring, citation-sourced practice problems | Already noted in `2026-08-09_ai-tutor-landscape-2026.md`. Citation-sourcing confirms this project's own "source-grounded, not hallucinated" requirement (Finding 3 of the Tina Huang review) |
| [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) (584★) | 33 copy-paste prompts, zero infrastructure | Confirms a prompt-only MVP is viable for simple cases — not applicable here, this project needs stateful tracking a prompt pack can't hold |
| [undefined-ui/second-brain-os](https://github.com/undefined-ui/second-brain-os) (1.1k★) | Self-maintaining Obsidian knowledge base | Reinforces the Obsidian convergence already logged in the Tina Huang review; this project replaced Obsidian with the hosted web app regardless (`CLAUDE.md`) |
| [zijinz456/OpenTutor](https://github.com/zijinz456/OpenTutor) (152★) | Local multi-agent tutor, FSRS | Confirms FSRS as a reasonable default (already locked) |
| [ChenChenyaqi/learn-anything](https://github.com/ChenChenyaqi/learn-anything) (494★) | Portable skill version of probe→plan→teach | Confirms the probe→plan→teach shape generalizes across implementations; adds nothing new beyond what Eero's own review already covers |
| [Fata](https://news.ycombinator.com/item?id=48489163) (124 HN pts) | Spaced repetition for AI-coding skill rot | Different problem (retaining skills you've outsourced to an agent), not applicable to this project's subject-agnostic router |
| Everything else found (study-buddy, agent-tutor-skill, AutoDeck, socratiskill, Learntime, StudyBits, ai-agent-to-learn-faster-and-better, mastery-tutor, ai-tutor, braiinz-education, TutorGPT) | Various smaller implementations | Each resembles one piece already covered above (FSRS review queues, local-first storage, Socratic probing, source-aware teaching). None introduce a mechanism not already discussed in findings 1–5 |

---

## What this means for the build plan

Matching the register of the Tina Huang review: nine items there, three here. None applied —
proposals for review, same as that file.

### Recommended: log as convergent validation (no build change)

1. **Add a one-line cross-reference in `DECISIONS.md` §2** noting that Eero Alvar's
   independently-built system arrives at the same teach/practice split as this project's
   universal-layer architecture. Same treatment as the Obsidian convergence note in the Tina
   Huang review — recorded, not treated as evidence.

### Recommended: feed into already-queued research, don't build yet

2. **When the note-taking-coaching idea from `HANDOFF.md` gets its own research pass**, use
   Eero's thinking-field design as a starting reference for what "how notes are taken" could
   mean technically — a raw reasoning-capture field, evidence-before-verdict applied earlier
   in the loop, not just at the gate. Subject to the same Bastani et al. guardrail already
   governing tool boundaries (§8).

2a. **Confidence capture — concrete spec proposed 2026-10-26, not yet built.** Eero's system
   uses a continuous confidence slider per answer. Orlando's proposed variant: **1–5 discrete
   buttons** (1 = guessing, 5 = certain), shown alongside every quiz/check answer, not just at
   the mastery gate. Rationale given: discrete buttons are faster to tap than a slider to
   drag, and a self-reported certainty score is cheap signal that sharpens what the Examiner
   and the probe phase can infer from a single answer — two people can give the same answer
   with very different certainty, same logic as the thinking-field finding above.

   This is a second, complementary channel to the thinking field, not a replacement:
   thinking field = *why*, confidence buttons = *how sure*. Both should be read together,
   since a confident-but-wrong answer and an unsure-but-wrong answer call for different
   responses (confident-wrong is more informative of a real misconception; unsure-wrong may
   just need more exposure).

   **Not yet checked against §8's tool-boundary guardrail or against the floor/escape-hatch
   mechanism** — e.g., does a run of low-confidence ratings count toward the Effort 7–9
   floor trigger, or stay a separate signal? That integration question is unresolved and
   should be answered before this is built, not assumed.

2b. **The broader framing behind this and the audience-scope item in `STATUS.md` #5**: the
   stated product philosophy is that **data volume and specificity is what makes
   personalization real** — the more signal captured per interaction (thinking field,
   confidence rating, pacing, which escape-hatch route fired), the more the system can
   tailor itself to one learner. This is directionally consistent with this project's
   existing design (the probe phase already exists to build "a detailed picture of
   understanding," per the inherited research), but it is worth naming explicitly as a
   stated product principle, not just an implementation detail — it should inform which
   future features get prioritized (anything that cheaply adds real signal) versus declined
   (anything that adds friction without adding signal, which already describes why streaks
   and fixed timers were rejected in §3–4 of the inherited `DECISIONS.md`).

2c. **Resolves a wording risk from the Oct 24 personal brainstorm** (Notion, "Notes for
   Discovery"): the idea of having AI "understand what type of learner the student is" reads
   as learning-styles framing, which is specifically refuted and rejected in the inherited
   `DECISIONS.md` §4 (Pashler et al. 2008; Kirschner 2017). The data-grounded personalization
   principle above is the correct replacement — adapt from demonstrated performance (the
   probe phase) and stated preferences (confidence ratings, pacing), not a fixed learner-type
   label. Same underlying goal, evidence-backed mechanism instead of a refuted one.

### Recommended: log as a queued idea, not a decision

3. **Add forgetting-curve decay on tracker/lesson structure (not just individual cards) as
   item 10 in `DECISIONS.md` §11's queued list**, parallel to item 8 (True Recall). Source:
   `sachitrafa/YourMemory`. No action until a specific need surfaces — same standard already
   applied to every other queued item.

### No change

4. **The Practice phase, the plan-as-graph, and the predict/teach/check loop all re-confirm
   decisions already locked** (§1, §2, §8, §9, and the agentic-workflow brief's
   orchestrator-worker design). No new build items from these.

---

## Adversarial review notes

Written directly from primary sources: all three Eero Alvar video transcripts were read in
full (not summarized secondhand), and the indie catalog links were checked individually for
what they actually claim, following the same discipline the Tina Huang review used.

Claims deliberately **not** made:

- **No efficacy claim is attributed to Eero Alvar's system or any indie project.** All are
  graded Evidence: None, same as Tina Huang's framework. Convergence with this project's own
  locked decisions is reported as a weak, recorded signal — explicitly not proof.
- **Star counts and HN points are reported as traction signals, not quality signals.** A
  highly-starred repo (DeepTutor, 43.7k★) and a near-unstarred one (several 1–4★ repos) are
  evaluated on what they actually do, not ranked by popularity.
- **The forgetting-curve-on-structure idea is logged as queued, not recommended.** It is one
  indie project with no outcome data, and adopting it would touch the tracker-writer's
  validated-transition design (§10c) — a bar this review has not attempted to clear.
- **GitHub star/fork/issue counts for Eero Alvar's and the indie projects were not
  independently re-verified for this specific document** beyond what the prior research
  sessions already confirmed against GitHub's own API — see session history for that
  verification. Numbers here match what was already checked, not re-pulled.

Uncertainty worth flagging: Eero Alvar's app is described in the video as free and
open-source, but no repository link was captured during video review — if his source becomes
relevant to cite directly later, it needs locating first.
