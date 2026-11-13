# ADR-0004: Result caching by content hash
- Source copy: https://app.notion.com/p/8b39219a469182d1a3fa815f9e2c9802
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:15.187Z
- Not saved: none

---

**Status:** Accepted · 2026-11-05
**Deciders:** Morgan (owner)
**Related:** ADR-0002 (decode engine); ADR-0001 (privacy)

## Context

Two outcomes drive this decision: results must be fast (low latency, the wait between pasting and seeing results), and nothing personal about the user may be exposed. An AI decode costs money and takes a few seconds, and the same public posting may be decoded by many people. Re-running the engine every time wastes money and makes users wait. ADR-0001 keeps user data on the device, so any cache must not become a store of personal data.

## Options considered

1. **No cache.** Rejected: every identical paste pays the full cost and the full wait.
2. **Per-user cache.** Rejected: it would store a record of what a person searched, which conflicts with ADR-0001's privacy stance.
3. **Shared cache keyed by content hash (chosen).** Key on a hash of the posting text plus the framework version, store the result only, and expire entries after a time limit.

## Decision

We will cache decode results in a shared server-side cache keyed by a hash of the posting text, the framework version, and the model and prompt version, so a change to any of them yields a fresh result instead of a stale one. The cache stores the decode result only, never who requested it, so it holds no record tying a person to a search. Entries expire after a set time (a TTL).

> ✅ Resolved: ADR-0001 was amended on 2026-11-05 to scope "decodes never leave the device" to a user's own identifiable history. That permits this anonymous, content-addressed cache of results for public postings as derived shared data, so this decision is now Accepted.

## Consequences

**Easier:** identical postings return instantly and at no AI cost; lower load at busy moments; the key carries no user identity, so the cache holds no record of who searched for what.

**Harder, accepted:** it stores decode results off the user's device, which ADR-0001's 2026-11-05 amendment permits as anonymous derived shared data; a cached result contains quotes drawn from the posting, so if a posting itself held personal data a quote could too, which the TTL and the no-identity key bound rather than eliminate; the cache is an optimization, so correctness must never depend on it (a miss or a flush must always fall back to a fresh decode).

**Resolved:** the owner chose option (a): ADR-0001 was amended on 2026-11-05 so that "decodes never leave the device" scopes to a user's own identifiable history, which permits this anonymous, content-addressed cache as derived shared data.

**Next:** set the TTL; choose the cache store (for example a Postgres table or a managed cache) in the data architecture section (section 6).
