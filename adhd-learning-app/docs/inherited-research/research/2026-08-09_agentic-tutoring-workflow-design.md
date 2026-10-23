# Research Brief: Persistent Multi-Session Agentic Teaching Loop

**Scope:** Architecture/design patterns for running the existing 5-phase learning loop (`specs/adhd-learning-system-design.md`) as an ongoing AI-agent-run process across many sessions, using Claude Code–style agents on top of the Obsidian+Anki compose path (`specs/research/2026-08-08_knowledge-management-tools.md`).
**Status:** Draft for review — not yet a build plan. Revised after two independent adversarial fact-checks; see "Adversarial review notes" at the end.
**Date:** 2026-08-09

---

## Executive Summary

The existing design already specifies *what* the loop should do (5 phases, escape hatch, Effort 1–9, integration gate). What it doesn't yet specify is *who runs it session over session* — how an agent examines rigorously instead of rubber-stamping, how quiz/practice content gets generated without hallucination, how the tracker stays the single source of truth under agent writes, and how any of this survives a hundred separate context windows without drifting off the locked decisions.

Four findings drive the design below:

1. **LLM-as-judge research documents real, specific bias risks in automated grading**, though the exact mechanism is narrower than "judges are simply fooled by confidence." The best-supported finding across the two peer-reviewed-adjacent sources actually checked is **self-preference/same-family bias** (judges favoring outputs similar to their own style) — a documented phenomenon in the LLM-judge literature, though not one either of this brief's two directly-fetched sources demonstrates firsthand (see finding notes and review notes below). Separately, at least one of those sources shows LLM judges' scores correlate with a model's own self-reported traits in ways that diverge from the model's actual behavior — a related but distinct caution about trusting model self-assessment, not evidence about grading *someone else's* answer. This is still a structural risk for a system whose entire mastery gate is oral-exam grading. The design response — forcing quote-per-criterion evidence rather than a holistic verdict — can be read as a rough analogy to forcing slow, deliberate (System-2-style) checking over fast, fluent (System-1-style) pattern-matching; that framing is this brief's own interpretive lens, not a claim drawn from the cited papers, and should be read that way.
2. **Context loss across sessions is a widely-discussed agentic failure class in current practitioner writing** — industry blogs and vendor content from 2025–2026 consistently name it alongside hallucinated actions and tool misuse as a recurring way agent systems break on long-running or multi-session tasks. This is practitioner-consensus-level evidence (not peer-reviewed research) but is directionally corroborated and low-risk to act on. A tutoring loop that runs for months needs an explicit state-restore contract, not "the agent will remember."
3. **The orchestrator-worker (hub-and-spoke) subagent pattern is widely recommended in current Claude Code / agentic-practice blogs** as the default multi-agent shape — a single orchestrator holds the big picture (tracker state, locked decisions, session history) and dispatches narrow-context specialist subagents (examiner, practice-composer, tracker-writer) for individual tasks, then reconciles their output before it touches the source of truth. This brief treats it as strong current practitioner guidance rather than an established academic standard, since the sourcing behind it is blog-tier, not primary Anthropic documentation or peer-reviewed work.
4. **Interleaved/deliberate practice has some controlled-trial support as a technique**, though the single study cited here is narrow (n=10 musicians, mixed significance) and should not be read as the full evidence base for interleaving generally — see caveat below. AnkiConnect and direct SQLite writes are documented ways to get agent-generated practice sets into Anki's review queue, but neither is actually "dependency-free" as originally claimed — see the corrected delivery-path section. This still closes a real gap the design doc's own research flagged: spacing/review has no ADHD-specific evidence behind it, but interleaving as a technique has some support, and the stack already chosen (Anki) supports it natively.

**Recommendation in one line:** build this as a single orchestrator agent with narrow tool-scoped subagents for the two genuinely adversarial jobs (grading, drift-checking), keep the tracker as the only durable state, and treat every subagent's context as disposable — never treat conversation memory as the system of record.

---

## Design constraints carried forward (not renegotiated here)

