# ADHD Learning App

A learning system for neurodivergent adults, built as a hosted web application.

Built as the Premium specialization project for the **Tech Fleet AI
Development Residency**, Fall/Winter 2026.

> **Start with [`STATUS.md`](./STATUS.md).** It records where the project
> stands, the open decisions, and how it came to replace an earlier project.

---

## What it does

Most study tools apply one method to everything. This one routes by material
type, because the same subject usually has a part you must *understand*, a
part you must *recall instantly*, a part your eye or ear must learn to
*judge*, and a part your hands or mouth must actually *do*. Treating those
four the same is what makes studying feel like it isn't working.

**The four modes:**

| Mode | What it's for |
|---|---|
| **MAP** | Understand how the pieces fit. Build a diagram, then explain it back. |
| **DRILL** | Recall exact things fast. One topic at a time, spaced over days. |
| **EXAMPLES** | Train the eye or ear. Many examples, deliberately shuffled. |
| **REPS** | Your body or mouth doing the real thing. No diagram substitutes. |

**Three layers underneath:**

1. **Universal** — retrieval practice and distributed practice, the only two
   techniques rated HIGH for cross-material generalization.
2. **ADHD supports** — externalized state, exactly one `current` lesson,
   effort self-rating, and an escape hatch.
3. **Subject-type router** — picks the mode from the material type.

**Two rules the system never breaks:**

- **The floor** — an effort self-rating of 7–9 means reduce scope and add
  scaffolding. Never press on.
- **The escape hatch** — on a failed gate, decompose, reframe, or park. Never
  repeat the same thing unchanged. Three failures in a row auto-park it.

Those two are also the project's clearest examples of guardrails on an
automated system, which is why they matter to the specialization behind it.

## Evidence base

The design reconciles commercial "build your own AI tutor" advice against
peer-reviewed research on adult ADHD working memory. Around 222,000 words of
research sit in [`docs/inherited-research/`](./docs/inherited-research/),
carried over from the predecessor project, including effect sizes per claim,
an adversarial review, and a record of claims that were tested and **killed**.

Full rationale with per-claim confidence ratings:
[`docs/inherited-research/adhd-learning-system-design.md`](./docs/inherited-research/adhd-learning-system-design.md)
Settled decisions: [`docs/inherited-research/DECISIONS.md`](./docs/inherited-research/DECISIONS.md)

## Stack

Set by the residency, not chosen here: **Next.js on Vercel**, **Supabase**
(database, auth, row-level security), **Material UI**, **GitHub** with CI/CD
gates, **Cloudflare**, **OpenRouter** for model routing.

## Status

Week 2 of the residency. Specification stage — **no application code yet.**

The first slice targets automation and agentics as its subject domain, with
all four modes present and REPS deliberately thin until Week 7.

## Repository layout

```
.
├── STATUS.md                  # Current state — read first
├── CLAUDE.md                  # Working rules for AI assistance
├── docs/
│   ├── WEEK2-PLAN.md          # Residency schedule and deliverables
│   └── inherited-research/    # ~222k words, Aug 2026 — read before researching
└── Week 2 Coding Challenge/   # Weekly submission folder (course convention)
```
