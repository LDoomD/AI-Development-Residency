# ADR-0002: Decode engine (AI + keyword, grounded)
- Source copy: https://app.notion.com/p/0439219a469183c5ac5f0139213e1277
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:15.005Z
- Not saved: none

---

**Status:** Accepted · 2026-11-04
**Deciders:** Morgan (owner)
**Related:** ADR-0001; ADR-0003 (three-bucket output); ADR-0004 (result caching); future ADR-0005 (AI model choice)

## Context

Accuracy is the core problem Hat Check solves: people make real career decisions on its output, and a confident wrong answer erodes trust fast. Job postings are messy, non-standard text. Keyword matching alone is precise on exact words but misses duties worded differently (low recall), which are exactly the hidden duties the product exists to reveal. An AI reader has high recall but can invent a match it cannot support (a precision risk). We need both high recall and high precision.

## Options considered

1. **Keyword matching only.** Free, instant, always available, fully transparent. Rejected: low recall misses the reworded and hidden duties that are the product's main value.
2. **AI reading only.** High recall and handles messy text, but can invent duties and is hard to check. Rejected: ungrounded AI output is the fastest way to lose user trust.
3. **AI reading and keyword, cross-checked and grounded (chosen).** The AI reads for meaning, keyword matching catches exact hits, and every AI-proposed match must cite a quote from the posting and map to a real framework entry, or it is dropped.

## Decision

We will decode a posting by running an AI reader and a keyword matcher in parallel: both read the posting at the same time, then their results are merged and de-duplicated. Every AI match must be grounded: it must cite an exact or near-exact quote from the posting and map to an entry in the framework, or it is dropped and not shown. Keyword matching also serves as the cross-check, and as the fallback when the AI is unavailable.

## Consequences

**Easier:** reveals reworded and hidden duties with a receipt on every claim, so nothing is invented; accuracy becomes measurable through an eval harness; stays honest to the "never invent, show the evidence" promise.

**Harder, accepted:** a cost for each decode; slower than keyword alone; an external dependency that can fail; it must be defended against prompt injection in the posting text.

**Next:** choose the AI model by measured accuracy on labeled examples (future ADR-0005); design the AI-down fallback (a labeled keyword-only read); add cost caps and prompt-injection defense.
