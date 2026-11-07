# AUDIT PASS 3: Respite and adult day services

Date: 2026-11-06. Independent auditor. Nothing was committed or edited. Evidence states: **proven** (a check that could fail ran and passed), **observed** (I saw it this session), **inferred** (follows from observed facts), **documented** (a government or published source says it), **reported** (a person said it, not verified), **not-assessed**.

Scripts are in the session scratchpad `/private/tmp/claude-501/-Users-landodoom-Desktop-AI-Developer-Residency--caregiving-coordinator/88c39ed8-fc0d-46c0-b385-032bd23092de/scratchpad/` (`qcheck.py`, `rows.py`, `uniq.py`, `blind.py`, `dups.py`, `poolscan.py`, `flags.py`, `pg.py`). Run with `python3 file.py` (not `-I`).

## 1. Quote and source check (Check 1)

Method: every table row with a quoted cell was matched to its cited source (file, Reddit post id, comment id), curly quotes, HTML entities and spaces were normalized, and I tested that the exact words are inside that source. Post id, comment id and forum URL id mismatches were also flagged.

State: **proven** for the exact-words test. Limit: it proves the words exist in the saved copy, not that the poster is honest or the class label is right.

| File | Quote rows checked | Misses |
|---|---|---|
| EVIDENCE.md | 14 | 0 |
| PASS1-HOWWELL.md | 80 | 0 |
| PASS2-HOWWELL.md | 62 | 0 |
| Total | 156 | 0 |

Extra: 0 quotes are over 20 words; 0 id mismatches across all 321 PASS rows of the three programs. Sanity test: changing one word or one post id made the script report a miss.

Result: **0 quote errors.**

## 2. Documented evaluation check (Check 2)

`PASS2-doc-acl-nfcsp-outcome-evaluation-2018.txt` and `PASS2-doc-acl-nfcsp-process-evaluation-lewin-slides.txt` here are byte-identical to the copies in the Area Agencies folder (`cmp` printed no difference, state **proven**). I checked every number in them; results are in `area-agencies-on-aging/AUDIT-PASS3.md` section 2: all numbers and pages are right, with one overstatement (below). The four other documents:

| Document and cited number | Found? | Page cited | Verdict |
|---|---|---|---|
| ACL outcome 2018: burden -0.095 vs +0.145 (line 148) | numbers yes | p. xix, PDF 19 | **Error C2-1:** report says the difference "was not statistically significant" (p. 8-7, PDF 97; p. 8-8, PDF 98). Line 148 omits it. |
| ACL outcome 2018: limit "mainly in-home respite" (line 152) | yes: "mainly in their home" p. xviii | n/a | correct |
| DaSH 2014 abstract: 173 caregivers, 8 daily interviews, fewer care stressors, more positive experiences, less anger | yes | abstract | correct but incomplete: the abstract also says caregivers had "more noncare stressors" on adult day days; PASS2 line 157 omits that |
| Cochrane (Maayan 2014 version): 4 trials, 753 participants, very low quality, no significant effects | yes | abstract | correct; omits that respite did worse than polarity therapy on perceived stress (n=38). Date "2014 version" is right (the saved record says 2014). |
| Zarit 2017 methods abstract | yes | abstract | correct |
| Frontiers in Health Services 2025 (Utz et al.): disruption led to isolation and stress; personal networks gave informal respite; respite linked to better wellbeing but caregivers hesitant | yes | abstract | correct. Published 25 July 2025, data 2019 to 2024. PASS2 says "abstract and headings only"; the saved file holds the full text. |

Report dates: none looks wrong for today (2026-11-06). All are old or small: DaSH and Cochrane 2014, Zarit 2017, ACL 2018, Lewin 2015 data.

State: **observed**. Limit: abstracts only for three papers (as PASS2 says); PMC blocked further requests.

## 3. Recount (Check 3)

### 3a. Arithmetic recount from the saved rows

| Test | Result | State |
|---|---|---|
| Per-cell W / D / M rebuilt from rows vs tables in section (a), both passes | all 30 cell-pass counts match | proven (`rows.py`) |
| Pass 1 headline "65 unique (6 / 48 / 11)" | 65 distinct quotes, 6 / 48 / 11, matches | proven |
| Pass 2 headline "50 unique (23 / 21 / 6)" | 56 distinct quotes minus 6 flagged "same writer" = 50, 23 / 21 / 6, matches | proven |
| Same source or text in both passes | none by id, quote, or 8-word shingle test | proven |

### 3b. Problems the files did not flag

