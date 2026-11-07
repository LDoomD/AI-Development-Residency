# AUDIT PASS 3: VA caregiver programs

Date: 2026-11-06. Independent auditor. Nothing was committed or edited. Evidence states: **proven** (a check that could fail ran and passed), **observed** (I saw it this session), **inferred** (follows from observed facts), **documented** (a government or published source says it), **reported** (a person said it, not verified), **not-assessed**.

Scripts are in the session scratchpad `/private/tmp/claude-501/-Users-landodoom-Desktop-AI-Developer-Residency--caregiving-coordinator/88c39ed8-fc0d-46c0-b385-032bd23092de/scratchpad/` (`qcheck.py`, `rows.py`, `uniq.py`, `blind.py`, `dups.py`, `poolscan.py`, `pg.py`). Run with `python3 file.py` (not `-I`).

## 1. Quote and source check (Check 1)

Method: every table row with a quoted cell was matched to its cited source (file, Reddit post id, comment id), curly quotes, HTML entities and spaces were normalized, and I tested that the exact words are inside that source.

State: **proven** for the exact-words test. Limit: proves the words exist in the saved copy, not that the poster is honest or the class label is right.

| File | Quote rows checked | Misses |
|---|---|---|
| EVIDENCE.md | 17 | 0 |
| PASS1-HOWWELL.md | 52 | 0 |
| PASS2-HOWWELL.md | 47 | 0 |
| Total | 116 | 0 |

Extra: 0 quotes are over 20 words; 0 post, comment or forum-URL id mismatches across all 321 PASS rows of the three programs. Sanity test: changing one word or one post id made the script report a miss.

Result: **0 quote errors.**

## 2. Documented evaluation check (Check 2)

State: **observed** (I read the saved text). Page = printed page and PDF page (counted by form feeds); the HTML papers have no pages.

| Document and cited number | Found? | Page in file | Page cited | Verdict |
|---|---|---|---|---|
| VA OIG 17-04003-222, Aug 16, 2018. About 65% of 1,822 approved veterans not decided in 45 days | yes | p. ii, PDF 4 (and p. 8, PDF 16) | p. ii, PDF 4 | number correct; **limit missing:** p. 8 says "The OIG did not include denied applications" in the timeliness analysis (line 127 of PASS2 does not say it) |
| 14% waited over six months; 55% of late ones took 3 to 6 months | yes | p. 8, PDF 16 | p. 8, PDF 16 | correct |
| 4% of 1,604 discharged veterans never eligible, "On average" about four years; about $4.8 million | yes | p. 10, PDF 18 (also p. ii) | p. 10, PDF 18 | correct |
| 84 of 211 coordinators used the guidebook | yes | p. 10, PDF 18 | same | correct |
| About 50% of 1,604 not consistently monitored; at least $36.7 million questioned | yes | p. iii, PDF 5 (also p. 11) | p. iii, PDF 5 | correct |
| Example: waited "almost three years" after an application was lost | text says applied Nov 2014, "waited almost three years to be enrolled" because the coordinator incorrectly found no service link | p. 10, PDF 18 | same | correct, but "after an application was lost" is not the reason; the reason given is a wrong eligibility finding (small wording error) |
| VA OIG 25-01406-224, Oct 28, 2026. Appeals about 416 days; clinical appeals about 36 days; backlog of 703 in July 2026; 3% and 4% granted | yes | p. ii, PDF 4; p. 7, PDF 14 | same | correct. **Date check:** VA OIG's own list shows "Date Issued 10/28/2026" (search result, `vaoig.gov/reports/all`). The date is real and 9 days before today. The same report also gives a longer window (581 days, 4% and 4%) on p. 11, PDF 18 that PASS2 did not use. |
| AJMC 2022 (Van Houtven): 31,343 participants, 12,680 (40.5%) discharged; 43.5, 22.2, 11.0, 9.4, 8.4% reasons; non-spouses discharged more | yes | Results, HTML | same | correct. File shows Am J Manag Care 2022 Aug 1;28(8):e289-e295. |
| PMC8054832: 26 veterans and caregivers, 60 to 90 minutes, 2016 to 2018, Oregon and Louisiana; three themes | yes | Abstract | same | correct (52 individual interviews plus 18 pair interviews) |
| PMC5435565 REACH costs: 24 VA facilities, 491, 33.6% lower VA costs, under $5 a day | yes | Abstract | same | correct; "491 matched care recipients" is loose: the abstract says "analysis sample of 491" (treated plus matched controls) |
| PMC12483318 REACH Hope: N=110 (56 vs 54); burden and anxiety down for moderate to high; no effect on depression, self-efficacy, safety | yes | Abstract | same | correct |
| PMC5645288 REACH VA in AI/AN communities: lessons list | yes | Abstract | same | correct |
| HSRD brief 470: about 17 unmet needs | yes | HTML | same | correct. Data are from the 2007 to 2009 Partners in Dementia Care study. |

