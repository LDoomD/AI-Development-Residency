# ADR: Store visit recordings encrypted in S3 with per-family keys

**Status:** Accepted
**Date:** 2026-10-31
**Suggested path:** docs/adr/0001-encrypted-s3-per-family-keys-for-recordings.md

## Context
The app stores recordings of caregiving visits. These are sensitive health-related data shared among family members (siblings). When a sibling leaves the family group, their access must be revocable. Two options were considered: database blobs, or encrypted objects in S3.

## Decision
Store visit recordings as encrypted objects in S3. Each family has its own encryption key (for example, a separate KMS key per family). The database stores only metadata and a reference to the S3 object.

## Rationale
- Revocation: access is controlled by a per-family key. Revoking or rotating that key cuts off access, which a shared database blob store does not allow cleanly.
- Isolation: a compromise or deletion affects one family, not all.
- Large binary files stay out of the database, which keeps it small and backups fast.

## Consequences
**Positive**
- Revocable, per-family access to recordings.
- Smaller database and faster backups.

**Negative / costs**
- More code: upload, download, and encryption/decryption paths.
- Key-management work: creating, rotating, revoking, and deleting keys, plus audit logging.
- Revoking a departing member may mean re-encrypting under a new key, so cost and process need defining.
- Metadata in the database and objects in S3 can drift, so consistency needs handling.

## Alternatives considered
- **Database blobs:** simpler, but access cannot be revoked per family without re-encrypting or restructuring data, and they bloat the database.

## Open questions
- How is key loss or recovery handled?
- Retention and deletion policy for recordings.
