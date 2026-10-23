# ADHD Learning System — Design Reconciliation

**Sources reconciled:** Angus Sewell "Build Your Own AI Tutor" (`magnet_1782917051.pdf`) × Gemini Deep Research, *Neuro-Cognitive Architecture of Adult ADHD Learning* (25 sources, majority PubMed/PMC — see Evidence base)
**For:** Orlando Castillo — any subject he wants to learn, no domain limit. Starting set listed in `specs/subjects.md`.
**Date:** 2026-08-03
**Amended:** 2026-08-09 — corrections 1–3 per `specs/build-plan.md` "Decisions pending sign-off," signed off 2026-08-09. See `specs/DECISIONS.md` for the consolidated decision record.
**Status:** design agreed, build in progress

---

## Verdict

The magnet guide gets the **control flow** right and the **asset design** wrong.

Its mastery gate is exactly what the research endorses — active retrieval with prediction-error resolution is the strongest single mechanism in the whole source set. What it gets wrong is treating audio, quiz and flashcards as the complete asset list, with no visual-spatial artifact and no reconciliation step between representations.

Keep the skeleton. Add the missing assets. Add the four loop phases it lacks.

> **Correction, 2026-08-09.** An earlier version of this document argued the verbal channel should be *replaced* by visual assets, on the premise that verbal processing is the specific ADHD bottleneck. **That premise is falsified.** Verbal WM deficit d ≈ 0.55, visuospatial d ≈ 0.49 — both impaired, similarly. Across Mayer's multimedia corpus (Cromley & Chen 2025, 591 effects), the strongest and most consistent result is **text + static diagrams together**. "Replace" is what the evidence rules out; "both, reconciled against each other" is what it endorses — which is precisely what the integration gate implements.

---

## The three-layer architecture

**Adopted 2026-08-09 (correction 3).** The original framing — one visual-spatial method applied to any subject — does not survive the research. The system has three layers instead, and the five-phase loop below sits inside layer 1.

### Layer 1 — Universal

Retrieval practice + distributed practice. The only two techniques rated **HIGH** for cross-material generalization (Dunlosky et al. 2013). These apply to every subject, unconditionally. The five-phase loop and the mastery gate live here.

### Layer 2 — ADHD supports

Applied on top of layer 1, regardless of subject:

- **Externalize state** — never require the learner to hold progress in working memory
- **Tablet/laptop over handwriting** — handwriting measurably hurts this profile (Shimko & James 2025)
- **Commitment device over reminders** — notification-based adherence failed in an ADHD RCT (Nordby et al. 2022, n=109)
- **A floor under every adaptive rule** — see "The floor," below

### Layer 3 — Subject-type router

Representation chosen by **material type**, not by learner preference. Interleaving is **+0.67 for paintings and −0.39 for vocabulary** (Brunmair & Richter 2019) — one global setting would actively damage half of what this system is pointed at.

This is an **ability/material moderator, not a learning style.** The distinction is what keeps this out of learning-styles pseudoscience (refuted: Pashler et al. 2008; Kirschner 2017). Nothing in this system may be justified by "Orlando is a visual learner."

**Built last** — it earns its keep only once material is actually flowing.

---

## Conflict matrix

| Magnet piece | Research finding | Verdict |
|---|---|---|
| Audio deep-dive + quiz + flashcards as the complete asset set | Text + diagrams together is the strongest multimedia result (591 effects). Verbal-only omits the stronger pairing | **FIX** — add a visual-spatial artifact alongside, not instead of, verbal assets |
| Conversational oral exam (OP4) | Active retrieval + prediction-error resolution → phasic striatal dopamine → lowered LTP threshold | **KEEP** — strongest piece in the guide |
| One `current` row, everything else locked | Reduces decision load; supports salience-driven focus | **KEEP** |
| `done / current / locked` status enum | Binary states carry no calibration signal | **FIX** — add a Paas effort rating per sprint |
| "Fumble → stay on this lesson until it clicks" | Repeating unchanged is demotivating and stalls the system | **DROP** — replaced by the escape hatch |
| No time structure | Short focused sprints as a working default | **ADD** (as a default, not a finding — see below) |
| Linear lesson ladder | Hierarchical drill-down balances load | **FIX** — replace ladder with layered graph |
| NotebookLM MCP as engine | No public developer API (enterprise-gated only, verified 2026-08-09) | **DROP as engine** — but see "Gemini Notebook," below |
| No deliberate failure testing | Prediction error on resolution is the dopamine trigger driving LTP | **ADD** — highest-value missing piece |
| No redraw-from-memory step | Proceduralization shifts execution prefrontal → basal ganglia; durability comes from here | **ADD** |

