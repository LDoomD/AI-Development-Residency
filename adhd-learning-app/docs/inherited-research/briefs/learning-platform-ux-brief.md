# BRIEF — Learning platform UX/UI: what to steal for the study surface

**Requested by Orlando Castillo, repo owner, interactive Claude Code session.**
Orlando is a UX/UI designer. He has judged the current study surface — markdown in
VS Code, and the HTML artifact pages built so far — as **bad UX and bad typography, and
wrong for a neurodivergent visual learner.** He is right. This brief finds out what
good actually looks like.

## Deliverable

`specs/research/2026-08-09_learning-platform-ux.md` — this file only.

## The constraint that shapes every recommendation

The study surface is a **self-contained HTML page** (a Claude artifact): inline CSS and
JS only, **no external fonts, no CDN, no remote images, no network calls**. System
typefaces and CSS/Canvas/SVG only. Recommendations that require a webfont or an image
CDN are useless here — say so and give the achievable version instead.

It must work on an iPhone in bed and on a Mac, in light and dark.

## Research these

1. **What the best learning products actually do, interaction by interaction.**
   Duolingo, Brilliant, Khan Academy, Quizlet, Memrise, Anki, Synthesis, Sana Labs,
   MasterClass, Coursera, Speak, Kahoot, Elicit. For each: what specific UI mechanic is
   worth stealing, and is it evidenced or just popular? **Brilliant is the highest-value
   target** — interactive visual explanation of abstract material is exactly the gap.
2. **Streaks, XP, gamification — the honest verdict.** Duolingo's streak is the most
   copied mechanic in the category. **This repo's own adherence research found reminders
   FAILED in an ADHD RCT (n=109) while team competition worked (+11pp, compounding).**
   Does the evidence support streaks/XP, or are they engagement metrics dressed as
   learning? Distinguish sharply between "increases time in app" and "increases learning."
3. **Typography and legibility research** — line length, size, weight, spacing, contrast
   for cognitive load and for ADHD/dyslexic readers specifically. What does the actual
   research say versus what design blogs repeat? Check whether "dyslexia-friendly fonts"
   like OpenDyslexic have evidence — **they may not.** Report what does have evidence.
4. **Cognitive accessibility guidance** — W3C COGA task force, WCAG 2.2 cognitive
   provisions. Concrete, applicable rules, not principles.
5. **Chunking, progressive disclosure, one-idea-per-screen.** Is there evidence for
   card/step interfaces over long scrolling documents for this population?
6. **Colour as functional encoding.** This project's design doc already calls for strict
   functional colour roles held constant. What does research say about colour coding for
   comprehension and recall, and how many distinct roles before it backfires?
7. **Motion and interaction** — does interactivity aid learning, or is it decoration that
   costs attention? Cover the generative-learning and interactive-simulation evidence.
8. **Anti-patterns.** What do these platforms do that actively harms learning while
   improving retention-as-a-business-metric? Name them.

## HARD CONDITIONS

- **Verify.** Peer-reviewed sources for learning claims; fetched product pages or app
  listings for product claims. **Discard anything unverifiable rather than caveating it.**
  State the discard count. This project has already caught four fabricated citations
  from search summarisers.
- **Grade every claim:** `High — rely on as-is` / `Moderate — directional` /
  `Extrapolated — tune by feel` / `Not covered`.
- **Separate "engagement" from "learning" ruthlessly.** Most of this industry optimises
  the former and markets it as the latter.
- Respect the existing findings in `specs/research/` — do not contradict them without
  evidence, and flag it explicitly where you do.

## Most important output

End with **"The spec"** — a concrete, buildable set of rules for the study page:
type scale in actual numbers, line length, spacing, colour roles and how many, component
patterns, what goes above the fold, mobile behaviour. Something that can be implemented
directly, not design philosophy. Orlando will judge it as a designer.

## Style

Terse, tables, graded. The spec at the end is the part that matters.
