Yes — here's a test that proves a non-admin can't change anyone's role, including their own, plus a minimal fix so the test has something real to check. Everything actually ran (Node's built-in test runner, no extra framework needed).

## What I built

**`update-family-role.fixed.js`** — the route with an authorization check added: before touching `family_access`, it looks up the requester's own role for that specific `care_recipient_id` and rejects with `403` unless it's `admin`. (I refactored the file into a small factory, `createFamilyRoleRouter(db)`, so the db dependency can be injected and the handler tested without a real database or HTTP server — that's the only structural change from your original logic.)

**`update-family-role.test.js`** — the actual deliverable, 5 cases against the fixed handler:
1. A viewer tries to self-promote to admin → `403`, role unchanged.
2. A non-admin (editor) tries to promote a *different* member to admin → `403`, unchanged.
3. Someone with no `family_access` row at all for this care recipient tries to act → `403`.
4. Someone who's admin for a *different* care recipient tries to act on this one → `403` (role is scoped correctly, not global).
5. Control: a real admin for this care recipient successfully changes someone else's role → `200`, role updated (so the fix isn't just blocking everything).

**`db.mock.js`** — tiny in-memory stand-in for `../db`, enough to support the two queries the route runs.

**`update-family-role.vulnerable.js`** + two extra test files (`demonstrate-vulnerability.test.js`, `sanity-check-same-test-against-vulnerable.test.js`) — not required, but I used them to prove the test is meaningful rather than trivially green: I ran the exact same assertions against your original (unpatched) logic and confirmed they fail there.

## Actually ran it

Installed `express` locally in this output folder (`npm install express`, needed for `express.Router()`) and ran with Node's built-in test runner (Node v26, no framework install needed for the test runner itself):

```
node --test update-family-role.test.js
```
Result: **5 pass, 0 fail.**

Sanity check — same assertions against the unpatched handler (`sanity-check-same-test-against-vulnerable.test.js`):
```
node --test sanity-check-same-test-against-vulnerable.test.js
```
Result: **0 pass, 2 fail** — both failures are `200 !== 403`, i.e. the unauthorized role change silently succeeded. That's your vulnerability, reproduced and now caught by the suite.

## One assumption flagged for you

The fix assumes an upstream auth middleware sets `req.user.id` for the authenticated caller. If your real middleware attaches the caller differently, that's the one line to adjust in `update-family-role.fixed.js`.
