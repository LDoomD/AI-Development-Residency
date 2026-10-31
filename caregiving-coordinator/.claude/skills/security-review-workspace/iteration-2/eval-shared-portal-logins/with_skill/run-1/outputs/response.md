# Security review: plan to store shared insurance portal passwords

**Guide:** OWASP Top 10:2025 plus `docs/risk-profile.md`. Plan review only; no code seen.

## Summary
1 Critical, 2 High, 1 Medium. Fix first: do not store these passwords in plain text.

### 1. Plaintext credential column (Critical) - A04 Cryptographic Failures
Anyone with database access reads every family's insurance logins at once. Those accounts hold health data. The risk profile rates this plan Critical.
**Fix:** Encrypt each value with an authenticated algorithm (AES-256-GCM) using a key held outside the database (a secrets manager or KMS). Never use home-made encryption.

### 2. No audit trail (High) - A09 Logging Failures
Siblings sharing logins means nobody can tell who viewed or changed one.
**Fix:** Log every reveal, edit, and delete (who, what, when). Never log the password itself.

### 3. Shared access is all-or-nothing (High) - A01 Broken Access Control
If one sibling leaves, the only way to revoke is changing the portal password for everyone.
**Fix:** Per-user permissions, a check on every read, and individual revocation. Show the password only on explicit request, and never return it in list responses.

### 4. Portal terms and design (Medium) - A06 Insecure Design
Many portals forbid sharing logins. Storing others' passwords makes you a password manager, with that liability.
**Fix:** Consider whether v1 needs this at all (the risk profile lists it as open), or use delegated or proxy access where portals offer it.


## Checked: plan against A01, A04, A06, A09 and risk profile.

## Not verified
No code, schema, backups, or hosting reviewed. A02, A03, A05, A07, A08, A10 skipped (no code).

## Needs a human decision
Are stored portal logins in scope for version 1?

## Next steps
Draft the schema with encrypted columns, then rerun this review on the code. Get a human security review before real data.