Three-layer architecture (retrieval+spacing / ADHD-support / subject-router); mandatory integration gate after visual artifacts; Effort 1–9 self-rating (not % cognitive load); decompose/reframe/park on failure, never repeat-unchanged; Obsidian (content+canvas) + Anki (.apkg/SQLite); no streaks/XP/leaderboards/lives, de-identified team competition only; no dyslexia fonts, no learning-styles framing; locked UX spec; no notification/reminder adherence mechanism; no chasing objective transfer as a metric; adaptivity must have a floor.

**One tension flagged, not resolved:** de-identified *team* competition as a gamification mechanic implies some cross-learner or cross-session leaderboard surface exists somewhere in the eventual system. Nothing in the current tracker/design touches multi-user data at all — this brief assumes it's out of scope for a personal, single-user build and doesn't design for it. Flagging so it isn't silently dropped if a team version is ever built.

---

## Proposed Workflow Design

### Why orchestrator-worker, not a swarm

Current practitioner guidance (2025–2026 Claude Code and general agentic-system blog content — see sourcing caveat in finding 3 above) converges on: default to a single agent; add subagents only where isolation earns its cost — parallelizable work, or work that needs a genuinely different incentive/context than the main thread. Two jobs in this loop actually need that isolation:

- **Grading** needs to *not* share context with the agent that just coached the learner through the lesson (a coach that also grades is the self-preference/leniency risk made structural).
- **Drift-checking against the locked decisions** needs to run with only the decisions doc and the proposed artifact in context — no session narrative to rationalize an exception.

Everything else (tracker updates, practice-set composition, session handoff) can run as tool calls from one orchestrator with good scoping, not separate agents. Over-decomposing into many agents multiplies the context-loss and coordination-failure surface for no benefit at this project's scale.

### Agent roles

