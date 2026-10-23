# DECISIONS — single source of truth

**What this is:** every decision made across all research to date, in one place. If a
question is "what did we decide about X," the answer is here or it isn't decided.

**Last updated:** 2026-08-09
**Research behind it:** 11 briefs (2026-08-08) + 6 briefs + synthesis (2026-08-09) +
external framework review (2026-08-09). All in `specs/research/`.

**How to read the grades:** *Locked* = decided, build against it. *Queued* = proposed by
research, not yet signed off. *Rejected* = considered and declined, with the reason, so it
doesn't resurface.

---

## 1. The stack — LOCKED

| Layer | Choice | Why |
|---|---|---|
| Content + canvas | **Obsidian** | Plain Markdown + JSON Canvas, no lock-in, near-zero exit cost |
| Review queue | **Anki** (`.apkg` / FSRS) | Real spaced-repetition engine, open, portable |
| Examiner / agent layer | **Claude Code skill/subagent** (covered by existing Claude Max) | Only piece rated High. A mastery gate is inherently interactive, so it belongs in a session — not a scheduled API script |
| Reading accommodation | **Gemini Notebook** (covered by existing Google AI Pro) | Audio overviews + source-grounded Q&A over dense primary material |
| Card generation | `anki-llm` / `pdf2anki` style scripts | Open source, writes into existing Anki, doesn't touch FSRS |

### Cost — $0 incremental

Everything above runs on subscriptions Orlando already pays for.

| Component | Covered by | Extra cost |
|---|---|---|
| Examiner | Claude Max | $0 |
| Gemini Notebook | Google AI Pro | $0 |
| Obsidian | free | $0 |
| Anki | free / open source | $0 |
| Card-generation scripts | free, run via Claude Code | $0 |

**Correction to `2026-08-09_oss-vs-paid-stack-synthesis.md`:** that brief estimated
~$5–20/mo for the Examiner. It assumed a standalone script calling the **Anthropic API**
(pay-per-token, billed separately from Max — the two are genuinely distinct). The brief was
not told about the existing Max and Google AI Pro subscriptions. With those, the estimate
drops to **$0**, and the Claude Code path is also the better architecture: a gate needs a
person present, so unattended scheduled runs buy nothing.

The only future case that would need real API billing is high-volume batch generation
(e.g. cards across a large PDF corpus at once). Not on the roadmap.

**Standing caveat:** no controlled study shows any notes/PKM tool improves learning
outcomes. Nothing here inherits credibility from the tool choice. Any evidence this system
has will come from its own design.

---

## 2. The architecture — LOCKED

**Three layers, not one universal method.**

1. **Universal layer** — retrieval practice + distributed practice. The only two techniques
   rated HIGH for cross-material generalization (Dunlosky et al. 2013).
2. **ADHD supports** — externalize state, tablet/laptop over handwriting, commitment device
   over reminders, a floor under every adaptive rule.
3. **Subject-type router** — representation chosen by material type. Interleaving is +0.67
   for paintings and −0.39 for vocabulary (Brunmair & Richter 2019); one global setting
   would damage half of what this is pointed at. **Built last.**

---

## 3. Non-negotiable mechanisms — LOCKED

| Mechanism | Rule | Evidence |
|---|---|---|
| **Integration gate** | Any visual/diagram artifact must be followed by verbal explain-back. The loop does not advance until the schema is explained in prose. | Drawing without reconciliation g = −0.15; with it g = +0.35 |
| **The floor** | Paas effort reading 7–9 → reduce scope, add scaffold. **Never press on.** | CSAL AutoTutor n=252: adaptivity without a floor amplifies the gap for struggling readers |
| **Escape hatch** | On a failed gate: decompose / reframe / park. **Never repeat unchanged.** 3 consecutive failures auto-park. | Motivational rule (not a plasticity claim — that version was falsified) |
| **Both channels** | Visual *and* verbal, together. Not visual instead of verbal. | Verbal WM deficit d≈0.55, visuospatial d≈0.49 — both impaired similarly. Text+diagrams is the strongest result across 591 effects (Cromley & Chen 2025) |
| **Effort measurement** | Paas 9-point self-rated scale. | Replaces the 40–60% load band, which was never measurable during a session |
| **Capture inbox** | One-line capture, no structure required. Engine converts to lessons later. | Real learning triggers are external and unpredictable |

