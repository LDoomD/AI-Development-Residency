# PASS 1: How well Caring Village features work for real families

Date: 2026-11-06. Branch feature-analysis-4. Saved data only; no website was scraped. Paths are under the repo root (docs/sources/...).
State key: observed = I saw it in a saved file; reported = a person's own account (not checked by me); documented = the company's own page; not-assessed = no usable evidence.
Rule used: a report counts only if it is an app-store review (or post) by a family caregiver or a neutral third party about Caring Village and that feature. Company marketing, app-maker posts and posts that only name the product do not count. Each counted report was read in full by me. Quotes were machine-checked against the saved text (exact match, 20 words max).

## (a) Summary table

| Cell | Capability (EVIDENCE.md) | WORKED | DID NOT WORK | MIXED | Total independent reports | Evidence state |
|---|---|---|---|---|---|---|
| F1 Relief finder | YES (documented: Care.com link-out) | 0 | 0 | 0 | 0 | not-assessed (0 reports found) |
| F2 Eligibility and applications | VERIFY | 0 | 0 | 0 | 0 | not-assessed (0 reports found) |
| F3 Paying for relief | YES (documented: blog) | 0 | 0 | 0 | 0 | not-assessed (0 reports found) |
| F4 Refusing parent support | VERIFY | 0 | 0 | 0 | 0 | not-assessed (0 reports found) |
| F5 Relatives cover time | YES (documented) | 7 | 8 | 8 | 23 | reported |
| F6 Account access | VERIFY | 0 | 0 | 0 | 0 | not-assessed (0 reports found) |
| F8 Personal guidance | VERIFY (AI helper documented; human coach not found) | 3 | 0 | 0 | 3 | reported |
| F9 Behavior and hard talks help | behavior YES (blog only); hard talks VERIFY | 0 | 0 | 0 | 0 | not-assessed (0 reports found) |
| F10 People who understand | VERIFY | 0 | 0 | 0 | 0 | not-assessed (0 reports found) |

Plain reading: the saved data gives many reports for F5 (relatives and tasks) and 3 for the AI helper (F8). It gives 0 reports for F1, F2, F3, F4, F6, F9 and F10. Silence is not proof the feature fails; it means reviewers did not write about it.

Total reviews of Caring Village found in saved data: 54 Apple reviews (ids a-1346 to a-1399) and 42 Google Play reviews (g-caring-village-0 to 41) = 96. Of these, 25 distinct reviews are counted above (one review can speak to more than one cell). The earlier note user-reviews-read-2026-11-06.md says 45 Apple reviews; the file has 54. I used the file count.

## (b) Reports behind each count

#### F5

