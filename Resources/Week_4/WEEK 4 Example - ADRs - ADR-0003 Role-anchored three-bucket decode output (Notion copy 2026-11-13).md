# ADR-0003: Role-anchored three-bucket decode output
- Source copy: https://app.notion.com/p/53e9219a469182a8a37001a5ec11fbf4
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:15.095Z
- Not saved: none

---

**Status:** Accepted · 2026-11-05
**Deciders:** Morgan (owner)
**Related:** ADR-0002 (decode engine); ADR-0001 (privacy)

## Context

Hat Check exists to help a job seeker prepare for an interview by seeing a posting fully. A flat list of matched duties is not enough. The seeker needs to see what the role normally involves that this posting left out, and what this posting adds beyond the standard role. We also weighed surfacing the AI's ungrounded guesses as an "unplaced" list, but showing possibly invented duties to a stressed job seeker is the opposite of transparency.

## Options considered

1. **Flat list of matched duties only.** Rejected: hides what is missing and what is extra, so it gives no interview-prep value.
2. **Matched duties plus an "unplaced / couldn't confirm" list of ungrounded guesses.** Rejected: parades low-confidence, possibly invented content and undermines trust.
3. **Role-anchored three-bucket comparison (chosen).** Compare the posting against the framework's expected duties for the role, and show three grounded buckets.

## Decision

We will present the decode as three grounded buckets, measured against the framework's expected duties for the identified role:

- **What's there:** expected duties that are quoted in the posting.
- **What's missing:** expected duties with no quote in the posting.
- **What's extra:** grounded duties found in the posting that are not standard for the role.

Ungrounded AI guesses are discarded, never shown. This requires three things: framework reference data shaped as role to expected duties; a role-identification step near the front of the pipeline that matches the posting's title to a framework role; and a set comparison between the expected set and the grounded duties found.

The "what's missing" and "what's extra" buckets are only as trustworthy as the identified role, so when role identification is low-confidence or finds no clean match we do not show "missing" or "extra." We fall back to the grounded "what's there" list and ask the user to confirm or pick the role. A confident wrong comparison is worse than none for an accuracy-first product.

## Consequences

**Easier:** a complete, interview-ready view; every bucket is grounded; "what's missing" turns an absence into a question the seeker can prepare for.

**Harder, accepted:** the framework data must carry the role-to-duties structure; role identification can be ambiguous when a title does not match cleanly, which the graceful-degradation rule in the Decision handles; "what's missing" means "no grounded quote was found," so a recall miss by the readers can masquerade as a genuinely absent duty, a limit the eval harness measures; "what's extra" means "not in this role's expected set," so a gap in the framework's expected duties can produce a false "extra."

**Next:** define how role identification handles unknown or ambiguous titles; design the framework data schema in the data architecture section (section 6).
