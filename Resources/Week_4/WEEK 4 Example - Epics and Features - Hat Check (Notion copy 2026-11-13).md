# Epics and Features - Hat Check
- Source copy: https://app.notion.com/p/ce99219a469183bf990f01e35ac08ed2
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:11.806Z
- Not saved: none (a link-preview block for the deliverable has no text)

---

# Find the deliverable here

(link preview: https://app.notion.com/p/ce99219a469183bf990f01e35ac08ed2#f409219a469182b89aed811b84dd3929)

## Epic 1 — Understand the job from one posting

The core value: paste one posting and get the job decoded against the Skills and Practices Framework.

### Feature 1.1 — Enter a title and posting (no account)

- Value: start immediately; nothing is saved past the session.
- Tickets: input screen (session-only); resolve the title to a job function with honest "not covered."

### Feature 1.2 — Decode the posting against the framework

- Value: see which standard hats the posting covers, misses, and adds, grounded in the framework.
- Tickets: match wording to activities, deliverables, and tools (AI recognition unioned with keyword, validated); roll up to hats via RACI; classify the three sets; compute match percent and the title-fit verdict.
- Scoring refactor (ADR-0039, 2026-11-04) — supersedes the one-item "covered" rule above; code owed, nothing built yet:
- T-prop-1: score each hat by its share (matched activities + deliverables ÷ the hat's total activities + deliverables) and classify full (25% or more), partial (above 0, under 25%), or none; tools no longer roll up to a hat and the "everyone" duty is excluded. Lands in both decode twins (src/domain/decode and eval/lib/decode.mjs).
- T-prop-2: the decode result carries a per-hat score and match level in place of the covered/missing boolean; the overall title-fit uses Formula D (full × 1 + partial × 0.5, over all standard hats), with the verdict thresholds unchanged.

### Feature 1.3 — See the result one part at a time

- Value: focus on one part, not a wall of detail.
- Tickets: results stepper (verdict, then each hat set with counts, then unplaced lines; each hat expands in place to show its evidence) (T06).
- T-prop-3 (ADR-0039): group hats by match level (full, then partial) with each hat's share shown, in place of the three covered / missing / non-standard sets.

### Feature 1.4 — Trust what you see

- Value: check every match; nothing is invented.
- Tickets: receipt showing all matched quotes per hat (each quote to its hat and RACI role, exact or similar), not one example; list the lines we could not place; "How it works" panel.
- Open (ADR-0039, owner Morgan): whether tools still show as supporting evidence under a hat, or drop from the matching output entirely.

### Feature 1.5 — Always get a grounded result

- Value: the app never leaves you with nothing.
- Tickets: AI-unavailable fallback (framework-only keyword read, labeled); a failed decode shows a plain error with Try again (T09).

### Feature 1.6: Prepare your application

- Value: turn the decode into action: what to put on the resume, how to phrase it as outcomes, ATS keywords, and cover letter and interview points, all built from the hats.
- Tickets: resume and application prep (T16).
- Note (ADR-0039): the prep groups come from the match levels — hidden hats (standard hats scoring none) first, then full and partial standard hats, then non-standard.

## Epic 2 — Foundations

### Feature 2.1 — Three-tier app and the CI architecture gate

- Tickets: Next.js + Material UI on Vercel; the architecture gate extended with tier rules.

### Feature 2.2 — Framework data tier

- Tickets: load the framework into Supabase (pinned, integrity-checked) and publish the read snapshot at build time.

## Epic 3 — Quality, trust, and compliance

### Feature 3.1 — Prove accuracy

- Tickets: the eval harness with labeled fixtures; pick the model by measured accuracy.
- T-prop-4 (ADR-0039): the eval scorer reads match levels; a labeled fixture carries an expected match level per standard hat, not just presence.

### Feature 3.2 — Security (OWASP)

- Tickets: prompt-injection defense, secrets, SSRF, cost caps, each with an executable security scenario.

### Feature 3.3 — Accessibility (WCAG 2.2 AA)

- Tickets: keyboard, focus, labels, contrast, targets; axe and checklist gates.

### Feature 3.4 — Licensing and attribution

- Tickets: MIT license and the CC BY 4.0 credit line wherever framework data appears, in one place.