Dates: no report date looks wrong. The two OIG reports, the 2022 paper, and the 2025 REACH Hope paper are real and in range. Old data: OIG 2018 looks at 2017 and the post-9/11 program before the 2020 rules; AJMC covers 2011 to 2016; REACH VA cost data cover 2007 to 2009.

Error found (C2-2): PASS2 search log (line 183 to 184) says 90 threads (1,155 comments) plus 40 threads (599) = 130 threads, 1,754 comments. The saved file `PASS2-reddit-comments-va.jsonl` holds 134 threads and 2,313 comments (counted by `post_key` and `id`). The posts file has 238 rows, as stated. The counts in the log do not reconcile with the file.

## 3. Recount (Check 3)

### 3a. Arithmetic recount from the saved rows

| Test | Result | State |
|---|---|---|
| Per-cell W / D / M rebuilt from rows vs tables, both passes | all 20 cell-pass counts match | proven (`rows.py`) |
| Pass 1 headline "43 unique (12 / 16 / 15)" | 43 distinct quotes, matches | proven |
| Pass 2 headline "41 unique (8 / 27 / 6)" | 43 distinct quotes minus 2 flagged "same writer" = 41, matches | proven |
| Same text in both passes | **one**: see V-1 | proven (`dups.py`, 8-word shingles, 100% match) |

### 3b. Problems the files did not flag

| ID | File : line | What | Effect |
|---|---|---|---|
| V-1 | PASS1 : 75 (post 1u10o61, r/CaregiverSupport) and PASS2 : 45 (post 1u136rg, r/VeteransBenefits) | Identical text: "I was not considered fit to serve as his primary caregiver due to an incident that occurred in March 2021". One husband, two posts. Counted once in each pass. | combined F2 loses 1 D; pass 2 unique 41 becomes 40 |
| V-2 | PASS2 : 53 and 107 (comment oz4dw8i) vs PASS2 : 77 (post 1v2rub2) | The comment sits in the thread of post 1v2rub2 ("PCAFC Backpay and Stipend hold up"). Both say: dad is the veteran, the writer was approved on a remanded appeal. The comment ("when we got approved i was so relieved ... absolutely 0 help from them AND his PACT social workers") is almost surely the thread opener. State: **inferred** (no usernames). | pass 2 unique -1 (M) |
| V-3 | PASS2 : 96 (comment o0m19ly) vs PASS2 : 46 (post 1qgdwq2) | "I am here with him 24/7. My neighbors are helping me with respite time" is in the thread of the post by the wife of a veteran with seizures; likely the same writer. Different cells (F5 vs F2). | pass 2 unique -1 (M); F5 report is not independent of the F2 report |
| V-4 | PASS2 : 47, 49, 50, 52, 56 to 60, 64, 65, 71 | 12 rows are labeled "veteran applicant": the patient applying, not a family caregiver. All 12 are DID NOT WORK in F2. The header of PASS2 says they are "still family-side reports". They are not caregiver voices. | report both ways (below) |
| V-5 | PASS2 : 54 and 51 | A former clinical assessor ("the acceptance rate was 4%", "years ago") and a commenter who "sounds like VA staff" are staff statements counted as D. | remove from family counts |
| V-6 | PASS2 : 83 and 110 (comment mv8lel2) | Advice from a paid caregiver in the program ("call the social worker ... You get AT LEAST 30...") counted as W in F3 and F8. It describes a rule more than an experience. | keep as weak W; flag |
| V-7 | PASS2 : 127 | OIG 2018 65% figure applies to approved applications only (p. 8). | add limit |
| V-8 | PASS2 : 183, 184 | Search-log counts do not reconcile with the saved file (C2-2). | correct the log |

### 3c. Blind re-reading: 15 random reports (seed 13)

Method: `blind.py va-caregiver 13 15`, quote plus about 500 characters each side, no class shown.