---

## The five-phase loop (inside layer 1)

Magnet implements roughly one and a half of these.

| # | Phase | Protocol | Magnet status |
|---|---|---|---|
| 1 | Visual schema deconstruction | Parse the system into functional nodes + spatial relationships | **missing** |
| 2 | Micro-sprint translation | Short bursts turning schema nodes into working logic | partial (unstructured) |
| 3 | Socratic self-explanation | Articulate *why* the architecture is built that way | present (OP4) |
| 4 | Predictive error testing | Deliberately break it; analyze the failure | **missing** |
| 5 | Model refactoring | Redraw the architecture from memory / restructure it | **missing** |

Phase 4 is the one worth building first *within the loop*. For technical material it's nearly free: break the loop, drop a tool call, malform the payload, watch what happens. That's a prediction error and a real debugging skill in the same rep.

**Note on sprint length (corrected 2026-08-09):** the "15-minute micro-sprint" is a **working default, not a research finding.** No source in the evidence base establishes it, and the 15-minute-attention-span claim it echoes is itself a myth (Bradbury 2016). Use it as a starting point and tune by feel. Session length is bounded by the Paas floor, not by a clock.

---

## The integration gate — non-negotiable

The loop **does not advance out of phase 1** until the schema has been explained back in prose.

Drawing without integration scores **g = −0.15** — worse than no activity at all. With a step forcing verbal-visual reconciliation, **g = +0.35**. The active ingredient was never the picture; it is the reconciliation between representations.

---

## The floor — non-negotiable

CSAL AutoTutor, n=252: *"Gains in comprehension scores were highest for conscientious readers, lowest for struggling readers."* **Adaptivity without a floor amplifies the gap.**

An effort reading of **7–9 on the Paas 9-point scale** reduces scope and adds scaffold. It never presses on.

> **Correction, 2026-08-09.** This replaces the original "hold load at 40–60% of working-memory capacity, <40% → DMN intrusion, >75% → fronto-parietal desynchronization." **That band was never measurable during a session** — you cannot instrument your own WM load percentage while studying — and the underlying claim rested on a single systematic review graded Moderate–directional. The Paas 9-point self-rated mental-effort scale replaces it: subjective, validated, and actually collectable mid-session.

---

## Information design rules — how material should be formatted

Directly operational. These govern how every agent in this system formats learning material.

| Rule | Mechanism | Implementation |
|---|---|---|
| Spatial matrix layouts | Reduces prose-decoding load | Tables and grids over multi-paragraph prose |
| Functional colour coding | Consistent mapping aids search | Strict functional colour roles — Execution / Logic gate / Exception — held constant across all diagrams, **always with a redundant non-colour cue** |
| Dynamic retro-cueing | Re-allocates working memory to active nodes | Highlight the active path, dim the inactive |
| Visual clutter elimination | Prevents load saturation | No decorative graphics, no redundant restatement |
| Hierarchical modular structure | Keeps load manageable | Drill-down layers, never one flat dense view |

**Corrected 2026-08-09:** the original table justified colour coding by "amplifies the N2pc early-attention signal" and hierarchical structure by "keeps IFG load in the 40–60% window." Both are over-specific neural claims the evidence base does not support at that resolution. The *practices* stay — they are sound universal-design choices — but the justifications are now stated at the level the evidence actually supports. Colour must always carry a redundant non-colour cue (WCAG 2.2 floor).

