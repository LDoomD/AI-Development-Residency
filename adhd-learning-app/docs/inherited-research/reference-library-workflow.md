# Reference Library — how uploaded books get used

**Cross-subject, not F&I-only.** Books uploaded for one course (F&I) get mined once and can
serve any later course (relationships, entrepreneurship, English, etc.) — see "Cross-subject
technique library" below. Nothing here is F&I-specific by design; F&I was just the first
course built.

## Where books live

`~/reference-library/` — **outside this repo, on purpose.**

This repo is on GitHub. Committing copyrighted books would republish them, which is a
problem whether the repo is public or private. The folder is also gitignored as a second
guard in case a book ever lands inside the project by accident.

```
~/reference-library/
├── f-and-i/
├── influence-and-trust/
└── charisma/
```

PDF is the format that works directly. EPUB needs converting first (`unzip` + read the
XHTML directly — deterministic, no OCR/visual-guessing risk). AZW3 may be DRM-locked;
Calibre's `ebook-convert` only works on DRM-free files.

## What happens after a book is read

Books do not get summarised chapter by chapter — most non-fiction is perhaps 20% substance
and a linear summary buries it. Instead, each book produces **two things captured once per
book**, plus **one row per technique**.

### Once per book

1. **Author's stated purpose** — pulled from the preface/intro/"how to use this book"/
   conclusion: what does the author explicitly say they want a reader to take away and do
   with it. Direct quote or close paraphrase, attributed. This is extractable, not inferred —
   most non-fiction authors say this outright.
2. **Framework** — the author's underlying mental model/mechanism (why their techniques
   work). May require more inference than #1; flag confidence accordingly.

### Per technique — the table

| Technique | What it does | Where it fits | Also applies to | Source | Evidence | Compliant? |
|---|---|---|---|---|---|---|
| *(name)* | *(mechanism, one line)* | subject-native step (e.g. F&I: meet-and-greet/discovery/menu/objection/close) | other subjects from `subjects.md` this could plausibly transfer to, with a one-line reason each | Author, *Title*, ch. or p. | High / Moderate / Extrapolated / Not covered | yes / caution / no |

Columns doing the real work:

- **Where it fits** — a technique you can't place in a real moment of *some* subject's
  actual practice is trivia. If it doesn't map to a step, it gets cut. The step vocabulary
  is native to whichever subject the technique was originally mined for — not forced into
  an F&I-shaped flow when the source subject is different.
- **Also applies to** — tagged using the exact subject names in `subjects.md`, never
  invented vocabulary. This is what makes the technique reusable across courses — see
  below.
- **Source** — chapter or page. Every claim traceable back to the book.
- **Evidence** — separates tested from practitioner lore. Lore can still be worth using;
  the point is knowing which you're holding when it fails.
- **Compliant?** — regulated subjects (F&I) need this column taken seriously; a technique
  that works and also gets you sued/fired is a bad technique regardless of effectiveness.
  Not every subject needs this column populated, but it stays in the schema.

## Cross-subject technique library

**`specs/technique-library.md`** — one flat table, every technique from every book,
regardless of which course it was mined for. This is what lets a Voss calibrated-question
technique (mined for F&I) also surface for entrepreneurship (client-needs discovery) or
relationships (hard conversations), without re-reading the book for each course.

**When starting a new course**, the order is:

1. **Research the subject's own literature first** — new books/sources specific to the new
   course, same as any other subject.
2. **Cross-check the existing technique library** — grep `technique-library.md` for tags
   matching the new subject, and review what's already there with reasoning for each
   candidate ("this technique from Book X could apply here because Y") — not a bare list of
   names.
3. **Narrow into what Orlando actually wants** from the new course, now informed by both
   the fresh research and what's reusable from the existing library.

Candidates are surfaced, never auto-injected — Orlando is the filter on relevance, not me.

## Then it becomes study material

1. **Technique table** → `specs/research/` — the sourced record
2. **Learning file** → `learning/{subject}/` — plain English, what to actually do
3. **Drill cards** → the exact wording of a label, a mirror, an objection response
4. **Roleplay scenarios** → I play the counterpart, Orlando runs the technique live

Which of those a given technique gets depends on its mode, per `specs/subjects.md`
(MAP/DRILL/EXAMPLES/REPS) — the same taxonomy used everywhere else in this project, not a
book-specific one.

## Retention safeguard: reconciliation, kept lightweight

Passive reading of an extracted technique table is weaker than actively generating your own
explanation of it (generation effect — see `specs/research/2026-08-13_book-extraction-retention-methodology.md`).
So a technique isn't "learned" from reading the table alone — but this is deliberately kept
**fast, not academic**:

- **Default:** one sentence, spoken or typed, on why the technique works — during a roleplay
  rep or right after reading it. Not an essay.
- **Source/evidence-grade detail sits in the corner of the card**, available on demand, never
  a required checkpoint before moving on.
- Digging into the author's full reasoning is opt-in, whenever curiosity strikes — never a
  prerequisite to progressing.

## Verification safeguard

This project already had a real incident of AI-extraction fabricating a quote and
cherry-picking a statistic (`specs/research/2026-08-09_book-synthesis-audit.md`), caught only
by independent re-verification, not a single pass. So: every extracted technique needs a
source citation (chapter/page) before it's trusted, and spot-checking against the actual
source is expected — not just before it "sounds right."

## What does not get produced

Long verbatim passages copied into project files. Techniques, mechanisms, the author's
stated purpose, and short quoted phrases with attribution — yes. Reproducing the book —
no. The extraction is meant to make the material usable, not to replace owning the book.
