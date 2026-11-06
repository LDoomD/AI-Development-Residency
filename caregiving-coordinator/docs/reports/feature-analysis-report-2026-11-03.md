# REPORT: Feature comparison analysis (2026-11-03)

## How to use this report with Claude
Paste this whole report into a chat, or point Claude at `docs/reports/feature-analysis-report-2026-11-03.md` in the caregiving-coordinator folder. The full working file is `docs/feature-analysis.md` (steps 1 to 4, with every quote and source path). On the Figma board, the table is the section "FEATURE COMPARISON ANALYSIS 2 — CAREGIVING" (table node 2436:9445, gaps box 2453:9806); the blank template was left unchanged. Discovery rule: nothing is chosen yet, and the OUR COMPANY row stays empty until the user decides the problems (it then holds "planned" guesses, not "yes").

## 1. What we did (the four board steps)
1. Picked competitors: the 8 businesses from the competitor analysis, 7 direct and 1 indirect. Group texts and paper notebooks are not businesses, so they appear as "what families use instead".
2. Listed their features in each company's own words, from pages saved under `docs/sources/competitors/`.
3. Compared them side by side in 8 feature columns grouped by caregiver need. Each box shows whether the company offers the feature, how well it works according to caregivers (with real counts), and the top problems.
4. Described the gaps: features caregivers need that no company offers well.

## 2. The competitors
- Caring Village: family care-coordination app. Free plan, Circle $14.99/month.
- CaringBridge: family updates site. Free, donor-supported nonprofit.
- Lotsa Helping Hands: care calendar for helpers. Free.
- Everplans: digital vault for documents and accounts. Free base, Premium $99.99/year.
- Epic MyChart: patient portal with proxy access for family.
- Lively: medical alert, senior phones, family app. Device plus monthly plan.
- Medical Guardian: medical alert. "About $1 a day".
- Medisafe (indirect): medication reminder app with a "Medfriend" family view. Free plus a paid plan.

## 3. The 8 features (grouped by need)
Family coordination: 1 shared calendar and task sign-up · 2 one update reaches everyone · 3 relatives join with their own access. Medications: 4 medication reminders the family can see. Records and documents: 5 store and share important documents · 6 see medical records and test results. Safety: 7 emergency help button and fall alerts. Caregiver support: 8 support for the caregiver.

## 4. How a box is rated
- Evidence: 439 caregiving-only app reviews, plus Google Play reviews and forum posts added 2026-11-03, plus 37 Reddit posts that name a company.
- 🟢 Mostly works = at least 2 of 3 sources say it worked. 🔴 Mostly problems = at least 2 of 3 describe a problem. 🟠 Mixed = in between. Too few = fewer than 5 sources.
- "No one mentions it" = the company offers it, but no review or post talks about it. "Not found on their site" = we couldn't find the feature on the company's pages.
- Re-run the counts: `python3 docs/sources/app-reviews/analysis/feature_ratings.py`

## 5. Main results (boxes with enough evidence)
- Work well: Caring Village calendar (14 of 15) and medications (4 of 5); CaringBridge updates (63 of 73) and calendar requests (4 of 5, thin); MyChart records (25 of 33; when it fails, messages go to a parent who never checks).
- Mixed: CaringBridge relatives joining (6 of 11; relatives can't get in or wait for approval). MyChart relatives joining (17 of 36; sign-in codes go to the parent's phone, and families share one password).
- Mostly problems:
  - Lively family alerts (3 of 46; the app crashes, alerts don't arrive)
  - Lively relatives joining (3 of 45; invites and sign-in fail)
  - Lively emergency (34 of 112; wrong locations, safety gaps)
  - Medical Guardian emergency (5 of 27; wrong readings, safety gaps, parents won't wear it, the call shows up as an unknown number)
  - Medisafe relatives joining (0 of 5) and medications (5 of 15); in both, the family can't see the same info
- No evidence either way: documents (Caring Village, Everplans) and caregiver support (6 companies offer something), because no review or post mentions those features.
- Blue row, Caregivers on Reddit (825 posts, any tool): support 292 · relatives' access 147 · calendar and tasks 144 · documents 128 · records 90 · medications 88 · updates 78 · emergency 66.

## 6. Gaps and opportunities (open problems, not features to build)
1. Letting relatives in without sharing one login is offered almost everywhere but rarely works well. Reddit: confirmed, and it goes beyond apps. Banks and agencies refuse the caregiver (52), passwords are lost (35), codes go to the parent's phone (23).
2. No company covers family coordination, records and safety together, so families stitch tools together. Reddit: confirmed. Group chats, notebooks, spreadsheets and pill boxes are named far more than any competitor, and posts say they fall apart.
3. Safety tools reach the older person, but the family side fails. Reddit: confirmed. Families want the button to reach them, not a dispatcher, and parents often won't wear the device.
4. Medication info the family can see exists in only two products. Reddit: confirmed but may be overstated (app makers post a lot on this).
5. Records work in MyChart but stay inside it. Reddit: unclear. MyChart works once a caregiver gets in; the bigger problems are getting in (gap 1) and doctors not sharing with family.
6. New from Reddit: documents. Two companies offer storage, but caregivers' problems are mostly about the power of attorney (no POA, or banks reject it: 42) and scattered papers (32).
7. New from Reddit: caregiver support is the biggest topic (292 posts) and is mostly about people (doing it alone 137, burnout 57, no respite 20). Six companies offer some support feature, and nobody mentions any of them.

## 7. Still open (the user's decisions)
- The OUR COMPANY row: which features would be "planned" for MVP #1. Only after the user picks the problems.
- Next course steps: UVP, then positioning statement, then Vision Boards (MMP and MVP #1, Audience 1 first).

## 8. Limits
- Reviews and posts come from people who chose to post and lean toward problems.
- Claude tagged each source once; no person double-checked. Big apps were keyword-filtered, not randomly sampled.
- The companies were chosen by the team. Lotsa and Everplans have almost no caregiver reviews.
- These are desk-research patterns, not measured rates.

## 9. Files
`docs/feature-analysis.md` (full) · `docs/sources/app-reviews/analysis/feature_ratings.py` and `feature-ratings.json` · `docs/sources/app-reviews/analysis/extra-tags-2026-11-03.json` · `docs/reddit-caregiver-findings-2026-11-03.md` · `docs/sources/INDEX.md`
