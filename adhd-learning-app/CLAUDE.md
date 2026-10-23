# CLAUDE.md — ADHD Learning App

## Read the inherited research before researching anything

This project carries ~222,000 words of research already done in August 2026.
**Before recommending, building, or researching any tool, mechanism, cost, or
approach — grep the inherited research first.**

```
grep -rni "<topic keywords>" docs/inherited-research/
```

Run that, or an equivalent targeted search, as the **first step** on any
topic — before `WebFetch`, `WebSearch`, or a research subagent. If it comes
back empty or thin, external research is justified. If it comes back with
something, **that is the answer.** Do not re-derive it externally, and do not
invent new vocabulary when the project already has some.

**Why this rule exists:** it was carried over from the predecessor project,
where this exact failure — answering from general knowledge or fresh web
research instead of checking the project's own settled specs — happened four
times in a single session on 2026-08-11. The research is cited, adversarially
reviewed, and in places records claims that were tested and *killed*. Ignoring
it risks reintroducing a falsified claim.

Start with:
- `docs/inherited-research/DECISIONS.md` — single source of truth, 12 sections
- `docs/inherited-research/subjects.md` — the MAP/DRILL/EXAMPLES/REPS taxonomy
- `docs/inherited-research/technique-library.md`
- `docs/inherited-research/adhd-learning-system-design.md` — design doc with
  evidence base and per-claim confidence ratings
- `docs/inherited-research/research/` — ~50 research documents

## What this project is

The Premium specialization project for the Tech Fleet AI Development Residency.
A learning system for neurodivergent adults, built as a hosted web app.
Read `STATUS.md` before anything else — it records current state, the open
decisions, and why this project replaced `growth-ads-system`.

**First subject: automation and agentics.** Not Spanish, not F&I.

## Inherited decisions vs. this build — important distinction

The research transfers. **The old stack does not.**

The predecessor was a local toolchain: Obsidian for content, Anki for review
scheduling, NotebookLM for source Q&A, run from a command line. The residency
requires a hosted three-tier web app. So:

| Inherited | Status here |
|---|---|
| Learning science, effect sizes, killed claims | **Carries over fully** |
| Three-layer architecture (universal / ADHD supports / router) | **Carries over fully** |
| MAP / DRILL / EXAMPLES / REPS taxonomy | **Carries over fully** |
| The floor, the escape hatch, the integration gate | **Carries over fully** |
| Obsidian + JSON Canvas for content | **Replaced** — web app |
| Anki + AnkiConnect for review queue | **Replaced** — but FSRS scheduling logic is still the right algorithm |
| NotebookLM as a manual surface | **Out of scope** for the residency build |
| `/specs` `/src` `/system` folder convention | **Replaced** — see layout below |

When the inherited research says "Obsidian" or "Anki", read it as a statement
about the *mechanism* (plain-text content; spaced-repetition scheduling), not
as a tool mandate for this build.

## Stack — set by the course, not open for debate

The residency mandates these. Do not propose alternatives.

- **Vercel** — hosting
- **Supabase** — database, auth, row-level security
- **Material UI** — component library
- **GitHub** — repo, with CI/CD gates from Week 6
- **Cloudflare** — network security, from Week 8
- **OpenRouter** — model routing, from Week 7
- **Claude Code** — development

## Course constraints that affect how you work

- **Never draft the "What I Did" or "What I Learned" sections** of any weekly
  submission. The instructor states: *"DO NOT use AI for this! I will check!"*
  Supply a factual list of actions taken as raw material if asked; the writing
  must be the user's own.
- Weekly submissions need a merged pull request, not a direct commit to main.
- Every week also needs product requirements written in Notion before code.

## Writing style

Plain English, eighth-grade reading level, in **every** artifact — including
academic and graded ones. Short sentences, common words, define a term the
first time it appears. Lead with the conclusion. Do not dumb down the
substance: keep the numbers, the caveats, and the uncertainty, just say them
plainly.

Every factual claim needs a working source link. An unsourceable claim gets
deleted, not estimated. If a source cannot be verified, label it unverified
rather than implying it was checked.
