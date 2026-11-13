# ADR-0001: Account-free, browser-only user data
- Source copy: https://app.notion.com/p/4ae9219a4691833aad98019313f23087
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:14.931Z
- Not saved: none

---

**Status:** Accepted · 2026-11-04 (amended 2026-11-05)
**Deciders:** Morgan (owner)
**Related:** ADR-0002; ADR-0004 (result caching)

## Context

Hat Check's vision promises a free, account-free product where a job seeker's data never leaves their device. The Week 4 class homework, by contrast, teaches sign-up and log-in with each person's data saved in the database and protected by row-level security. These pull in opposite directions, so we had to decide where a user's decoded jobs are stored.

## Options considered

1. **Account-free, browser-only (chosen).** A user's decodes live only in their own browser. Supabase holds only the shared framework reference data, read-only. Honest to the vision and simplest to build. Downside: no sync across devices, and nothing is kept if the browser is cleared.
2. **Accounts and saved data in Supabase (with row-level security).** Matches the class checklist exactly, but breaks the "no account, data never leaves your device" promise and adds auth and personal-data duties.
3. **Account-free now, optional login later.** Ships account-free for MVP #1 but leaves room for an opt-in sync in a later release. Keeps the promise now, costs more planning up front.

## Decision

We will keep Hat Check account-free. A job seeker's decodes are stored only in their own browser, and never leave their device. Supabase stores only the shared framework reference data, which everyone reads and no user writes.

**Scope clarification (amended 2026-11-05):** "a user's decodes" means a user's own identifiable history, the record of what this person looked at, which stays on their device. It does not forbid an anonymous, content-addressed cache of decode results for public postings, keyed by the posting's text with no user identity attached. Such a cache is derived shared data, in the same class as the framework reference data, and is permitted (see ADR-0004).

## Consequences

**Easier:** no login to build or secure; no personal data to protect, leak, or delete; the app keeps its core promise of free and private; a far smaller security and compliance surface.

**Harder, accepted:** no cross-device sync; a cleared browser loses a user's history; no email re-engagement; no server-side data to learn from.

**Next:** choose the browser storage mechanism (for example localStorage or IndexedDB); add a guard so no personal data is ever written to Supabase.
