---
name: engineering-quality-check
description: Runs a quality check on code changes before they are called done, covering tests actually run, a code review checklist, documentation, and a record of big decisions. Use when the user says work is done or ready to merge, asks for a code review, asks "is this ready", or is about to commit or open a pull request. Also use for casual asks like "review my last commit", "is this good enough to merge", "can I commit this", "prove it actually works and not just on my machine", or "what do I show to prove it is done". Make sure to use this skill before any claim that work is finished, even if the user never asks for a review. Do not use for security-only or accessibility-only reviews, for planning a new project, or for writing new features.
---

# Engineering Quality Check

Before a change is called done, prove it works and that the next person can
understand it. Claims need evidence: a test you ran beats a test you believe
would pass.

## Ground rules

- **Evidence before claims.** Never say "tests pass", "builds", or "works"
  unless you ran the command in this session and saw the result. Quote the
  command and the result.
- **Review the change, not the whole project.** Look at what was added or
  edited (`git diff`, `git status`).
- **The bar is code health.** Approve a change once it clearly improves the
  overall health of the code, even if it is not perfect. Do not block on taste.
- **Say what you could not check.** If tests do not exist or cannot run, say so
  plainly.
- **Review first, change later.** Do not rewrite code unless asked after the
  report.
- **Plain language.** Explain terms the first time.

## Before you start

1. See what changed: run `git status` and `git diff`. If there is no change,
   ask what to check.
2. Find how this project runs tests and checks (`package.json` scripts, a
   Makefile, `README`). If you cannot find them, ask one question.
3. Read `references/code-review-checklist.md`.

## Workflow

1. **Run the checks.** Run tests, then the linter and build if the project has
   them. Also run the architecture gate:
   `node .claude/skills/judge-arch/scripts/arch-gate.mjs`. Record each command,
   its result, and any failures. A gate failure means the work is not ready.
2. **Review the change** with the checklist: design, behavior, complexity,
   tests, naming, comments, and style.
3. **Check tests for the change.** New behavior needs a test. A bug fix needs
   a test that fails without the fix.
4. **Check documentation.** README, comments, setup steps, and API notes match
   the new behavior.
5. **Check for a big decision.** If the change picked a technology, changed
   structure, or set a rule others must follow, use the
   `architectural-decision-records` skill to draft a record in `docs/adr/`. A
   decision record is a short note saying what was decided and why.
   (`assets/decision-record-template.md` remains as a quick fallback.)
   For a non-trivial change that adds, moves, or restructures code, also run the
   `judge-arch` skill for an architecture review in fresh context.
6. **Write the report** with `assets/quality-report-template.md`.

## Verdict

Choose one and give the reason:

- **Ready:** checks ran and passed, and no blocking issues remain. If the user
  pasted passing results and nothing else contradicts them, give Ready and say
  the evidence was supplied by the user, not run by you. Do not downgrade to
  "Cannot tell" only because you did not rerun it.
- **Ready after small fixes:** list them.
- **Not ready:** list what blocks it.
- **Cannot tell:** checks could not run. Say what is missing.

## Quality check before finishing

- Every claim about passing checks has a command and result behind it.
- Each review comment names a file and line, why it matters, and a suggestion.
- Blocking issues are separated from nice-to-have comments.
- The report lists what was not checked.
- It suggests one next step, such as committing, fixing the list, or adding
  a missing test.

## If something goes wrong

- **No tests exist.** Say so, mark it as a risk, and suggest the first test
  worth writing.
- **Tests fail.** Report the failure output. Do not call the work done.
- **The diff is huge.** Suggest splitting it, then review the riskiest part
  first.
- **Commands need credentials or a network.** Say which could not run.

## Files in this skill

- `references/code-review-checklist.md`: what to look for.
- `assets/quality-report-template.md`: the format of the report.
- `assets/decision-record-template.md`: a short template for big decisions.

## Sources

Google, Engineering Practices: The Standard of Code Review:
https://google.github.io/eng-practices/review/reviewer/standard.html
Martin Fowler, Architecture Decision Record (24 March 2026), which credits
Michael Nygard with the term in 2011: https://martinfowler.com/bliki/ArchitectureDecisionRecord.html
