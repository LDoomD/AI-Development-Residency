# Ideas — parked, not planned

Things worth building later. Nothing here is committed to or scheduled.

---

## Product visualizer / menu app

**Date raised:** 2026-08-08
**Status:** idea only — no design, no estimate, not started

A desktop app that visually presents the F&I products. Built with vibe coding + ruflo,
designed with his own UX/UI skills.

### Why this one is worth keeping

**It builds three subjects at once.** Per `specs/subjects.md`, this is REPS for
vibe coding (#19), UX/UI design (#20) and agentic engineering (#3) — three of the
subjects where the research says reps in the real task are the only thing that
transfers. Building it *is* studying it, which is rare and worth exploiting.

**It shares a data model with the study material.** The products, what each one covers,
and which bucket it sits in are the same facts whether they are being studied or being
rendered on screen. Define that product data once — as structured data, not prose — and
it feeds both the learning files and the app. That is the actual architectural insight
here, and it is worth designing for even before the app exists.

### The question that decides what this can be

**Can he use his own tool in the box with real customers, or is the menu dictated by the
store?** Dealerships typically run menu presentation through their DMS or a specific
menu vendor, and menu presentation is a compliance surface — identical presentation to
every customer is a legal defense against discrimination claims, not just a sales
process. **UNVERIFIED — needs checking against how his specific store operates and what
its compliance policy requires.** Do not assume.

Two versions follow from the answer:

| Version | Constraint | Verdict |
|---|---|---|
| **Practice tool — for himself** | None. No customer, no compliance surface, no approval needed. | Safe to build any time |
| **Live tool — used with customers** | Store policy, DMS integration, compliance sign-off, possibly state disclosure requirements | Needs real answers before a line of code |

**The practice-tool version is the one to build first regardless.** It has no blockers,
it directly rehearses the menu presentation he needs to be fluent in, and if the live
version ever becomes viable the work carries over.

### Prerequisites

- The three-bucket product grouping is currently **under correction** (see the banner in
  `learning/f-and-i-sales/00-map-the-deal-and-the-products.md`). Don't hard-code a
  product taxonomy that's still wrong.
- He should have run real sessions first. Building a tool to rehearse a presentation he
  has not yet given would be building blind.
