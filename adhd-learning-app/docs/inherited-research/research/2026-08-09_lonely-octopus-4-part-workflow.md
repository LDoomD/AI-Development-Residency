# External Framework Review — Tina Huang's 4-Part AI Learning Workflow

**Source:** "How to Learn 10x Faster: A 4-Part Workflow Using AI" — Tina Huang, July 2026,
published at `resource.lonelyoctopus.com/doc/d84f0222-d86b-46be-ba3f-0a4f76e41a5d`
(companion YouTube video referenced but not reviewed here).

**Reviewed:** 2026-08-09. Source supplied by Orlando, who holds a Notion Student Pro
licence and already uses Notion.

**Evidence grade of the source itself: None — practitioner workflow, not research.**
This is one creator's personal workflow. It cites no studies, reports no outcomes, and
makes no measured claims. It should be read as a **design input**, never as evidence, and
nothing in it may be cited in `build-plan.md` or `adhd-learning-system-design.md` as
support for a decision. It is reviewed here because it is well-constructed and because it
addresses a real gap this project has, not because it validates anything.

---

## Executive summary

This framework solves a **different problem** than the one this project has been building
for, and that is the single most important finding in this review.

It is a **planning and follow-through** workflow: how to find the right path through a new
subject, personalize it, and actually execute against it. This project's system is an
**encoding and retention** workflow: how to make studied material stick.

Nothing in the four steps verifies that learning occurred. There is no retrieval practice,
no spaced repetition, no mastery gate, no comprehension check. Step 4 is named "The Memory
System" but is a record of *what you did* — Pomodoro logs, notes, resources — not a system
for *remembering what you studied*. That is not a flaw in the framework; it is simply out
of its scope.

The recommendation is therefore **compose, do not choose**. Steps 1–2 are worth adopting
as a new front-end phase ahead of the existing 5-phase loop, because they fill the exact
gap `2026-08-09_new-research-synthesis.md` (Part 3, item 11) already identified — the
project specifies a review queue and a mastery gate but nothing about *how the learner
arrives at a session with something to study in the first place*. Step 3 should be
harvested for function and its implementation skipped. Step 4 substantially converges with
decisions this project already made independently.

---

## The framework as published

| Step | Name | What it does | Tool |
|---|---|---|---|
| 1 | Stand on the Shoulders of Giants | Gather real sources on a topic, import them, generate a structured multi-week study plan **built from those sources** | Gemini Notebook (formerly NotebookLM) |
| 2 | Customize It for You | Paste the generic plan into a chatbot with full personal context; it cuts what doesn't apply and rebuilds around actual level and goal. Then convert to an interactive HTML checklist | Claude (or preferred model) |
| 3 | The Productivity System | A bespoke always-on-top pixel-art macOS Electron app ("Typewriter") that displays and tracks Markdown checklists, logs sessions, and persists progress | Custom app, built with Codex |
| 4 | The Memory System | Everything — Pomodoro logs, study plans, notes, resources — into a persistent searchable store; point a local AI agent at it to query your own learning history | **Obsidian** |

The document also includes a model-routing table: local models for anything private,
ChatGPT for visual/diagram-heavy material, Gemini for large context, Claude for speed and
directness.

---

## Findings

### 1. Convergent validation on Obsidian (mild positive signal)

Step 4 independently arrives at Obsidian as the central persistent store, which is this
project's locked choice (`build-plan.md`, "Stack decision"). This is worth noting but
worth **not overweighting**: two practitioners choosing the same popular tool is weak
evidence, and `build-plan.md`'s own standing caveat applies unchanged — no controlled
study of any notes/PKM tool improving learning outcomes exists, so nothing built on
Obsidian inherits credibility from that choice.

### 2. The NotebookLM usage is consistent with the existing decision

Step 1 uses NotebookLM as a manual, human-in-the-loop surface — exactly the role
`build-plan.md` ("NotebookLM: retained as a manual surface, not as engine") already
assigns it. The verified 2026-08-08 finding that NotebookLM has **no public developer
API** is unchanged and constrains adoption: Step 1 cannot be automated into an agentic
loop. It stays a manual step the learner performs, with the output dragged into the vault
as Markdown.