| ID | File : line | What | Effect |
|---|---|---|---|
| R-1 | PASS1 : 127 (F5 "None found") | Raw scan finds relatives covering time in at least 4 saved posts: 1t2ley3 (mother's sibling gives respite when parents travel; W), 1xhv1fc (sister pays for the adult day program, mother goes 3 days; W), 1v0i2br (siblings rotate "weeks" and argue in a group chat; M), 1g1q8i5 (older sister live-in, other sister once a week, respite 2 x 4 hours; M). | F5 count is 0 in pass 1; at least 4 exist. They show families do this by hand with no respite-program tool. |
| R-2 | PASS1 : 44, 49, 85 | Ontario family (1uaypm6: "Ontario Health at Home") and a "PSW"/"government subsidised" family (1wnm7mw, Canada or Australia, inferred) are counted. The Figma audience is US. | remove from F1, F3 (-1 M, -1 D in F1; -1 D in F3) |
| R-3 | PASS1 : 54, 69, 70, 122 | Four reports are about disability programs for an adult sibling (autism regional center; Down syndrome day program; two about an adult sister with intellectual disability and Medicaid waivers): 1jbos7w, 1ulutf3, 1x8maxn, 1ea6sbh. They are not Audience 1 or 2. | remove (-1 D F1, -2 D F2, -1 D F4) |
| R-4 | PASS1 : 114 | 1pjz76s: a 20-year-old caring for a dying 42-year-old father with a "support worker" (likely outside the US; not an elder). | remove (-1 D F4) |
| R-5 | PASS2 : 45, 46, 47 | Three F1 rows are not first-hand use: line 45 "did not use the program; infection fear", line 46 "everyone that I know ... have loved it", line 47 "I know many people ... some not so much". | remove (-1 W, -1 D, -1 M in F1) |
| R-6 | PASS2 : 86 | "The cost is $50.00 for 4 hours" (Nojoy3) classed MIXED; the same writer says "It's been very positive" and the thread calls it "very affordable". | W in F3 |
| R-7 | PASS2 : 42 and 132 | Username Grandma1954 appears in two threads (427236 "used the same place for respite", 486582 "asked not to bring him back"). Likely one person and one husband counted as two reports. | state **inferred**; probable -1 unique report |
| R-8 | PASS2 : 95 (comment n88kibl) and AAA PASS2 | "respite scholarship from my county's Department on Aging" is counted here and could be counted in the AAA folder. The row's note admits it. | do not add the two programs' counts |
| R-9 | PASS1 section (c), F4 | The F4 filter had 42 hits, 35 read; the other 7 were "not read". My own scan (below) found at least 5 valid refusal reports that were not used. | F4 DID NOT WORK is undercounted by about 5 |

### 3c. Blind re-reading: 15 random reports (seed 12)

Method: `blind.py respite-adult-day 12 15`, quote plus about 500 characters each side, no class shown.

| # | Cell | Source | My class | Earlier | Agree? | Note |
|---|---|---|---|---|---|---|
| 1 | F3 | comment kshhpga | W | W | yes | "awarded a grant"; aide then no-showed |
| 2 | F4 | post 141n3zy | D | D | yes | |
| 3 | F5 | comment 19rwapzp | W | W | yes | |
| 4 | F1 | forum 185938 jeannegibbs | W | W | yes | |
| 5 | F3 | post 199f9t2 | D | D | yes | |
| 6 | F1 | comment kshhpga | D | D | yes | |
| 7 | F1 | post 1vgm6un | W | W | yes | hospice respite |
| 8 | F1 | comment nocpk9d | D | D | yes | |
| 9 | F3 | comment nlqa7au | D | D | yes | writer is a paid caregiver who cannot afford to stop |
| 10 | F4 | post 1pa6ff2 | D | D | yes | |
| 11 | F3 | forum 185938 Nojoy3 | W | M | NO | see R-6 |
| 12 | F4 | post 1nzrvux | D | D | yes | |
| 13 | F1 | post 1kuag4c | W (weak) | W | yes | only a search, no use yet |
| 14 | F3 | post 1wnm7mw | D | D | yes | non-US (R-2) |
| 15 | F1 | comment mmbxba2 | D (mild M) | D | yes | |

Result: **14 of 15 agree; 1 disagrees (#11).** One more is out of scope (#14). State: **observed**. Limit: 15 reads, one rater.

### 3d. Independent raw re-scan (not looking at labels first)

| Cell | What I did | Result |
|---|---|---|
| F4 | respite or day-program words within 110 characters of refuse, doesn't want, hates | 45 hits, 23 used as rows, 22 not used. Of the unused, at least 5 are valid first-person refusals: 17m966i, 17xy9oq, 1d8qcrh, 1gfz22e, 1uu1436 (all D). F4 is undercounted; direction unchanged. |
| F5 | respite words near sibling, brother, sister, my son, my daughter with a "takes, watches, covers, stays" verb | 13 hits; 4 valid (R-1) |
| F1 / F3 | forum thread 427236 read comment by comment | I also find anonymous281721 ("weekday daycare through our local Council on Aging ... excellent care", W) not counted, and cwillie (Canada, government home care) correctly not counted |
| F2 | read the 7 pass-1 rows in full context | 2 are intellectual-disability waiver cases (R-3); the rest hold up |

State: **observed**. Source: `poolscan.py`, `blind.py`, `forum.py`.

### 3e. Counts after my corrections (combined passes)

Adjusted = removals R-2 to R-5, R-6 class change, adds R-1 (F5, tentative from 700-character windows) and anonymous281721. The F4 undercount is shown separately.

| Cell | Earlier W / D / M (total) | Adjusted W / D / M (total) |
|---|---|---|
| F1 | 21 / 26 / 8 (55) | 21 / 23 / 6 (50) |
| F2 | 3 / 3 / 3 (9) | 3 / 1 / 3 (7) |
| F3 | 5 / 18 / 8 (31) | 6 / 17 / 7 (30) |
| F4 | 4 / 24 / 3 (31) | 4 / 22 / 3 (29); plus about 5 missed D = 4 / 27 / 3 (34) |
| F5 | 2 / 1 / 0 (3) | 4 / 1 / 2 (7) |
| F6 | 0 | 0 |
| F8 | 1 / 3 / 1 (5) | 1 / 3 / 1 (5) |
| F9 | 0 / 6 / 1 (7) | 0 / 6 / 1 (7) |
| F10 | 1 / 0 / 0 (1) | 1 / 0 / 0 (1) (same post as an F1 row) |
| Pass 1 headline | 65 (6 / 48 / 11) | 58 (6 / 42 / 10) |
| Pass 2 headline | 50 (23 / 21 / 6) | 47 (22 / 20 / 5) |

Scope flags: 11 rows are labeled "unclear (grandchild)" or "other relative"; 4 of those are the disability cases above. Vendor, promo or survey-bait scan of the full text of all counted rows: 0 true hits (the match on "our app" was the word "application"). State: **observed**; limit: keyword scan.

## 4. Try to disprove (Check 4)

robots.txt: read for `aging.ny.gov` and `www.ncdhhs.gov` (general agents allowed). No aplaceformom.com, gao.gov or Trustpilot fetches.

| Cell | Searched | Found | Effect |
|---|---|---|---|
| F5 (earlier "LIMITED, owner decides") | saved ARCH pages; Firecrawl "respite voucher family member paid relative timesheet" | Saved ARCH page "How do I get paid to be a family caregiver" lists Structured Family Caregiving and adult foster care by relatives. Alabama and New York vouchers can pay a relative (EVIDENCE.md quotes verified). Rules differ: NC voucher may pay "any worker" who does not live in the home and is not POA or guardian (`ncdhhs.gov/divisions/aging/nc-lifespan-respite-program`, search excerpt); South Carolina's voucher cannot pay a family member living in the home (`screspitecoalition.org/programs-services/respite-voucher-program/`, search excerpt); Arizona excludes spouse, child, parent (`des.az.gov`, search excerpt); NY memo: "Family members may be hired as respite providers" but not the primary caregiver. | LIMITED stands: a relative can be paid in some states; no scheduling or tracking tool |
| F6 | saved pages; no web search needed (account access is not a respite service) | nothing | NO, inferred |
| F10 | saved ARCH pages and Alzheimer's Association adult day page; reddit F10 row | one post: a day center "offers a support group for caregivers" | stays VERIFY, thin |
| F4 (NO) | tried to find any respite page with a script or helper for a refusing parent | The Alzheimer's Association page has a tip to try twice a week for a month; 4 family reports describe tricks that worked ("giving him the agency around it", a story to get her to go) | NO stands: tips only, no feature; the successful tricks were the families' own |
| YES cells (F1 finder, F3 cost info) | looked for evidence they fail ordinary families | F1: families report waits, 2 to 4 week minimums, $225 a day, hours that clash with work; Lewin slide 45: 41% of AAAs meet respite needs; ACL p. xviii: a third did not know the service existed. F3: cost reports run $50 for 4 hours to $5,900 for 20 days; ACL/Lewin show funding is the top unmet reason | information is available but money and slots are not; both downgraded in confidence |

State: **documented** for web pages (excerpts or saved pages, read 2026-11-06; not saved to docs/sources because this audit may write only the AUDIT file). Limit: excerpts for the four state pages.

## 5. Corrections list (earlier files)

| # | File : line | Error | Fix |
|---|---|---|---|
| 1 | PASS2-HOWWELL.md : 148 | burden drop given without "not statistically significant" (ACL p. 8-7, 8-8; PDF 97, 98) | add the caveat |
| 2 | PASS1-HOWWELL.md : 127 | F5 "None found" but 4 relative-cover posts exist | list them (R-1) |
| 3 | PASS1-HOWWELL.md : 44, 49, 85 | Ontario and PSW/subsidised (non-US) posters counted | remove or label non-US |
| 4 | PASS1-HOWWELL.md : 54, 69, 70, 122 | disability-sibling cases counted as respite reports | remove (R-3) |
| 5 | PASS1-HOWWELL.md : 114 | non-elder, likely non-US case counted in F4 | remove |
| 6 | PASS2-HOWWELL.md : 45, 46, 47 | second-hand or non-user statements counted as reports | remove from counts |
| 7 | PASS2-HOWWELL.md : 86 | MIXED should be WORKED | change |
| 8 | PASS2-HOWWELL.md : 42, 132 | same username in two threads counted as two reports | note or merge |
| 9 | PASS2-HOWWELL.md : 157 | DaSH "more noncare stressors" omitted | add |
| 10 | PASS2-HOWWELL.md : 163 | Cochrane polarity-therapy comparison omitted | add |
| 11 | PASS1-HOWWELL.md : section (c) F4 | 7 F4 hits "not read"; at least 5 were valid refusals | read and add |
| 12 | EVIDENCE.md : F10 row | "VERIFY; no source shows caregivers meet each other through respite" is true of saved pages; one family post says a center offers a caregiver group | keep VERIFY, cite the post |

## 6. Final verdict per cell

| Cell | Final | Conf. | Family reports W/D/M | Documented evaluations | One sentence | Disagree with earlier? | Differs from Figma? |
|---|---|---|---|---|---|---|---|
| F1 Relief finder | YES for finding (ARCH respite locator, adult day listings); LIMITED for getting a slot (waits, minimums, hours) | medium | 21 / 23 / 6 | DaSH 2014 (less stress on adult day days); Cochrane 2014 (no proven benefit, very low evidence); ACL 2018; Lewin 2015 | Families can find providers; many cannot get a slot they can pay for. | no | no, Figma "Yes, when families can get it" |
| F2 Eligibility and applications | LIMITED (state vouchers differ; Colorado closed; some need a referring agency) | medium | 3 / 1 / 3 | none | Each state has its own rules, and the money can run out. | no | no |
| F3 Paying for relief | YES for learning cost and who pays (ARCH how-to-pay, sliding scales, hospice 5%); LIMITED for actual money | medium | 6 / 17 / 7 | Lewin (funding top reason unmet); Cochrane | Information is good; families still report $225 a day and up. | no | no (Figma says relief is real but costs too much) |
| F4 Refusing parent support | NO (tips only, no helper or script) | medium-high | 4 / 22 / 3 (about 4 / 27 / 3 with missed reports) | none | The one-month-trial tip exists; no feature helps a parent who says no. | no | no |
| F5 Relatives cover time | LIMITED (some state vouchers pay a relative and need a signed timesheet; no scheduling or task tracking) | medium | 4 / 1 / 2 (tentative) | Frontiers 2025 (informal respite from networks); ACL (83% get family help) | A payment rule exists in some states; families split time by hand. | no | differs: Figma "No" |
| F6 Account access | NO | medium | 0 / 0 / 0 | none | Respite does not touch accounts and the application adds paperwork. | n/a (not assessed before) | no |
| F8 Personal guidance | LIMITED (Connecticut care manager; some day centers offer counseling; hospice social worker) | low | 1 / 3 / 1 | ACL 2018 (indirect) | Some one-to-one help exists but it is not a coach. | no | no |
| F9 Behavior and hard talks help | LIMITED for behavior (staff at some centers; some centers expel) ; VERIFY for hard talks | low | 0 / 6 / 1 | none | Behavior can get a person sent home as well as helped. | no | no |
| F10 People who understand | VERIFY (one report of a center with a caregiver group) | low | 1 / 0 / 0 | Frontiers 2025; DaSH (not about peers) | No source shows respite connects caregivers to each other. | no | no, Figma does not list it for this program |

State: verdicts are **inferred** from documented and reported evidence; counts are **proven** arithmetic on **reported** rows. Disagreements with earlier helpers: none on verdicts. Disagreements on counts: F1, F2, F3, F4, F5. Evidence differs from Figma: F5.

## 7. Not checked

- Whether any Reddit or forum writer is who they say; usernames were not saved on Reddit.
- Most Reddit replies (only 45 threads were fetched).
- The unused F1, F3 and F9 hits were not re-read in full; F4 and F5 were re-scanned.
- The NC, SC and AZ voucher pages were read as search excerpts, not full pages; the NY memo as an excerpt.
- Adult day center satisfaction surveys (no national source found).
- Full text of DaSH, Cochrane and Zarit 2017.
- GAO and state auditor reports (blocked or unreachable).
- Skills: skeptical-audit applied. All code, UI, security and release skills judged not relevant (no code or UI reviewed).
