---
name: invest-task-scoping
description: "Grades work against the INVEST checklist (Independent, Negotiable, Valuable, Estimable, Small, Testable), splits what is too big into pieces of up to 2 weeks, and writes each piece as a user story with acceptance criteria and Given/When/Then scenarios, one at a time, waiting for approval. Use when the owner says 'INVEST', 'user story', 'split this task', 'break this into tasks', 'acceptance criteria', or starts a new deliverable, epic, feature or backlog and wants it scoped. Do not use for tiny fixes like a typo, open-ended research, or work that is already small and clear."
---

# INVEST task scoping

INVEST is a checklist for deciding whether a piece of work is ready to build. This skill applies it the same way every time, so work stays small, testable and about outcomes. It works for any project. Course-specific details live in the project's own notes, not here.

## Ground rules (and why)

- **Outcomes, not solutions.** Say what the person needs and why. Don't dictate screens, tools or code. A good story captures the essence, not the details, which keeps it Negotiable.
- **Small = aim for 1 week, 2 weeks at most.** The course instructor says "one week or two weeks". Flag anything over 1 week.
- **Split into slices a person can use, not into layers.** "Just the database" has no value to anyone until something uses it. Each piece should deliver something a person can try.
- **Order dependencies are not defects.** If piece 3 can only be built after piece 2, mark Independent as a fail with the reason, and put the pieces in build order. Perfect independence isn't always possible.
- **Unknowns get a spike.** If Estimable fails because something is unknown, add a short time-boxed piece to find out, then estimate the rest.
- **One story at a time.** Show it, then stop and wait for the owner's yes before the next.
- **Don't pad.** Ask before producing more than about 9 pieces. The instructor's example is 6 epics with 3 features each and 3 tasks each, and he fills in only what is "good enough".
- **Work from saved files, not memory.** If the item comes from a vision board, scope or handoff report, read that file first.
- **Short and plain.** The owner has ADHD: about 30 lines per reply, a table and a few lines, no paragraphs.

## Pick the mode

- **Backlog mode** (the default; code, and the INVEST backlog deliverable): the full steps below, with a story sentence.
- **Homework mode** (analyses and other deliverables, such as a market analysis): grades, split, definition of done and checks, with no "As a..." sentence unless asked. Mark the file `Mode: homework` at the top. The owner hasn't confirmed this mode yet, so if unsure, ask once.

## Steps

1. **Take one candidate** (a feature, epic or task). If it's unclear which deliverable or epic it belongs to, ask once.
2. **Grade the six letters** pass or fail, with a one-line reason for every fail.

   | Letter | Passes when |
   |---|---|
   | Independent | It stands on its own; nothing unbuilt blocks it |
   | Negotiable | It states the outcome, not a fixed solution |
   | Valuable | A user or the business gets something from it |
   | Estimable | The team can size the effort |
   | Small | Done within 1-2 weeks |
   | Testable | Anyone can check it works by using it |

3. **Split anything that fails Small or Independent** into pieces of up to 2 weeks (aim for 1). Grade each piece again.
4. **Write each piece with the task template** in [references/task-template.md](references/task-template.md): the story, the problem, the definition of done, acceptance criteria and Given/When/Then scenarios. A full example, plus a story that gets rewritten, is in [references/worked-example.md](references/worked-example.md).
5. **Show the output in this shape, then stop:** one line saying what is being scoped; the grade table for the original; the pieces as one line each with a size; Story 1 in full; the receipt; and the question "Story 1 as written? If yes, I'll show Story 2."
6. **Save to a file only when asked,** as markdown, in a folder the owner names. Use `## Story 1: <title>` headings, then run the checker below.

## Receipt (end of every answer, under a `## Receipt` heading)

- **Audited:** which pieces were graded on all 6 letters.
- **Split:** what was split, and from what.
- **Written:** the stories, acceptance criteria and scenarios produced.
- **Not checked:** what wasn't confirmed (for example, whether the size estimates match the team's real speed).

## Check a saved file

Run `python3 scripts/check_invest.py <file>` (the path to `scripts/` is relative to this skill's folder). It fails on a story without the formula, without Given/When/Then, without acceptance criteria or a definition of done, over 2 weeks, or without the receipt. It warns when a story names a screen or tool, or runs over 1 week. Fix every failure before calling the file done.

## When not to use it

Tiny fixes, open-ended research, and work that is already small and clear. The instructor doesn't list exclusions, so these are judgment calls. If unsure, say so and ask.

## If this skill didn't load when it should have

The hook in `.claude/hooks/invest-trigger.mjs` only fires on specific phrases. Add the owner's exact words to a new row in `references/misses.md`, then to the `description` above and the hook's test file, and rerun the tests in `evals/`.

## Files

- [references/task-template.md](references/task-template.md): the ticket and task body.
- [references/worked-example.md](references/worked-example.md): a full example and a rewrite.
- [references/sources.md](references/sources.md): where each rule comes from.
- [references/misses.md](references/misses.md): phrases that should have triggered it and didn't.
- `scripts/check_invest.py`: the checker. `evals/evals.json`: the test prompts and what a good answer holds.