| # | Class | Audience | Source (path + id/URL) | Quote (copied exactly, 20 words max) | Limit |
|---|---|---|---|---|---|
| 1 | WORKED | adult child (caring for a parent) (in-laws and a child) | docs/sources/app-reviews/all-reviews.jsonl (id a-1356, apple, 5 stars, 2025-12-13) | "It also makes asking for help so much easier." | Says asking is easier; does not say relatives then showed up. |
| 2 | WORKED | unclear | docs/sources/app-reviews/all-reviews.jsonl (id a-1372, apple, 5 stars, 2025-09-12) | "area for tasks and to dos that can be delegated to others" | Feature praise; no story of a task being done. |
| 3 | WORKED | adult child (caring for a parent) (father with dementia) | docs/sources/app-reviews/all-reviews.jsonl (id a-1365, apple, 5 stars, 2025-11-21) | "Being able to use the app to coordinate various activities and responsibilities" | Says coordination got easier; no detail on who did what. |
| 4 | WORKED | adult child (caring for a parent) (8 siblings) | docs/sources/app-reviews/all-reviews.jsonl (id a-1351, apple, 5 stars, 2026-04-10) | "so that one of us can join them in person or on a call" | Calendar used to pick which sibling attends. Reviewer also says Caring Village is better than texting. |
| 5 | WORKED | unclear | docs/sources/app-reviews/all-reviews.jsonl (id a-1350, apple, 5 stars, 2026-04-13) | "Sharing updates, schedules, and tasks is simple and intuitive." | General praise. |
| 6 | WORKED | adult child (caring for a parent) (mother with cancer) | docs/sources/app-reviews/all-reviews.jsonl (id a-1355, apple, 5 stars, 2026-01-06) | "Having a shared calendar to coordinate tasks gave structure to days that felt overwhelming" | Reviewer is the main caregiver; hired caregiver also used it. |
| 7 | WORKED | unclear | docs/sources/app-reviews/google-play/google-play-reviews-caring-village.json (review index 38; also all-reviews.jsonl id g-caring-village-38) | "keep track of what needs to be done, and who is responsible for making it happen" | 2017 review; does not say tasks were finished. |
| 8 | MIXED | unclear (professional care manager) | docs/sources/app-reviews/all-reviews.jsonl (id a-1387, apple, 4 stars, 2020-09-01) | "ask for volunteer from family at times there is no staff in the home" | Works for assigning, but the same review lists privacy and care-plan problems. |
| 9 | MIXED | unclear (grandchild) | docs/sources/app-reviews/all-reviews.jsonl (id a-1390, apple, 1 stars, 2019-01-19) | "while you can have repeating events you can’t have more than one person sign up" | 1 star, but text calls it a great app. Recurring tasks cannot be shared by two people. |
| 10 | MIXED | unclear | docs/sources/app-reviews/all-reviews.jsonl (id a-1388, apple, 4 stars, 2020-02-13) | "One family member has issues using email so hasn’t joined the village." | 4 stars. Invite by email left one relative out. |
| 11 | MIXED | spouse or partner | docs/sources/app-reviews/all-reviews.jsonl (id a-1374, apple, 4 stars, 2025-08-26) | "when I send the email to family and friends to join it does not always work." | 4 stars. Invites sometimes fail. |
| 12 | MIXED | unclear | docs/sources/app-reviews/google-play/google-play-reviews-caring-village.json (review index 18; also all-reviews.jsonl id g-caring-village-18) | "I loved using it but other family.members had more difficulty than I would have expected." | 5 stars. Says relatives struggled. |
| 13 | MIXED | unclear | docs/sources/app-reviews/google-play/google-play-reviews-caring-village.json (review index 7; also all-reviews.jsonl id g-caring-village-7) | "family with iPhones can't access the app." | 3 stars. Overseas family could not join (2021, Australia). |
| 14 | MIXED | adult child (caring for a parent) (5 siblings) | docs/sources/app-reviews/all-reviews.jsonl (id a-1391, apple, 3 stars, 2019-01-05) | "“friends” and “inner circle” can see almost everything" | 3 stars. Cousins had to be removed because the sharing levels showed private papers. |
| 15 | MIXED | unclear | docs/sources/app-reviews/all-reviews.jsonl (id a-1384, apple, 3 stars, 2021-09-28) | "where a family member cannot join" | 3 stars. Support took days to answer. |
| 16 | DID NOT WORK | unclear | docs/sources/app-reviews/all-reviews.jsonl (id a-1381, apple, 2 stars, 2023-04-06) | "Wish the calendar appts would go to everyone in inner circles category instead of only to the person assigned." | 2 stars. |
| 17 | DID NOT WORK | unclear (patient before surgery) | docs/sources/app-reviews/all-reviews.jsonl (id a-1389, apple, 1 stars, 2019-03-13) | "Most people couldn’t even sign in and when they could the calendar/scheduling function was a total fail." | 1 star, 2019. Family and friends could not use it. |
| 18 | DID NOT WORK | unclear | docs/sources/app-reviews/all-reviews.jsonl (id a-1364, apple, 1 stars, 2025-11-24) | "I received notification that I needed to upgrade and pay in order to have more than TWO members" | 1 star, 2025. Relatives were locked out after a free limit. |
| 19 | DID NOT WORK | adult child (caring for a parent) (mother) | docs/sources/app-reviews/google-play/google-play-reviews-caring-village.json (review index 5; also all-reviews.jsonl id g-caring-village-5) | "Also the limits to the village (only 5 people) is a real deterrent." | 2 stars, 2026. Group size limit. |
| 20 | DID NOT WORK | unclear | docs/sources/app-reviews/all-reviews.jsonl (id a-1366, apple, 1 stars, 2025-10-27) | "Most disappointing is how poorly the calendar (doesn’t) work." | 1 star, 2025. Calendar sync. |
| 21 | DID NOT WORK | unclear | docs/sources/app-reviews/all-reviews.jsonl (id a-1367, apple, 1 stars, 2025-10-20) | "Trying to create a task, just didn’t work" | 1 star, 2025. |
| 22 | DID NOT WORK | unclear | docs/sources/app-reviews/google-play/google-play-reviews-caring-village.json (review index 20; also all-reviews.jsonl id g-caring-village-20) | "Checklist feature didn't work. Then it locked me out." | 1 star, 2026. |
| 23 | DID NOT WORK | unclear | docs/sources/app-reviews/all-reviews.jsonl (id a-1394, apple, 1 stars, 2017-10-18) | "Calendar doesn’t open and freezes the app on iphone7." | 1 star, 2017. Old bug; may be fixed. |

#### F8

| # | Class | Audience | Source (path + id/URL) | Quote (copied exactly, 20 words max) | Limit |
|---|---|---|---|---|---|
| 1 | WORKED | unclear | docs/sources/app-reviews/all-reviews.jsonl (id a-1372, apple, 5 stars, 2025-09-12) | "even an AI capability to ask pertinent questions regarding care" | AI helper, not a human coach. |
| 2 | WORKED | unclear | docs/sources/app-reviews/all-reviews.jsonl (id a-1373, apple, 5 stars, 2025-09-11) | "The new AI feature is a game changer!" | AI helper, not a human coach. Reviewer asks it if care-plan tasks are done. |
| 3 | WORKED | unclear | docs/sources/app-reviews/google-play/google-play-reviews-caring-village.json (review index 9; also all-reviews.jsonl id g-caring-village-9) | "The AI tool is great as well." | AI helper, not a human coach. |

