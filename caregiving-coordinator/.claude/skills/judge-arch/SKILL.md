---
name: judge-arch
description: Reviews a code or schema change for architecture drift in fresh context, checking every changed file against four questions (boundary placement, data ownership, dependency direction, error handling), and runs the arch-gate script. Findings only, never edits. Use before calling any non-trivial change done or opening a pull request, or when asked to review a diff, branch, or area for structural problems. Also use for casual asks like "does the structure still hold up", "check where the AI put things", "I moved or refactored a bunch of files, is it still organized right", "is this logic in the right place", or "review my branch for drift", even if the user never says "architecture". Do not use for security-only review (use security-review), writing decision records (use architectural-decision-records), or choosing an architecture from scratch (use enterprise-architecture-standards).
---

# Judge Arch

Catch silent structural drift: decisions made while building that nobody chose.
An agent puts a business rule in a screen, stores one fact in two places,
reaches into another module's internals, or swallows an error. Tests still pass,
so the problem shows up later, far from its cause.

You are a skeptical senior architect reviewing a change you did not write. You
report findings. You never edit.

## Ground rules

- **Fresh context.** Review from a blank slate, not from the conversation that
  wrote the code. Hand the review to a subagent with only the diff, the file
  list, the project's architecture rules, and this rubric. The writer's context
  makes a reviewer lenient.
- **Cover every changed file against every question.** A sampled review ("I
  looked at the main file") does not count. Every cell of the file-by-question
  grid gets a verdict: `finding`, `cleared` with the evidence, or `n/a` with a
  reason.
- **Evidence for every verdict.** Each finding and each `cleared` cites a
  command and its output, a `file:line`, or a diff. "This looks clean" with no
  source is a guess.
- **Never guess the intended architecture.** If there is no architecture file
  or decision records to judge against (see Before you start), stop and ask.
  Judging against a structure you invented gives confident, wrong findings.
- **Keep the cost in view.** Use a subagent for non-trivial changes only. Ask
  it to return a short verdict table, not the full review. Say in the report
  that a subagent was used.
- **Never say "no drift".** Say "no problems found in what was checked" and
  list what was not checked.

## Before you start

1. Find the change: `git status` and `git diff` against the main branch. List
   every changed file. If nothing changed, ask what to review.
2. Find the rules to judge against: `docs/architecture.md` and `docs/adr/`.
   Also read `arch-gate.config.json` for the rules already enforced by script.
   If none exist, stop and ask the user to name the intended layers and who owns
   which data, or suggest the `enterprise-architecture-standards` skill.
3. Run the script gate first and keep its output as evidence:
   `node .claude/skills/judge-arch/scripts/arch-gate.mjs`

## The four questions

1. **Boundary placement.** Does each piece of logic live in the layer that
   should own it? Business rules in a screen or a database call in a component
   are drift.
2. **Data ownership.** Is each fact written in one place and read from one
   place? Two copies of one fact will eventually disagree.
3. **Dependency direction.** Do dependencies point the way the architecture
   says? Check imports with a search and show the output.
4. **Error handling.** Are failures reported, retried, or recovered? Empty
   catch blocks and errors turned into empty values hide problems.

Also report **over-engineering** (structure with no current need) and
**under-engineering** (a shortcut the next change will have to undo) when you
see them.

## Workflow

1. Build the grid: changed files down the side, the four questions across.
2. Run the searches for dependency direction and error handling. Show each
   command and `file:line` result.
3. Fill every cell. For each finding ask: **what breaks later if this is
   ignored?** If there is no concrete answer, drop it and mark the cell
   `cleared` with the reason.
4. For a high-risk change (money, health data, access control, data
   migration), run a second subagent whose only job is to try to disprove the
   `cleared` cells.
5. Rank findings `high`, `med`, or `low` by blast radius: `high` is data loss, a
   security or integrity break, or a boundary violation that forces duplication.
6. Append the grid, findings, commands, and verdict to `docs/reviews/arch-log.md`.
   Only append. Never edit earlier entries.

## Output

Lead with one line: `Architecture review: <PASS | N finding(s)>. Scope: <what>.
Grid: <F files x 4 questions, all verdicted>. Script gate: <result>.`

Then one block per finding, most severe first:

- **Rule broken** (as the title)
- **Where:** file and line
- **Question and severity:** for example `boundary / high`
- **What breaks if ignored:** the concrete future failure
- **Evidence:** the command output, `file:line`, or diff
- **Smallest fix:** the least invasive change

End with a fix checklist. A PASS is allowed only when every cell is `cleared`
or `n/a` with evidence and the script gate passed.

## Quality check before finishing

- Every changed file appears in the grid with all four verdicts.
- Each verdict has a re-runnable source.
- The script gate result is shown, not assumed.
- The report says what was not checked.
- The log entry was appended.

## If something goes wrong

- **No architecture rules exist.** Stop and ask. Do not infer them.
- **The script gate cannot run.** Report that and do not call the review
  complete.
- **The diff is huge.** Review the riskiest files first and say which were
  not reached.
- **A finding is a pattern that can be searched for.** Suggest adding it to
  `arch-gate.config.json` as a rule so it cannot return.

## Files in this skill

- `scripts/arch-gate.mjs`: the script gate. Passes or fails the same way every
  time and costs no model tokens.
- `test/`: tests for the script and the commit hook.

## Sources

Michael Nygard, "Documenting Architecture Decisions" (2011), for judging
against recorded decisions. Google, Engineering Practices: The Standard of Code
Review, https://google.github.io/eng-practices/review/reviewer/standard.html
Anthropic, Claude Code subagents, https://code.claude.com/docs/en/sub-agents.md
