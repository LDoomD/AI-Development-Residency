# Feature comparison analysis (started 2026-11-03)

Follows the four steps on the Figma board, section "ABOUT FEATURE ANALYSIS" (file `HcDDdEGAnikTImO8v7UPMp`, node `5:2593`). Discovery only: no product ideas go into the feature columns. The OUR COMPANY row stays empty until the gaps (step 4) are written, then holds "planned" guesses only (Fleety, `docs/sources/fleety/answer-1-feature-analysis-and-next-steps.md`).

## Step 1: competitors (approved 2026-11-03)

Approved by the owner 2026-11-03: the 8 businesses from the competitor analysis (`docs/competitive-analysis.md`, same as the Figma table): 7 direct, 1 indirect. The two workarounds in that table (group texts, paper notebook and visit log) are not businesses and have no features to compare; they go in the gaps box (step 4) as "what families use instead". Info columns use the company's own words from that file; nothing new was researched.

| Company | Direct or indirect | Kind of tool (market segment) | Website | Pricing (company's words) | Who uses it and who pays (company's words) |
|---|---|---|---|---|---|
| Caring Village | Direct (coordination) | Family care-coordination app | https://caringvillage.com/ | Free plan, up to two members, ad-supported; Popular Circle $14.99/month | Family and professional caregivers; joining a village as a member is free; businesses contact sales |
| CaringBridge | Direct (coordination) | Family care-coordination app | https://www.caringbridge.org/ | No cost; donor-supported nonprofit | Family caregivers and the people they update; paid for by donors |
| Lotsa Helping Hands | Direct (coordination) | Family care-coordination app | https://lotsahelpinghands.com/ | Free | Caregivers organizing care, and friends and family who want to help |
| Everplans | Direct (access to accounts) | Digital vault and emergency access | https://www.everplans.com/ | Base app free; Premium $99.99/year | Individuals and families; also offered through financial advisors and enterprise partners |
| Epic MyChart | Direct (access to records) | Patient portal with proxy access | https://www.mychart.org/ | Not found in the saved pages | "over 190 million patients"; who pays not found in the saved pages |
| Lively | Direct (monitoring and safety) | Medical alert and senior phone | https://www.lively.com/ | Devices (Mobile2 $89.99 sale) plus service plans; no long-term contracts; annual caregiver subscription | Older adults and their caregivers |
| Medical Guardian | Direct (monitoring and safety) | Medical alert | https://www.medicalguardian.com/ | "about $1 a day"; device may be discounted or free through insurance | Older adults and families ("over 600,000+ families") |
| Medisafe | Indirect (covers part of the need) | Medication reminder app | https://medisafeapp.com/ | Free, with a paid subscription; also sold to pharma ("patient engagement engine") | Patients and their "Medfriend" or caregiver |

Template wording to change in the second version: the question under MARKET ("Community engagement or loyalty software?") becomes "What kind of caregiving tool is it?", and under MARKET SEGMENT ("...Community Engagement Software market...") becomes "Which caregiving market segment does it fit?". The table has 6 competitor rows; 2 rows will be added for the eight.

## Step 2: what each competitor offers (DRAFT for the owner to review; updated 2026-11-03 with the pages found)

Features as each company names them on its own saved pages (paths under `docs/sources/`). Company claims only: whether a feature works well is judged in step 3 from reviews. The first save had empty or "page not found" files; on 2026-11-03 the real pages were found from each site's own menu and saved (see `docs/sources/INDEX.md`, "2026-11-03 feature analysis: missing competitor pages found").

**Caring Village** (`competitors/caring-village/`: home, faq, pricing, about, and `pages-2026-11-03/app.txt`)
- Shared calendar: "One calendar for the whole village", "request volunteers for appointments", "Changes synced to every phone"; Google Calendar sync and printable calendar on paid plans
- Shareable to-do lists: "Tasks with a named owner", "Claimed with one tap: 'I'll do it'"
- Medication tracking: "Each dose marked as taken", "Missed-dose reminders"
- Wellness journal: "one shared timeline", "Mood, symptoms and daily check-ins"; export for doctors on paid plans
- Secure messaging: "Send one update and the whole village has it"
- Document storage: "medical records, legal documents and IDs" (custom folders on paid plans)
- Customizable care plans: "Progress the whole family can see"
- Preparedness checklists; AI assistant "Julia" ("answers caregiving questions 24/7")
- Invites: "Add family, friends and care pros with role-based permissions"; "Family members join free"; free plan 1 village, 2 members

**CaringBridge** (`competitors/caringbridge/`: home, about-us; App Store listing; `help-center-2026-11-03/`)
- Posts: health updates to everyone at once; journal of the health journey, journaling guide
- Requests (replaced the Planner in December 2023): ask for childcare, chores, errands, meals, pet care, transportation, visiting, with dates and times; "One person can pick up each request"
- Meal Train link; Instacart; gift cards; GoFundMe fundraising
- Privacy: Public, Semi-Private (default), or Private ("Only people you add to the Approved Visitors List can view your page"); access requests; Co-Authors; block or remove a visitor
- Comments, reactions, private messages; text-message notifications

