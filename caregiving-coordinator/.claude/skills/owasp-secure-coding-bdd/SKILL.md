---
name: owasp-secure-coding-bdd
description: Guides secure design of new code before and while it is written, by turning OWASP guidance into plain-language behavior scenarios (Given/When/Then) for each feature that handles input, logins, permissions, files, secrets, or sensitive data, saved as readable specs. Use when planning or building a feature that takes user input, stores data, calls another service, or controls who can see what, and when the user asks how to build something securely. Make sure to use this skill at the start of such a feature, not after, even if the user never says "security". Do not use to review existing code for weaknesses (use security-review), to prove one specific fix with a runnable test (use writing-security-tests), or to set up a Gherkin or CI framework.
---

# OWASP Secure Coding Scenarios

`security-review` finds weaknesses in code that exists. This skill works earlier:
it writes down, in plain sentences, how a feature must behave when someone
misuses it, so the feature is built secure from the start. A scenario is a
sentence of the form "Given a situation, when something happens, then this must
be the result."

## Ground rules

- **Specs, not a framework.** Write scenarios as plain Markdown. Do not install
  a Gherkin tool or CI. `writing-security-tests` turns one scenario into a real
  test when the code exists.
- **Misuse first.** Every scenario describes what an attacker or a careless
  user does, and what the system must do in response.
- **Ask what the feature touches.** Input, logins, permissions, files,
  secrets, other services, or sensitive data decide which scenarios apply.
- **Project-specific risks come from `docs/risk-profile.md`.** Read it. Each
  item that applies to the feature gets at least one scenario.
- **Never invent a standard.** Cite the OWASP source for each scenario, and say
  "not verified this session" if you did not open it.
- **Plain language.** Explain terms the first time.

## Before you start

1. Ask one question: "What does this feature do, and what does it touch?"
2. Read `docs/risk-profile.md` and `docs/architecture.md` if they exist.
3. Read `references/scenario-topics.md` for the topics to cover.

## Workflow

1. List the feature's entry points (forms, endpoints, files, background jobs).
2. For each, pick the matching topics from `references/scenario-topics.md`.
3. Write two to five scenarios per entry point in `docs/security-specs/<feature>.md`:
   - one for **valid use**,
   - at least one for **the most likely misuse**,
   - one for **failure** (what is shown and logged when something breaks).
4. Mark each scenario `automatable` (a test can check it) or `review` (a
   person or `security-review` must judge it).
5. Note which `arch-gate.config.json` rule backs it, if any.
6. Show the specs to the user. After they approve, point to
   `writing-security-tests` for turning the first `automatable` scenario into
   a runnable test.

## Output format

For each scenario:

```
Scenario: <short name>
  Given <starting state>
  When <the action, including the misuse>
  Then <what must happen, including what must NOT be shown or stored>
Source: <OWASP reference>   Check: automatable | review   Gate rule: <name or none>
```

## Quality check before finishing

- Every entry point has a valid-use, a misuse, and a failure scenario.
- Every applicable item in the risk profile has a scenario.
- Each scenario cites a source.
- No scenario asks for a tool or framework the project does not use.

## If something goes wrong

- **No risk profile.** Ask what data the feature holds and who may see it, then
  offer to draft the profile.
- **The feature is already built.** Say so, write the scenarios anyway, and
  suggest `security-review` for what exists.
- **Scenarios multiply.** Keep the five that matter most and list the rest as
  "later".

## Files in this skill

- `references/scenario-topics.md`: topics to cover, with OWASP pointers.

## Sources

OWASP Top 10:2025, https://owasp.org/Top10/
OWASP Cheat Sheet Series, https://cheatsheetseries.owasp.org/
OWASP Application Security Verification Standard,
https://owasp.org/www-project-application-security-verification-standard/