**Dyslexia content-authoring rules** (from `specs/research/2026-08-09_dyslexia-cognitive-science.md`) apply to all authored material: morphology-first vocabulary glossing, capped sentence complexity, chunking. Audio/TTS is a real accommodation (d ≈ 0.35). **No "dyslexia fonts"** — debunked; letter-spacing helps, the font does not.

**Note the irony:** the Angus PDFs themselves violate most of these — dense multi-column layout, decorative flourishes, text competing with graphics. Converting them to plain `.md` measurably improved their readability for this profile. Keep consuming that vault as markdown.

**Caution on colour:** the functional colour scheme serves cognition, not brand. Do not reuse an existing brand palette here — brand palettes optimize for identity, and collapsing the two will weaken both.

---

## Revised system

| Piece | Magnet version | Revised |
|---|---|---|
| 1. Tracker | `Level, Lesson, Status(done/current/locked)` | Add `load_rating` (Paas 1–9), `last_retrieved`, `strength`, `lapses`, `escape_count` |
| 2. Lesson engine | NotebookLM MCP → audio + quiz + cards | Local: **visual schema + verbal explanation together**, reconciled via the integration gate |
| 3. Study | Listen → test → drill | Deconstruct schema → translation sprint → self-explain |
| 4. Examiner | Oral exam, no rubric | Oral exam **with written rubric** + deliberate-break test + redraw from memory |
| 5. Loop | Pass unlocks next | Pass unlocks next **or** routes to review; fail triggers escape hatch, never a hard repeat |

### The escape hatch (replaces "stay until it clicks")

On a failed gate, choose one — **never repeat unchanged**:

| Route | When | Effect on load |
|---|---|---|
| **Decompose** | Concept has too many interacting parts | Lowers intrinsic load |
| **Reframe** | Format isn't landing | Lowers extraneous load |
| **Park** | Prerequisite is missing elsewhere | Removes the block; route around |

Three consecutive failures on one lesson auto-parks it. The system must never be able to stall.

> **Correction, 2026-08-09.** The original justification — "repeated exposure past the 75% threshold suppresses plasticity outright," making repetition *actively harmful* — is **deleted.** It contradicts the prediction-error mechanism this same document depends on: if error and re-attempt drove plasticity suppression, phase 4 (deliberate failure testing) would be self-defeating. The escape hatch stands as a **motivational and anti-stall rule**, which is what the evidence actually supports, not a neural claim.

### Capture inbox

Missing from magnet entirely. Real learning triggers are external and unpredictable — a bug at work, a question from a customer, a pattern in a deal. One-line capture, no structure required at capture time. The engine converts inbox items into lessons later.

---

## Gemini Notebook — reading accommodation, not engine

**Verified 2026-08-09.** NotebookLM was rebranded **Gemini Notebook** (July 2026). A programmatic API now exists but is **enterprise-gated** (Google Cloud arrangement, VPC-SC/CMEK) — there is still no self-serve developer API. Browser-automation MCPs exist but rely on stealth fingerprinting against Google's ToS, and are rejected.

**However:** Gemini Notebook is now natively integrated into the Gemini app for AI Pro subscribers — notebooks can be created, attached as conversation sources, and bound to a Gem. Orlando has Google AI Pro, so this is available first-party, on his real account, at no additional cost.

**Role in this system:**

- **Audio overviews** of dense primary sources (CA F&I law, Reg Z/TILA, dealer regs). Audio bypasses decoding load entirely — the highest-value use for this profile.
- **Source-grounded Q&A with citations** when stuck on a specific passage.
- **Not** the plan generator — a domain map and prioritized reading list already exist.
- **Not** the mastery gate. See the boundary rule below.

> **The boundary — Gemini helps you learn it; the Examiner decides whether you know it.**
> Bastani et al. (PNAS 2025): AI tutoring helps only when guardrailed to hints rather than answers. Unguarded, it raises in-session performance while *eroding* unassisted performance. A source-grounded assistant that always explains is exactly that shape. It must never issue a mastery verdict.

