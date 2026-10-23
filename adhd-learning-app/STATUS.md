# Project status — start here

**Last updated:** 2026-10-23
**Phase:** Week 2 of the residency. Specs stage. No application code written yet.

---

## What this is

The **Premium specialization project** for the Tech Fleet AI Development
Residency (Fall/Winter 2026). It is a learning system for neurodivergent
adults, rebuilt as a hosted web application.

**Subject domain for the first slice: automation and agentics.** Not Spanish,
not F&I.

To be clear about what that means: the subject decides what the **seed content
in the database looks like** — the lessons, cards, and examples needed to demo
a working loop. It does **not** mean using this app to study agentics while
simultaneously building it during the residency. The build is the work; the
subject is just what the content is about.

Practical consequence: enough sample content is needed to click through a real
lesson in each mode, and no more. Authoring a full curriculum is out of scope.

Second consequence, worth stating honestly: because the app will not have a
real daily user during the eight weeks, **learning effectiveness cannot be
validated in that window.** The residency grades engineering, security, and
architecture — not learning outcomes — so this is acceptable. But no claim
should be made that the system is proven to improve retention. The research
supports the *design*; it does not substitute for evidence that this build
works.

## How this project came to be

It replaced an earlier choice. The original residency project was
`growth-ads-system`, a multi-channel ads and sales reconciliation panel. It
was dropped on 2026-10-23 for one decisive reason: **its critical path ran
through other companies' approval queues.**

Week 3 of the residency requires a working app deployed on Vercel by Nov 2.
The ads product needed Google Ads Standard access (~10 business days, manual
review), Meta Full Access (500 API calls in 15 days first), Shopify Level 2
protected-customer-data approval, Amazon per-seller authorization, and Mercado
Libre ad-spend access that could not even be confirmed to exist. With no
platform data, the app had nothing to show. It also fit Week 8 (SEO/AEO)
badly, since a dashboard behind a login has nothing to optimize.

`growth-ads-system` is **parked, not deleted.** Its research is sound and the
business idea survives for later.

This project has no third-party approval gates at all.

## Where the research came from

`docs/inherited-research/` is copied verbatim from the earlier
`ADHD-Learning-System` project — roughly 222,000 words built in August 2026.
It includes learning science with effect sizes, an adversarial review, killed
claims documented as killed, prior art, and 14 book extractions.

**That research transfers at 100%. The implementation does not.** The old
build was a local command-line toolchain (Obsidian + Anki + NotebookLM). This
one is a hosted web app (Vercel + Supabase + user accounts), because that is
what the residency requires. Same thinking, different platform.

The old `ADHD-Learning-System` folder stays on disk as the original archive.
Read from it; do not build in it.

## The design, in brief

Three layers, from `docs/inherited-research/DECISIONS.md`:

1. **Universal** — retrieval practice + distributed practice.
2. **ADHD supports** — externalized state, one `current` lesson at a time,
   effort self-rating, an escape hatch.
3. **Subject-type router** — MAP / DRILL / EXAMPLES / REPS, dispatched by
   material type.

Two mechanisms matter most, and they are the project's best examples of
agent guardrails:

- **The floor** — effort self-rating of 7–9 means reduce scope and add
  scaffolding. **Never press on.**
- **The escape hatch** — on a failed gate: decompose, reframe, or park.
  **Never repeat unchanged.** Three consecutive failures auto-park.

## Scope for the residency

| When | What |
|---|---|
| **Week 3** (due Nov 2) | Router + MAP, DRILL, EXAMPLES working. REPS deliberately thin: record and self-rate, no AI judging. |
| **Week 7** (due Dec 14) | REPS becomes properly agentic — audio evaluation via OpenRouter. That week's assignment is literally "make your application agentic somehow." |

All four modes exist from Week 3 so the router has something real to route
between. The hardest mode lands in the week designed for it.

---

## Open decisions

### 1. The chosen subject is tagged for only two modes
`docs/inherited-research/subjects.md` tags subject #3 "Agentic engineering" as
**MAP + REPS only** — no DRILL, no EXAMPLES. Subject #2 "Vibe / agentic
marketing & growth hacking" is MAP + EXAMPLES + REPS, still no DRILL.

That collides with building all four modes. Either the tagging gets revised or
the first slice demonstrates fewer modes. A revision looks defensible —
agentic engineering plainly has DRILL material (API signatures, CLI flags,
framework patterns) and EXAMPLES material (reading good agent code against
bad) — but the August tagging was a considered judgment and should be changed
deliberately, not silently.

### 2. Personal tool or multi-user product?
The old `CLAUDE.md` stated: "a personal learning system for one user, not a
general product." The residency requires user accounts and secured user data
in Weeks 3 and 5. That re-scope needs a decision.

### 3. Repo naming — the course contradicts itself
Week 1 says: one repo named `AI Development Residency`, with a folder per
week. Weeks 3–8 say: a separate repo per week
(`AI DEVELOPMENT RESIDENCY - WEEK 3 - APP`, then clone to a Week 6 repo).
These cannot both be followed. **Ask Morgan.**

### 4. Does Week 4 use this app?
Week 4's premium section reads "This week you are building the same thing as
Standard Residency students" — the O*NET career-coaching chatbot, separate
repo. It is the only week whose premium section names a specific app instead
of the student's own. **Worth confirming with Morgan**, since every other week
substitutes the specialization project.

---

## Next actions

1. **Message Morgan.** Specialization choice (overdue since Oct 19), the
   project switch, the repo-naming contradiction, and the Week 4 question.
2. **Create the public GitHub repo** under the name Morgan confirms.
3. **Finish Week 2 specs** — due **Oct 26**. See `docs/WEEK2-PLAN.md`.
4. **Swap Section 8 of the research paper** to this project. Sections 1–7
   stand as written; the specialization did not change.

## Residency reference

- Schedule, due dates, and submission mechanics: `docs/WEEK2-PLAN.md`
- Specialization: **AI Automation + Advanced agentic workflows**, combined
- Instructor: Morgan Denner — mdenner@techfleet.org
