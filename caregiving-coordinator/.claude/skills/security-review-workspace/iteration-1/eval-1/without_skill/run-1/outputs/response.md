# Response

I read `routes/pharmacy-link.js`. Before touching the fix, here's what's actually wrong with it, because the tests only make sense in light of these:

1. **SQL injection** in both routes — `userId`, `careRecipientId`, `pharmacyUsername`, and `pharmacyPassword` are spliced directly into the SQL string. Any of them can break out of the query.
2. **Plaintext credential logging** — the `console.log` line prints the pharmacy username *and password* to your logs on every link. That's the pharmacy portal password, in cleartext, sitting wherever your logs end up.
3. **Plaintext credential storage** — the password is stored in the `pharmacy_links` table with no encryption. A DB dump or read-replica leak hands over working pharmacy logins for every care recipient.
4. **No authorization / IDOR** — neither route checks that the caller is actually allowed to touch the given `careRecipientId`. The POST trusts a client-supplied `userId` outright, and the GET returns *any* care recipient's full row (including the password) to *anyone* who guesses or enumerates the ID.
5. **No input validation** — missing or malformed fields just flow into the query.

I fixed all five, and — since you specifically asked that the controls be tested, not just fixed — I wrote a test suite that exercises each control directly rather than just hitting the happy path.

## What I produced

In `outputs/`:

- **`pharmacy-link.fixed.js`** — the corrected route. Parameterized queries throughout; passwords are encrypted (AES-256-GCM) before storage via a new crypto helper instead of logged or stored raw; both routes require `req.user` and verify that user is linked to the `careRecipientId` before doing anything (via a `care_recipient_links` ownership check — see assumptions below); input is validated before any DB call; the GET response strips out all credential fields.
- **`pharmacy-credential-crypto.js`** — small `encryptSecret`/`decryptSecret` helper (AES-256-GCM, key from `PHARMACY_CREDENTIAL_KEY` env var). Pharmacy passwords have to be reversible (the app needs to actually log into the portal later), so this is encryption, not hashing.
- **`pharmacy-link.security.test.js`** — Jest + Supertest test suite, **11 tests, all passing against the fixed file** (I actually installed jest/supertest/express in a scratch dir and ran it — not just written-and-assumed). It mocks the db layer and asserts on what was actually sent to it, which is what makes these tests catch regressions instead of just smoke-testing happy paths:
  - *Authorization*: unauthenticated POST is rejected before any DB call; a user with no link to the care recipient gets 403 on both POST and GET; a spoofed `userId` in the POST body is ignored in favor of the authenticated session's user.
  - *Input validation*: missing password, and a non-string `careRecipientId` (odd-type injection attempt), are rejected with no DB call.
  - *SQL injection*: asserts the literal injected string (e.g. `"attacker'; DROP TABLE pharmacy_links; --"`) never appears in the SQL text, that the SQL uses `$n` placeholders, and that the malicious value shows up only in the bound-params array.
  - *Credential logging*: spies on `console.log` and asserts the plaintext password never appears in any logged argument.
  - *Encryption at rest*: asserts the plaintext password is never in the values passed to `db.query`, then does a full round-trip — decrypts the stored ciphertext with the real crypto helper and confirms it equals the original password.
  - *Response leakage*: asserts the GET response JSON never contains a `password`-matching field, and that the SELECT query itself doesn't even ask for password columns.

## Assumptions (no app scaffolding existed yet to confirm against)

- `db.query(sql, params)` is a parameterized-query helper (pg/mysql2-style). If your real `db` module has a different signature, only the query calls need updating — the authorization/encryption/validation logic doesn't depend on it.
- There's auth middleware upstream that sets `req.user`. I added a `requireAuth` check as a placeholder — swap it for whatever your real auth stack produces.
- I assumed a `care_recipient_links` table mapping `user_id` to `care_recipient_id` for the authorization check. If family-to-recipient permissions live somewhere else in your schema, that's the one query to redirect.
- No `package.json` existed, so I didn't wire these into a project-level test command. Tests are self-contained; run with `npm install --save-dev jest supertest express` then `npx jest pharmacy-link.security.test.js` from this `outputs/` folder (I verified this exact combination works).

Before you merge your own fix, I'd suggest running this suite against it rather than against my version — if you land on a different encryption scheme or query shape, update the two tests that inspect `insertParams` positionally (encryption-at-rest and SQL-injection-POST), everything else should hold as written.
