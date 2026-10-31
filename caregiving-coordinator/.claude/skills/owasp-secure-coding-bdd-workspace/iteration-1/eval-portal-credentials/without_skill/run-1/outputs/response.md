# Designing "paste your insurance portal login" safely

**Start by questioning the design.** Storing users' insurance passwords is high risk: a breach exposes health and financial data, and it likely violates the portals' terms of service. Scraping behind a login is also brittle and may trigger account lockouts.

**Safer alternatives, in order of preference**
1. Use an official API or standard OAuth (for example FHIR Patient Access APIs, which US payers must offer). The app gets a revocable, scoped token and never sees the password.
2. Use an aggregator (Flexpa, Particle, and similar) that handles the connection and consent.
3. Let users upload an EOB or claim PDF, or enter the claim number manually.
4. Only if none of these work, store credentials (see below).

**If you must store credentials**
- Never log them, return them to the client, or put them in URLs, analytics, or error reports.
- Send over TLS only. Encrypt at rest with envelope encryption (a KMS-held key, per-user data keys), in a separate store from the main data.
- Collect the minimum: read-only or delegated accounts where the portal allows. Show a clear consent screen saying what is stored and why.
- Decrypt only inside a narrow worker that logs in, fetches status, and discards the plaintext. No admin or support access to plaintext.
- Enforce authorization: a user can only trigger checks on their own linked accounts, and (for caregivers) only with explicit, auditable delegation.
- Rate-limit and back off to avoid lockouts. Handle MFA and CAPTCHA by pausing and asking the user, never by bypassing them.
- Let users disconnect at any time, which deletes the credentials immediately. Also delete on account closure and after a period of inactivity.
- Keep an audit log of access (without secrets). Alert on unusual use.
- Treat fetched claim data as sensitive health data: encrypt it, minimize retention, and consider HIPAA and state privacy obligations.
- Sanitize and validate everything scraped from portals. Never trust it.

**Before building:** write a threat model, decide the breach story (rotate keys, notify users), and get legal review.