**Lotsa Helping Hands** (`competitors/lotsa-helping-hands/`: home, about, help center; App Store listing; `pages-2026-11-03/`)
- Care calendar where helpers sign up for tasks (meals, rides to appointments, visits)
- Announcements to the whole team or only to chosen groups, by email
- Groups: posts, tasks and notes "only visible to the groups you select"; private groups only Site Admins can add people to
- Well wishes; photo gallery
- No features or FAQ page exists on the site (checked 2026-11-03)

**Everplans** (`competitors/everplans/`: home, pricing, about)
- Store family documents, IDs, vital info and accounts in one place
- Secure sharing of items with trusted people (Premium)
- Reminders and alerts about important dates
- Guided planning ("smart planning system"), articles, videos and checklists
- Free plan limited to 3 items

**Epic MyChart** (`competitors-2/epic-mychart/www_mychart_org.txt`)
- View medications, test results and bills
- Find and schedule care
- "Manage care for you and your family" (proxy access)
- Connect with your doctor virtually
- Access and share your information in one place; one login for all your care

**Lively** (`competitors-2/lively/www_lively_com.txt` and `shop-pages-2026-11-03/`)
- Urgent Response button: "Certified agents are ready to respond in emergencies, big or small, 24/7"; agents may call "a caregiver or loved one"
- Fall detection on the Mobile2 device ("Requires a subscription to fall detection", add $9.99/month)
- Lively Link app: "Invite friends and family to connect to your Lively device"; "they'll receive Urgent Response alerts" and "can view her location"
- Medical alert plans: Basic $24.99/month, Premium $34.99/month (device $89.99 on sale)
- Nurse On-Call (can refill prescriptions by phone), Ask Lively 24/7 operators, Lively Rides, Care Advocate
- Everyday Support for Caregivers ($99/year, through Wellthy, AARP, Instacart, Norton): "Dedicated Care Coordinator", "Assistance coordinating appointments, paperwork, insurance, transportation", "option to invite family members, so everyone stays organized and informed", online caregiver community

**Medical Guardian** (`competitors-2/medical-guardian/www_medicalguardian_com.txt`)
- Wearable and home medical alert devices with one-button help to a 24/7 U.S. monitoring center
- GPS location; fall detection (add-on; "does not work 100% of the time")
- Monitoring center can contact "a neighbor, caregiver, or family member"
- Member portal (MyGuardian); water-resistant devices

**Medisafe** (`competitors/medisafe/www_medisafeapp_com_.txt` and `pages-2026-11-03/features.txt`)
- Medication management for complex and "as needed" schedules
- Family scheduling and tracking: "track all your family's medication doses and schedules in one place"; "Medfriend feature to know when a loved one missed a dose so you can give them a nudge"
- Drug interaction warnings
- Refill and appointment reminders
- 90+ measurement trackers; reports sent to doctors
- Resource centers for a dozen conditions

Limits: Everplans, MyChart and Medical Guardian were not re-fetched (their saved main pages had full text, but they are single pages, so smaller features may be missing). Lively's plan grid did not copy as text, so which plan includes the Lively Link app is not known.

## Step 3: side-by-side comparison (DRAFT for the owner to review; updated 2026-11-03)

Feature columns approved by the owner 2026-11-03, grouped by caregiver need. Same content as the Figma section "FEATURE COMPARISON ANALYSIS 2 — CAREGIVING" (node `2436:9443`, right of the Feature Analysis section; the blank template is unchanged).

**How to read each box**
- A filled box means the company names the feature on its own saved pages (step 2). **Not found on their site** = we could not find it; it may still exist.
- First line: what caregivers say in app reviews. 🟢 **Mostly works** = at least 2 out of 3 reviews about it say it worked. 🔴 **Mostly problems** = at least 2 out of 3 describe a problem. 🟠 **Mixed** = in between. **Too few reviews to judge** = fewer than 5. **Not checked in reviews** = reviews were not sorted by this topic (columns 5, 6, 8). **No reviews collected** = no caregiver reviews for this app.
- Second line: the real count. Third line: what the feature is.

**Where the review counts come from (re-runnable):** `python3 docs/sources/app-reviews/analysis/feature_ratings.py` writes `feature-ratings.json`. It uses the 439 caregiving-only reviews (`verified-tags.json` filtered by `relevance-final.json`). "Worked" reviews are matched to a column by the keyword themes in `worked_themes.py`; "problem" reviews by their category tag (column 1: organized vs not_syncing, reminders_failing; column 2: updates vs alerts_unreliable, not_syncing, family_cant_see_same_info, app_reliability; column 3: access_for_others, family_cant_see_same_info; column 4: meds vs reminders_failing, alerts_unreliable, family_cant_see_same_info, not_syncing; column 7: where, emergency vs readings_wrong, alerts_unreliable, safety_gap). A review can count in more than one column. Claude sorted each review once in an earlier session; no person double-checked. Epic MyChart and Everplans reviews are small separate samples, not part of the 439.

