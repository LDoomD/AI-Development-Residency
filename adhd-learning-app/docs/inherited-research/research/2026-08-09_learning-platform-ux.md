# Learning Platform UX/UI — What to Steal for the Study Surface

> **RESEARCH TIER.** Requested by Orlando Castillo (UX/UI designer, repo owner) after judging
> the current study surface — markdown in VS Code, HTML artifact pages — as bad UX, bad
> typography, and wrong for a neurodivergent visual learner. This report finds what good
> actually looks like, verifies it, and ends with a buildable spec.
>
> **Date:** 2026-08-09 · **8 research areas, 8 parallel research passes, 21 sources discarded
> for failing verification** (2 typography, 1 chunking, 2 colour, 3 motion, 5 anti-patterns,
> 11 gamification — some studies double-count across areas' sub-claims, see each section).
>
> **The hard constraint that shapes every recommendation below:** the study surface is a
> self-contained HTML page (a Claude artifact) — inline CSS and JS only, **no external fonts,
> no CDN, no remote images, no network calls.** System typefaces and CSS/Canvas/SVG only. It
> must work on an iPhone in bed and on a Mac, in light and dark. Recommendations requiring a
> webfont or image CDN are flagged as not achievable here, with the achievable substitute
> given instead.
>
> **Grading key:** `High — rely on as-is` / `Moderate — directional` /
> `Extrapolated — tune by feel` / `Not covered`.

---

## 1. Learning product UI mechanics

| Product | Mechanic | Evidenced or popular-only | Source |
|---|---|---|---|
| Duolingo | Heart/life system + streak counter with loss-aversion "streak freeze" save | Popular-only | [Streak Design](https://yukaichou.com/gamification-study/master-the-art-of-streak-design-for-short-term-engagement-and-long-term-success/), [Duolingo Streak System Breakdown](https://medium.com/@salamprem49/duolingo-streak-system-detailed-breakdown-design-flow-886f591c953f) |
| Duolingo | Non-punitive instant feedback: wrong answer → gentle character reaction, not a harsh red error screen | Popular-only | [Fun in Every Frame](https://60fpsdesign.substack.com/p/fun-in-every-frame), [Duolingo shape language](https://blog.duolingo.com/shape-language-duolingos-art-style/) |
| Brilliant | Full-screen problem card with drag-and-drop / tap manipulation of a visual element, real-time feedback as you adjust it | Popular-only | [Brilliant – App Store](https://apps.apple.com/us/app/brilliant-learn-math-coding/id913335252) |
| Brilliant | State-machine-driven micro-animations (built in Rive): color-coded learning-path nodes, streak counter synced to a completion celebration | Popular-only | [How Brilliant.org motivates learners with Rive](https://rive.app/blog/how-brilliant-org-motivates-learners-with-rive-animations) |
| Brilliant | Persistent "Level Gameboard" progress tracker + in-lesson success flourishes | Popular-only | [Brilliant.org × ustwo](https://ustwo.com/work/brilliant/) |
| Khan Academy | Progressive step-reveal hints: each click reveals exactly one solution step; all hints together assemble a full worked example | **Evidenced** (worked-example effect / scaffolded hints is established cognitive-load research; KA's own blog invokes this rationale) | [Khan Academy: use of hints](https://support.khanacademy.org/hc/en-us/community/posts/115003344211-Use-of-hints) |
| Khan Academy | Mastery grid: each skill is a colored square in a unit map; hover previews, click jumps to that exercise | Popular-only | [Mastery progress visualization](https://support.khanacademy.org/hc/en-us/articles/18735142028045) |
| Quizlet | "Learn" mode cycles question format and difficulty by session history; missed terms auto-requeue | Popular-only | [A Smarter Learn Mode](https://quizlet.com/blog/new-a-smarter-learn-mode) |
| Memrise | Flashcard pairs a native-speaker video clip with a user mnemonic image | Popular-only | [Memrise Review](https://thinkbetterblog.com/reviews/memrise-review-mnemonics-and-video-for-faster-vocabulary) |
| Anki | SM-2-derived scheduler: per-card interval expands/contracts on a per-card ease factor | **Evidenced** (spaced repetition is one of the most replicated findings in memory research) | [Anki FAQs: scheduling algorithm](https://faqs.ankiweb.net/what-spaced-repetition-algorithm) |
| Khan Academy (hints) and Anki (scheduling) are the only two mechanics in this table with direct learning-science backing; everything else is popular design, not proven pedagogy. |

**Discarded:** Sana Labs' and Synthesis's "adaptive/gamified UI" claims — both returned only generic marketing language with no verifiable specific mechanic.

**Portability to a CSS/Canvas/SVG-only, no-network page:**
- **High** — Anki's interval scheduler (pure JS + localStorage state machine); Khan Academy's step-reveal hint (sequential DOM reveal).
- **Moderate** — Brilliant's drag/tap-to-manipulate diagram with live feedback (SVG/Canvas + pointer events map directly, though Brilliant's real implementation is native/WebGL); Khan Academy's color-coded mastery grid; Quizlet's re-queue-on-miss drilling.
- **Extrapolated** — Duolingo's non-punitive feedback animation and streak framing (feel can be mimicked; no spec exists to copy exactly).
- **Not covered** — Speak's syllable-level speech recognition and Memrise's native-speaker video (both need audio/ML pipelines the no-network constraint rules out); Coursera's peer-grading (needs a multi-user backend).

---

## 2. Streaks, XP, gamification — the honest verdict

| Mechanic | Effect on engagement | Effect on learning | Grade | Source |
|---|---|---|---|---|
| Gamification bundle (points+badges+levels+leaderboards) | Positive, well-replicated | Cognitive-outcome **g=0.49** (k=19, N=1,686), held up in high-rigor-only subsplit | Moderate — real, but a *bundle* effect, never isolated to streaks/XP alone | Sailer & Homner (2020), *Educational Psychology Review* 32:77–112, `10.1007/s10648-019-09498-w` |
| Gamification, competency-lens framing | Boosts autonomy/relatedness perceptions | "Minimal impact on competency" — the skill-outcome variable | Moderate — **contradicts** the row above on a near-identical intervention set | *Educational Technology Research and Development* (2024), N=2,500, `10.1007/s11423-023-10337-7` |
| Streaks specifically (loss-aversion, all-or-nothing) | Claimed large by vendor | **Not covered** — zero peer-reviewed studies isolate the streak mechanic from the rest of the app | Not covered | All streak-efficacy claims traced to Duolingo's own vendor-funded pages or unsourced blog paraphrase |
| Leaderboards / ranked points, low-trait-competitiveness users | **Negative** — low-competitiveness users are driven away | Not measured for this subgroup | Moderate (directional, not ADHD-specific) | `10.1016/j.chb.2018.09.028`-family; *Computers & Education* (2024) `S0360131524002100` |
| Extrinsic/tangible contingent rewards on intrinsic motivation | Short-term compliance up | **Undermines** free-choice intrinsic motivation for completion/performance-contingent rewards | **High** — 128 controlled experiments | Deci, Koestner & Ryan (1999), *Psychological Bulletin* 125(6), `10.1037/0033-2909.125.6.627` |
| Team competition (this project's own prior finding) | +11pp attempt rate, gap widened over time | Adherence is this project's existing learning proxy | High (already confirmed) | `specs/research/2026-08-08_spaced-repetition-tools-and-adherence.md` |

**11 sources discarded** — all vendor pages, business-school case studies, or blog posts repeating unsourced loss-aversion/streak-efficacy numbers without a checkable study behind them.

**Engagement and learning are not the same dependent variable.** The strongest peer-reviewed evidence for gamification's *learning* effect (Sailer & Homner) is a bundle effect — never isolated to a streak counter or XP bar — and sits beside a same-year meta-analysis on a near-identical intervention set finding "minimal impact on competency." Streaks, the single most-copied Duolingo mechanic, have **zero isolated peer-reviewed learning evidence**. What the literature does support is a mechanism for harm: contingent extrinsic rewards undermine intrinsic motivation (Deci/Koestner/Ryan), and leaderboards repel low-competitiveness users. A hard, resettable streak is a loss-aversion device with the exact bimodal-collapse shape this project's own adherence research (Grad et al., 634 residents) already found fails — 20% zero-cases, 27% heavy users, no exam effect.

**Recommendation: no individual streak counter, no XP bar as the primary motivational spine. Keep the team-competition mechanic already validated in this project's prior research.** If any streak-like device ships, it must decay rather than hard-reset (borrowing the FSRS "postpone, don't punish" logic already recommended in the spaced-repetition research) — never a visible zero. XP/points are defensible only as private, non-comparative progress feedback, never a leaderboard. The one gamification mechanic with a real, replicated, compounding effect in an adherence context is **team competition with de-identifying aliases (+11pp, widening gap)** — that is the mechanic to build.

---

## 3. Typography and legibility

| Variable | Recommended value/range | Grade | Source |
|---|---|---|---|
| Line length | 45–75 characters/line; ~66 cpl single-target; struggling readers trend toward 45–50 | High | Tinker & Paterson eye-movement line; *Visible Language* lit review |
| Body font size | ≥16px (1rem) base | Moderate | British Dyslexia Association Style Guide (2018) — practitioner consensus, not RCT |
| Line-height | ≥1.5× font-size (WCAG floor); 1.2–1.5× band shows fastest/most-accurate reading | High (floor) / Moderate (optimum) | WCAG 2.1 SC 1.4.12 Text Spacing; BDA Style Guide |
| Paragraph spacing | ≥2× font-size between paragraphs | High | WCAG 2.1 SC 1.4.12 |
| Letter-spacing | Normal by default; WCAG requires layout survive ≥0.12em user-applied spacing; extra-large spacing (~+0.2–0.3em) measurably raised dyslexic reading speed/accuracy | High (floor) / Moderate-High (dyslexia benefit) | WCAG 2.1 SC 1.4.12; Zorzi et al., *PNAS* 109(28), 2012 (n=94, controlled, replicated) |
| Font weight | No controlled evidence heavier weight improves legibility; avoid italics (measurably worsens reading) | Not covered (weight) / Moderate (avoid italics) | Rello & Baeza-Yates, ASSETS 2013 (n=48, eye-tracking) |
| Font family / "dyslexia fonts" | System sans-serif only (Helvetica/Arial/San Francisco); **no evidence OpenDyslexic or Dyslexie outperform them** | High (that they do NOT help) | Rello & Baeza-Yates 2013; Wery & Diliberto, *Annals of Dyslexia* 2017 (n=59 children) |
| Contrast, normal text | ≥4.5:1 | High | WCAG 2.1/2.2 SC 1.4.3 |
| Contrast, large text (≥24px, or ≥18.67px bold) | ≥3:1 | High | WCAG 2.1/2.2 SC 1.4.3 |
| Contrast, enhanced | ≥7:1 normal / ≥4.5:1 large | High | WCAG 2.1/2.2 SC 1.4.6 (AAA) |
| Pure black-on-white / white-on-black | Avoid; use off-black on off-white and softened dark-mode equivalents | Moderate | BDA Style Guide (practitioner consensus, no RCT located) |

**Verdict on "dyslexia fonts": folklore, not evidence.** The two best-designed controlled studies (Rello & Baeza-Yates 2013; Wery & Diliberto 2017) both found no reading-speed or accuracy benefit from OpenDyslexic over system sans-serifs, and subjects in the former actually preferred Helvetica/Verdana. What *does* have evidence is spacing, not letterform: Zorzi et al. (PNAS 2012, n=94) found extra-large inter-letter spacing produced a replicated reading-speed/accuracy gain in dyslexic children. **Discarded: 2** — "OpenDyslexic reduces letter confusion via weighted bottoms" (marketing claim, no supporting study found) and "colored overlays cure dyslexia-related reading difficulty" (contested, non-replicated).

**CSS numbers:** `font-size: 1rem` (16px) minimum body text, `line-height: 1.5`, `max-width: 60–66ch`, `letter-spacing: normal` with an optional user toggle up to `0.1em`, `margin-bottom: 2em` on paragraphs, `font-weight: 400` body / `600–700` headings only, contrast ≥4.5:1 (target 7:1) in both themes using off-black/off-white, never pure `#000`/`#fff`.

---

## 4. Cognitive accessibility guidance (WCAG 2.2 / W3C COGA)

| Rule/SC | Requirement | Applies how | Grade | Source |
|---|---|---|---|---|
| SC 2.2.1 Timing Adjustable (A) | Any content time limit must be off/adjustable(≥10×)/extendable, or exempt | No hard timers by default; any self-timed element (quiz countdown, auto-advance) must be pausable/extendable by the learner | High | WCAG 2.2 |
| SC 2.2.6 Timeouts (AAA) | Warn before inactivity causes data loss, unless preserved >20h | Persist progress/notes to `localStorage` so inactivity never loses state | High | WCAG 2.2 |
| SC 3.2.6 Consistent Help (A) | Repeating help mechanisms must stay in the same relative position | If a hint/help control repeats across sections, keep it in the identical spot every time | Moderate | WCAG 2.2 |
| SC 3.3.7 Redundant Entry (A) | Previously entered info must auto-populate or be selectable, not re-typed | Auto-fill/"same as before" on any repeated form field | High (if repeated-entry forms exist) | WCAG 2.2 |
| SC 3.3.8 Accessible Authentication — Minimum (AA) | No memory-only cognitive test to authenticate, unless an alternative exists | Only applies if the page gates access; if it does, allow paste/password managers | Not covered (no auth in scope) | WCAG 2.2 |
| SC 2.4.11 Focus Not Obscured — Minimum (AA) | Focused component must not be fully hidden by sticky content | Sticky nav/toolbar must never fully cover a keyboard-focused element | High | WCAG 2.2 |
| SC 2.4.13 Focus Appearance (AAA) | Focus indicator ≥2px perimeter, ≥3:1 contrast against adjacent color | Audit every `:focus` outline; do not use `outline: none` or rely on 1px default | High | WCAG 2.2 |
| COGA Pattern 4.6.1 Limit Interruptions | No distracting auto-play/pop-ups during a task; provide a disable option | No auto-playing animation or interstitials; ship a visible reduce-motion toggle | Moderate | W3C `coga-usable` |
| COGA Pattern 4.9.1 Let Users Control When Content Moves/Changes | Auto-advancing content must be pausable or off by default | Any auto-advancing flashcard/timer ships with pause/stop, not auto-run | Moderate | W3C `coga-usable` |
| COGA Pattern 4.2.4 Make Each Step Clear | Multi-step flows show completed/current/pending steps | Render an explicit "Step 2 of 4" indicator for any multi-step flow | Moderate | W3C `coga-usable` |
| COGA Pattern 4.5.5 Easy Undo for Form Errors | One-step reversal, not multi-step correction | Single-action clear/undo on any input, no manual retyping | Extrapolated | W3C `coga-usable` |
| COGA Pattern 4.7.5 Don't Rely on Memory/Calculation | Don't require holding info across steps in the learner's head | Surface running score/prior answer on-screen rather than requiring recall | Extrapolated | W3C `coga-usable` |

---

## 5. Chunking, progressive disclosure, one-idea-per-screen

| Principle | Effect | Grade | Source |
|---|---|---|---|
| Segmenting principle — break lessons into learner-paced segments | Small-to-medium effect; Hedges' g ≈ 0.32–0.36 pooled; one study found d=0.34 transfer, d=0.43 perceived-difficulty | High | Rey et al. 2019, *Educational Psychology Review* (56 studies, 88 comparisons) |
| Working-memory chunk limit | ~7±2 items (Miller 1956), revised to ~4 chunks under rigorous conditions (Cowan 2001) | High | Miller 1956; Cowan 2001 |
| Cognitive Load Theory — minimize extraneous load | Framework-level, not one effect size; consistently supported across derived techniques | High (mechanism) / Moderate (derived rules) | Sweller 1988, 2011 |
| Paginated vs. continuous scroll | Paginated reading shows better integrated comprehension, more strategic backtracking, especially for younger/less-skilled readers | Moderate — directional | Krenca et al. 2024, *Journal of Research in Reading*; ISLS scrolling-disruption work |
| ADHD + display medium + spacing → comprehension | Significant ADHD-vs-non-ADHD gap and a 3-way interaction (presentation × spacing × attention); no extractable effect size | Moderate — directional | Solan et al., *Research in Developmental Disabilities* (PubMed 23023301) |
| Progressive disclosure (HCI) | 30-year design heuristic from usability practice; no controlled effect size located | Extrapolated | Nielsen Norman Group |
| Card/step UI vs. scrolling, ADHD-specific | No direct study found | Not covered | — |

**Recommendation: card/step interface, not a scrolling document.** No ADHD-specific card-vs-scroll study exists, so this chains three individually-verified findings: working memory holds ~4 chunks (Cowan 2001); the segmenting principle has real replicated backing for learner-paced segments over one continuous block (Rey et al. 2019); and general paging-vs-scroll research favors paging for comprehension and removes the "where was I" re-orientation cost a scroll imposes on every attention lapse — a cost the Solan et al. ADHD-attention interaction suggests matters more for this population, not less.

**Content per card:** one idea/concept, sized to ~3–4 new chunks (Cowan's ceiling) — roughly 50–150 words or one diagram + 1–2 sentences, then an explicit "next" action. The word-count band is extrapolated (the segmenting literature segments by idea boundary, not character count); treat it as a starting point to tune by testing.

---

## 6. Colour as functional encoding

| Claim | Rule | Grade | Source |
|---|---|---|---|
| Colour is pre-attentive (parallel, pre-conscious visual search) | Use colour for a small set of at-a-glance category distinctions, not text-level detail | High | Treisman & Gelade (1980), Feature Integration Theory |
| Reliable categorical-colour identification ceiling | ~6–12 distinct categorical colours max for an accurate coding scheme | High | Colin Ware, *Information Visualization*; corroborated in Munzner, *Visualization Analysis and Design* |
| Basic colour categories are few (~11, only ~4 primary chromatic anchors) | Map roles to maximally-separated basic hues, not shades of one category | Moderate | Healey & Enns visualization-perception literature |
| Colour-vision deficiency is common | Every functional colour role needs a redundant non-colour cue | High | NEI: ~8% Northern-European-ancestry men / <1% women red-green colourblind (global pooled ~4.5%/0.4%) |
| Colour must not be the sole conveyor of information | Formal rule | High | WCAG SC 1.4.1 Use of Color (A) |
| Colour-coding aids recall, but benefit shrinks/reverses as colour count grows or mapping is unstable | Keep the set small and fixed | Moderate | *Heliyon* 2022; PMC "guidance reversal effect" |
| Fixed colour-to-meaning mapping beats decorative/ad hoc colour | Lock roles to fixed hues; never reuse those hues decoratively | Moderate (inferred from consistency + visual-search literature; no single study isolates this exact comparison) | *Frontiers in Psychology* (2022) |

**Discarded: 2** — an unverifiable "31% better on detail tasks" red-vs-blue figure and an unsourced "11% performance increase" colour-coding claim, both traced to blog summaries with no checkable primary study.

**Bottom line:** 3 functional colour roles (Execution / Logic gate / Exception, per `specs/adhd-learning-system-design.md`) is well inside the 6–12 ceiling — no change needed on capacity grounds. **Upgrade that design doc's grade from "Extrapolated — tune by feel" to "Moderate — directional"**: the colour-count limit and colourblind redundant-encoding requirement are High-confidence; the specific claim that constant roles beat ad hoc colour has strong supporting theory but no single head-to-head study, so it stays short of High. Every colour-coded role must pair with a second cue (icon/shape/label) at point of use.

---

## 7. Motion and interaction

| Claim | Effect | Grade | Source |
|---|---|---|---|
| Generative learning activities (interactivity, self-explanation, manipulation) | Largest transfer effects among Mayer's multimedia principles | High | Mayer multimedia-principles meta-analysis (2025), *Educational Research Review* |
| Removing seductive details (decorative/tangential motion, images, sound) | Retention d≈0.27, transfer d≈0.65 improvement when removed | High | Rey, G.D. (2012), *Educational Research Review* 7(3) |
| Seductive-detail effect replicates across text/image/animation; worst for low-prior-knowledge learners | Hurts | High | Sundararajan & Adesope (2020), *Educational Psychology Review* |
| Self-directed navigation of interactive simulations vs. passive/instructor-controlled | Helps engagement and self-efficacy | Moderate | Sitzmann (2011), *Personnel Psychology*; Vogel et al. (2006) |
| PhET-style light guidance (vs. none or heavy) | Most exploration and content attention | Moderate | Podolefsky, Perkins & Adams (phet.colorado.edu) |
| Enhanced interactive video, paused vs. concurrent with motion/narration | g≈0.52 if paused; split-attention penalty if simultaneous | Moderate | 2022 meta-analysis of interactive video features |
| Autoplay/scroll-triggered motion and vestibular sensitivity | Nausea/vertigo/disorientation risk | High | WCAG 2.2 SC 2.3.3 Animation from Interactions |
| `prefers-reduced-motion` respect | Standard mitigation | High | WCAG 2.3.3 techniques; CSS Media Queries spec |
| ADHD attention re-engagement after a distractor | Measurably slower/disrupted | Moderate | Eye-tracking VR ADHD-attention study, PMC |

**Discarded: 3** — a gamified-app "sustained attention" RCT claim that conflates reward mechanics with motion; two non-peer-reviewed arXiv preprints on ADHD video interfaces.

**Guidance:** Build interactivity that is **learner-controlled and tied to content manipulation** (sliders, drag-to-reorder, reveal-next), **learner-paced not autoplaying**, and **minimally but present guided**. Avoid decorative/autoplay animation entirely (d≈0.27–0.65 documented retention/transfer cost — the single clearest "cut this" finding here) and motion simultaneous with reading. Wrap all non-essential animation in `@media (prefers-reduced-motion: reduce)`; even essential animation (e.g. a simulation showing change over time) needs a manual step/pause control.

---

## 8. Anti-patterns

| Anti-pattern | Platform(s) | Business metric served | Learning harm | Grade |
|---|---|---|---|---|
| Streak loss-aversion + guilt notifications | Duolingo | DAU, reopen rate | Shifts goal from comprehension to streak-preservation; produces rushed, shallow review | High |
| Consumable hearts/lives locking content | Duolingo | Ad revenue, subscription upsell | Punishes error-making and correction — exactly the retrieval practice that produces learning gains | High |
| Points/energy that reward time-on-task, gameable | Khan Academy (energy points; company removed them from teacher dashboards for this reason) | Session length, reported activity | Decouples reward from competence — Goodhart's Law; masks unlearned material as "progress" | High |
| Reopen-maximizing notification ML ("bandit algorithm") | Duolingo | Reopens | Trains response to social triggers, not the actual forgetting curve — degrades review-timing efficiency | Moderate |
| Real-time competitive leaderboards with time-pressure scoring | Kahoot! | Engagement, "fun" | Rewards speed over accuracy; demotivates the majority, not just the minority it excites | Moderate |
| Fake/rolling countdown timers on pricing | Udemy, Coursera | Conversion | Front-loads decision pressure before fit is evaluated — correlates with early-dropout pattern | Moderate |
| Variable-ratio surprise rewards | Duolingo and category-wide | Compulsive reopens | Slot-machine reinforcement schedule — optimizes checking behavior, not learning; extra-relevant for ADHD reward sensitivity | Moderate |
| Massed one-off quiz loops presented as sufficient practice | Kahoot, quiz-style drills generally | Session-completion counts | Massed practice: good immediate score, ~14% worse delayed retention vs. spaced practice's ~18% better | High (mechanism) / Moderate (platform mapping) |
| Confirmshaming on cancel/inactivity | Duolingo | Churn reduction | Trains guilt-driven app-opening, orthogonal to intrinsic motivation | Extrapolated |
| Enrollment/start metrics masking low completion | Coursera, MasterClass, MOOCs broadly | Marketing metrics | Structural evidence the category optimizes signups over mastery (completion as low as 3%) | High (data) / Moderate (intent) |

**Discarded: 5** — no verifiable anti-pattern documentation found for Brilliant, Memrise, Anki, Synthesis, Sana Labs, Speak, or Elicit individually; excluded rather than caveated. (Anki, notably, appears to be the category's positive counter-example — open-source, no engagement-optimization business model.)

**Avoid list for this page:** no streak counters or loss-triggered guilt copy · no consumable lives/payment gates on wrong answers · no points/XP rewarding time-on-page over correct spaced retrieval · no reopen-optimized notifications · no leaderboards or speed-scoring (single ADHD user, not a classroom) · no fake urgency/countdowns · no single-session "quiz and done" presented as sufficient · no confirmshaming · no variable-ratio surprise rewards — deterministic, transparent feedback only.

---

## The spec

Buildable rules for the study page. Numbers, not philosophy.

### Layout & structure
- **Card/step interface, not a scrolling document.** One idea per card: one term, one worked example, or one diagram + 1–2 sentences (~50–150 words). Explicit forward control (`Next`), no auto-advance.
- **Above the fold on mobile (iPhone, ~390×844 CSS px):** the current card's content plus its primary action button. No secondary chrome (settings, history) competing for that space.
- **Step indicator on any multi-step flow:** literal "Step 2 of 4" or equivalent — never leave step position implicit (WCAG COGA 4.2.4).
- **Persist all state to `localStorage`** on every card transition — no reliance on session memory; a reload must resume where the learner left off (WCAG SC 2.2.6).

### Type
- Body: `font-size: 1rem` (16px) minimum, system stack (`-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif` — no webfonts).
- `line-height: 1.5`.
- `max-width: 60ch` per text block (66ch upper bound).
- `letter-spacing: normal` by default; ship a user toggle up to `+0.05–0.1em` (Zorzi et al. spacing effect).
- Paragraph spacing: `margin-bottom: 2em` relative to font-size.
- Weight: `400` body, `600–700` headings only — never as a legibility crutch, never italics for body text.
- No "dyslexia-friendly" font substitution — the evidence doesn't support it; spend the budget on spacing/contrast instead.

### Colour
- **3 functional roles, fixed for the life of the page** (Execution / Logic gate / Exception, per the existing design doc — confirmed within the 6–12 perceptual ceiling).
- Every role gets a **redundant non-colour cue** — icon, shape, or text label — never colour alone (WCAG SC 1.4.1; ~1 in 12 men have colour-vision deficiency).
- Contrast: **≥4.5:1** body text, **≥3:1** large text (≥24px or ≥18.67px bold), both light and dark themes. Target 7:1 where free.
- No pure `#000`/`#fff` — use off-black on off-white (e.g. `#1a1a1a` on `#f5f5f0`) and an equivalent softened pair for dark mode.

### Motion
- No autoplay, no decorative animation, no ambient looping graphics.
- Every animation must carry information about the content (a simulation, a value changing) or it gets cut.
- All non-essential motion wrapped in `@media (prefers-reduced-motion: reduce)`.
- Any animation tied to content (e.g. a diagram evolving) ships with a manual pause/step control — never purely automatic.
- Interaction never overlaps a competing motion/narration stream (split-attention penalty).

### Interactivity
- Prioritize **learner-controlled, content-linked manipulation**: drag/tap a variable in a diagram and see dependent values update live (SVG/Canvas + pointer events — this is the CSS/Canvas/SVG-only translation of Brilliant's mechanic).
- Progressive step-reveal for hints/worked examples (Khan Academy pattern) — one step per click, not the full answer at once.
- Light, present guidance beats none or heavy hand-holding.

### Feedback & progress
- **No streaks, no XP bar, no leaderboard.** If any streak-like device ships, it decays rather than hard-resets (never a visible zero).
- Points/progress, if shown, are **private and non-comparative** — a personal record, not a rank.
- The one gamification mechanic with real evidence in this project's own adherence research: **team competition with de-identifying aliases** (+11pp, compounding). Build this, not a streak.
- Wrong answers are the least-punished, most-informative moment on the page — no lockouts, no lives, no timers on correction.

### Accessibility floor (non-negotiable, WCAG 2.2)
- No hard time limits without pause/extend/off (SC 2.2.1).
- Focus indicator ≥2px perimeter, ≥3:1 contrast; never `outline: none` (SC 2.4.13).
- Sticky elements never fully obscure a focused control (SC 2.4.11).
- Any repeated form field auto-fills or offers "same as before" — never re-typed (SC 3.3.7).

### What's still open (Not covered / Extrapolated — tune by feel)
- Exact word-count-per-card band (extrapolated from segmenting-principle idea-boundaries, not a measured number).
- Card/step vs. scroll specifically in an ADHD population (no direct study exists — recommendation is chained from adjacent evidence).
- Whether a decaying (non-reset) streak actually outperforms no-streak-at-all for this population — no isolated study exists either way; build it privately and watch adherence data, per this project's existing measurement approach.
