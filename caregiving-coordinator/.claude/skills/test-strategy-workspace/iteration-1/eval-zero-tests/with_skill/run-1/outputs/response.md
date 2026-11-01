# Test plan: appointments, medication list, sibling invites

Skill applied: test-strategy. Not checked: I did not inspect your repo, so I don't know if a test tool exists. Run `cat package.json` and look at the `scripts` section. If there is no test script, I recommend Node's built-in `node:test` (no install) or Vitest, and I'll ask before adding either.

## Risk order
1. Sibling invites (permissions, shared access)
2. Medication list (health data, wrong dose or time can hurt someone)
3. Appointments (scheduling logic)

## Behaviors and level

| Behavior | Level |
|---|---|
| Appointment time/overlap and reminder-date rules | Unit |
| Medication entry validation (empty name, bad dose, duplicate) | Unit |
| Invite token is single-use, expires, can't be guessed | Unit |
| Create/read/update/delete each feature against a real test database | Integration |
| Invitee sees only the family they were invited to; non-members get 403 | Integration (misuse) |
| Expired or reused invite is rejected | Integration (misuse) |
| Two siblings edit the same medication at once | Integration (edge) |
| Database down returns a clean error, no stack trace or health data | Integration (failure) |
| Invite, accept, add a medication, see it as the sibling | End-to-end (one only) |

Aim for many unit tests, a moderate number of integration tests, and one or two end-to-end tests.

## Merge gate (commands that must pass)
- test suite (`npm test`, once it exists)
- linter, if configured
- `arch-gate` script
- secret scan, if available

## Test data
All fake: invented names and medications. No real health data in fixtures.

## Not tested (for now)
Visual styling, load and performance, email delivery by a real provider (use a stub).

Next step: tell me which feature to start with, and I'll save this to `docs/test-plan.md` using the template.
