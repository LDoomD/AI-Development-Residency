# ADHD Tools Landscape — Verified Survey

> **RESEARCH TIER — NOT MERGED INTO THE DESIGN DOC.**
> **Date:** 2026-08-08 · **5 claims discarded as false/stale/non-existent · 14 marked UNVERIFIED.**
> Prices read from vendor pages or App Store IAP listings, not secondary sources.
> Blocked by 403s (ACM, Trustpilot, G2, EIF) and a WebSearch session cap.

## Headline: **every tool surveyed is proprietary. No open source. No public API found for any.**

---

## Pricing (verified from vendor or App Store)

| Tool | Price | Free tier |
|---|---|---|
| **Goblin Tools** | Pro **$3/mo**, 1-wk trial | ✅ Web version free, no ads, no paywall |
| **Structured** | **$6.99/mo · $29.99/yr · $99.99 lifetime**, PPP-adjusted | ✅ Full planner, "no data selling" |
| **Llama Life** | **$6/mo · $39/yr** | Trial, no card |
| **Focusmate** | Plus **$8/mo annual · $12/mo** | ✅ 3 sessions/week |
| **Tiimo** | **No USD figure published.** App Store IAP: $36–54/yr · $11.99–14/mo | ✅ Limits unspecified |
| **Flow Club** | **$40/mo · $33.33/mo annual** | ❌ |
| **Sunsama** | **$25/mo · $20/mo annual ($240/yr)** | ❌ **No free tier** |
| Inflow | $47.99/mo · $199/yr | 7-day trial |

⚠️ **Discard these circulating figures — contradicted by vendors:** Tiimo "$7.99/mo, $79.99/yr"; Structured "$3.99/$27.99" and "$19.99/yr"; Dubbii "$4.99/$29.99".

**Subscription stacking:** Tiimo + Llama Life + Focusmate Plus + Sunsama + Structured ≈ **$440–460/yr** before coaching. A predictable failure mode for a population with documented difficulty cancelling recurring charges. Sunsama's no-free-tier $240–300/yr is the sharpest exposure; FLOWN's **$900 lifetime** tier sold to an impulsivity-characterized population is its own question.

---

## Mechanisms worth stealing

### 🏆 Focusmate — the best-specified commitment device found
- Sessions of **25 / 50 / 75 min**, auto-paired with a stranger; favourites bias future matching
- *"Over 99% of bookings get matched… On the rare occasion that you do not, you can book at the next time slot, 15 minutes later"* — **15-min slot grid with guaranteed re-roll**
- **Video mandatory** throughout
- Ritual: greet → **state goals aloud** → silent work → *"check in with your partner and celebrate your progress"*
- **Enforcement, verbatim:** *"If you're late or don't show, Focusmate can detect it and your timeliness score will be reduced, and your account can also be frozen."*

> **The stealable part: reputation score + account freeze — real asymmetric downside for flaking.** This is the same shape as the team-competition result (+11pp, compounding) from the adherence review, and unlike reminders, which failed in an ADHD RCT.
>
> ⚠️ **But note the tension:** it imposes a reputational penalty for exactly the symptom it treats. And mandatory always-on video with an unvetted stranger is a real safety/privacy surface, remedied only by an after-the-fact report button.

### Llama Life — the cleanest time-blindness mechanism
Per-task countdown; the list sums to a **total list time** and projects an **estimated finish time**. Adding a task immediately renders as a later end-of-day. **That projection is the actual mechanism** — it makes over-commitment visible at the moment of committing, not afterwards.

### Sunsama — estimate-vs-actual as a first-class object
Task cards carry **planned time alongside actual logged time** on the card itself, not in a report. Three-phase ritual: morning planning (timebox onto calendar, *"so you always know what fits today"*) → execution (focus mode, current task + elapsed, auto break reminders, app muting) → evening shutdown prompt with auto-captured wins.
⚠️ **The WIP limit is rhetorical only** — the site states the principle but publishes **no numeric cap**. Do not claim one.

### Tiimo — duration as vertical extent
Schedule as a visual timeline where **duration is encoded spatially**. Time-blindness handled via countdown plus **widgets and Live Activities** — next item and running timer live on the OS surface and never require re-entering the app.

### Structured — "Replan"
Calendar events and Reminders **imported into** one day timeline (not shown beside it). **"Replan"** = bulk re-flow of the day when you fall behind — architecturally the right answer to plan-breakage. ⚠️ Paywalled.