---

## 4. What we rejected, and why — LOCKED

So these don't come back:

| Rejected | Reason |
|---|---|
| Streaks, XP bars, leaderboards, consumable lives/hearts | Loss-aversion guilt mechanics; extrinsic rewards undermine intrinsic motivation (Deci/Koestner/Ryan 1999) |
| Push notifications / reminders as adherence | Failed in an ADHD RCT (Nordby et al. 2022, n=109) |
| "Dyslexia fonts" (OpenDyslexic etc.) | Debunked (Rello & Baeza-Yates 2013; Wery & Diliberto 2017). Letter-spacing helps; the font does not |
| Learning-styles framing anywhere | Refuted (Pashler et al. 2008; Kirschner 2017) |
| Hard timers / rigid Pomodoro | Paas scale replaces it (Smits et al. 2025) |
| Orton-Gillingham as a design principle | Its own best evidence (Stevens et al. 2021) found non-significant effects even in children |
| Newport's *Deep Work* long-block model | Conflicts with the ADHD attention-regulation literature already cited |
| NotebookLM MCP / browser automation / burner Google account | No public API (enterprise-gated only); Patchright stealth automation is a ToS + fragility problem — **and unnecessary, since Gemini Pro gives first-party access** |
| AI tutoring SaaS (Socra, StudyFetch, etc.) | No independent efficacy data; would replace the validated stack |
| The "Typewriter" Electron app | Function (visible checklist + session log) is free as a Markdown file in the vault |
| Objective cognitive transfer as an outcome metric | Two RCTs found none. Design for function/completion/QoL instead |
| Citing popular science books as evidence | Kahneman disowned his own Ch.4 priming studies; Ericsson disavowed the 10,000-hour rule; Duhigg's keystone habits have no controlled evidence |

---

## 5. Claims we killed — LOCKED

Four claims in the original design doc were falsified by research and must be corrected:

| Claim | Status |
|---|---|
| Method of loci `d = 0.88` | **Wrong.** Real value `g ≈ 0.42–0.65`. Cite `g = 0.65` |
| 40–60% working-memory load band | **Not measurable.** Replaced by Paas 9-point scale |
| 15-minute micro-sprint as a *finding* | **It's a default**, not a research result. Relabel |
| "Repeated failure suppresses plasticity" | **Delete.** Contradicts the prediction-error mechanism the same doc depends on |

Also: the scope line still reads "AI engineering + UX design." Should be general scope —
the router carries specificity instead.

---

## 6. The "10x" question — DECIDED

**Retired as a literal target.** No technique produces an order-of-magnitude speedup in
genuine learning. Every commercial claim in that direction is debunked or unstudied.

**What's real, by dimension:**
- First-pass encoding speed — barely moves (desirable difficulties deliberately make it feel *slower*)
- Repetitions to reach mastery — moves meaningfully
- **30-day retention at equal study time — the biggest, most defensible effect**

**Where a felt 10x legitimately comes from:** replacing a near-zero-efficiency baseline
(cramming, re-reading, highlighting), not from compressing cognition.

**The two honest metrics:** repetitions-to-criterion, and 30-day retention — measured
against *your own prior baseline*, not a fixed multiplier.

---

## 7. Dyslexia — content authoring, not CSS — LOCKED

The biggest gap the new research closed. Adult dyslexia is a phonological + orthographic
decoding deficit, not a font problem.

**Rules that govern all authored content:**
- Morphology-first vocabulary glossing (break words into meaningful parts)
- Capped sentence complexity
- Chunking
- TTS / audio as a real accommodation (d ≈ 0.35 — modest but real)

**Typography (already locked from UX research):** 16px+ system sans-serif, 1.5 line-height,
60–66ch width, increased letter-spacing available up to +0.1em, 3 fixed functional colour
roles with redundant non-colour cues, WCAG 2.2 floor.

---

## 8. Tool boundaries — LOCKED

**The one rule that matters:**

> **Gemini helps you learn it. Claude decides whether you know it.**

