# Session handoff — 2026-10-24 (evening)

Written at the end of a long session, so the next one can pick up without
re-deriving anything.

## Read these, in this order

1. **`STATUS.md`** — current state and open decisions (one resolved today,
   see below)
2. **`CLAUDE.md`** — working rules
3. **`docs/WEEK2-PLAN.md`** — schedule and Week 2 deliverables, due **Oct 26**

## What happened this session

**Product decisions locked:**
- **Multi-user product**, not a personal tool — resolves `STATUS.md` open
  decision #2 (updated in that file today).
- **Core problem reframed.** Not "notes are slow to turn into practice" —
  the actual problem is that the intended user was never taught *how to
  learn* (plan → monitor → reflect), and existing tools do the thinking
  *for* the learner instead of building that skill. This was proposed in
  `docs/inherited-research/research/2026-08-13_learning-how-to-learn.md`
  back in August but never locked into `DECISIONS.md` — still not locked,
  flagged as a next action below.
- **New scope surfaced, not yet built:** note-taking coaching (the system
  looks at *how* notes are taken, not just what's in them — genuinely new,
  no prior research exists on this in the project) and a mentor/coaching
  agent distinct from the router and the mastery-gate Examiner.
- **Phone involvement resolved** — no push notifications (already
  rejected, `DECISIONS.md` §4, ADHD RCT). Settled on: "Add to Home Screen"
  as the environmental cue, a self-authored if-then plan widget, and
  one-tap voice note capture. Full writeup:
  `docs/research/2026-10-24_phone-engagement-mechanisms.md`.
- **Ruled out:** NotebookLM and Google Docs sync (no public API / OAuth
  approval-gate risk — same shape of problem that killed the prior
  `growth-ads-system` project), gamification, streaks.

**Personal context captured** (his own words, not research — saved for
traceability):
- `docs/research/2026-10-24_lived-experience-notes.md`
- `docs/research/2026-10-24_personal-experience-and-ideas.md`

**Market research + competitive analysis (Assignment B1)** — done in
FigJam, not in this repo:
- Board: *Market Research and Competitive Analysis Workshop Template*
  (Figma board key `HcDDdEGAnikTImO8v7UPMp`)
- 10 market segments sized and sourced — cross-checked two ways: direct
  WebSearch, then independently via a 4-agent ruflo research swarm. The
  swarm caught real errors in the first pass (a fabricated-looking
  "$5.1B" academic-coaching figure that doesn't exist on the publisher's
  page; two likely "report-mill" sources — dataintelo.com,
  growthmarketreports.com — now excluded everywhere). A final merged
  table was built with corrected numbers, both versions kept side by side
  on the board for comparison.
- Competitive analysis: 7 competitors fully written up (RemNote, Mochi,
  Quizlet's AI tools, Anki, Inflow, Tiimo, Khanmigo), each sourced.
- Workshop instructions reference saved:
  `docs/research/2026-10-24_audience-segmentation-workshop-instructions.md`

**Audience Segmentation, Goals, Motivations, and Use Cases** — also done
in FigJam, a separate board (key `Bi8Wr9BoAYpVDbWJWKWxx6`):
- 4-lens segmentation filled in (geographic, behavioral, demographic,
  socioeconomic)
- Two audiences defined: **Neurodivergent Adult Learners** (primary) and
  **Self-Taught Adults Rebuilding How They Learn** (the sharper
  ESL/immigrant/never-taught-how-to-learn sub-pattern from his own
  account)
- Motivations, situational goals, life goals, and a use-case table built
  for each audience, formatted to match the template's existing example
  tables (same column widths, bold header with divider, same font size)

## Where things stand on the Week 2 deliverables

- **Assignment A (research paper)** — unchanged since last session. Still
  has the "notes for the author, delete before sending" section at the
  bottom that needs stripping, and §2.4 needs to be in his own words
  before it goes to Morgan. The uncommitted edit to
  `Week 2 Coding Challenge/research-paper.md` from before this session is
  still sitting there — not touched tonight, included in tonight's commit
  since it was already pending.
- **Assignment B1 (market research)** — substantially done, in FigJam
  (see above).
- **Audience segmentation/goals/use cases** — done, in FigJam (see above).
- **B2 (Release Vision & Scope), B3 (Epics/Features), B4 (Build plan), B5
  (Backlog), B6 (Pitch deck)** — not started.
- **Message to Morgan** — still not drafted. Five things it needs to
  cover: specialization approval (overdue since Oct 19), the project
  switch, the repo-naming contradiction, the Week 4 question, Notion vs.
  Word docs. This blocks creating the GitHub repo.

## Explicitly queued as the next thing to do

**Work Prioritization Workshop** — same Figma file as the audience
segmentation work (key `Bi8Wr9BoAYpVDbWJWKWxx6`), sections already visible
on the board: `WORK PRIORITIZATION WORKSHOP INSTRUCTIONS` (id `27:180`),
`PRIORITIZE USE CASES` (id `27:204`), and `Part 3: Pick your Most
Important Pieces of Work for the Next Iteration, and Drop Them Here`
(id `27:169`). Read the instructions section first before filling anything
in, same approach as the last two workshops.

## Important: where today's work actually lives

Almost everything built tonight is in two FigJam boards, **not in this git
repo**:
- Market Research and Competitive Analysis:
  `https://www.figma.com/board/HcDDdEGAnikTImO8v7UPMp/`
- Audience Segmentation, Goals, Motivations, and Use Cases:
  `https://www.figma.com/board/Bi8Wr9BoAYpVDbWJWKWxx6/`

Only the supporting research write-ups under `docs/research/` are
version-controlled. If a future session needs the FigJam content, read it
live from these boards rather than assuming it's in a local file.

## Still unresolved, carried over

1. **Lock the self-regulation decision into `DECISIONS.md`** — proposed in
   the Aug 13 research, confirmed again tonight by direct personal
   account, still never formally signed off as decision #13.
2. **Repo naming** — blocked on Morgan, see above.
3. **Subject-mode tagging** (`subjects.md` marks "Agentic engineering" as
   MAP + REPS only, conflicts with shipping all four modes) — still open.
