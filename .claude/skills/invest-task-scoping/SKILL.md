---
name: invest-task-scoping
description: "Use when the owner wants to scope, right-size, grade or split work with INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable): turning a release scope, epic, feature or task into small user stories with acceptance criteria and Given/When/Then scenarios. Also use when they say 'INVEST', 'user story', 'split this task', 'break this into tasks', or start a new deliverable and want it scoped. Grades each piece, splits what is too big, and waits for approval before the next story. Do not use for tiny fixes like a typo, for open-ended research, or for work that is already small and clear."
---

# INVEST task scoping

INVEST is a checklist for deciding whether a piece of work is ready to build. This skill applies it the same way every time, so work stays small, testable and about outcomes. It works for any project. Course-specific details live in the project's own notes, not here.

## Ground rules

- **Outcomes, not solutions.** Say what the person needs and why. Don't dictate screens, tools or code. That keeps the work Negotiable.
- **Small = up to 2 weeks, ideally 1.** The course instructor says "one week or two weeks". Flag anything over 1 week.
- **One story at a time.** Show it, then stop and wait for the owner's yes before the next.
- **Don't pad.** Ask before producing a long list. The instructor's example is about 6 epics, with 3 features each and 3 tasks each, and he fills in only what is "good enough". Make that the ceiling to start from.
- **Work from saved files, not memory.** If the item comes from a vision board, scope or handoff report, read that file first.
- **Short and plain.** The owner has ADHD: a table and a few lines, no paragraphs.

## Steps

1. **Take one candidate** (a feature, epic or task). If it's unclear which deliverable or epic it belongs to, ask once.
2. **Grade the six letters** pass or fail. Give a one-line reason for every fail.

   | Letter | Passes when |
   |---|---|
   | Independent | It stands on its own; nothing unbuilt blocks it |
   | Negotiable | It states the outcome, not a fixed solution |
   | Valuable | A user or the business gets something from it |
   | Estimable | The team can size the effort |
   | Small | Done within 1-2 weeks |
   | Testable | Anyone can check it works by using it |

3. **Split anything that fails Small or Independent** into pieces of up to 2 weeks (aim for 1). Grade each piece again.
4. **Write each piece with the task template** in `references/task-template.md`: the story, the problem, the definition of done, acceptance criteria and Given/When/Then scenarios.
5. **Show the grade table and the first story, then the receipt, then stop.** Wait for the owner's yes. After each yes, show the next story.
6. **Save to a file only when asked**, as markdown, in a folder the owner names.

## Receipt (end of every answer)

- **Audited:** which pieces were graded on all 6 letters.
- **Split:** what was split, and from what.
- **Written:** the stories, acceptance criteria and scenarios produced.
- **Not checked:** what wasn't confirmed (for example, whether the size estimates match the team's real speed).

## When not to use it

Tiny fixes, open-ended research, and work that is already small and clear. The instructor doesn't list exclusions, so these are judgment calls. If unsure, say so and ask.

## If this skill didn't load when it should have

Add the owner's exact words to the `description` above, and test it on a few prompts.

## Sources

Course definition and the task template come from the owner's NotebookLM notes (Week 2 lecture transcript and checklist, Week 2 challenge template), saved as a summary, not the original files. Verify against the Notion template before submitting. The owner's audit format comes from their own INVEST prompt (2026-11-05).
