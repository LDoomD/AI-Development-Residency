# Research Brief: AI-Powered Learning-Tool Landscape (New Entrants), August 2026

**Prepared for:** Personal ADHD/dyslexia learning-system build
**Scope note:** This brief covers only tools/evidence *not* already surveyed in prior passes (ADHD productivity apps, general PKM tools, and the UX-mechanics pass on Duolingo/Brilliant/Khan Academy/Synthesis/Sana Labs/Memrise/Quizlet/Elicit). It does not re-litigate cognitive-science fundamentals already cited elsewhere in this project.
**Fact-check status:** This draft was reviewed by two independent adversarial fact-checkers who verified load-bearing citations against primary/near-primary sources (arXiv paper text, PNAS/Wharton summary, GitHub API). One confirmed correction and one presentational fix were applied — see "Adversarial Review Notes" at the end.

---

## Executive Summary

The 2025–2026 wave of AI learning tools splits into five clusters: (1) LLM-based "Socratic" tutoring platforms that wrap a pedagogy layer around a foundation model, (2) voice-based conversational tutors (almost entirely language-learning, limited relevance here), (3) AI essay/explanation graders aimed at teachers grading bulk student writing, (4) open-source command-line projects that use an LLM to auto-generate Anki-importable flashcards from PDFs/notes, and (5) "agentic" study-planning assistants that claim to manage a learner's schedule and material across sessions.

Three things stand out for this build:

1. **Independent efficacy evidence is thin but not absent, and it cuts both ways.** The strongest new data point is *not* vendor-supplied: a peer-reviewed Harvard RCT (Kestin et al., *Scientific Reports*, June 2025) found a pedagogically-designed AI tutor produced roughly double the learning gains of active-learning classroom instruction in less time. Against that, a PNAS field RCT (Bastani et al., 2025, ~1,000 Turkish high-schoolers) found an *unguarded* GPT-4 tutor raised practice-problem scores 48% while *lowering* unassisted exam scores 17% — a documented "AI-as-crutch" skill-atrophy effect — while a version with hint-only guardrails raised practice scores 127% with no exam harm. A third, DeepMind-run RCT on a hint-first tutoring model (LearnLM) found comparable results to human tutoring, including a modest edge on novel-transfer problems. The lesson for an ADHD/dyslexia build isn't "AI tutoring works" or "doesn't work," it's that **guardrail design (hints vs. answers) is the variable that determines whether AI tutoring helps or actively erodes unassisted skill** — a real risk given ADHD learners already lean on external scaffolds and may transfer that dependence to an AI answer-giver rather than building retrievable memory. This also intersects with an existing project decision: this project's failure-trigger protocol (decompose/reframe/park) already asks a stuck learner to do cognitive work rather than get handed an answer — an AI tutor that answers instead of hints could functionally substitute for that step rather than support it, so any adopted/built tutor should be hint-first by design, not just by marketing claim.
2. **Almost every consumer product in this space (Socra, StudyFetch, and the dozen "AI study planner" apps) publishes zero independent efficacy data of its own.** Their "science-backed" claims cite the same general literature (spaced repetition, active recall) already in this project's evidence base — they are citing the science to sell a UI, not demonstrating that their specific implementation produces the claimed gains. Treat all such claims as unverified marketing.
3. **The genuinely composable finds are the open-source CLI projects**, not the polished SaaS products. Tools like `anki-llm` and `pdf2anki` slot directly into the existing Obsidian+Anki stack (they emit `.apkg`/CSV that Anki imports natively) without requiring migration off FSRS, off Obsidian notes, or into a subscription silo. The SaaS "all-in-one" platforms (StudyFetch, Socra, StudyEdge) actively compete with the existing stack for ownership of notes, flashcards, and scheduling — adopting one wholesale would mean abandoning FSRS's validated scheduling algorithm for an opaque, unvalidated in-house one.

---

## Tool-by-Tool Findings

### 1. LLM-based Socratic tutors / adaptive AI course platforms

