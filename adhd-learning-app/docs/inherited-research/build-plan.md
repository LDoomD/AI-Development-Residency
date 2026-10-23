# Build Plan

**Status:** research complete · stack decided · three decisions pending sign-off
**Date:** 2026-08-08
**Companion artifact:** https://claude.ai/code/artifact/4ee2fa03-1fee-468b-a73b-81ae10918e8d

---

## Stack decision — Obsidian (content + canvas) + Anki (review)

Both free candidates store plain Markdown on disk, so an agent writes to the folder
with no API and no lock-in. That part is a tie. The decision turns on the rest.

| Factor | Obsidian | Logseq | Call |
|---|---|---|---|
| Agent write path | plain `.md` in vault | plain `.md`/Org | tie |
| Cost | free core, no gating | free, no gating | tie |
| Open source | **proprietary core** | **AGPL-3.0, forkable** | Logseq |
| Agent-writable canvas | **JSON Canvas — open MIT spec, app-independent** | no equivalent | **Obsidian** |
| Native SRS | none | `#card` in-app | moot — see below |
| Ecosystem maturity | larger | active (last push 2026-08-08) but smaller | Obsidian |

**Why Obsidian despite losing on open source.** Loop phases 1 and 5 are both canvas
operations — build the spatial schema, redraw it from memory. JSON Canvas is the only
open, versioned, app-independent format in the survey that an agent can write without
touching a UI. Logseq's native SRS would be a real advantage, but
`2026-08-08_knowledge-management-tools.md` already concluded Anki's SQLite/`.apkg` is
the cleanest programmatic target for the review queue regardless of the notes app in
front of it — which neutralizes Logseq's one exclusive win.

**Trade-off, stated plainly.** We give up AGPL forkability. Because notes are plain
Markdown and canvases are an open MIT spec, exit cost is near zero — if Obsidian turns
hostile the files are already ours in formats other tools read. That is what makes a
proprietary core acceptable here and not elsewhere.

**Verified before deciding:** Logseq is not stalled — repo pushed 2026-08-08, 44.4k
stars, not archived. The rejection is on fit, not on project health.

---

## The reframe

Not "one visual-spatial method for any subject." That premise does not survive the
research. Instead three layers:

1. **Universal layer** — retrieval practice + distributed practice. The only two
   techniques rated HIGH for cross-material generalization (Dunlosky et al. 2013).
2. **ADHD supports** — externalize state, tablet/laptop over handwriting, commitment
   device over reminders, and a floor under every adaptive rule.
3. **Subject-type router** — representation chosen by material type, because
   interleaving is +0.67 for paintings and −0.39 for vocabulary. One global setting
   would actively damage half of what the system is pointed at.

## The integration gate

Drawing without integration scores **g = −0.15** — worse than no activity. With a step
forcing verbal-visual reconciliation, **g = +0.35**. The loop therefore does not advance
out of phase 1 until the schema has been explained back in prose. The active ingredient
was never the picture.

## The floor (non-negotiable)

CSAL AutoTutor, n=252: *"Gains in comprehension scores were highest for conscientious
readers, lowest for struggling readers."* Adaptivity without a floor amplifies the gap.
Effort reading 7–9 on the Paas scale reduces scope and adds scaffold; it never presses on.

The Paas 9-point mental-effort scale replaces the 40–60% load band, which was never
measurable during a session.

---

## Decisions pending sign-off

1. **Rewrite/delete the four falsified claims** — drop `d = 0.88` (cite `g = 0.65`),
   swap the load band for Paas, relabel the 15-minute sprint a default rather than a
   finding, delete "repeated failure is harmful" (it contradicts the prediction-error
   mechanism the same doc depends on).
2. **Fix the scope line** — line 4 still reads "AI engineering + UX design,
   continuous-learning domains." Should be the general scope; the router carries the
   specificity instead.
3. **Adopt the reframe** — restructure the design doc around the three layers above
   rather than around the five phases alone.

---

## Build order (after sign-off)

1. Amend the design doc per decisions 1–3. One commit, no new research.
2. Stand up the Obsidian vault; commit the folder convention into `specs/`.
3. **Examiner first** — the mastery gate. Only piece rated High, and it works before any
   visual layer exists.
4. `.apkg` generation, so passed material lands in a real review queue.
5. Canvas layer + integration gate. Most likely to need iteration; does nothing without
   the gate.
6. Router — **in progress**, `src/router/route_lesson.py`. See `DECISIONS.md` §10 for
   current state (MAP/DRILL wired, EXAMPLES/REPS not built).

**Router trigger — decided 2026-08-11:** manual `modes` tag in lesson frontmatter, using
the existing MAP/DRILL/EXAMPLES/REPS taxonomy from `subjects.md` (multi-value — most
subjects need 2+ modes at once), not a new vocabulary, not inferred from folder, and not
asked at creation time. See `DECISIONS.md` §10a for the why.

---

## Caveat to carry into the build

No controlled study of any notes/PKM tool improving learning outcomes exists — searched
two ways, zero results. Nothing built on Obsidian, Logseq or Anki inherits credibility
from that choice. Any evidence this system has will come from its own design.

---

## Visual + verbal: both, together (decided by Orlando, 2026-08-08)

Both channels stay. This is not a compromise — it is the best-evidenced setting.
Across Mayer's multimedia corpus (Cromley & Chen 2025, 591 effects), the strongest and
most consistent result is **text + static diagrams together**, not either alone.

The narrow correction that still stands: the original doc said to *replace* verbal
assets with visual ones because the verbal channel is the specific ADHD bottleneck.
That premise failed — visuospatial WM deficit d ≈ 0.49 vs verbal d ≈ 0.55, both impaired
similarly. "Replace" is what the evidence rules out. "Both" is what it endorses.

Supporting signal, and the most favourable one in the whole corpus for this design:
Nesbit & Adesope (2006) Table 7 — studying concept maps helped **low verbal ability**
learners (**d = +0.436**) while high-verbal learners gained nothing (d = −0.327, n.s.).
This is an **ability moderator, not a learning style**, which is what keeps it out of
learning-styles pseudoscience. Grade: **Moderate — directional** (k = 2 in that cell;
do not build load-bearing structure on it).

Unchanged: the integration gate stays. Drawing without verbal reconciliation is
g = −0.15; with it, g = +0.35. Both channels, reconciled against each other, is
precisely what the gate implements.

## NotebookLM: retained as a manual surface, not as engine

**Verified 2026-08-08:** Google's official NotebookLM FAQ documents **no public
developer API** — no programmatic notebook creation, source addition, or content
retrieval, no third-party integration surface. Grade: **High — rely on as-is** for the
absence of documented API; the support page directs API questions to a support email.

**Therefore:**

- **NOT the engine.** Building on it would require browser automation against Orlando's
  Google account — fragile, and an account-risk surface. The original design doc's DROP
  verdict stands, but for the *technical* reason, not the original one.
- **The original reason for dropping it was wrong.** The doc demoted audio deep-dives
  because they "load the bottlenecked verbal channel." That premise is falsified (see
  above). Audio overviews are a legitimate channel, not a downgrade.
- **RETAINED as a manual study surface.** Everything this system writes is plain
  Markdown. Drag it into NotebookLM, get an audio overview, listen while driving. The
  integration is file-level — no API, nothing to break, no account risk.

This is the second payoff from choosing plain-Markdown storage: Obsidian reads it and
NotebookLM ingests it, with no glue code in between.