This is a real limitation on the "agentic loops" ambition, not a fatal one. The plan-
generation step happens once per subject, not once per session, so manual execution is
tolerable.

### 3. Source-grounded plan generation is a meaningful safety property

The framework generates the plan **from imported real sources**, not from model memory.
This distinction matters and should be preserved if adopted. It is the difference between
a plan whose reading list points at material that exists and one whose reading list is
plausible-sounding hallucination — a risk `2026-08-09_ai-tutor-landscape-2026.md` flagged
for AI-generated study content generally.

Residual risk that remains even with source grounding: the model chooses *sequencing and
emphasis*, and nothing validates that its chosen order is pedagogically sound. Treat the
generated plan as a strong first draft to be reviewed, not as an authority.

### 4. Externalized visible checklist — genuinely aligned with the ADHD support layer

Step 2's interactive HTML checkoff artifact and Step 3's always-visible checklist window
both implement **externalizing state** — the core of this project's ADHD support layer
(`adhd-learning-system-design.md`). Progress is visible without being recalled from
working memory, which is the mechanism that matters given the verbal/visuospatial WM
deficits already documented (Alderson et al. 2013, d ≈ 0.49–0.55, already cited).

Notably, this externalization is **guilt-free by construction** — it shows what remains,
not a streak that can be broken. That is compatible with this project's locked rejection
of streaks and loss-aversion mechanics. If adopted, this property must be preserved
deliberately; it would be easy to add a streak counter to a checklist app and silently
violate a locked decision.

### 5. Pomodoro / fixed timers — partial conflict with a locked decision

Step 3 builds around Pomodoro-style timed sessions. This project already reviewed and
declined fixed hard timers in favour of the **Paas 9-point subjective effort scale**,
based on the Smits et al. (2025) Pomodoro/Flowtime RCTs already cited in
`2026-08-08_visual-spatial-encoding.md`.

**Resolution: take the logging, decline the timer.** The valuable part of Step 3 is that
sessions get *recorded* — duration, what was worked on, whether it completed. The rigid
25-minute enforcement is the part the evidence does not support and the project already
rejected. Log sessions; don't let a countdown dictate when to stop.

### 6. The Typewriter app is a large detour, and its function is nearly free

The published Electron app specification is long and detailed (frameless always-on-top
window, pixel-art styling, custom fonts, sounds, confetti, progress sidecars). Building it
would be a substantial project in its own right and sits nowhere in `build-plan.md`'s
locked build order — which puts **Examiner first**, as the only component rated High.

The *function* it provides — a visible checklist plus a session log — is available on day
one as a plain Markdown file in the Obsidian vault, which is where Step 4 says everything
should end up anyway. Recommend explicitly declining the app build and capturing the
function in Markdown.

### 7. The critical gap: nothing checks whether learning happened

Across all four steps there is no retrieval practice, no spacing, no mastery gate, no
comprehension check. The workflow's completion signal is **"the checkbox is ticked"** —
that is, activity, not understanding.

This is precisely the failure mode this project's Examiner exists to prevent, and it maps
directly onto the risk pattern already documented in `2026-08-09_ai-tutor-landscape-2026.md`
via Bastani et al. (PNAS 2025): systems that make practice feel productive can boost
in-session performance while leaving unassisted later performance flat or worse. A ticked
checklist is a very weak proxy for learning.

Stated plainly: **this framework would get Orlando to the desk with a good plan and a
clear next action, and would not, on its own, produce retention.** That is the half this
project already built. The two halves are complementary and neither is sufficient alone.

### 8. On the "10x" title

The framework's title uses the same "10x" expression that prompted
`2026-08-09_10x-learning-claims-audit.md`. The document makes no measured claim to back
it — no figures, no comparison, no outcome data — so it is best read as marketing
phrasing, consistent with Orlando's clarification that his own use of "10x" was an
expression rather than a target. The audit's conclusion is unaffected and unchanged: the
honest metrics remain **repetitions-to-criterion** and **30-day retention against your own
prior baseline**.

---

## What this means for the build plan

Nine concrete items. None of these are applied — this is a proposal for review.

### Recommended: adopt as a new front-end phase