**Socra** (hisocra.com)
- What it does: Chat-based AI tutor that uses Socratic questioning (asks guided questions rather than giving direct answers) and converts the resulting dialogue into structured study notes. Positioned explicitly against "just ask ChatGPT for the answer" usage.
- Cost: Free tier (web/iOS/Android), no credit card required; paid tiers exist but pricing wasn't independently confirmed at time of writing — check hisocra.com/pricing directly before relying on this.
- Efficacy evidence: None independent. All claims are vendor-stated methodology descriptions, not measured outcomes.
- Composability: Low. It's a closed conversational product with its own note format — importing its output into Obsidian would be manual copy-paste, and its "study notes" don't map onto Anki's card format without extra tooling.

**LearnLM (Google DeepMind)** — not a standalone consumer product but relevant as an evidence source
- What it is: A generative model fine-tuned specifically for pedagogy (Socratic questioning, scaffolded hints, pedagogical feedback), used as the tutoring layer inside products like Google's education tools.
- Evidence: A DeepMind-run exploratory RCT (Nov 2025 report, arXiv 2512.23633; 165 students, five UK secondary schools, on the Eedi math platform) used a three-arm design — static-hint control, human-tutor, and LearnLM-with-human-in-the-loop. It measured two things: (a) supervising human tutors approved 76.4% of LearnLM's drafted tutoring messages with zero or minimal edits, a pedagogical-plausibility measure, and (b) an actual learning-outcome measure — students in the AI-supported arm solved subsequent novel transfer problems at 66.2% vs. 60.7% for the human-tutor-only arm (+5.5 percentage points), i.e., performance at least comparable to, and slightly better than, human tutoring alone on transfer tasks. This is DeepMind's own study (not fully independent), but it's a more rigorous methodology than typical vendor claims, does include a genuine learning-outcome measure (not just message-approval), and is worth noting as the most "pedagogically grounded" foundation-model tutoring approach currently published.
- Composability: N/A as a product; relevant mainly as a signal that a well-prompted, hint-first system prompt matters more than model choice if one were to build a custom tutor on top of an API (relevant if this project ever builds a bespoke Claude/GPT-based tutor rather than adopting a SaaS one).

**StudyFetch (Spark.E)**
- What it does: All-in-one AI study platform — turns uploaded lecture notes/PDFs/audio into flashcards (with its own spaced-repetition scheduler, not FSRS), practice tests, an AI chat tutor ("Spark.E"), and an essay grader with feedback, all inside one proprietary workspace.
- Cost: Free tier (10 chats/month, 1 study set, 2 uploads); Base $7.99/mo ($4.99/mo annual); Premium $11.99/mo ($7.99/mo annual, or $99.99/yr); a $3.92/week cram-mode tier also exists. These figures come from third-party review sites, not a live pull of StudyFetch's own pricing page at finalization time — treat with the same "verify before relying on it" caveat given to Socra's pricing above.
- Efficacy evidence: None independent found. Marketing pages assert general spaced-repetition science but no study of StudyFetch's own scheduler or outcomes.
- Composability: Low-to-none. It duplicates every layer of the existing stack (notes, cards, scheduler, tutor) inside its own silo, and its spaced-repetition algorithm is undocumented/unvalidated — adopting it means giving up FSRS.

**DeepTutor** (arXiv preprint, "Agentic Personalized Tutoring") and related academic prototypes (e.g., CONVOLEARN)
- What it is: Research-stage agentic tutoring architectures being published in 2026 arXiv preprints — proposing multi-agent tutor designs with persistent learner models. Not a shipped consumer product.
- Composability: None currently — flagging only because this is where the next generation of "real" agentic tutors is likely to originate; worth a re-check in 6–12 months if any of this research spins out into an open-source release.

### 2. Voice-based AI tutors

