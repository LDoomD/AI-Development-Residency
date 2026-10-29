---
name: writing-security-tests
description: Turns a security finding into one real, runnable test that proves the fix, in whatever test framework the project already uses. Use after a security-review finding, when the user asks to prove a fix works, verify a vulnerability is closed, or write a test for a security issue. Make sure to use this skill whenever code claims to fix an injection, auth, access-control, secret-storage, or logging problem, even if the user only says "add a test for that" or "does this actually work now". Do not use for writing the security review itself (use security-review), for general feature tests with no security finding behind them, or for setting up a BDD/Gherkin framework or CI pipeline the project doesn't have yet.
---

# Writing Security Tests

A fix that was never run proven wrong. This skill turns one security finding
into one executable test, so "I fixed it" becomes "here's the test, and it
passes."

## Why one test at a time, in the project's own framework

A batch of well-organized scenarios that can't run anywhere is not evidence,
it is a plan for evidence. If the project has no BDD runner, no feature-file
index, and no CI wiring, writing Gherkin for them produces documentation, not
proof. Write the test in whatever the project already uses to run tests. If
nothing exists yet, propose the smallest reasonable default (for a Node/
Express project, that is usually Jest or Vitest plus Supertest) and get a yes
before installing anything.

## Ground rules

- **One finding, one test, confirmed first.** Before writing anything, say
  which finding you're testing and what the test will actually check — the
  "seam": the request, function, or boundary the test calls, not the
  internals behind it. Wait for a yes.
- **Red before green where it's cheap.** If practical, show the test failing
  against the vulnerable code first, then passing against the fix. This is
  the only way to know the test would actually have caught the bug.
- **Use the project's real framework.** Never invent a format (Gherkin, a
  custom DSL) the project has no way to run. If you're not sure what's
  already set up, check `package.json`, a test folder, or ask.
- **Evidence before claims.** Never say "this passes" unless you ran it in
  this session. Quote the command and the output.
- **Test the control, not the happy path.** A security test sends the attack
  (the injection payload, the cross-user request, the missing session) and
  checks it's rejected or neutralized, not that the normal case still works.
- **Name the attack and the control** in the test's description or comment:
  what it's trying to do, and what structural thing stops it (a parameterized
  query, an authorization check, encryption at rest), so a reader doesn't
  mistake a passing test for a vague "it's secure."

## Workflow

1. **Get the finding.** Take it from a `security-review` report, or ask the
   user to describe the vulnerability and the fix if there's no report yet.
2. **Confirm the seam.** State the one sentence version: "this test will POST
   a SQL-injection payload to `/pharmacy-link` and check the query stays
   parameterized." Wait for confirmation before writing code.
3. **Find or propose the test setup.** Look for an existing test framework.
   If none exists, propose one (matching the project's stack) and ask before
   installing it.
4. **Write the test.** One test (or a small, obviously-related group) per
   finding. Mock only what you must to isolate the control under test — don't
   mock away the thing you're trying to prove.
5. **Run it.** Show the command and the real output, including a failure if
   the fix isn't actually in place yet.
6. **Repeat per finding**, rather than writing every test for every finding
   up front with none of them run.
7. **Summarize** which findings now have a passing test, which don't yet, and
   why, using `assets/test-coverage-summary-template.md`.

## Quality check before finishing

- Every test actually ran in this session; the command and result are shown.
- Each test names the attack it's checking and the structural control that
  stops it.
- No test is written in a format the project has no way to execute.
- The summary says plainly which findings are proven (test passes) versus
  still open, never "tests written" as a stand-in for "tests passing."

## If something goes wrong

- **No test framework exists yet.** Propose the smallest reasonable default
  for the stack and ask before installing. Don't silently add dependencies.
- **The finding can't be tested without a live system** (e.g. a third-party
  API, a real database with real data). Say so, and suggest the closest safe
  substitute (a mock, a test database) rather than skipping the test.
- **The fix isn't actually in place yet.** Write the test anyway, show it
  failing, and say that's what it's doing — a red test is still useful
  evidence of what the fix needs to do.
- **There are many findings.** Work through them one at a time in severity
  order (Critical first), not in one large batch.

## Files in this skill

- `assets/test-coverage-summary-template.md`: the format of the per-finding
  summary.

## Sources

This skill's design follows a measured comparison on this project's own
code: a version written as pre-wired BDD/Gherkin scenarios produced
documentation that could not execute without CI infrastructure the project
doesn't have, while a plain prompt with no skill at all independently wrote
and ran a real, passing test suite. The red-green, one-seam-at-a-time
approach follows the same practice described in Matt Pocock's `tdd` skill:
https://github.com/mattpocock/skills
