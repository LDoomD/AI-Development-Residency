# Security Test Coverage: routes/update-family-role.js

## Proven (test written and passing)

| Finding | Attack tested | Structural control | Test file | Command run |
| --- | --- | --- | --- | --- |
| Missing authorization on role change — any caller could promote/demote any family member for a care recipient | Non-admin (`viewer1`) PATCHes `/family-role/cr1/viewer2` to set `role: admin` | Authorization check: requester's own `family_access` role for that care recipient must be `admin` before the UPDATE runs | `update-family-role.test.js` | `ROUTE_VERSION=fixed npx jest` → 3 passed, 3 total |
| Same finding, self-escalation case — a non-admin promoting themselves | Non-admin (`viewer1`) PATCHes `/family-role/cr1/viewer1` to set `role: admin` (targets own id) | Same authorization check, applied regardless of whether target == requester | same file | same run → passed |

Both tests were run red (against the unmodified vulnerable fixture, `ROUTE_VERSION=vulnerable`) and failed as expected (403 expected, 200 received, role actually changed), then green (against the fixed route) and passed. Command/output for both runs is in `run-vulnerable.log` and `run-fixed.log` in this directory.

A third "control" test (an actual admin can still change roles) also passed on the fixed version, confirming the fix doesn't break the legitimate case.

## Still open (no passing test yet)

None for this finding — both attack paths named in the request (promoting someone else, promoting self) are covered.

## Not attempted

- No test for a *different* care recipient's admin trying to change roles on a care recipient they're not attached to at all (requester has zero `family_access` row for that `care_recipient_id`). The fixed code's `rows[0] && rows[0].role` handles this (`requesterRole` is `undefined`, falls through to 403), but it wasn't asked for and isn't separately asserted — flagging it as a natural next test if wanted.
- No test for malformed/missing `role` values in the request body (e.g. an admin submitting `role: 'superadmin'`) — that's a separate input-validation finding, not the authorization bug this test targets.
