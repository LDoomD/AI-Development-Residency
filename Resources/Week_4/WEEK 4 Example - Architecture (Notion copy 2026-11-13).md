# Architecture
- Source copy: https://app.notion.com/p/00e9219a46918328addd81a17880900c
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:13.410Z
- Not saved: none

---

> 🧭 This is the technical architecture for Hat Check: the plan for how the app is built, written before we build it. We fill it in together, one decision at a time. Every important choice also gets a short "why" recorded as an ADR (Architecture Decision Record).

**Product context:** Vision and Scope - Hat Check (https://app.notion.com/p/3d59219a469182d09f0701b9add32085) · Epics and Features - Hat Check (https://app.notion.com/p/ce99219a469183bf990f01e35ac08ed2)

**Status:** Draft, started 2026-11-04

---

## 1. What we're building

_Plain-language summary of the app and who it serves, pulled from the vision. The "why" behind the whole system._

⬜ To fill together

## 2. Where the app lives (the three tiers)

_The browser (what the user sees), the app server (does the work), and the database (stores what must last). Which work happens in each place, and where each server runs._

⬜ To fill together

## 3. Technology decisions (the ingredients)

_The languages, framework, UI library, database, AI service, and hosting we pick, and the reason for each. One row per choice._

⬜ To fill together

## 4. How the code is organized (the layers)

_Presentation, domain (the business rules), and data layers. The one rule that matters most: the business rules never depend on the screen or the web._

⬜ To fill together

## 5. Software pattern (the shape of the system)

_The overall style (for example a modular monolith) and how we handle the decode logic, with the trade-offs we accept._

⬜ To fill together

## 6. Data architecture

_What data the app holds, who owns each fact (one home per fact), where it is stored, and the database diagram._

⬜ To fill together

## 7. The four enterprise promises

_How the design keeps each promise: reliability, scalability, maintainability, and security._

- **Reliable:** one small failure never takes down the whole app.
- **Scalable:** it still runs well at the busiest moment, not just on a quiet day.
- **Maintainable:** a new developer can understand and safely change it.
- **Secure:** people's data stays private and only the right person can reach it.

⬜ To fill together

## 8. How a decode flows end to end

_Follow one request: a user pastes a posting, and we trace it through the browser, the server, the AI, the framework data, and back to the screen._

**One decode, step by step.** Each step reflects a recorded decision.

1. **Guard the input** (browser and server): cap the paste size, reject an empty paste, and treat the posting as data, never as instructions (prompt-injection defense).
2. **Check the cache:** hash the posting text plus the framework version; on a hit, return the stored result at once (ADR-0004).
3. **Identify the role:** match the posting's title to a role in the framework (ADR-0003).
4. **Read in parallel:** the AI reader and the keyword matcher read the posting at the same time (ADR-0002).
5. **Merge and de-duplicate:** combine both lists and note which reader found each duty.
6. **Ground every match:** keep only duties with a real quote from the posting and a real framework entry; drop the rest (ADR-0002).
7. **Compare to the role's expected duties:** sort the grounded results into what's there, what's missing, and what's extra (ADR-0003).
8. **Attach receipts and store:** each shown duty carries its quote, its framework entry, and which reader found it; save the result to the cache (ADR-0004).
9. **Show on screen:** the three buckets, each item with its receipt. The user's decode stays in their browser (ADR-0001).

## 9. Decision log (ADRs)

_The full Architecture Decision Records live on the ADRs page, one per decision. This section is the running index._

- ADR-0001: Account-free, browser-only user data (https://app.notion.com/p/4ae9219a4691833aad98019313f23087): account-free, browser-only user data (accepted).
- ADR-0002: Decode engine (AI + keyword, grounded) (https://app.notion.com/p/0439219a469183c5ac5f0139213e1277): decode engine, AI + keyword, grounded (accepted).
- ADR-0003: Role-anchored three-bucket decode output (https://app.notion.com/p/53e9219a469182a8a37001a5ec11fbf4): role-anchored three-bucket output (accepted).
- ADR-0004: Result caching by content hash (https://app.notion.com/p/8b39219a469182d1a3fa815f9e2c9802): result caching by content hash (accepted).

**All records:** ADRs (https://app.notion.com/p/0f29219a4691835c8077816bf784f9ef)

## 10. Open decisions

_Choices we have not made yet, parked here so nothing is lost._

- **AI-down fallback:** the exact behavior when the AI service is unavailable, a labeled keyword-only read. Parked by owner.
- **AI model choice:** which model, decided by measured accuracy on labeled examples through an eval harness (future ADR-0005).
- **Role identification edge cases:** how to handle unknown or ambiguous job titles (raised by ADR-0003).