This category is dominated by language-learning conversation apps — **Talkio AI** ($10/mo, 40+ languages, 400+ AI personas), **Langua** ($24/mo, ElevenLabs voices, strongest conversational naturalism), **Praktika** ($8/mo, cheapest), and **Pingo** (Google Play's "Best of 2025," 3M+ users). One 2025 study (Thao, Ly, Thu & Kien) reported a 75% improvement in speaking scores over 8 weeks for one such app — a single vendor-adjacent academic study, not independently replicated.

- Relevance assessment: **Low relevance to this project.** These are language-acquisition tools, not general ADHD/dyslexia study aids — voice conversational practice for a second language doesn't compose meaningfully into an Obsidian+Anki-based general learning system unless a language-learning goal specifically exists. Noted for completeness per the request scope but not recommended for adoption without a language-learning use case.

### 3. AI essay/explanation graders

**EssayGrader.ai** — independently rated #1 in a teacher-conducted comparative review (per the review's own framing — "independent" here means teacher-run blog review, not academic study). Bulk upload, LMS integration, built-in AI-detection, FERPA/COPPA/SOPPA/PIPEDA compliance claims, structured feedback across content/style/grammar/structure.
- Composability: Not directly relevant to a self-directed personal learner (it's built for teachers grading a classroom's worth of student essays), but the underlying capability — "give an LLM a written explanation and have it grade against a rubric with specific revision feedback" — is exactly the mechanism behind the well-established "explain it back" self-testing technique. That mechanism is trivially buildable as a custom prompt inside the existing Claude-based workflow rather than adopting a teacher-oriented SaaS tool.
- Efficacy evidence: None on learning outcomes (only "grading accuracy vs. teacher agreement" type claims, and even those come from vendor-adjacent sources).

**Turnitin Feedback Studio**, **Grammarly** — established, not new to 2025-2026, mentioned only because they appeared in the same category searches; not further profiled since they predate this survey's window and aren't purpose-built tutoring tools.

### 4. Open-source LLM-based Anki/SRS flashcard-generation projects

These are the most directly relevant new finds for this project, since they output into the *existing* Anki install rather than replacing it.

**`anki-llm`** (raine/anki-llm, GitHub)
- What it does: A CLI/TUI toolkit for bulk-generating and editing Anki flashcards via LLM, with an interactive terminal review UI (generate multiple card variants, compare, dedupe, edit before committing). Talks to Anki directly via AnkiConnect. Also does TTS audio generation for cards. Supports OpenAI, Gemini, DeepSeek, Ollama, and any OpenAI-compatible endpoint (so a local/self-hosted model works too).
- License/maintenance: MIT license; 285 stars, 14 forks, verified via a live GitHub API pull at finalization time — actively maintained (last push within the past two weeks of writing), real usage signal.
- Efficacy evidence: None (it's a workflow tool, not a pedagogy product — the "efficacy" question is just "does spaced repetition + active recall work," already answered by prior literature already in this project's evidence base).
- Composability: **High.** Operates directly on an existing Anki collection via AnkiConnect; workspace configs are version-controllable (fits a git-tracked Obsidian vault workflow); doesn't touch or replace FSRS scheduling at all — it only automates card *creation*, leaving Anki's own (FSRS) scheduler untouched.

**`pdf2anki`** (shimo4228/pdf2anki, GitHub)
- What it does: CLI pipeline that turns PDFs/text/Markdown into Anki decks using Claude specifically, with vision support for image extraction, 8 card types (including cloze and image occlusion), Bloom's-Taxonomy tagging, and a 6-dimension confidence-scoring/self-critique loop before accepting a card. Explicitly built on Piotr Woźniak's (SuperMemo creator's) "20 Rules of Knowledge Formulation" as its card-quality framework — a real (if old) piece of SRS design theory, not marketing fluff.
- License/maintenance: AGPL-3.0; smaller project (44 commits) but has a real test suite (624 tests, 92%+ coverage) and an evaluation framework (precision/recall/F1 against keyword ground truth) — unusually rigorous for a hobby project.
- Composability: **High.** Since it's built around Claude specifically and outputs Anki-importable decks, it's a near-perfect match for a Claude-centric, Anki-based stack. AGPL license means any modifications distributed would need to stay open — fine for personal use, worth noting if any code from it is ever redistributed.

**`PDF2Anki-AI`** (n-hadi) and **`doc-to-anki-with-llm`** (elpadev) — simpler, lighter-weight equivalents (PDF/doc → LLM-generated Q&A → CSV or `.apkg`). Less actively maintained/fewer features than the two above but worth knowing as fallback options or reference implementations if building a custom version.

### 5. Agentic study-plan assistants

**Taskade (EVE agent)** — general-purpose agentic workspace; its "EVE" assistant can read a learner's stated topics/exam dates/chapter weights and schedule spaced reviews at fixed intervals (claimed: 1/3/7/14/30 days) across a calendar/Gantt view.
**StudyEdge AI** — bundles a study scheduler, AI flashcards, an AI tutor, and a "grade trajectory" tracker that claims to monitor retention per topic.
**Reclaim.ai** — general calendar-scheduling agent (not study-specific) that finds and protects time blocks, relevant only as a scheduling-layer composable, not a learning tool per se.

- Efficacy evidence: None found for any of these on actual learning/retention outcomes — these are productivity/scheduling automation claims, not pedagogy claims, and none has been independently evaluated.
- Composability: Low as a *replacement* for existing ADHD-scheduling tools already surveyed in this project (Tiimo, Sunsama, etc.), and none integrate with Obsidian or Anki directly. If a "study plan across sessions" agent is wanted, the more composable path is almost certainly a custom Claude-based agent/skill operating directly on the Obsidian vault and AnkiConnect (similar to what `anki-llm` already does for card generation) rather than adopting a third SaaS scheduling silo.

---

## Independent Efficacy Evidence — Summary Table

| Study | Design | Finding | Independence |
|---|---|---|---|
| Kestin et al. 2025, *Scientific Reports* | RCT, 194 Harvard students, crossover design, pedagogically-designed GPT-4 tutor vs. best-practice active-learning classroom | AI-tutored group learned ~2x as much in less time, reported higher engagement | Peer-reviewed, university-affiliated, genuinely independent |
| Bastani et al. 2025, *PNAS* | RCT, ~1,000 Turkish high-schoolers, 3 arms (control / unguarded GPT-4 / hint-only GPT-4 tutor) | Unguarded AI: +48% practice, **−17% unassisted exam score** (skill atrophy). Hint-guarded AI: +127% practice, no exam harm | Peer-reviewed, independent, directly relevant risk finding for this project |
| DeepMind LearnLM RCT, Nov 2025 (arXiv 2512.23633) | Exploratory RCT, 165 UK secondary students, Eedi math platform, 3 arms (control / human tutor / AI-supported) | 76.4% of AI tutor's messages approved by human tutors with no/minimal edit (pedagogical-quality measure) **and** AI-supported students solved novel transfer problems at 66.2% vs. 60.7% for human-tutor-only (a genuine learning-outcome measure, at least comparable to human tutoring) | Vendor-run (DeepMind), not fully independent |
| All SaaS vendor claims (Socra, StudyFetch, StudyEdge, Taskade EVE, voice tutors) | Marketing pages citing general literature | No product-specific outcome data | **Not independent — vendor marketing only** |

*A "Liu et al. 2026" multi-experiment finding (AI assistance boosts immediate performance but reduces persistence on subsequent unassisted tasks) surfaced in earlier drafting but its author/year/finding could not be primary-verified in this pass. It has been removed from this table rather than presented alongside verified studies, since an unconfirmed citation sitting next to peer-reviewed ones invites false confidence. It's directionally consistent with the Bastani finding above and worth chasing down properly before it's cited anywhere else in this project — treat it as a lead, not a source, until then.*

---

## What This Means for the Build Plan

**Adopt (high composability, low switching cost):**
- **`anki-llm`** — for bulk LLM-assisted card generation/editing directly against the existing Anki collection via AnkiConnect, with interactive review before committing. MIT-licensed, actively maintained, supports local/self-hosted models if data-privacy matters.
- **`pdf2anki`** — specifically because it's Claude-native, applies a real card-quality framework (Woźniak's 20 rules), and has genuine automated testing. Best fit if the primary source material is PDFs (textbooks, handouts).
- Either can be layered as an Obsidian-vault → Anki pipeline: draft/annotate in Obsidian, run the CLI over exported notes or source PDFs, review generated cards in the CLI's TUI, then let Anki's existing FSRS scheduler take over. No new subscription, no new silo, no loss of the already-validated FSRS scheduling.

**Consider only for a narrow, bounded use (e.g., a single "explain it back" self-check prompt), not as an adopted platform:**
- The essay-grading mechanism behind EssayGrader.ai/StudyFetch — but build this as a custom Claude prompt/skill against personal notes rather than adopting a teacher-oriented SaaS tool with irrelevant classroom features (LMS integration, bulk grading, plagiarism detection).
- A hint-first (not answer-first) Socratic tutoring prompt, informed directly by the Bastani et al. guardrail finding and corroborated by the LearnLM RCT's comparable/better-than-human-tutor transfer results — if any conversational tutor is built or adopted, the practice-vs-exam skill-atrophy risk is the single most load-bearing design constraint, arguably more important than model choice. As noted in the executive summary, this constraint should be read together with this project's existing failure-trigger protocol (decompose/reframe/park): a hint-first tutor supports that protocol, an answer-first one could quietly replace it.

**Do not adopt (low composability, would compete with/replace the existing stack):**
- Socra, StudyFetch, StudyEdge AI — all are closed, all-in-one platforms that duplicate notes, flashcards, and scheduling functions the existing Obsidian+Anki(+FSRS) stack already handles, with unvalidated in-house scheduling algorithms replacing a validated one (FSRS), and zero independent efficacy evidence of their own to justify the switch.
- Taskade/EVE, Reclaim.ai as *learning*-plan agents — general productivity-agent claims with no education-specific evidence; redundant with ADHD scheduling tools already surveyed in this project.
- Voice-based AI language tutors (Talkio, Langua, Praktika, Pingo) — out of scope unless a language-learning goal is added; flagged for completeness only.

**Open question worth flagging back to the user:** none of the newly-surveyed products have any dyslexia- or ADHD-specific accommodations (adjustable pacing, reduced text density, executive-function scaffolding) built in — they're general-population study tools. If accessibility-specific AI tooling is wanted, that would need a separate, narrower search (this pass found none).

---

## Adversarial Review Notes

This brief was checked by two independent adversarial fact-checkers before finalizing. Summary of what changed as a result, in the style of `specs/research/2026-08-08_adversarial-review.md`:

- **Corrected (both critiques flagged this independently):** The LearnLM/DeepMind RCT summary originally said the study measured "pedagogical plausibility, not... learning gains per se." That understated the study — it was a genuine 3-arm RCT that also measured a real learning-outcome proxy: AI-supported students solved novel transfer problems at 66.2% vs. 60.7% for human-tutor-only students (+5.5pp). The LearnLM writeup, the executive summary, and the summary table were all updated to include this finding, so the study isn't unfairly downgraded relative to the Kestin headline result.
- **Disputed and resolved via live re-check:** Critique 2 claimed the `anki-llm` GitHub stats (285 stars / 14 forks / 645 commits) were fabricated and that the real figures were ~1.5k stars / 106 forks — a serious citation-integrity charge. Critique 1 had independently confirmed the original 285/14 figures via the GitHub API. Rather than split the difference, this repo was re-checked live against the GitHub API at finalization time: **285 stars, 14 forks confirmed correct as originally stated.** Critique 2's number appears to be either a confusion with a different, similarly-named repo or a hallucinated figure. Original numbers were kept; commit count (645) is treated as plausible but not independently re-verified in this pass (not load-bearing for the recommendation either way).
- **Presentational fix (Critique 1's recommendation, reasonable):** The "Liu et al. 2026" citation was self-flagged in the draft as unverified but still sat as a row in the formal evidence table next to peer-reviewed studies, which invites a "if it's in the table, it checks out" misread. Moved it to a footnote under the table, explicitly labeled as a lead to verify or drop rather than a source to cite.
- **Minor caveat added:** StudyFetch's pricing figures are sourced from third-party review sites, not a live pull of the vendor's own pricing page. Added the same "verify before relying on it" caveat the draft already gave Socra's pricing, per Critique 2's suggestion — low stakes, but consistent hedging is cheap.
- **New connection surfaced (Critique 2), added rather than just noted:** Critique 2 pointed out the brief never explicitly connects the Bastani hint-vs-answer guardrail finding to this project's existing failure-trigger protocol (decompose/reframe/park) — an answer-first AI tutor could functionally substitute for that required cognitive step rather than support it. This connection is now made explicitly in the executive summary and the build-plan section, since it's a genuine new design constraint worth weighing, not just a citation footnote.
- **Confirmed accurate, no change needed:** Kestin et al. 2025 (N=194, ~2x gains, less time), Bastani et al. 2025 (48%/−17%/127% figures), the 76.4% LearnLM approval figure itself, `pdf2anki`'s license/test-suite claims (AGPL-3.0, 624 tests, 92%+ coverage), and the brief's clean handling of already-locked project decisions (FSRS preserved, no dyslexia-font or learning-styles framing, no gamification proposed) — both critiques independently verified these and found nothing to fix.