| Tool | Does | Does NOT |
|---|---|---|
| **Gemini Notebook** | Audio overviews of dense primary sources; grounded Q&A with citations when stuck on a passage | Decide mastery. Generate your study plan (you already have one). Generate your cards |
| **Claude / Examiner** | Mastery gate, evidence-before-verdict grading | Answer freely during a gate |
| **Anki** | Review queue, FSRS scheduling | — |
| **Obsidian** | Durable storage, canvas, `tracker.md` as sole durable state | — |

**Why the boundary is strict:** Bastani et al. (PNAS 2025) — AI tutoring helps only when
guardrailed to hints, not answers. Unguarded, it boosts practice scores while *eroding*
unassisted exam performance. A source-grounded chatbot that always explains is exactly that
failure shape.

**Known seam:** anything produced in Gemini lives in Google's product, not your vault.
Export to Markdown is manual. Material will silently accumulate outside the system if this
isn't handled deliberately.

---

## 9. Agent design — LOCKED (design), NOT BUILT

- **One orchestrator + two narrow subagents:** an independent grading verifier, and a
  drift-checker against locked decisions. Not a swarm.
- **`tracker.md` is the sole durable state.** Not conversational memory.
- **Evidence-before-verdict grading** — structurally forced, not "be strict" in a prompt.
- **Content generation gated and separate from live tutoring** (hallucination risk).
- **A "never list"** — the drift guard that stops rejected mechanisms (streaks, timers,
  notifications) from creeping back in during future edits.

---

## 10. Build order — LOCKED

1. **Amend the design doc** per §5 corrections. One commit, no new research. ← *approved 2026-08-09*
2. **Stand up the Obsidian vault** + commit the folder convention
3. **Examiner first** — the mastery gate. Only piece rated High; works before any visual layer exists
4. **`.apkg` generation** — passed material lands in a real review queue
5. **Canvas layer + integration gate** — most likely to need iteration; does nothing without the gate
6. **Router — IN PROGRESS (started 2026-08-11)** — `src/router/route_lesson.py`. Reads a
   lesson's `modes:` frontmatter and dispatches MAP→canvas/gate, DRILL→Anki, EXAMPLES→Anki
   filtered deck, REPS(conversational)→Claude roleplay (see §10c). REPS(physical/
   production) has no mechanism yet — the router flags this loudly rather than silently
   no-oping. First lesson tagged: `learning/f-and-i-presentation/01-the-menu.md`
   (`modes: [MAP, DRILL]`). Remaining work: tag the rest of `learning/`, decide a
   physical/production REPS mechanism.

### 10b. EXAMPLES mode mechanism — LOCKED (promoted from research 2026-08-11)

**Anki filtered decks** (`Random` order + `Reschedule OFF`, i.e. preview mode) — a native
Anki feature, not an add-on. Promoted from `specs/research/2026-08-10_examples-mode-tooling-search.md`,
which was never adopted into the blueprint despite reaching a clear recommendation.

Reschedule OFF means answering a card in a filtered deck does not touch its FSRS
stability/difficulty/interval in the underlying DRILL schedule — EXAMPLES-mode drilling
and DRILL-mode spaced review can share the same cards with zero interference. Covers
6–7 of the 9 EXAMPLES-tagged subjects directly with card-content changes only (ear
training, listening comprehension, UX/dog-behavior/ad pattern recognition). Two
exceptions carried over from that research, not solved here: synthesis ear training has
no ready tool (hand-author audio cards into the same filtered-deck mechanism), and
`birdears` (AGPL-3.0) remains an optional standalone add for music ear training
specifically if procedurally-generated (not pre-recorded) intervals matter later.

### 10c. REPS mode mechanism — PARTIALLY LOCKED (decided 2026-08-11)

**REPS is not one mechanism.** Of the 16 subjects tagged REPS in `subjects.md`, some are
conversational (F&I sales, comedy/charisma, communication/relationships) and some are
physical/production (sewing, body-composition training, vibe coding, writing poetry,
data analytics). These need different mechanisms and are decided separately, not forced
into one.