**Known seam:** material produced in Gemini lives in Google's product, not the vault. Export to Markdown is manual and currently undesigned — see open items.

---

## Evidence base

25 sources supplied, majority primary peer-reviewed (PubMed / PMC), directly on-topic.

| Claim layer | Coverage | Confidence |
|---|---|---|
| ERP markers, fronto-parietal deficits, EEG theta/alpha | ~10 primary studies on adult ADHD working memory | **High — rely on as-is** |
| Verbal vs visuospatial WM deficit (d ≈ 0.55 / 0.49) | Alderson et al. 2013 meta-analysis | **High** |
| Text + diagrams together outperforms either alone | Cromley & Chen 2025, 591 effects | **High** |
| Integration gate (g = −0.15 without / +0.35 with) | Leutner & Biele 2025 | **High** |
| Method of loci / spatial dual-coding | Ondřej 2025 meta-analysis | **Moderate** — real effect is **g ≈ 0.42–0.65**, not d = 0.88 |
| Retrieval + distributed practice as HIGH-utility | Dunlosky et al. 2013 | **High** |
| Interleaving reverses by material type | Brunmair & Richter 2019 | **High** |
| Adaptivity floor | Fang et al. 2021 (CSAL AutoTutor, n=252) | **High** |
| Enactment / visuo-motor anchoring | Direct recall study | **High** |
| Sprint length, functional colour codes, the 5-phase loop | No corresponding source | **Default — tune by feel** |
| Review scheduling / spacing | Absent from *this* evidence base; covered separately in `specs/research/2026-08-08_spaced-repetition-tools-and-adherence.md` | **Judgment call — see open items** |

> **Correction, 2026-08-09.** The original table cited method of loci at **d = 0.88, graded High.** The headline figure did not survive re-examination; the defensible range is **g ≈ 0.42–0.65**, and the confidence grade drops to Moderate. It is no longer load-bearing for any design decision.

Weaker entries in the original list (Reddit, a commercial EEG vendor blog, news-medical) map to peripheral claims about hyperfocus, not to any core mechanism above.

The source set handled one contradictory finding well: *"The Ability to Direct Attention in Working Memory Is Not Impaired in Adults With Symptoms of ADHD"* is used correctly — to support retro-cueing as an intact capability — rather than omitted.

---

## Open items

**1. Spacing is genuinely absent from *this* evidence base.**
The original research routes retention through proceduralization and LTP via prediction error, and never addresses review intervals. Later research (`2026-08-08_spaced-repetition-tools-and-adherence.md`) supplies external support, but the original 25-source set did not. The review queue is built as a **judgment call backed by separate research**, explicitly not as a finding of the source set this document reconciles.

**2. Pass-rate calibration vs. the adaptivity floor.**
How to detect a lenient Examiner without violating the floor. A pass-rate that is "too high" could mean lenient grading — or a learner being correctly scaffolded. Flagged, **not resolved**. Do not implement an automatic difficulty increase on high pass rates.

**3. The Gemini → vault export seam.**
Manual today, undesigned. Material will silently accumulate outside the system if this isn't handled deliberately.

**4. No STUDY-session trigger is specified.**
The system has a review queue and a mastery gate but nothing describing how the learner arrives at a session. Queued — see `DECISIONS.md` §11.

---

## Build plan

Superseded by the build order in `specs/build-plan.md`, reproduced here for reference:

| Step | Deliverable | Status |
|---|---|---|
| 1 | Amend this document (corrections 1–3) | **done 2026-08-09** |
| 2 | Obsidian vault + folder convention | in progress |
| 3 | **Examiner** — the mastery gate | next |
| 4 | `.apkg` generation → review queue | |
| 5 | Canvas layer + integration gate | |
| 6 | Subject-type router | last |

Step 3 is the piece that makes everything else real: it is the only component rated High, and it works before any visual layer exists.
