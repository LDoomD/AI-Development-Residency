# Security decision record: routes/pharmacy-link.js

Per owasp-secure-coding-bdd's required OWASP threat-modeling flow (steps 1-4).

## Step 1: Scope

- **Entry points:** `POST /pharmacy-link` (body: userId, pharmacyUsername, pharmacyPassword,
  careRecipientId), `GET /pharmacy-link/:careRecipientId` (URL param).
- **Exit points:** JSON responses; `console.log` (stdout/log aggregator); the `pharmacy_links` SQL
  table.
- **Assets worth protecting:** the pharmacy portal credential pair (a reusable third-party login,
  not a hash-able app password), the mapping of which family member linked which care recipient.
- **Trust boundaries crossed:** unauthenticated-looking HTTP request -> SQL database; HTTP request
  -> log stream; one family member's data -> a different, potentially unrelated caller.
- **Selected cheat sheets:** SQL_Injection_Prevention, Query_Parameterization (both query sites
  concatenate input into SQL), Authorization, Insecure_Direct_Object_Reference_Prevention (GET route
  has no ownership check; POST route trusts a client-supplied `userId`), Cryptographic_Storage
  (password must be reversible, so Password_Storage's hashing does not apply here), Logging (the
  `console.log` line prints both credential fields in clear text), Secrets_Management (encryption
  key sourcing, noted as a follow-up, not fully resolved by this change).

## Step 2: Threats (STRIDE-mapped, ranked)

| # | Threat | STRIDE | Sheet | Exploitability | Impact | Rank |
|---|---|---|---|---|---|---|
| 1 | SQL injection via `careRecipientId`/`userId`/credential fields in the INSERT | Tampering | SQL_Injection_Prevention | High (every field interpolated) | Critical (full DB read/write) | **High** |
| 2 | SQL injection via `careRecipientId` path param in the SELECT | Tampering | SQL_Injection_Prevention | High | Critical | **High** |
| 3 | Any caller can read any care recipient's pharmacy username+password (no ownership check) | Information Disclosure | IDOR / Authorization | High (sequential/guessable ids, no auth needed) | Critical (live 3rd-party credential theft) | **High** |
| 4 | POST trusts `req.body.userId` instead of the authenticated caller, so a link can be attributed to/created as anyone | Spoofing | Authorization | Medium (needs a POST, no auth check exists to even stop it) | High | **High** |
| 5 | Pharmacy password stored in plain text in `pharmacy_links` | Information Disclosure | Cryptographic_Storage | Medium (requires DB access, but SQLi above provides it) | Critical | **High** |
| 6 | Pharmacy username+password printed to application logs in clear text | Information Disclosure | Logging | Medium (requires log/stdout access) | Critical (logs are often lower-privileged to read than the DB) | **High** |

All six threats ranked High: this route's entire purpose is handling a replayable third-party
credential, so disclosure or injection here is a direct credential-theft path, not a secondary risk.

## Step 3: Countermeasures and risk response

| Threat | Countermeasure applied | Risk response |
|---|---|---|
| 1, 2 | Parameterized queries (`$1`/`$2` bound params) on both the INSERT and SELECT | Eliminate |
| 3 | Added a `care_relationships` ownership check before returning or creating a link; GET returns 404 for both "not found" and "not yours" | Eliminate |
| 4 | Acting user now taken from `req.user` (authenticated session), `req.body.userId` ignored | Eliminate |
| 5 | AES-256-GCM envelope encryption of the password at rest, unique IV per record, key held outside the row | Mitigate (ciphertext still exists; key compromise is the residual risk — see below) |
| 6 | Removed the `console.log` line entirely; replaced with a sanitized event log carrying only user id, care recipient id, and timestamp | Eliminate |
| Key sourcing for #5 | Read from `PHARMACY_CREDENTIAL_KEY` env var today, with the file documenting this is a floor, not the target (HSM/KMS/Vault) | **Accept, with a stated reason**: this project has no secrets manager yet; env var is better than hardcoding or a fast hash, but is not the end state. Tracked as a follow-up, not silently dropped. |

No threat above was left with no countermeasure.

## Step 4: Assessment (this record)

- **Surface:** `routes/pharmacy-link.js`, both routes.
- **Sheets selected:** SQL_Injection_Prevention, Query_Parameterization, Authorization,
  Insecure_Direct_Object_Reference_Prevention, Cryptographic_Storage, Logging, Secrets_Management
  (partial).
- **Threats and ranking:** six threats, all ranked High (table above).
- **Countermeasures:** five eliminated, one explicitly accepted with a stated reason and a named
  follow-up (see "What's missing" below).
