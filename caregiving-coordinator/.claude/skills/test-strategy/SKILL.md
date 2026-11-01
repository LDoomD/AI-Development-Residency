---
name: test-strategy
description: Plans what kinds of tests a product or feature needs and where to put them, using the test pyramid (many fast unit tests, fewer integration tests, very few end-to-end tests), and decides which checks must run as scripts before merge. Use when starting a product or feature, when a project has no tests or only one kind, or when tests are slow or flaky. Also use for casual asks like "what should I test", "what checks should run before merging", "how many tests is enough", "my tests are slow or flaky", or "what can I skip testing", even if the user never says "strategy". Make sure to use this skill when a feature is planned and no test plan exists. Do not use for running the checks on a finished change (use engineering-quality-check), turning a security finding into a test (use writing-security-tests), or load testing.
---

# Test Strategy

Decide what to test, at what level, and which checks run automatically, before
the code is written. A test plan answers: if this breaks, which test fails, and
how fast do we find out?

## Ground rules

- **Use the project's existing test tool.** Do not add a framework unless there
  is none, and then ask first.
- **Fast and many at the bottom.** Unit tests cover rules and calculations.
  Integration tests cover a module with its real database or service. End-to-end
  tests cover only the few journeys that must never break.
- **Anything with a pass or fail answer should be a script.** Linters, the test
  suite, the arch-gate, and secret scanning run as commands. The model reads the
  result and does not judge them by eye.
- **Risk decides depth.** Code that handles money, health data, permissions, or
  deletion gets more tests than a settings page.
- **Evidence, not belief.** Never say tests pass without the command and
  result.

## Before you start

1. Find how tests run now (`package.json` scripts, a Makefile, the README). If
   none, say so.
2. Read `docs/PRD.md`, `docs/architecture.md`, and `docs/risk-profile.md` if they
   exist, to find the risky parts.
3. Ask one question if unclear: "Which feature or area is this plan for?"

## Workflow

1. **List the behaviors** the feature must have, including misuse and failure.
   If `docs/security-specs/` has scenarios for it, reuse them.
2. **Assign each behavior a level:** unit, integration, or end-to-end. Use the
   lowest level that can catch the failure.
3. **Mark the risky ones** and add edge cases: empty, huge, wrong type,
   duplicate, two users at once, service down.
4. **Choose the merge gate:** the list of commands that must pass before merge
   (tests, linter, build, `arch-gate`, a secret scan if available).
5. **Plan the data.** Test data is fake. Never use real personal or health
   data in tests.
6. **Write the plan** to `docs/test-plan.md` with `assets/test-plan-template.md`.
7. **Say what stays untested** and why.

## Output

A test plan with: behaviors and their level, the merge gate commands, the test
data approach, and a "Not tested" list.

## Quality check before finishing

- Each behavior has a level and a named test location.
- Misuse and failure cases exist for every risky feature.
- The merge gate lists real commands that exist in this project.
- No real personal data appears in the plan or fixtures.
- "Not tested" is present.

## If something goes wrong

- **No test tool exists.** Recommend one that fits the language and ask before
  adding it.
- **Tests are flaky.** Treat a flaky test as a bug. Find the cause (timing,
  shared state, network) before adding more tests.
- **The plan is too big.** Keep the riskiest five behaviors and list the rest as
  later.

## Files in this skill

- `assets/test-plan-template.md`: the layout of `docs/test-plan.md`.

## Sources

Ham Vocke, "The Practical Test Pyramid", on martinfowler.com,
https://martinfowler.com/articles/practical-test-pyramid.html
Google, Testing Blog, "Just Say No to More End-to-End Tests",
https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html
