# Security Review: routes/pharmacy-link.js

Reviewed before commit. This route handles linking a family member's pharmacy portal credentials so the whole family can see refill status — that means it's storing a third-party login (username + password) for a vulnerable population (parents under care). Found several serious issues.

## Findings

### 1. SQL Injection — Critical
**Lines 12-15 and 23-25**

Both queries build SQL via string interpolation of raw request input:

```js
await db.query(
  `INSERT INTO pharmacy_links (user_id, care_recipient_id, username, password)
   VALUES ('${userId}', '${careRecipientId}', '${pharmacyUsername}', '${pharmacyPassword}')`
);
...
`SELECT * FROM pharmacy_links WHERE care_recipient_id = '${req.params.careRecipientId}'`
```

Any of these fields (especially `pharmacyUsername`/`pharmacyPassword`, which are attacker-controlled free text, not validated identifiers) can break out of the string literal and inject arbitrary SQL — read/write/drop any table the DB user can reach.

**Fix:** Use parameterized queries / prepared statements everywhere (e.g. `db.query('INSERT INTO pharmacy_links (...) VALUES ($1,$2,$3,$4)', [userId, careRecipientId, pharmacyUsername, pharmacyPassword])`).

### 2. Pharmacy credentials stored in plaintext — Critical
**Line 13-14 (schema/insert), Line 26 (`SELECT *`)**

The pharmacy portal password is inserted and presumably stored as plaintext in `pharmacy_links.password`. This is a third-party credential (not even this app's own auth), for medically sensitive accounts belonging to elderly care recipients. A single DB read (backup leak, insider access, SQL injection above, etc.) exposes live pharmacy logins for every linked family.

**Fix:** Encrypt the password at rest (envelope encryption with a KMS-managed key, not just app-level AES with a hardcoded key) rather than storing it plaintext. Decrypt only at the point of use (e.g., when the refill-status job logs in on the family's behalf).

### 3. Credentials logged in plaintext — High
**Line 17**

```js
console.log(`Linked pharmacy account for care recipient ${careRecipientId}: ${pharmacyUsername}/${pharmacyPassword}`);
```

This writes the pharmacy username and password straight into application logs. Logs are typically retained long-term, shipped to third-party aggregators, and readable by a broader set of engineers/on-call staff than the database is — this is often a bigger exposure surface than the DB itself.

**Fix:** Remove the password from the log line entirely (log only `careRecipientId` and maybe a masked username, e.g. `jo***@pharmacy.com`). Never log secrets.

### 4. No authentication/authorization check — High
**Line 9 (`POST /pharmacy-link`) and Line 22 (`GET /pharmacy-link/:careRecipientId`)**

Neither handler verifies that the requester (`userId` from the body, or whoever is making the GET request) is actually an authorized family member/caregiver for `careRecipientId`. `userId` is taken from the request body and trusted as-is — nothing stops any authenticated (or even unauthenticated, if there's no middleware upstream) caller from:
- linking pharmacy credentials to *any* `careRecipientId` they don't belong to, or
- fetching the stored username/password for *any* `careRecipientId` by guessing/enumerating IDs in the GET route.

**Fix:** Derive the acting user from session/auth middleware (not `req.body.userId`), and check a `care_relationships` (or equivalent) table to confirm that user has permission for `careRecipientId` before insert or select. Also consider rate-limiting/least-privilege: the GET route in particular should never need to return the raw password to the frontend at all (see #5).

### 5. Sensitive data over-exposure via `SELECT *` — Medium
**Line 24-26**

The GET endpoint returns the full row — including the plaintext (or even encrypted) `password` column — straight to the client as JSON. The UI only needs refill status / linked state, not the credential itself.

**Fix:** Select and return only the non-sensitive columns needed to render "linked" status (e.g. `user_id`, `care_recipient_id`, `linked_at`, `pharmacy_name`), never the password column, regardless of encryption.

### 6. No input validation — Low/Medium
**Line 10**

`userId`, `pharmacyUsername`, `careRecipientId` are used unchecked — no type/format/length validation, no check that `careRecipientId` is a real recipient the system knows about. Combined with #1 and #4, this widens the injection and spoofing surface.

**Fix:** Validate shapes (e.g. UUID format for IDs) and reject malformed input before it reaches the query layer.

## Summary Table

| # | Issue | Severity | Location |
|---|-------|----------|----------|
| 1 | SQL injection via string interpolation | Critical | lines 12-15, 23-25 |
| 2 | Pharmacy password stored in plaintext | Critical | lines 13-14, 26 |
| 3 | Password written to application logs | High | line 17 |
| 4 | No auth/ownership check on link or read | High | lines 9, 22 |
| 5 | `SELECT *` leaks password to API response | Medium | lines 24-26 |
| 6 | No input validation | Low/Medium | line 10 |

## Bottom line

This file should not be committed as-is. The combination of SQL injection + plaintext credential storage + credential logging + missing authorization means any one of several common attack paths (injection, log access, API enumeration) leads directly to live pharmacy account takeover for care recipients — a uniquely bad outcome for an elderly/vulnerable user base. Fix #1, #2, #3, and #4 before this ships; #5 and #6 should be fixed in the same pass since they're small.
