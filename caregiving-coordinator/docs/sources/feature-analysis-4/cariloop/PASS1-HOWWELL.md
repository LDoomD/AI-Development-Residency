# Cariloop: how well do the features work for families? (PASS 1, saved data only)

Date: 2026-11-06. No website was scraped. Paths are under `docs/sources/` unless they start with `feature-analysis-4/`. Evidence states used: observed, inferred, documented, reported, not-assessed. Every count below is **reported** (a person said it). None is **observed** by us.

## Short answer

- Independent reports about **Cariloop itself**: **3** (2 Google Play reviews, 1 Reddit r/AskHR comment). Only 2 are about a feature (both F8, both WORKED). That is far below the 15 target. The data does not exist in the saved files.
- The saved Reddit archive has **0** Cariloop mentions (checked again: 0 of 49,315 posts, 0 of 142 forum threads, 0 of 17,956 app review rows).
- Families do ask about employer-paid coach programs (Wellthy 2 posts, Torchlight 1, an unnamed work care-navigator 1) but those posts have no answers saved, so 0 outcomes.
- Comparable programs (not Cariloop): 4 app reviews (3 WORKED, 1 DID NOT WORK), all F8. Use only as a loose hint.

## (a) Table: one row per cell

Capability state is from `feature-analysis-4/cariloop/EVIDENCE.md` (state: documented from company pages). Counts are Cariloop-only reports. Last column = comparable programs (not Cariloop).

| Cell | Capability (EVIDENCE.md) | WORKED | DID NOT WORK | MIXED | USED, NO VERDICT | Total Cariloop reports | Comparable programs (W / DNW / M) |
|---|---|---|---|---|---|---|---|
| F1 Relief finder | LIMITED (employer only) | 0 | 0 | 0 | 0 | 0 | 0 / 0 / 0 |
| F2 Eligibility and applications | VERIFY | 0 | 0 | 0 | 0 | 0 | 0 / 0 / 0 |
| F3 Paying for relief | LIMITED (employer only) | 0 | 0 | 0 | 0 | 0 | 0 / 0 / 0 |
| F4 Refusing parent support | VERIFY | 0 | 0 | 0 | 0 | 0 | 0 / 0 / 0 |
| F5 Relatives cover time | LIMITED (employer only) | 0 | 0 | 0 | 0 | 0 | 0 / 0 / 0 |
| F6 Account access | VERIFY | 0 | 0 | 0 | 0 | 0 | 0 / 0 / 0 |
| F8 Personal guidance | LIMITED (employer only) | 2 | 0 | 0 | 0 | 2 | 3 / 1 / 0 |
| F9 Behavior and hard talks help | LIMITED (employer only) | 0 | 0 | 0 | 0 | 0 | 0 / 0 / 0 |
| F10 People who understand | LIMITED (employer only) | 0 | 0 | 0 | 0 | 0 | 0 / 0 / 0 |

Extra Cariloop report with no cell: Google Play 2024-11-16, app will not let the user exit (DID NOT WORK, app problem). Cariloop total = 3 reports.

## (b) The reports behind each count

### Cariloop-only reports