| # | Cell | Source | My class | Earlier | Agree? | Note |
|---|---|---|---|---|---|---|
| 1 | F2 | post 1u5wh64 | D | D | yes | |
| 2 | F3 | post 1m6kjs8 | W | W | yes | VA pays caregiver, and a nursing home in full on hospice (the writer's account) |
| 3 | F3 | comment mv8lel2 | W (weak) | W | yes | rule description, V-6 |
| 4 | F1 | post 199f6z4 | D | D | yes | a VA day-center contract fell through |
| 5 | F3 | post 1o3aoxn | D | D | yes | veteran applicant, belongs in F2 not F3 |
| 6 | F2 | post 1x0bfh0 | M (no outcome yet) | M | yes | still at the first meeting |
| 7 | F3 | comment o5vk5nc | D | D | yes | 14 hours on hold |
| 8 | F1 | post 1w4oijc | D | D | yes | |
| 9 | F2 | post 1hojdyi | M | M | yes | qualified; veteran refused |
| 10 | F3 | post 1qx885u | M | M | yes | approved; cannot find the stipend amount |
| 11 | F8 | comment oz4dw8i | D | D | yes | PACT social workers are not caregiver coaches; V-2 |
| 12 | F1 | post 1ase3fe | M | M | yes | |
| 13 | F1 | post 13njcjy | W (weak) | W | yes | one line |
| 14 | F2 | comment orv556m | D | D | yes | |
| 15 | F2 | post 1lwgcii | M | M | yes | denied, then Veteran Directed Care |

Result: **15 of 15 agree on class.** Three are weak or in the wrong cell (#3, #5, #11). State: **observed**. Limit: 15 reads, one rater. The Reddit classes are easy here because denials and approvals are plainly stated; the harder question is who is speaking (V-4).

### 3d. Independent raw re-scan (not looking at labels first)

| Cell | What I did | Result |
|---|---|---|
| F2 / F3 | PCAFC or caregiver-program words near approved, denied, apply, stipend, waiting (posts and all comments) | 86 hits; 15 used as rows; 71 not used. The unused hits are mostly advice, other programs, or repeats; the first-person ones I read (for example p44jifk "5 1/2 months to get the approval") point the same way. Direction unchanged. |
| F5 | PCAFC words near sibling, secondary, backup, split, rotate | 47 hits, all about "secondary caregiver" as a family role in other posts; none describes a VA tool that assigns or tracks tasks |
| F6 | VA words near login, password, my healthevet, delegate, POA, fiduciary | 9 hits. Comment nqe7dmf: "The VA does not recognize outside POA's so if you call 1-800-827-1000 they will not be able to help you without the 21-0845." (reported). One existing row (1ehy6kb, locked out of late father's VA account). |

State: **observed**. Sources: `poolscan.py` output.

### 3e. Counts after my corrections (combined passes)

"All voices" removes V-1, V-2, V-3. "Caregiver side" also removes the 12 veteran applicants and the 2 staff voices (V-4, V-5).

| Cell | Earlier W / D / M (total) | All voices W / D / M (total) | Caregiver side W / D / M (total) |
|---|---|---|---|
| F1 | 10 / 7 / 7 (24) | 10 / 7 / 7 (24) | 10 / 7 / 7 (24) |
| F2 | 5 / 28 / 8 (41) | 5 / 27 / 8 (40) | 5 / 13 / 8 (26) |
| F3 | 7 / 6 / 8 (21) | 7 / 6 / 8 (21) | 7 / 5 / 8 (20) |
| F4 | 0 / 0 / 1 (1) | 0 / 0 / 1 (1) | 0 / 0 / 1 (1) |
| F5 | 0 / 0 / 1 (1) | 0 / 0 / 0 (0) | 0 / 0 / 0 (0) |
| F6 | 0 / 1 / 0 (1) | 0 / 1 / 0 (1) | 0 / 1 / 0 (1) |
| F8 | 3 / 4 / 1 (8) | 3 / 4 / 0 (7) | 3 / 3 / 0 (6) |
| F9 | 0 / 1 / 0 (1) | 0 / 1 / 0 (1) | 0 / 1 / 0 (1) |
| F10 | 1 / 0 / 0 (1) | 1 / 0 / 0 (1) | 1 / 0 / 0 (1) |
| Pass 1 headline | 43 (12 / 16 / 15) | 43 (12 / 16 / 15) | 43 |
| Pass 2 headline | 41 (8 / 27 / 6) | 38 (8 / 26 / 4) | 24 (8 / 12 / 4) |

The large change is in F2: 28 DID NOT WORK drops to 13 once the 12 veterans applying for themselves and 2 staff are set aside. The direction (more denials and waits than approvals) holds; the size does not. The OIG appeals audit independently shows 3% and 4% of appeals granted (documented), so the direction is also supported by a government source.

Scope flags: 5 "grandchild" and 2 "other relative" rows; 2 pass-1 rows are about a VA contract day center or VA-paid private aide agency (not a caregiver program). Vendor, promo or survey-bait scan of the full text of all counted rows: 0 true hits. State: **observed**; limit: keyword scan.

## 4. Try to disprove (Check 4)

robots.txt: `www.va.gov` general rules read (disallows only `/cgi-bin/`, `/search` and a few paths; none I used). `vaoig.gov` was read by the earlier helper; I used one search-result page. No aplaceformom.com, gao.gov or Trustpilot fetches.

| Cell | Searched | Found | Effect |
|---|---|---|---|
| F5 (earlier VERIFY) | Firecrawl "Veteran Directed Care hire family member"; saved VA pages | VA's own page: "Veterans or their representatives receive help developing a spending plan and hiring workers (which might include their own family member or neighbor)" (`va.gov/geriatrics/pages/Veteran-Directed_Care.asp`, search excerpt). VA PCAFC page (scraped earlier by the first helper and saved): the veteran can name 1 primary and "Up to 2 secondary family caregivers ... backup support"; "Eligible primary family caregivers may also receive ... A monthly stipend." The primary must be a spouse, child, parent, other relative, or someone living with the veteran. Saved VA respite page lists "adult family member" help as informal respite. | F5 is not VERIFY: the VA pays one relative and lets a veteran hire another. Nothing assigns tasks or tracks them. LIMITED. |
| F6 (earlier VERIFY, leans NO) | scraped `va.gov/health-care/manage-health/`; saved PCAFC legal and financial page | My HealtheVet lists who can manage VA health care online: veterans, and CHAMPVA spouses, dependents and survivors for their own care. No caregiver delegate is listed. The saved PCAFC page offers a "certified concierge", legal and financial planning, and attorney referrals; a person with POA or guardianship may sign the VA application. | no help getting into a parent's bank, insurance or online accounts; VA paperwork and planning only. NO for account access. |
| F6 reported | Reddit comment nqe7dmf | VA requires its own form 21-0845 for a third party | supports NO |
| F4 | saved VA dementia tips page; PGCSS flyer | tips for a dementia patient who resists bathing or medication; the veteran must agree to the caregiver | LIMITED stands, tips only |
| YES/LIMITED cells F2, F3 | looked for evidence they fail ordinary families | OIG 2018: 65% late decisions, 14% over six months; OIG 2026: appeals take about 416 days and 3% to 4% granted; AJMC: 40.5% discharged; family rows: 5 to 6 month waits, denials, stipend payments held up | confirms the Figma "strict rules" gap; confidence high |
| F8 | looked for any VA evaluation of its own coaching | none found; REACH Hope RCT is for TBI-with-dementia caregivers and is a new program, not VA's offer | stays LIMITED, low evidence |

State: **documented** for web pages (excerpt or scrape, read 2026-11-06; not saved to docs/sources because this audit may write only the AUDIT file). Limit: VA pages change often (the PCAFC page says "3 days ago" in the search result).

## 5. Corrections list (earlier files)

| # | File : line | Error | Fix |
|---|---|---|---|
| 1 | PASS2-HOWWELL.md : 45 (and PASS1 : 75) | same husband counted in both passes | remove one |
| 2 | PASS2-HOWWELL.md : 53, 107 | comment by the thread opener of post at line 77, counted as a separate report | merge |
| 3 | PASS2-HOWWELL.md : 96 | probably the same writer as line 46 | note |
| 4 | PASS2-HOWWELL.md : 8 and 11 | says veteran applicants are "still family-side reports" and rolls 12 of them into "41 new independent family or neutral reports" | split voices (caregiver, veteran, staff) |
| 5 | PASS2-HOWWELL.md : 51, 54 | staff voices counted as reports | remove |
| 6 | PASS2-HOWWELL.md : 83, 110 | advice from a paid caregiver counted as an experience | flag as weak |
| 7 | PASS2-HOWWELL.md : 127 | OIG 65% missing the "denied applications excluded" limit | add |
| 8 | PASS2-HOWWELL.md : 132 | "after an application was lost" is not the reason given in the report (incorrect eligibility finding) | fix wording |
| 9 | PASS2-HOWWELL.md : 183, 184 | thread and comment counts do not match the saved file (134 threads, 2,313 comments) | correct |
| 10 | PASS2-HOWWELL.md : 159 | "491 matched care recipients" should read "analysis sample of 491 (treated plus matched controls)" | fix |
| 11 | EVIDENCE.md : F5 and F6 rows | F5 VERIFY; F6 "leans NO" | F5 LIMITED (VDC and stipend); F6 NO for accounts, LIMITED for planning |
| 12 | EVIDENCE.md : no row for Veteran Directed Care | family posts name it and VA pays relatives through it | add (the VA page above) |
| 13 | PASS2-HOWWELL.md : F5 section | the one "F5" report is neighbors, not relatives, and not a VA feature | keep as note, not as a count |

## 6. Final verdict per cell

| Cell | Final | Conf. | Family reports W/D/M (caregiver side; all voices in brackets) | Documented evaluations | One sentence | Disagree with earlier? | Differs from Figma? |
|---|---|---|---|---|---|---|---|
| F1 Relief finder | LIMITED (enrolled veterans only; clinical criteria; local VA social worker, no address search) | medium-high | 10 / 7 / 7 | none on finding relief | The VA arranges aides and respite for enrolled veterans; about as many reports are good as bad. | no | no |
| F2 Eligibility and applications | LIMITED (70% rating for the paid program; the general program needs no application; long waits, many denials) | high | 5 / 13 / 8 (5 / 27 / 8) | VA OIG 2018; VA OIG 2026; AJMC 2022; PMC8054832 | Applying is possible, but waits run months and appeals about 416 days with 3% to 4% granted. | no | no |
| F3 Paying for relief | LIMITED (30 days free respite and a stipend in the 70% program; copay otherwise; payments often late) | high | 7 / 5 / 8 (7 / 6 / 8) | same four plus OIG 2018 (improper payments) | The VA pays for qualifying families, but approval, payment delays and copays are common. | no | no |
| F4 Refusing parent support | LIMITED (dementia tips; veteran must agree to the caregiver) | low | 0 / 0 / 1 | none | Nothing helps a veteran who refuses; one tips page for dementia resistance exists. | no | mild: Figma "No" |
| F5 Relatives cover time | LIMITED (VA pays one relative, lets the veteran name 2 backups and hire relatives through Veteran Directed Care; no tasks or schedule tool) | medium | 0 / 0 / 0 | none | The VA pays or names relatives but does not assign or track their time. | yes (was VERIFY) | differs a little: Figma "Partly: up to 2 backups" omits the paid relative and Veteran Directed Care |
| F6 Account access | NO for bank, insurance and online accounts (VA planning and referrals only; POA may sign the VA application; VA wants its own form for a third party) | medium | 0 / 1 / 0 | none | The VA helps plan and refer; it does not get a caregiver into accounts. | yes (was VERIFY, leans NO) | differs: Figma "Partly: legal and financial planning and a monthly payment" |
| F8 Personal guidance | LIMITED (4 coach calls in REACH VA; Health and Wellbeing coaching at some sites; local team) | medium-low | 3 / 3 / 1 (3 / 4 / 0) | REACH cost study 2017; REACH Hope RCT 2025 (new program); OIG 2018 (monitoring gaps) | A coach exists for veterans' families; reports of calls not returned and a forward to a social worker. | no | no |
| F9 Behavior and hard-talk help | LIMITED (dementia tips page, texting and video series; S.A.V.E. suicide-talk training) | low | 0 / 1 / 0 | REACH cost study; REACH Hope RCT; HSRD brief 470 | VA teaches behavior and one hard talk, for veterans' families only, with almost no family feedback. | no | no |
| F10 People who understand | LIMITED (peer mentoring, REACH VA group sessions, support groups; veterans' families only) | low | 1 / 0 / 0 | REACH VA in AI/AN communities (implementation only) | Peer help exists but only one family said so. | no | no |

State: verdicts are **inferred** from documented and reported evidence; counts are **proven** arithmetic on **reported** rows. Disagreements with earlier helpers: F5, F6. Disagreements on counts: F2 (28 D becomes 13 D on the caregiver side), F5, F8, pass-2 headline (41 becomes 38 or 24). Evidence differs from Figma: F5, F6 (and F4 mildly).

## 7. Not checked

- Who is speaking in each Reddit post (no usernames); "veteran applicant" labels come from the earlier helper and I confirmed only some by reading.
- VA data on actual approval and denial rates (Reddit figures like "80% denied" and "4%" are unverified and not used).
- The PGCSS and REACH VA coach programs have no evaluation I could find.
- GAO reports (gao.gov blocked by instruction) and OIG reports 20-00178 and 22-02064-155.
- The VDC page, My HealtheVet page and PCAFC stipend text were read as search excerpts or a one-page scrape on 2026-11-06 and not saved to docs/sources.
- Whether Veteran Directed Care is available in the family's area (it is local) and whether a spouse can be hired.
- Skills: skeptical-audit applied. All code, UI, security and release skills judged not relevant (no code or UI reviewed).
