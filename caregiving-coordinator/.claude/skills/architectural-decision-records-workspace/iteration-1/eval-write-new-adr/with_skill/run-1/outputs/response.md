Draft ADR (not saved to docs/adr/ yet; shown for your approval). Suggested file: `docs/adr/0002-store-visit-recordings-encrypted-in-s3.md`. I have not checked whether docs/adr/ exists. If it does not, `0001-record-architecture-decisions.md` is created first and this becomes 0002.

# ADR-0002: Store visit recordings encrypted in S3 with one key per family

- **Status:** Proposed
- **Date:** 2026-10-31 (date decided: please confirm)
- **Decided by:** (your name)

## Context

Visit recordings are sensitive health information shared by several siblings. When a sibling leaves a family group, their access must be revocable. Recordings are large, and the team is small.

## Decision

Store each recording as an encrypted object in S3, using a separate encryption key per family. Revoking access means rotating or removing that family's key, not changing database rows.

## Options considered

1. **Encrypted S3 objects, one key per family.** Chosen: access can be revoked per family without touching other families' data.
2. **Database blobs.** Rejected: no per-family revocation, and large files bloat the database and its backups.
3. **S3 with one shared key.** Rejected: revoking one family's access would affect everyone (assumed; confirm if this was considered).

## Consequences

- **Good:** Revocable access when a sibling leaves; the database stays small.
- **Bad:** More code and key-management work (create, store, rotate, delete keys). A lost key means unrecoverable recordings.
- **Enforcement:** Not set yet. Candidate gate rule: fail if recording code writes to a database blob column. Rule name to be added to `arch-gate.config.json`.

Open questions: where keys are held (e.g. AWS KMS), and the key-loss recovery plan.

Skills: applied architectural-decision-records. Not relevant: the other skills (no code to review).