### Goblin Tools — nine single-purpose LLM wrappers
No account, no project model. Magic ToDo, Formalizer, Judge, Taskmaster, Professor, Consultant, Estimator, Compiler (braindump→actions), Chef.
⚠️ **The "spiciness slider" is NOT documented by the vendor** — secondary sources only. Do not attribute it to them.

---

## ⚠️ Evidence: zero vendors publish outcome data with n + methodology + control

| Vendor | Claim | Status |
|---|---|---|
| **Focusmate** | *"average productivity increase of 143%"* | **Internal survey, no n, no instrument, no control.** `/research` **404s**. Arithmetic also wrong — 143% increase is 2.43×. The oft-cited "Steel/Kaufman study" **appears not to exist** |
| **Shimmer** | 83% report better management; **12% BDEFS improvement**; 17% BFIS, both "within 3 months" | **No n, no control arm, no published study, no citation.** ⚠️ **Most misleading in the set precisely because it looks most scientific** — validated instrument names lending clinical veneer to uncontrolled pre/post numbers |
| **Tiimo** | *"rooted in executive functioning research"* | No citation, no study, no clinical partner |
| **Inflow** | *"research shows," "science-informed," "leading ADHD clinicians"* | Zero study names or links. A claimed 8-week RCT could **not** be verified — do not cite |
| Sunsama, Structured, Llama Life, Flow Club, Caveday, FLOWN, Dubbii | — | **Nothing at all** |
| **Goblin Tools** | — | ✅ **The honest outlier.** Discloses accuracy *"can vary,"* results are *"guesswork,"* *"we take no responsibility for the results"* |

**The category's uncited stock phrase** — *"rooted in executive functioning research" / "evidence-based approaches" / "science-informed"* — appears near-verbatim across **Tiimo, Focusmate AND Inflow.**

**One real academic source:** Alghory A, *Digital CBT Apps for ADHD: A Systematic Review of Recent Evidence*, European Psychiatry 2025, `10.1192/j.eurpsy.2025.1417`, PMC12436941. Verified. Calls apps *"promising,"* *"moderate to significant effectiveness"* — but **only six included studies, no named apps, no risk-of-bias assessment.** Conference-abstract scale. **Grade: weak.**

---

## ⚠️ The biggest find: Goblin Tools is being subscription-farmed

Two App Store clones monetize a deliberately-free ADHD tool:

- `id6739871366` (dev "Mai Tuan Viet", 4.0/25) — **$2.99/mo · $12.99/6mo · $19.99/yr.** Reviews: *"Stolen from Bram De Buyser"*; the original was free but this version *"TURNED the PRICING into a SUBSCRIPTION MODEL"*
- `id6479981873` (dev "FREE AI UTILS COMPANY LIMITED", 4.4/311) — weekly $3.99–4.99 / monthly $1.99–9.99 / annual $19.99–29.99 for renamed clones ("Task Helper," "Tone Tweaker," "Time Guesser"). Reviews report **pricing not disclosed at signup**

> **A free tool built for this population, monetized by third parties against it.**

---

## Other criticisms

**Tiimo** (4.6, ~19,000 ratings, Editors' Choice): notifications **too weak to break hyperfocus** (users request *"an alarm sound or longer vibration"*); **rigidity** — *"the whole minute to minute planning doesn't always work,"* users want durations without fixed slots; persistent bugs; no two-way calendar sync.

**Llama Life:** 4.5 stars but only **115 ratings**; Capterra 5.0 from **two** reviews. Statistically meaningless — do not cite as validation.

**Privacy:** only **Structured** made an affirmative "no data selling" statement on any page fetched. These apps ingest task-level life data **plus explicit ADHD/autism self-identification.**

---

## Not covered / unverified

No verified user-complaint corpus for **Sunsama, Structured, Focusmate, Flow Club, Caveday, FLOWN** — the "Sunsama is expensive/slow" reputation is **unverified**. Also unverified: Tiimo user counts, Caveday monthly price, Llama Life API existence, Goblin Tools open-source status (**never stated anywhere**), Mozilla Privacy Not Included findings, Inflow's Cerebral acquisition.

---

## Implications

1. **No open source anywhere in this category.** Nothing to fork; you build or you subscribe.
2. **No public APIs.** No integration path — this is a build-vs-buy decision, not a compose decision.
3. **The evidence bar is on the floor.** Publishing *anything* with an n and a control would put you ahead of every vendor here.
4. **Steal three mechanisms:** Focusmate's reputation-score commitment device, Llama Life's estimated-finish-time projection, Structured's Replan bulk re-flow.
5. **Note what the good mechanisms have in common:** they make consequences *visible and immediate* — which matches the adherence evidence (competition works, reminders don't).
