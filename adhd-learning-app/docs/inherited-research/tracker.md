# Learning Tracker

Single source of truth. **Exactly one row is `current`.** That rule does the most work in this system — it removes "what should I study today" entirely.

## Field reference

| Field | Values | Purpose |
|---|---|---|
| **Status** | `current` · `queued` · `parked` · `done` | Only one `current` at any time |
| **Effort** | 1–9, self-rated once at the end of a session | 1–3 = too easy, widen scope. 4–6 = target. **7–9 = shrink to a smaller chunk and add scaffolding — never push through.** Replaces the old 40–60% load band, which was never measurable during a session |
| **Strength** | `solid` · `shaky` · `gone` | Set at the gate. Drives the review queue |
| **Lapses** | integer | Failed gates on this lesson. **3 → auto-park** |
| **Last retrieved** | date | When you last actually recalled it, not when you read it |

## Status rules

| Transition | Trigger |
|---|---|
| `queued` → `current` | Previous lesson passes its gate |
| `current` → `done` | Gate passed — set Strength, stamp Last retrieved |
| `current` → `parked` | Escape hatch fired (decompose / reframe / park), or 3 lapses |
| `parked` → `queued` | Blocking prerequisite resolved |
| `done` → `queued` | Review queue surfaces it *(judgment call — not research-backed)* |

**Never** `current` → `current` unchanged. A failed gate must change something: decompose the concept, reframe the format, or park it and route around. The system must never be able to stall.

---

## Lessons

**Reordered 2026-08-09.** Presentation moved ahead of compliance: the first thing the new
job puts Orlando on is presenting, so that's what gets learned first. Law is not dropped —
it's queued behind the thing he needs on day one.

| Topic | Lesson | Status | Effort | Strength | Lapses | Last retrieved |
|---|---|---|---|---|---|---|
| F&I presentation | Session 1 — the menu: what's on it and why it's ordered that way | `current` | – | – | 0 | – |
| F&I presentation | Session 2 — delivering it without sounding like a salesman | `queued` | – | – | 0 | – |
| F&I sales | Session 3 — products and the three buckets | `queued` | – | – | 0 | – |
| F&I sales | Session 4 — the three federal crimes and the one test | `queued` | – | – | 0 | – |

---

## Gate rubric

The examiner passes you only if **all four** hold. Written down because LLMs grade leniently by default.

| # | Criterion |
|---|---|
| 1 | Explained the structure without reading from notes |
| 2 | Articulated *why* it's built that way, not just what it does |
| 3 | Predicted what breaks when a named component fails |
| 4 | Redrew or restated the model from memory |

**The gate is not optional and not politeness.** Research in `specs/research/2026-08-08_visual-spatial-encoding.md`
found that studying a diagram *without* being made to reconcile it verbally performs
**worse than doing nothing at all** (g = −0.15); with the reconciliation step it turns
positive (g = +0.35). Criterion 1 is that step. Skipping it doesn't save time, it
removes the effect.

Fail any → escape hatch, log a lapse. Do not repeat the lesson unchanged.
