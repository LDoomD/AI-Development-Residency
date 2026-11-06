# Handoff report template

Copy the skeleton below and fill in every section. Keep the section headings exactly as written (`## 0. Start here` through `## 9. Verification receipt`), because `scripts/check_handoff.py` looks for them.

The examples come from two kinds of projects, so the format stays general:
- (A) a product discovery project
- (B) a software feature build

Replace them with your own content.

---

## Skeleton

```markdown
# Handoff: <project> → <next milestone> (<YYYY-MM-DD>)

Replaces: <older report file names, or "none">

> Paste to start: "Read this handoff report. Confirm in a few lines where we are and what <next milestone> starts from. Then <first step> and show it to me before doing anything else."

## 0. Start here
- Where we are: <the milestone just finished, and the overall goal>
- The outcome so far, in one sentence: <the key result the next milestone builds on>
- Next milestone: <name>, and its definition of done or template

## 1. Locked outcomes
<One block per finished milestone. Each outcome is tagged Approved or Proposed, with where it lives.>

## 2. Key findings and data
<The tables, numbers and verdicts the next milestone needs. Every number has its source next to it, and a confidence level: Authoritative / Credible secondary / Estimate.>

## 3. Excluded and deferred
<What was set aside, why, and when or where it comes back.>

## 4. Open decisions
<What the owner still has to decide. The next session must not decide these alone.>

## 5. Bridge to the next milestone
<A table: this output → where it goes in the next template or step, and why.>

## 6. First steps
<A numbered list. Step 1 is usually "show X to the owner before doing anything.">

## 7. Working rules
<A pointer to the project's rule files, plus the 5-10 rules most likely to be broken next.>

## 8. Where things live
<Files, links, data folders and the version-control state: branch, last commit, anything not saved.>

## 9. Verification receipt
- Outcomes and where each came from: <a short claim → source list, or "see sections 1-2">
- Checks run: <for example, "check_handoff.py passed; numbers re-read from results.json">
- Not checked: <what wasn't verified, and why>
- How this prevents drift: <for example, "decisions tagged Approved; exclusions listed; first step requires owner review">
```

---

## What good looks like, section by section

**1. Locked outcomes**
- (A) "Target audience: adult children caring for a parent, and spouses. **Approved** 2026-11-04 (`docs/audience.md`)."
- (A) "Largest opportunity: helping exhausted caregivers get relief. **Approved** 2026-11-05 (`docs/market.md`, section 4)."
- (B) "Auth uses session cookies, not JWT. **Approved** (ADR `docs/adr/0003-sessions.md`)."
- (B) "Rate limit of 100 requests a minute. **Proposed**, not yet confirmed by the owner."

**2. Key findings and data** (put sources next to the numbers):

| Finding | Number | Source | Confidence |
|---|---|---|---|
| Caregivers who say a break would help vs have used one | 39% vs 13% | AARP report 2025, p.26 (`docs/sources/aarp.pdf`) | Authoritative |
| p95 checkout latency after the cache change | 180 ms | `perf/2026-11-05.json` | Credible secondary |

**3. Excluded and deferred**
- (A) "MVP scoring is deferred to the release-planning milestone. It's out of date, and it comes back there."
- (B) "Social login is out of scope for v1. The owner said 'not before launch.'"

**4. Open decisions**
- "Who pays: families, employers or insurers? Needed before positioning."

**5. Bridge to the next milestone**

| This output | Goes into | Why |
|---|---|---|
| The 4 gaps from the competitive analysis | The feature list (rows) | Features should fill the gaps |
| The approved API contract | The integration tests | The tests check the contract |

**6. First steps**
1. Fill in the research checklist, or the plan, and show it to the owner.
2. Build the inputs table: each input, used or left out, and why.
3. ...

**7. Working rules** (examples of the kind that get broken):
- "Questions get answers, not edits."
- "Preview tables before publishing."
- "Never overwrite old versions."

**9. Verification receipt**
- "Not checked: competitor prices weren't re-checked today. They were last checked on 2026-11-04."

## What to leave out

- **The story of the session,** step by step.
- **Long quotes and raw evidence.** Link to the evidence file instead.
- **Old versions and correction history,** unless the next milestone needs to know something was wrong.