| Role | Runs as | Context it gets | Context it must NOT get | Writes to |
|---|---|---|---|---|
| **Orchestrator** ("session-runner") | Main agent, persists for one session | `system/tracker.md` current row, `specs/adhd-learning-system-design.md`, last session's handoff note | — | Dispatches to subagents; does not grade or drift-check itself |
| **Lesson coach** | Same context as orchestrator (not a subagent) | Current lesson content, learner's running answers this session | — | Obsidian vault (schema notes, canvas) |
| **Examiner** (Socratic gate) | Fresh subagent, one-shot per gate attempt | The 4-criterion rubric (verbatim from `tracker.md`), the learner's transcript for *this gate attempt only* | The coach's session narrative, prior gate outcomes, any framing like "the learner has been trying hard" | Nothing directly — returns a structured verdict to the orchestrator |
| **Adversarial re-grader** | Fresh subagent, invoked only when Examiner returns PASS | The same rubric + transcript, told explicitly to argue for FAIL | The Examiner's verdict or reasoning | Nothing — returns agree/disagree to orchestrator |
| **Practice-composer** | Fresh subagent, invoked between sessions or on demand | Tracker rows with `strength: shaky` or `gone`, lesson content for those rows only | Current lesson's answer key (to prevent leakage into its own generated distractors) | Draft Anki notes (`.apkg`-bound or AnkiConnect payload), not sent live until orchestrator approves |
| **Tracker-writer** | Tool call from orchestrator, not a separate reasoning agent | The single diff to apply | — | `system/tracker.md` (sole writer) |
| **Drift-checker** | Fresh subagent, invoked before any artifact is committed | The locked-decisions list (this brief's constraints section, or a dedicated `specs/decisions-locked.md` if promoted) + the artifact being committed | The rationale that produced the artifact | Blocks or approves the commit; never edits content itself |
| **Session-closer** | Tool call from orchestrator, end of session | Final tracker state, gate outcomes, Effort rating | — | Writes a one-paragraph handoff note (see below) |

### Handoff protocol (mitigates context loss)

Every session ends by writing a short, structured handoff — not a transcript dump. Concretely, append to a `system/session-log.md` (the repo already has a "session log" pattern per recent commits):

- Tracker row touched, before/after status
- Gate outcome + which of the 4 criteria failed if any
- Which escape-hatch route fired, if any
- Effort rating (1–9) as logged
- One line: what the next session should NOT re-litigate (e.g., "reframe already tried once — do not reframe again, decompose instead")

The orchestrator's *only* required reading at session start is: current tracker row + last handoff note + the locked-decisions list. This bounds the "what does the agent need to remember" problem to a fixed, small artifact instead of relying on conversation history existing at all — the correct answer to context loss is external durable state, not larger context windows.

### The examiner: mitigating leniency specifically

The evidence base here is narrower than a first pass on this brief suggested. Of the two arXiv sources originally cited, one (2606.09843, the self-report psychometric paper) is about LLMs' introspective self-reports diverging from their actual behavior on a trait instrument — not about how a judge grades someone else's answer. The other (2604.23178, "Judging the Judges") is a real paper about bias-mitigation strategies in LLM-as-judge pipelines, but its central finding is about verbosity/style/formatting bias and the cost-effectiveness of debiasing techniques, not specifically about self-preference or same-family convergence. Neither source, read carefully, directly demonstrates the "prefers same-family outputs" claim — that is a separately documented phenomenon in the self-preference-bias literature (e.g., work specifically titled around self-preference bias in LLM-as-a-judge setups) that this brief has not independently verified against a primary source. Design response below is still reasonable engineering caution against a real, named class of bias, but the specific citations are scoped down accordingly:

1. **Separate context, not separate prompt.** The Examiner subagent never sees the coaching conversation — only the rubric and the answer transcript. This targets self-preference/leniency-style risks generally, since there's no prior "this learner is doing great" framing to anchor on, independent of exactly which paper best documents the mechanism.
2. **Force System-2 structure onto the grading itself.** The Examiner must, for each of the 4 rubric criteria in `tracker.md`, (a) quote the specific span of the learner's answer that satisfies it, or (b) state explicitly it's missing. A verdict with no quoted evidence per criterion is treated as invalid output by the orchestrator and re-run. This is a practical, self-motivated mitigation — the "forces System-2" framing is this brief's own analogy, not a tested claim from the cited literature: fast fluent agreement can't easily produce a quote-per-criterion trace, only actual comparison can.
3. **Adversarial second pass on PASS only.** Because false negatives (unfairly failing) are self-correcting via the escape hatch (decompose/reframe/park — never punitive), while false positives (wrongly passing) silently corrupt the tracker's `strength` field and the whole review queue downstream, the adversarial re-grader is only invoked to challenge PASS verdicts, not to double-check FAILs. Two independent PASS verdicts required to actually pass the gate.
4. **No partial credit language.** All 4 criteria must independently pass; the rubric already says this. The examiner is instructed to never output "mostly explained" or "close enough" as a passing judgment — binary per-criterion, matching the existing tracker rubric exactly.
5. **Rubric criteria are read from `tracker.md` verbatim at grading time, never restated from memory** — prevents rubric drift across sessions where the agent might otherwise "remember" a slightly softened version.

### Deliberate-practice / interleaved review, scheduled against Anki

- **Composer scope:** pulls only from rows marked `strength: shaky` or `gone`, plus a floor requirement to include at least one item from a *different* topic than the current lesson (interleaving, not blocked practice). **Evidence caveat:** the only interleaving citation in this brief's source list is a small music-performance study (n=10 advanced clarinetists, mixed significance on some rater subscales only, weak inter-rater reliability). It supports interleaving directionally but should not be read as strong or general controlled-trial support on its own — a broader interleaving literature exists (e.g., domain-general work on interleaved vs. blocked practice in problem-solving) but wasn't independently verified for this brief and isn't cited here as if it were.
- **Delivery path, corrected:** the safest, actually dependency-free path is generating a `.apkg` file for import — this requires nothing beyond file generation. **AnkiConnect is not dependency-free**: it requires the Anki desktop app running with the AnkiConnect add-on installed, which is a real runtime dependency, not an edge case. **Direct SQLite writes to Anki's own database carry a real corruption/data-loss risk if Anki is open at the same time** — Anki's own guidance is not to write to `collection.anki2` concurrently with a running instance. Direct-SQLite-write should only be used when Anki is confirmed closed, and AnkiConnect should be used only when a running desktop instance with the add-on is a confirmed precondition, not assumed. `.apkg` generation is the default; the other two are conditional fallbacks with explicit preconditions, not equally clean alternatives.
- **What it must not do:** generate net-new quiz facts about a subject unsupervised. The composer is scoped to rehearsing/reframing content that already exists in the Obsidian vault for that lesson — it transforms existing verified material into interleaved question form, it does not invent new claims about the subject matter. This is the direct mitigation for hallucinated quiz content: the composer's tool access should exclude open-ended generation and require every question to cite the vault note it was drawn from.
- **No streak/adherence pressure on the review queue itself** — per the locked "no notification/reminder adherence mechanism" decision, the composer prepares material; nothing in this design pings the learner to do it. Surfacing "what's due" happens only when the learner opens the tracker or Anki themselves.

### Tracker/review-queue automation

The tracker-writer is intentionally a thin tool call, not a reasoning agent, because `tracker.md` is the single source of truth and every existing status-transition rule is already fully specified (see the Status rules table in `system/tracker.md`). Automating it means: after a gate verdict or escape-hatch trigger, apply exactly one of the already-enumerated transitions, stamp `Last retrieved`, increment `Lapses`, and auto-park at 3 lapses — never inventing a new transition. The orchestrator should refuse to let the tracker-writer apply anything not in that table; this is a good place for a hard validation check (reject the write, don't silently coerce it) rather than agent judgment.

### Drift prevention across many sessions

Two independent mechanisms, not one:

1. **Structural** — narrow context per subagent means an examiner or composer literally cannot rationalize an exception to a locked decision it was never shown reasoning about; it only sees rubric + transcript, or vault note + interleaving requirement.
2. **Explicit gate** — the drift-checker subagent runs before any artifact (new lesson format, new UI-facing text, new gamification-adjacent feature) is committed, checking it against the locked-decisions list verbatim (fixed percentages instead of Effort 1–9, streaks, dyslexia-font language, learning-styles framing, notification/reminder mechanisms, objective-transfer metrics). This is cheap — it's a short checklist against a short artifact — and it's a high-leverage guard against a plausible-but-wrong "helpful" change creeping in over dozens of sessions (e.g., an agent deciding on its own that a small streak counter would help motivation).

---

## Failure-Mode Table

| Failure mode | Mechanism | Mitigation in this design |
|---|---|---|
| **Rubber-stamping / lenient grading** | LLM-judge literature documents real bias risks in automated grading (verbosity/style bias confirmed in the fetched sources; self-preference bias documented elsewhere in the field but not directly verified against this brief's own citations); fluent pattern matching can plausibly read a plausible answer as sufficient | Separate-context Examiner subagent, quote-per-criterion forced evidence, adversarial re-grader on PASS only, rubric read verbatim from `tracker.md` each time |
| **Context loss across sessions** | Recurring theme in current practitioner/vendor writing on agentic-system failure; conversation memory isn't durable state | External durable state only (`tracker.md` + `session-log.md`); orchestrator's session-start reads are fixed and small, not a hope that history persists |
| **Hallucinated quiz/practice content** | Agent generates plausible-sounding but fabricated or ungrounded facts, especially under open-ended generation | Composer restricted to rehearsing existing vault content, required to cite the source note per question; no unsupervised new-fact generation |
| **Drift from locked design decisions** | Many small "helpful" agent decisions compound over dozens of sessions with no single reviewer catching the trend | Dedicated drift-checker subagent with the locked-decisions list as its only context, run before any artifact commit |
| **Escape-hatch abuse (soft repeat-unchanged in disguise)** | An agent could satisfy "never repeat unchanged" by reframing so trivially it's effectively unchanged | Session-closer's handoff note explicitly records which escape route already fired, blocking the same route twice in a row |
| **Tracker corruption from a reasoning agent writing state** | An LLM "helpfully" inventing a transition not in the Status rules table, or silently coercing invalid data | Tracker-writer is a validated tool call, not free-form generation; invalid transitions are rejected, not coerced |
| **Anki data corruption from concurrent writes** | Writing directly to `collection.anki2` while the Anki desktop app is open risks corruption or silent data loss | Default to `.apkg` generation; gate direct-SQLite-write behind a confirmed "Anki is closed" precondition |
| **Over-automation removing learner agency** | Fully autonomous scheduling could quietly become a de facto reminder/notification system, violating the no-notification decision | Composer prepares material only; nothing pushes or pings; surfacing happens only on learner-initiated open |
| **Single orchestrator as a bottleneck/single point of failure** | If the orchestrator's own reasoning drifts (e.g., misjudges Effort or invents a status), nothing downstream catches it | Drift-checker and tracker-writer validation both sit *outside* the orchestrator's own judgment, functioning as independent checks rather than trusting one agent end-to-end |
| **Gamification creep** | Team-competition is the one sanctioned mechanic; an agent could add adjacent mechanics (progress bars framed as streaks, badges) as "polish" | Explicit item on the drift-checker's fixed checklist |
| **Cognitive-load / Effort misjudgment overriding the floor** | An agent could "helpfully" push a struggling learner past Effort 7-9 to keep pace with a schedule | Effort rating is learner self-reported per `tracker.md`, not agent-inferred; escape hatch is mandatory on 7-9, not a suggestion the orchestrator can override |

---

## What This Means for the Build Plan

Build in this order — each phase should run stably across real multi-session use before the next is added, since adding multi-agent complexity before the single-agent loop is proven is itself a plausible source of coordination failures:

1. **Tracker automation as a validated tool, not a subagent.** Lowest risk, unblocks everything, matches the existing build plan's Phase 1. Get the Status-rules table enforced mechanically first.
2. **Session handoff protocol** (`session-log.md` write/read contract). Cheap, and it's the direct fix for context loss — should exist before any grading automation, so gate outcomes have somewhere durable to land.
3. **Examiner as an isolated subagent with the quote-per-criterion + adversarial-recheck design.** This is a high-value correctness investment given the leniency-bias evidence (scoped as described above), and the existing rubric in `tracker.md` is already usable as-is — no redesign of the rubric needed, only of who grades against it and how.
4. **Practice-composer scoped to existing vault content, feeding Anki via `.apkg` by default.** Build after the examiner is trusted, since its main risk (hallucinated content) is best caught by feeding it already-verified material rather than by policing its output after the fact. Treat AnkiConnect/direct-SQLite as conditional fallback paths with their preconditions (running instance + add-on; Anki closed) explicit in the implementation, not glossed over.
5. **Drift-checker subagent, gated on the locked-decisions list.** Lower urgency early (few artifacts exist yet to drift), but should exist before the system has run long enough for compounding small deviations to be hard to spot — i.e., stand it up once phases 1-4 are in real use, not after months of unmonitored operation.

Do not build a full multi-agent swarm (finder/verifier/synthesizer as separate persistent agents, shared blackboard memory, etc.) unless a specific bottleneck in this five-step build demonstrates the need — the current evidence supports orchestrator-plus-narrow-subagents as reasonable for a single-learner system at this scale, and each additional persistent agent is additional surface for the context-loss and coordination failure modes above.

---

## Adversarial Review Notes

This brief was checked by two independent adversarial fact-check passes. Both fetched the primary sources directly rather than trusting the original draft's characterizations. Summary of what changed, matching the transparency style of `2026-08-08_adversarial-review.md`:

**Corrected — mischaracterized citations:**
- The claim that "judges converge toward a model's own self-report" was originally attached to arXiv 2606.09843 (the self-report psychometric paper). That paper is about LLMs' introspective self-reports diverging from their own behavior on a trait instrument, not about how a judge grades someone else's output — a different phenomenon. The claim has been rewritten to describe what each cited paper actually shows, and the "same-family output preference" claim is now labeled as a separately-documented phenomenon in the field that this brief has not independently verified against a primary source, rather than something the two cited papers demonstrate. (Both critiques agreed on the core problem; they disagreed slightly on exactly what arXiv 2604.23178 shows — one read it as supporting self-preference bias, the other read it as being about verbosity/style bias and debiasing cost-effectiveness specifically. The text above follows the more specific, second reading and flags the ambiguity rather than picking a side without direct re-verification.)
- The unsupported add-on claim that "rubric instructions measurably reduce verbosity bias but not self-preference/position bias" has been removed — no cited source demonstrates this specific split.

**Corrected — factual/technical error:**
- "AnkiConnect / direct SQLite writes ... both are dependency-free, ... no vendor API risk" was wrong on two counts: AnkiConnect requires a running Anki desktop app plus an installed add-on (a real dependency), and direct SQLite writes while Anki is open carry a documented corruption/data-loss risk. The delivery-path section now treats `.apkg` generation as the actual dependency-free default and states the preconditions for the other two paths explicitly. This also updated the failure-mode table (new row) and the build-plan section.

**Softened — confidence-inflation on blog-sourced claims:**
- "The orchestrator-worker pattern is the current standard for Claude Code multi-agent work" and "context loss ... is a named, common agentic failure class" were sourced entirely to marketing/content blogs (explainx.ai, thepromptshelf.dev, nimblebrain.ai, galileo.ai, chrislema.com), not primary or peer-reviewed sources. Both critiques agreed the underlying claims are directionally plausible and consistent with what's commonly said in 2026 practice, but the phrasing has been downgraded throughout from "the standard" / "a named failure class" to "widely recommended in current practitioner blogs" / "widely discussed in practitioner writing," so the brief doesn't imply research-literature weight it doesn't have.

**Softened — cherry-picked/narrow citation:**
- The interleaving claim ("real controlled-trial support as a technique") rested on a single small study (n=10 clarinetists, mixed significance, weak inter-rater reliability in places). This has been explicitly caveated in the interleaving section rather than presented as general strong evidence; the brief now notes a broader literature likely exists but wasn't independently verified here.

**Downgraded phrasing, kept as interpretation:**
- The Kahneman System-1/System-2 framing for the examiner design is this brief's own analogy, not a claim drawn from the cited LLM-judge papers. Language was changed from declarative ("this is a System-1/2 problem") to explicitly interpretive ("can be read as," "this brief's own interpretive lens").

**Considered and kept unchanged (judgment call, noted disagreement):**
- Both critiques found no duplicate re-citation of already-established sources (Dunlosky/Karpicke/Cepeda-tier findings, the tools-survey list) and no silent contradiction of locked decisions — the one real tension (team-competition gamification implying an undesigned multi-user surface) was already explicitly flagged by the original draft rather than glossed over. No change needed on either point.
- The overall architectural recommendation (orchestrator + two narrow adversarial subagents, external durable state, quote-per-criterion grading, `.apkg`-by-default Anki delivery) is engineering reasoning, not an empirical claim, and neither critique disputed the reasoning itself — only the evidentiary weight attached to some of its supporting citations. That reasoning is kept as originally proposed.

---

**Sources consulted for currency of 2025-2026 practice claims:**
- [LLM-Judge Bias Mitigation (2026)](https://futureagi.com/blog/evaluating-llm-judge-bias-mitigation-2026/)
- [Judging the Judges: Bias Mitigation Strategies in LLM-as-a-Judge Pipelines](https://arxiv.org/pdf/2604.23178)
- [An LLM-Native Psychometric Instrument Reveals a Self-Report–Behavior Gap Across 25 Models](https://arxiv.org/pdf/2606.09843)
- [Claude Code Subagents and Multi-Agent Workflows (2026)](https://explainx.ai/blog/claude-code-subagents-multi-agent-workflows-2026)
- [Claude Code Multi-Agent Orchestration: 6 Patterns (2026)](https://thepromptshelf.dev/blog/claude-code-multi-agent-orchestration-patterns-2026/)
- [AnkiConnect — MCP server](https://explainx.ai/mcp-servers/ankiconnect)
- [Optimizing Music Learning: Blocked vs. Interleaved Practice Schedules](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4989027/) — narrow (n=10), see caveat above
- [AI Agent Failure Modes: What Goes Wrong and Why](https://nimblebrain.ai/why-ai-fails/agent-governance/agent-failure-modes/)
- [7 AI Agent Failure Modes and How to Prevent Them](https://galileo.ai/blog/agent-failure-modes-guide)
- [AI Context Failures: Nine Ways Your AI Agent Breaks](https://chrislema.com/ai-context-failures-nine-ways-your-ai-agent-breaks)