### Reviews read but not counted (and why)
| Review | Why not counted |
|---|---|
| a-1352 and g-caring-village-1 (support team answered fast; one got a custom video) | This is customer support, not an ongoing coach (F8). Reported, but a different feature. |
| a-1351, a-1359, a-1360 (upload and keep documents) and a-1364, a-1391 (documents vanished; friends could see Medicare card) | Document storage, not getting into a parent's bank, insurance or portal accounts (F6). Adjacent only. |
| a-1362 ("a great place to learn about all the myriad resources available") | Too vague to match F1, F2 or F3. |
| a-1372 ("information on proper paperwork to have in place") | Paperwork tips, not eligibility or applications (F2). |
| g-caring-village-19 ("Social media for people who want to grandstand") | About the feel of the village, not about finding other caregivers (F10). |
| a-1364, g-caring-village-5 and similar price complaints | These are about Caring Village's own subscription price, not about learning what respite costs (F3). |
| Every other 5-star or 1-star review (login bugs, medication bugs, calendar-day bugs, "game changer") | Not about the nine features. Care-plan and medication problems (not one of the nine features): g-caring-village-0, g-caring-village-5, g-caring-village-36 (care plan stuck on the prior day). Missing past notes: a-1379, a-1374. |
| Reddit posts p1jwq5te, p1q4s3sb, p1qk7k7k | Each asks whether Caring Village is good. None describes using it. |

## (c) Filters used and raw hit counts
| Filter | Where | Raw hits | What I did |
|---|---|---|---|
| app name = caring-village | docs/sources/app-reviews/all-reviews.jsonl, all-reviews2.jsonl, all-reviews3.jsonl, all-reviews4.jsonl | 54 Apple reviews | Read every one. |
| Google Play file for Caring Village | docs/sources/app-reviews/google-play/google-play-reviews-caring-village.json | 42 | Read every one. |
| text contains "caring village" inside reviews of other apps | all four all-reviews files | 0 | Nothing to count. The 42 Google reviews also sit in all-reviews.jsonl (same ids), so I counted them once. |
| "caring village" or "caringvillage" in Reddit | posts.jsonl (43,665 posts) and posts_targeted.jsonl (5,650 posts) | 3 and 0 | Read all 3; none counted. |
| "caring village", "caringvillage", "everplan", "deputy" in forums | docs/sources/forums/agingcare and alzconnected (142 .txt files) | 0 | Nothing to count. |
| "caring village" in BBB and Trustpilot saves | docs/sources/competitors-4/review-sites/ | 0 | BBB file has Cariloop and A Place for Mom only; Trustpilot file is Everplans only. |
| Caring Village in docs/sources/competitive-analysis-2/themes/caring-village.json | earlier pass by a reader | 29 reviews kept | Cross-check only. I re-read the raw reviews and classified them myself; I did not copy its counts. |

## (d) Cells still marked VERIFY: does the saved data settle them?
| Cell | Settled? | Evidence |
|---|---|---|
| F2 Eligibility and applications | No | 0 reviews mention checking eligibility or applying. Capability stays VERIFY (silence, not NO). |
| F4 Refusing parent support | No | 0 reviews. g-caring-village-18 says "it depends on how much info the patient wants to share", which is about a patient's privacy, not about accepting help. |
| F6 Account access | No | 0 reviews about bank, insurance or portal logins. Reviews only cover uploading documents (a-1351, a-1360). Leans NO, still silence. |
| F8 Personal guidance | Partly | Three reviews (a-1372, a-1373, g-caring-village-9) confirm an AI helper exists and works for those users (reported). No review mentions a human coach or expert. So: AI helper YES (reported); human one-to-one coach still unproven. |
| F9 Hard talks | No | 0 reviews. Behavior help (blog only) also has 0 reviews. |
| F10 People who understand | No | 0 reviews mention meeting other caregivers. a-1355 says caregiving felt "very lonely" and the app helped her feel less alone, but that is her own family village, not other caregivers. |

## (e) Not checked
- Whether the Google Play and Apple reviews are a fair sample of all users (only reviews people chose to post; reviews skew to 5 stars and to bug complaints).
- Reviews on sites other than the stores (Trustpilot, BBB, Reddit comments). None are saved for Caring Village. Reddit saved data holds posts only, not comment threads for the 3 Caring Village posts.
- Whether old bugs (2017 to 2022 reviews) are fixed. Newer reviews (2025 to 2026) still report calendar and task failures (a-1366, a-1367, g-caring-village-20).
- Reviewer type was taken from the review text. Many reviews do not say who is cared for, so audience is "unclear".
- No website was scraped in this pass.