- **`@security` scenarios added:** `outputs/pharmacy-link.feature`, 8 scenarios across 4 Feature
  blocks, tagged `@security` plus the matching `@owasp:*` topic tag for each.
- **Real guarantees, stated separately from what each scenario checks:**
  - *Scenarios check:* one injection payload is rejected/neutralized; one cross-family read is
    denied; one unrelated-recipient create is denied; one client-supplied `userId` is ignored; one
    password round-trips as ciphertext; one password is absent from a response; one log line is
    absent of the credential pair.
  - *Structural guarantees that make every case safe, not just the tested one:* the bound SQL
    parameter (driver-level, applies to every value regardless of content); the
    `care_relationships`-scoped join/lookup (applies to every care recipient id, not just the one
    tested); reading the acting user from `req.user` instead of the request body (applies to every
    field name an attacker might try, not just `userId`); AES-256-GCM with a key held outside the
    row (applies to every row in the table); the removal of the `console.log` call (applies to every
    future request, not one payload).

## What's missing / honest limits (read before relying on this)

1. **No `bdd-comprehensive-testing` skill, shared feature index, or CI runner exist in this project
   yet.** `outputs/pharmacy-link.feature` is written as the file that belongs at
   `features/backend-input/pharmacy-link.feature`, but it is not indexed in a `features/bdd-index.json`,
   not listed in a `features/INDEX.md`, and not wired into any CI job. **It does not currently run
   anywhere.** Until that scaffolding exists, treat every scenario in it as `not-assessed` per the
   skill's own evidence rule ("a security control with no runnable scenario is not-assessed, never a
   pass"), not as a passing test. The concrete next steps, in order:
   - create `features/` at the repo root;
   - add a Gherkin runner (e.g. Cucumber.js for this Node/Express stack) and step definitions that
     actually exercise `pharmacy-link.fixed.js` against a test database;
   - generate `features/bdd-index.json` + `features/INDEX.md` from the `.feature` files;
   - add a CI job (or at minimum a pre-push hook) that runs the `@security` subset on every push and
     fails the build on a regression.
2. **`care_relationships` table and `req.user` auth middleware are assumed, not implemented.**
   `pharmacy-link.fixed.js` is written against the contract this route needs; neither the table nor
   the middleware exists in this project yet. The fix is not runnable until both land.
3. **`PHARMACY_CREDENTIAL_KEY` sourcing is a stated accept, not a resolved control.** An env var is
   the floor for an early-stage solo project; it is not where this should land before any real
   pharmacy credentials are stored. Revisit with a real secrets manager before this ships for real
   users.
4. **`check-security-coverage.mjs` / `check-cheatsheet-catalog.mjs` were not run.** Those gates live
   in the owasp-secure-coding-bdd skill's own repo and are not installed in caregiving-coordinator.
   This record substitutes for that automated gate until it is adopted here.

## Evidence ledger

| Control | Attack it stops | `@security` scenario | Source read this session | State |
|---|---|---|---|---|
| Parameterized INSERT/SELECT | SQL injection via any interpolated field | `pharmacy-link.feature`: "rejects a SQL injection payload in careRecipientId" / "...in the URL id" | SQL_Injection_Prevention.md, Query_Parameterization.md | `observed` (code shows bound params at `pharmacy-link.fixed.js:132-136, 175-182`); not yet `proven` (scenario not executing in CI) |
| care_relationships ownership check | Horizontal IDOR / broken access control | "A caregiver cannot read another family's pharmacy link..." / "...cannot create a pharmacy link for a care recipient they are not related to" | Insecure_Direct_Object_Reference_Prevention.md, Authorization.md | `observed`; not yet `proven` |
| Session-sourced acting user | Spoofed `userId` in request body | "...uses the authenticated session, not a client-supplied user id" | Authorization.md | `observed`; not yet `proven` |
| AES-256-GCM envelope encryption | Plain-text credential theft from a stolen DB copy | "A linked pharmacy password is stored as authenticated ciphertext..." | Cryptographic_Storage.md | `observed`; not yet `proven`; key-management is `accepted` with a stated reason, not `proven` |
| Sanitized event log (no credential fields) | Credential leakage via application logs | "Creating a pharmacy link logs the event without the username or password" | Logging.md | `observed`; not yet `proven` |

**Definition-of-done status for this change: NOT met.** The right sheets were applied, every control
has a written `@security` scenario, and the structural guarantee is named for each — but the scenarios
are not yet in a shared feature index and are not wired into CI, so per the skill's own rule this is
`observed`, not `proven`. Items 1-3 under "What's missing" are the blocking work before this can be
called done rather than reviewed.