| # | Cell | Class | Quote (max 20 words, exact) | Audience | Source | Limit |
|---|---|---|---|---|---|---|
| 1 | F8 | WORKED | "Staff wonderful incredibly helpful in your time of need" | unclear | Play review 2022-04-30; docs/sources/competitors-4/manual-saves/google_play_cariloop_full_2026-11-04.txt (play.google.com/store/apps/details?id=com.cariloop.member) | Google Play; saved page shows 2 of 9 reviews. |
| 2 | none (app bug) | DID NOT WORK | "Won't let me exit app. I have to restart my phone to exit." | unclear | Play review 2024-11-16; docs/sources/competitors-4/manual-saves/google_play_cariloop_full_2026-11-04.txt (play.google.com/store/apps/details?id=com.cariloop.member) | App problem, not a feature cell. |
| 3 | F8 | WORKED | "I have personally used the service and it could not have been more helpful." | unclear (HR staff at an employer) | r/AskHR comment; docs/sources/feature-analysis-4/cariloop/reddit_askhr_sichx0_cariloop_2026-11-06.txt (https://www.reddit.com/r/AskHR/comments/sichx0/) | Neutral third party; on a post by an HR person comparing vendors, not by a family caregiver. |

Not counted as reports: Apple listing shows 23 ratings, 4.48 stars (`docs/sources/app-stores/apple-named/Cariloop.json`); no review text was saved, so no feature can be read from it. BBB: 0 complaints, 0 reviews (`competitors-4/review-sites/bbb_2026-11-04.txt`). The r/AskHR post also has one comment asking "How does Cariloop work?" (a question, no verdict).

### Comparable employer-linked coach or advocate programs (NOT Cariloop; hint only)

| App review id | Program | Cell | Class | Quote (exact) | Audience | Source | Limit |
|---|---|---|---|---|---|---|---|
| b-500 | Wellthy | F8 | WORKED | "asked Wellthy to help and they were so persistent in calling every day" | unclear | docs/sources/app-reviews/all-reviews2.jsonl | Apple review. Wellthy is a comparable caregiver-coordinator service (employer-paid status NOT verified in these files). |
| b-502 | Wellthy | F8 | WORKED | "Great product was able to help support elderly parent from a distance" | adult child | docs/sources/app-reviews/all-reviews2.jsonl | Apple review. |
| b-209 | Accolade | F8 | WORKED | "I don’t know what I would’ve done without her when my husband had cancer." | spouse | docs/sources/app-reviews/all-reviews2.jsonl | Apple review; Accolade nurse. Health-plan advocate service, loosely comparable. |
| b-30 | Accolade | F8 | DID NOT WORK | "Accolade is your insurance company’s outsourced customer service platform." | unclear | docs/sources/app-reviews/all-reviews2.jsonl | Apple review; complaint about the "care advocate" service. |

Wellthy app also has 6 reviews about login and app problems (b-499, b-501, b-503, b-504, b-505, b-506). These are about the app, not a caregiver-help cell, so they are not counted.

### Families asking, no outcome saved (not counted)

- p1h9p97b (CaregiverSupport) https://www.reddit.com/r/CaregiverSupport/comments/1h9p97b/: asks if anyone used an employer-offered service (Wellthy, Torchlight, or a care navigator). Source: docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl.
- p15edl7o (AgingParents) https://www.reddit.com/r/AgingParents/comments/15edl7o/: asks if anyone used an employer-offered service (Wellthy, Torchlight, or a care navigator). Source: docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl.
- p1e6j86w (AgingParents) https://www.reddit.com/r/AgingParents/comments/1e6j86w/: asks if anyone used an employer-offered service (Wellthy, Torchlight, or a care navigator). Source: docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl.
- p1n0vjxy (CaregiverSupport) https://www.reddit.com/r/CaregiverSupport/comments/1n0vjxy/: asks if anyone used an employer-offered service (Wellthy, Torchlight, or a care navigator). Source: docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl.

Note: these Reddit files hold the post only. Comments were not saved for most posts, so answers cannot be read.

## (c) Search filters and raw hits

| Filter | Raw hits |
|---|---|
| 'cariloop' in saved Reddit posts (posts.jsonl + posts_targeted.jsonl, 49,315 unique posts) | 0 |
| 'cariloop' in 142 saved forum threads (AgingCare + AlzConnected) | 0 |
| 'cariloop' in 17,956 saved Apple/Google app review rows (all-reviews*.jsonl) | 0 |
| 'care coach' in Reddit, forums and app reviews | 0 |
| 'care navigator|nurse navigator|patient navigator' in Reddit and forums | 9 |
| 'caregiver benefit|caregiving benefit|benefits for caregivers' in Reddit/forums (read: none is a coach report) | 8 |
| 'EAP|employee assistance' in Reddit/forums (read: 4 posts, none report an outcome with a coach) | 4 |
| 'wellthy' in Reddit | 2 |
| 'wellthy' app reviews (all rows, app name wellthy) | 10 |
| 'torchlight' in Reddit | 1 |
| 'accolade' app review rows (read: only those naming a spouse/parent or 'advocate' were considered) | 427 |
| `grep -i cariloop` over docs/sources (all files) | hits only in company pages, planning files, scripts and the files named above (no new family report) |
| BBB save, Google Play save, r/AskHR thread, search_cariloop.json | BBB 0/0; Play 2 of 9 reviews shown; AskHR 1 usable comment; search_cariloop.json is empty (`[]`) |

Hits I read: all 3 Cariloop reports, all 4 comparable reviews, all 4 ask-posts. I did not read the other Accolade, Included Health, Rightway and Alight review rows one by one; I filtered them for family words (21 rows) and read those 21.

## (d) Cells still VERIFY: does the saved data settle them?

| Cell | Settled? | Evidence |
|---|---|---|
| F2 Eligibility and applications | No | 0 independent reports mention a Cariloop coach checking eligibility or filing an application. Stays VERIFY (not-assessed). |
| F4 Refusing parent support | No | 0 independent reports. The Play listing says coaches help with "Managing family dynamics" (documented, company text) but nobody reports a refusing parent. Stays VERIFY. |
| F6 Account access | No | 0 reports. Stays VERIFY. |

## (e) Not checked

- Trustpilot (blocked), Apple review text, Glassdoor-type or employer-forum posts, Facebook groups, YouTube (not searched for Cariloop), LinkedIn, news. None saved.
- Reddit comments (not saved for most posts) and any reply to the three ask-posts.
- Whether Wellthy, Torchlight or Accolade are employer-paid: not verified in these files (inferred only).
- Real Cariloop use by employees: employers hold satisfaction surveys; none saved.
- Features F1, F3, F5, F9, F10: no independent report either way (0 found).
