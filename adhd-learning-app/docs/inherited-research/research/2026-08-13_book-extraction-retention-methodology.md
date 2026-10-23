# Book extraction & retention methodology — how AI-mined book notes actually work

Follow-up to `reference-library-workflow.md` (the existing F&I-specific extraction design) and `2026-08-09_book-synthesis-audit.md` (documented prior incident). Prompted by Orlando asking for a deep, evidence-checked answer to "how do I get the value of these books without reading them cover to cover, and don't lie to me" — and whether the answer generalizes past F&I to the whole ADHD learning system. Six parallel research passes, 2026-08-13.

## The central question, answered honestly

**Can a passively-read AI-extracted summary substitute for reading the book?** Genuinely mixed evidence, resolved by *how* the extraction is consumed, not by the extraction itself:

- **Generation effect — well-established** (meta-analysis of 86 studies, d≈0.40, Bertsch et al.): actively generating your own explanation of material beats reading a pre-made one. Self-explaining produces the largest benefit among rereading/paraphrasing/self-explaining.
- **A passively-read summary is closer to "reading someone else's summary" than "reading the book"** — and a direct study found plain summarizing *underperformed* rereading on assessment scores, EXCEPT when the summary was high-quality and actively engaged with. One 2025 study found AI-generated summaries matched human ones on comprehension, but flagged risk of "superficial engagement" from passive consumption.
- **Bottom line: the extraction can work, but only if the pipeline forces you to generate something from it — not just receive it.** Passive delivery of a technique table is the failure mode; active reconciliation is the fix.

## Facts vs. framework — framework wins for transfer

Isolated technique/fact lists don't transfer to new situations. The author's underlying mental model does, because it's what lets you recognize a new situation as an instance of the same pattern (standard transfer-of-learning finding, Yale CTL and others). This matches this project's own prior finding (`2026-08-09_book-synthesis-audit.md`) that Ericsson/Kahneman/Duhigg's *frameworks* are more durable than their specific anecdotes.

**Implication:** the existing technique-table format (`reference-library-workflow.md`) is action/fact-oriented by design. It should also capture, once per book, the author's core underlying framework/mental model — not just a list of what-to-do rows.

## What NOT to copy from popular productivity culture

- **Progressive summarization (Tiago Forte's "Second Brain" method) — no real evidence.** Even Forte's own defenders concede it's "not a tool for memory... not a tool for thinking," explicitly a retrieval/filing tool. Consistent with this project's existing skepticism toward that genre.
- **"Levels of processing" ("relate it to your life") is weaker than commonly presented.** Craik & Lockhart themselves walked it back in 1990 (circularity critique — depth can't be measured independently of the recall it explains). Useful heuristic, not the bulletproof law it's often sold as. Functionally subsumed by the generation-effect/desirable-difficulty literature already in this project's corpus.
- **Book-summary apps (Blinkist etc.) have a real, repeated criticism pattern**, not just assumption: user reviews describe padded/shallow output, and Blinkist's own founders concede summaries are "a starting point, not a replacement" for the book.

## The best-corroborated failure mode: the Collector's Fallacy

The single most consistent finding across Zettelkasten-community criticism, PKM anti-pattern writing, and book-summary-app reviews: people mistake **collecting** notes/highlights for **understanding** them. Documented example: a Zettelkasten practitioner made 121 separate notes from one book and got stuck — the notes captured the author's words, not the reader's own interpretation. The diagnosed fix, independently repeated: fewer notes, more synthesis.

**This is the concrete risk of scaling book extraction across the whole learning system** — producing a large, ungrowing pile of technique tables nobody revisits is worse than doing nothing, because it creates the *feeling* of having learned without the substance.

## Practitioner signal worth following

Thomas Frank's approach (chapter-by-chapter notes in his own words, immediately after reading, rejecting heavier academic systems as too cumbersome) is closer to the generation-effect finding than most "book note" content. Ali Abdaal explicitly cites the testing effect and recommends *Make It Stick* — evidence-grounded, though his own practice (2,000+ highlights) leans more collector than his stated philosophy.

## Architectural fit against this project's existing locked decisions

- **MAP/DRILL/EXAMPLES/REPS taxonomy generalizes cleanly** — already proven across 20 unrelated subjects in `subjects.md`. Only the technique table's "where it fits the F&I flow" column is F&I-specific; that becomes "where it fits *this subject's own* structure" per book/subject.
- **Doesn't violate the Gemini-teaches/Claude-grades tool boundary** (`DECISIONS.md` §8) — extraction is a third bucket, content generation, which §9 already named as needing its own gate ("content generation gated and separate from live tutoring — hallucination risk") but never built. Queued item #6 ("prototype LLM card generation with mandatory human review," `DECISIONS.md` §11) becomes load-bearing once extraction scales past F&I — should be promoted to a real locked decision before scaling, not treated as optional.
- **New candidate decision, not yet covered anywhere:** should extracted notes require an explicit "reconcile in your own words" checkpoint before they count as study material — the same principle behind the existing integration gate (passive diagram-viewing without reconciliation scores worse than nothing), extended from diagrams to book notes generally.

## Proposed pipeline changes (pending sign-off — modifies a locked file)

Two additions to `reference-library-workflow.md`'s existing technique-table format:

1. **A "framework" section per book** (not per technique) — the author's core underlying mental model, captured once, separate from the action-oriented technique rows.
2. **A required reconciliation step** before a technique counts as learned — Orlando explains the technique back in his own words (verbally or written) rather than just reading the extracted table. This is the direct fix for both the generation-effect finding and the collector's-fallacy risk.

Both changes are additions to an existing locked file, not a redesign — held here as proposed, not applied, pending explicit sign-off per this project's existing "decisions pending sign-off" convention.