Change from the first draft: the counts were rerun by this one script. Lively "one update reaches everyone" moved from not rated to Mostly problems (2 of 24), because problem reviews about the family app crashing or alerts not arriving are now counted in column 2; Lively emergency was 25 of 80 before the 2026-11-03 additions (26 of 81 in the first draft; one review was counted twice).

**More reviews added 2026-11-03 (owner asked to fill the thin boxes).** Collected in the built-in browser and saved under `docs/sources/` (see INDEX.md, "2026-11-03 feature analysis: more reviews"):
- Google Play, read through the Play Store's own review data: Lotsa (all 20 written reviews), Lively Link (1,451 read; 66 about family access kept), CaringBridge (2,080 read; 36 about family and help kept), Epic MyChart (6,169 newest read, July to November 2026; 58 with a family or caregiving word kept). Everplans has no reviews on Google Play. Caring Village's 42 Play reviews were already saved.
- Caregiver forums: AgingCare and ALZConnected threads that name the apps (found with DuckDuckGo). Reddit is blocked in the built-in browser and was not used.
- Claude tagged each new review by column (`docs/sources/app-reviews/analysis/extra-tags-2026-11-03.json`); `feature_ratings.py` adds them to the counts and skips reviews already in the older files.
- Still thin: Lotsa (none of its 20 Play reviews clearly come from someone caring for a relative), Everplans (no caregiver reviews anywhere we looked), Caring Village (every review the stores show is already counted), and the columns no review talks about.
- Kept to a keyword filter for the big apps, so these are not random samples.

| Company | 1. Shared calendar and task sign-up | 2. One update reaches everyone | 3. Relatives join with their own access | 4. Medication reminders family can see | 5. Store and share important documents | 6. See medical records and test results | 7. Emergency help button and fall alerts | 8. Support for the caregiver |
|---|---|---|---|---|---|---|---|---|
| OUR COMPANY | (left empty until step 4) | | | | | | | |
| Caring Village | 🟢 Mostly works · 14 of 15 reviews · calendar, claimable to-dos | Too few (3) · journal and messages | Too few (1) · role-based invites | 🟢 Mostly works · 4 of 5 reviews · doses checked off, missed-dose reminders | Not checked · medical, legal, IDs | Not found | Not found | Not checked · AI assistant Julia, checklists |
| CaringBridge | Too few (4) · Requests with dates, one helper each; no shared calendar | 🟢 Mostly works · 61 of 71 reviews · posts to everyone | 🟠 Mixed · 6 of 11 say it works · private page, approved visitors, co-authors | Not found | Not found | Not found | Not found | Not checked · support messages, journaling guide, Meal Train |
| Lotsa Helping Hands | Too few (1) · care calendar with sign-up | Too few (2) · announcements by email | Too few (0) · groups set who sees what | Not found | Not found | Not found | Not found | Not checked · well wishes |
| Everplans | Not found | Not found | No reviews collected · secure sharing (Premium) | Not found | No reviews collected · documents, IDs, accounts | Not found | Not found | No reviews collected · planning articles and checklists |
| Epic MyChart | Not found | Not found | 🟠 Mixed · 13 of 25 say it works · manage care for your family (proxy) | Too few (0) · view medications; no reminders named | Not found | 🟢 Mostly works · 14 of 15 reviews · test results, medications, bills | Not found | Not found |
| Lively | Too few (2) · human Care Coordinator ($99/yr add-on); no shared calendar | 🔴 Mostly problems · 3 of 46 say it works · family app alerts when the button is pressed | 🔴 Mostly problems · 3 of 45 say it works · invite family to Lively Link | Not found | Not found | Not found | 🔴 Mostly problems · 34 of 107 say it works · wrong locations, missed alerts | Not checked · Care Coordinator, caregiver community, Nurse On-Call |
| Medical Guardian | Not found | Not found · family contacted only in an emergency | Not found · family access not named | Not found | Not found | Not found | 🔴 Mostly problems · 3 of 19 say it works · wrong readings, safety gaps | Not found |
| Medisafe | Not found | Not found | 🔴 Mostly problems · 0 of 5 say it works · Medfriend | 🔴 Mostly problems · 5 of 15 say it works · Medfriend sees missed doses | Not found | Not found | Not found | Not checked · condition resource centers |

What the table shows (reading, not proof):
- Common: relatives joining (7 of 8) and support for the caregiver (6 of 8) are offered by most companies, but few reviews speak to how well they work.
- Unique: medical records (MyChart only); emergency help (Lively and Medical Guardian only).
- Missing: no company offers all of family coordination, records and safety. Lively comes closest (safety plus a paid human coordinator), but its family app only sends emergency alerts.
- Where there are enough reviews: coordination (Caring Village calendar and medications, CaringBridge updates) and MyChart records mostly work; letting relatives in is mixed at best (CaringBridge 6 of 11, MyChart 13 of 25) and mostly fails at Lively and Medisafe; safety alerts mostly have problems.
