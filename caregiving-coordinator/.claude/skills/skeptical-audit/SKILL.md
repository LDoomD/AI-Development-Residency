---
name: skeptical-audit
description: Applies an evidence standard to any factual claim in a report, review, audit, or status update, tagging each claim as proven, observed, inferred, documented, reported, or not-assessed with a re-runnable source and a stated limit. Use when writing or checking a report, when someone says something is "secure", "working", "compliant", or "tested", or when auditing another review for unsupported claims. Also use for casual asks like "how do you know that", "what is that based on", "which of these did you actually check versus assume", "is that verified or a guess", or "show me your evidence", even if the user never says "evidence". Make sure to use this skill before any summary that states results as facts. Do not use for judging architecture (use judge-arch), writing code, or casual chat with no claims to check.
---

# Skeptical Audit

A claim without a source is a guess that sounds confident. This skill makes
every factual statement carry how it is known, so a reader can tell a fact from
a hope.

## Ground rules

- **Tag every factual claim** with its evidence state (below), a source someone
  can re-run or open, and one stated limit.
- **Never upgrade a state without new evidence.** Reading code does not prove it
  runs. A test that passed once does not prove it passes now.
- **"Not assessed" is a valid and honest answer.** Say it instead of filling a
  gap with a guess.
- **Absence of findings is not a clean bill.** "No problems found in what was
  checked" is allowed. "Secure", "accessible", "compliant", and "tests pass" need
  the command and its result shown.
- **Separate what you did from what you believe.** Report both, labeled.

## Evidence states

| State | Meaning | Needs |
|---|---|---|
| `proven` | A check that would fail if the claim were false runs in CI or on demand and passed | The command and its output |
| `observed` | You saw it directly this session | The command, `file:line`, or screenshot |
| `inferred` | Followed from observed facts by reasoning | The facts it follows from |
| `documented` | An authoritative source says so | The link and the date read |
| `reported` | Someone told you | Who said it and when |
| `not-assessed` | Not checked | Why not |

## Workflow

1. List every factual claim in the draft (results, counts, "works", "safe").
2. Tag each with a state, a source, and a limit.
3. Downgrade any claim whose source does not support its state. Move it down
   one state or to `not-assessed`.
4. Rewrite the summary so the strongest wording matches the weakest supporting
   state.
5. Add a short "Not checked" list at the end.

## Output format

A table, one row per claim:

| Claim | State | Source | Limit |
|---|---|---|---|

Then the "Not checked" list. Keep it short: only claims that matter to a
decision.

## Quality check before finishing

- No claim is left without a state.
- No `proven` claim lacks a command that could have failed.
- The summary wording is no stronger than its weakest source.
- "Not checked" is present, even if it says "nothing outside scope".

## If something goes wrong

- **A source cannot be re-run** (a one-off screenshot, a conversation). Tag it
  `observed` or `reported`, never `proven`.
- **Two sources disagree.** Report both, do not pick one silently.
- **The reader wants a yes or no.** Give it, followed by its state.

## Sources

Adapted from the practice of separating observation from inference found in
audit and incident-review writing, for example Google SRE Book, "Postmortem
Culture: Learning from Failure",
https://sre.google/sre-book/postmortem-culture/