1. **Add a "Phase 0 — Plan intake" to `adhd-learning-system-design.md`'s loop**, ahead of
   the existing 5-phase cycle. Three steps, all manual, run once per subject rather than
   once per session:
   (a) source-grounded plan generation (NotebookLM, per its existing manual-surface role);
   (b) personalization pass against Orlando's actual background, ADHD/dyslexia profile, and
   goal;
   (c) output committed to the vault as plain Markdown.
   This fills the gap Part 3 item 11 of `2026-08-09_new-research-synthesis.md` already
   identified.

2. **Require the personalization pass (1b) to carry the dyslexia content-authoring rules**
   from `2026-08-09_dyslexia-cognitive-science.md` — morphology-first vocabulary glossing,
   sentence-complexity caps, chunking. The plan-customization prompt is the natural place
   to enforce these, because it is the moment content structure gets decided. This makes
   item 4 of the synthesis's next-steps list concrete rather than aspirational.

3. **Require plans to be source-grounded, and record the source list in the vault
   alongside the plan.** Non-negotiable if Phase 0 is adopted; it is the property that
   separates a real reading list from a hallucinated one.

4. **Add an explicit handoff from Phase 0 into the existing loop.** The plan produces
   *what to study in what order*; the existing 5-phase loop and the Examiner remain the
   only things that determine whether any of it was learned. The handoff should be written
   down so the plan is never mistaken for the system.

### Recommended: harvest function, decline implementation

5. **Adopt the visible-checklist externalization as a plain Markdown file in the vault** —
   not an Electron app. Explicitly note in the build plan that the Typewriter app is
   reviewed and declined, so it does not resurface later as an apparently-endorsed idea.

6. **Adopt session logging; decline the Pomodoro timer.** Record duration, subject, and
   completion. Keep the Paas 9-point effort scale as the stop signal, per the locked
   decision.

7. **Add a "no streak on the checklist" note to the never-list** (the drift-guard artifact
   proposed in `2026-08-09_agentic-tutoring-workflow-design.md`). A progress checklist is
   one small feature away from becoming a streak mechanic, and the never-list is the
   mechanism that is supposed to catch exactly this.

### Recommended: no change

8. **The model-routing table needs no action.** It is sensible practitioner advice and
   overlaps conceptually with the project's subject-type router, but the router is locked
   as *last* in the build order and is about matching **technique to material type** — an
   evidence-backed decision (Brunmair & Richter 2019, already cited) — not about matching
   vendor to task. Do not conflate them.

9. **Obsidian stays locked; this review does not strengthen the case.** Convergence noted,
   `build-plan.md`'s no-PKM-evidence caveat unchanged.

---

## Adversarial review notes

This brief was written from the primary source directly (full page text extracted and
read) rather than from a summary, so the framework description above is verified against
what the document actually says, not reconstructed from memory or from the video.

Claims deliberately **not** made:

- **No efficacy claim is attributed to this framework.** The source reports no outcomes,
  so this brief grades it "Evidence: None" and treats it purely as a design input. The
  "10x" in its title is explicitly identified as unbacked marketing phrasing rather than
  quietly repeated.
- **The Obsidian convergence is deliberately downgraded.** Two practitioners picking the
  same popular tool is weak evidence; it is reported as a mild signal and paired with the
  existing no-evidence caveat rather than presented as validation.
- **Bastani et al. (PNAS 2025) is applied by analogy, not as direct evidence.** That study
  concerns AI tutoring guardrails, not checklist-based planning workflows. It is cited
  here for the *pattern* — activity metrics diverging from unassisted performance — and
  the analogical nature of the link is stated rather than hidden.
- **The Pomodoro conflict is stated as a partial conflict with an existing project
  decision**, not as a claim that Pomodoro is ineffective in general. The Smits et al.
  (2025) finding already in this project's corpus is the basis; no new claim is added.
- **No claim is made about the YouTube video**, which was referenced by the document but
  not reviewed. If it contains material claims or outcome data not in the written
  document, this review would need updating.

Uncertainty worth flagging for Orlando: the source is a Notion-published document behind a
custom domain, and this review captured it on 2026-08-09. Published practitioner workflows
change without version history, so the description above may drift from the live page.
