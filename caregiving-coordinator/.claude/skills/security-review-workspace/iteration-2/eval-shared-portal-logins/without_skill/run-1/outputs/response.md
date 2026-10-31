# Plan review: plaintext insurance portal passwords

**Verdict: do not ship this plan.** Storing third-party portal passwords in plaintext is a critical risk.

## Problems
1. **Plaintext storage (critical).** Any database leak, backup, log, SQL injection, or admin or developer access exposes every family's insurance login. Insurance portals hold health data (PHI), so a breach could carry HIPAA-style and state breach-notification consequences.
2. **Hashing won't work.** You must replay these passwords, so you need reversible encryption, not a hash. That is a sign you are holding credentials you probably shouldn't hold.
3. **Sharing by copying credentials.** There is no audit trail of who viewed a password. You can't revoke one sibling's access without changing the password. Portals may also treat shared logins as a terms-of-service violation, and shared logins break MFA.
4. **Blast radius.** Password reuse means one leak can compromise other accounts.

## Better options
- **Best: don't store them.** Link to the portal and let each sibling use their own account. Many insurers offer delegate or proxy access, authorized representative forms, or family sharing.
- **If you must store them:**
  - Encrypt each secret with AES-256-GCM, using envelope encryption with keys in a KMS (AWS KMS, GCP KMS or Vault), never in the same database or repo.
  - Support per-user key wrapping, or a zero-knowledge design, for stronger isolation.
  - Enforce authorization per family or circle.
  - Reveal secrets only on explicit click, and require re-authentication.
  - Write an audit log of every reveal.
  - Never log or return secrets in API list responses.
  - Support key rotation and deletion.
- **Alternative:** recommend that families use a real password manager's shared vault (1Password or Bitwarden families), and have the app link to it.

## Next steps
Make this decision first, document it, and add a test that confirms the DB column never holds readable text.