**Conversational REPS — LOCKED.** Claude as roleplay scene partner, per
`specs/research/2026-08-09_f-and-i-presentation-technique.md` §1 (117-study meta-analysis
on behaviour-modelling training, graded High): mixed positive/negative models (watch a
*bad* example alongside a good one, not just good ones — the most counterintuitive and
actionable finding), trainee-generated scenarios (write your own customer scenario rather
than only using canned ones), and an explicit goal set before each rep. Declarative
product knowledge decays; practised delivery does not — this is why REPS gets prioritized
over re-reading once MAP/DRILL are solid.

**Physical/production REPS — NOT DECIDED.** No research exists for this half of the tag
(sewing, body-composition training, vibe coding, writing poetry, data analytics, etc.).
Deliberately left open rather than inventing a mechanism with no evidence behind it —
same failure mode already flagged once this session for the router taxonomy and the
EXAMPLES-mechanism claim. Revisit when a lesson in one of these subjects actually needs
routing.

### 10a. Router trigger mechanism — LOCKED (decided 2026-08-11)

**Manual tag in lesson frontmatter, using the existing MAP/DRILL/EXAMPLES/REPS taxonomy
from `subjects.md` — not a new vocabulary.** Each lesson file in `learning/` carries a
`modes` field listing one or more of the four modes already defined in `subjects.md`:
MAP (structure, diagram + explain-back), DRILL (exact recall, spaced), EXAMPLES
(eye/ear training, shuffled volume), REPS (physical/verbal doing, no substitute). This is
**multi-value**, matching subjects.md's checkbox table — most subjects need 2+ modes at
once (e.g. F&I sales is MAP+DRILL+REPS). The router reads this tag rather than inferring
type from folder/subject or asking a classification question at creation time.

**Why manual over inferred:** mode is a property of the content, not of where it lives —
a single folder/subject mixes modes (F&I has MAP-type menu-structure material and
DRILL-type product/compliance facts). Inferring from location would misclassify. Asking
at creation time adds a step to authoring; a frontmatter field is a single deliberate
decision the author already has full context for.

**Correction:** an earlier version of this entry proposed inventing new tags
(`visual-spatial`/`verbal-recall`/`procedural`) without checking `subjects.md` first —
wrong, since the taxonomy this router is meant to serve already existed. Fixed 2026-08-11.

---

## 11. Queued — decided by research, NOT yet signed off

These came out of the 2026-08-09 briefs. Deliberately **not** blocking the build.

| # | Proposal | Source brief |
|---|---|---|
| 1 | Add 3 habit primary sources to the evidence table: Gollwitzer & Sheeran 2006 (implementation intentions, d≈0.65), Lally et al. 2010 (66-day median, range 18–254, missed days don't reset), Wood & Neal 2007 (habit cues) | book-synthesis-audit |
| 2 | Design a **STUDY-session trigger** as an if-then habit stack anchored to an existing routine — dashboard/environmental state, never a notification. Currently nothing specifies how you arrive at a session | book-synthesis-audit |
| 3 | Add the dyslexia content-authoring rules table to the design doc **before** any real F&I content is authored | dyslexia-cognitive-science |
| 4 | Add a **Phase 0 — plan intake** ahead of the 5-phase loop (source-grounded, manual, once per subject) | lonely-octopus review |
| 5 | Build the **never-list** + provider-agnostic Examiner wrapper *before* writing any agent prompt | agentic-workflow + oss-vs-paid |
| 6 | Prototype LLM card generation with **mandatory human review** | ai-tutor-landscape |
| 7 | Log two unresolved tensions as open items: pass-rate calibration vs. adaptivity floor; orchestration layer vs. three-layer architecture | synthesis |
| 8 | True Recall (second SRS system) — standalone yes/no decision | ai-tutor-landscape |
| 9 | Team-competition adherence mechanism — **deferred**, no home in a solo-learner architecture | learning-platform-ux |

---

## 12. Still genuinely open

1. **Spacing has no support in the original evidence base.** The review queue is a
   judgment call, explicitly not a cited finding. (The 2026-08-08 spaced-repetition brief
   adds external support, but the original design doc's evidence base did not contain it.)
2. **Pass-rate calibration vs. the adaptivity floor** — how to detect a lenient Examiner
   without violating the floor. Flagged, not resolved.
3. **The Gemini → vault export seam** — manual today, no design yet.
