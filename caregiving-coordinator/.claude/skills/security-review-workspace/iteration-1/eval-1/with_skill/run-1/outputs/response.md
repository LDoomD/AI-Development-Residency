I read `pharmacy-link.js` and ran the OWASP secure-coding threat-modeling flow on it before touching
fix code, because "fixed" and "tested" are two different claims and you asked specifically about the
second one.

## What's actually wrong

Six things, all High-risk because this route's whole job is handling a replayable third-party
credential:

1. **SQL injection** in the `INSERT` (POST) — every field, including the credential pair, is
   string-interpolated into the query.
2. **SQL injection** in the `SELECT` (GET) — `req.params.careRecipientId` goes straight into the
   query string.
3. **IDOR / broken access control** — the GET route returns the pharmacy username+password for any
   `careRecipientId` to any caller, with zero ownership check.
4. **Spoofable actor** — the POST route trusts `req.body.userId` instead of an authenticated
   session, so anyone can attribute (or create) a link as someone else.
5. **Plain-text credential storage** — the pharmacy password sits unencrypted in the DB. Note: this
   is *not* a "hash the password" fix like a login password — the app has to replay this credential
   to the pharmacy's portal later, so hashing would make it unusable. The correct control is
   reversible AES-256-GCM encryption at rest, per OWASP's Cryptographic Storage sheet, not Password
   Storage.
6. **Credentials in logs** — `console.log` prints both the username and password in clear text.

## What I produced

All in `.claude/skills/security-review-workspace/iteration-1/eval-1/with_skill/run-1/outputs/`:

- **`pharmacy-link.fixed.js`** — rewritten route: parameterized queries for both endpoints,
  session-sourced actor identity, a `care_relationships`-scoped authorization check (fail-closed,
  404 for both "not found" and "not yours" so the response can't be used to enumerate), AES-256-GCM
  envelope encryption for the stored password, and a sanitized log call that never prints the
  credential pair. It's written against two things this project doesn't have real modules for yet
  (auth middleware populating `req.user`, and a `care_relationships` table) — both are called out
  explicitly in the file as the integration seam, not silently assumed.
- **`pharmacy-link.feature`** — 8 executable `@security` Gherkin scenarios, one pair per control
  (SQL injection on each route, horizontal IDOR, spoofed-actor, encryption-at-rest, password never
  returned in a response, credential-free logging), tagged `@owasp:*` per topic.
- **`security-decision-record.md`** — the full threat-modeling record the skill requires: scope,
  STRIDE-mapped threats with ranking, countermeasure-per-threat with its risk response, and an
  evidence ledger separating what's `observed` (code shows the control) from `proven` (a CI-enforced
  test proves it).

## The honest gap — tests are written, not yet wired

The skill's whole point is that a control without an executable, CI-enforced test isn't done. This
project has no `bdd-comprehensive-testing` skill, no `features/` index, and no CI runner, so
`pharmacy-link.feature` is **not currently running anywhere** — it's the file that belongs at
`features/backend-input/pharmacy-link.feature` once that scaffolding exists, written now so the
controls don't ship as untested prose in the meantime. The decision record spells out the concrete
next steps in order: stand up `features/`, add a Gherkin runner (Cucumber.js fits this Express
stack), generate the index files from the `.feature` files, and wire the `@security` tag into CI or
at least a pre-push hook. Until that lands, treat these as reviewed-and-written, not proven.
