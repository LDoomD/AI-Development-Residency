# Review: routes/pharmacy-link.js

I'd hold off on committing this one — there are several serious security issues, not just style nits. This route stores a real third-party credential (the parent's pharmacy portal login), so the bar here is higher than normal CRUD code.

## Critical

**1. SQL injection (both routes)**
Both the `INSERT` (line 12-15) and the `SELECT` (line 23-25) build queries with raw template-string interpolation instead of parameterized queries:

```js
`INSERT INTO pharmacy_links (user_id, care_recipient_id, username, password)
 VALUES ('${userId}', '${careRecipientId}', '${pharmacyUsername}', '${pharmacyPassword}')`
```

Any of `userId`, `careRecipientId`, `pharmacyUsername`, or `pharmacyPassword` containing a `'` lets an attacker break out of the string and run arbitrary SQL. Given this field holds a pharmacy *password*, you should assume users will paste in passwords containing quotes, backslashes, etc. — this isn't just a theoretical attack vector, it'll break on legitimate input. Use parameterized/prepared statements (`?` or `$1` placeholders) for every value.

**2. Plaintext password storage**
`pharmacyPassword` is inserted into the DB as-is. This is a real external-service password (the parent's pharmacy login). If the database is ever dumped or leaked, every linked family's pharmacy credentials go with it. These credentials should be encrypted at rest (e.g., envelope encryption with a KMS-managed key), not stored as plaintext in a `password` column.

**3. Credentials logged in plaintext**
Line 17 logs the full username/password pair to the console:
```js
console.log(`Linked pharmacy account for care recipient ${careRecipientId}: ${pharmacyUsername}/${pharmacyPassword}`);
```
This will end up in log aggregation, crash dumps, or anyone with log access — a textbook credential leak. Remove the password from the log line entirely (and probably the username too).

**4. GET endpoint returns raw credentials**
`SELECT * FROM pharmacy_links ...` followed by `res.json(rows)` sends the stored username *and password* back over the API to whoever calls this endpoint. Even if the DB weren't compromised, this turns the API itself into a credential-disclosure endpoint. Select only the columns the client actually needs (e.g., link status, pharmacy name) and never return the password.

## High

**5. No authentication / authorization check**
Neither route verifies that the authenticated caller is actually allowed to act on `careRecipientId`. `userId` is taken straight from the request body (not from a session/auth token), so anyone who can guess or enumerate a `careRecipientId` can:
- POST a pharmacy link under any `userId` they like, or
- GET any other family's pharmacy credentials via `/pharmacy-link/:careRecipientId`.

There's no check that the requesting user is actually a family member linked to that care recipient. This needs an auth middleware pulling `userId` from a verified session, plus an authorization check (is this user permitted to see/manage this care recipient's links) before touching the DB.

## Medium

**6. No input validation**
No checks that `userId`, `careRecipientId`, `pharmacyUsername`, `pharmacyPassword` are present, correctly typed, or within reasonable length — anything in `req.body` goes straight into the query.

**7. No duplicate/update handling**
A second POST for the same care recipient just inserts another row rather than updating the existing link, which can leave stale credentials in the table alongside new ones.

## Summary of fixes needed before merge
- Switch both queries to parameterized statements.
- Encrypt pharmacy passwords at rest; never store/return them in plaintext.
- Strip credentials from the log line.
- Add auth middleware + an authorization check scoping access to the requesting user's actual family/care-recipient relationship.
- Validate request body shape.
- Restrict the GET response to non-sensitive fields.

Given the sensitivity of what this route handles (a stored third-party password tied to a parent's medical/pharmacy account), I'd treat the plaintext storage/logging and the missing authorization check as blockers, not follow-ups.
