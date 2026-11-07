# Geriatric care managers (Aging Life Care): independent audit, pass 3 (2026-11-06)

Auditor: a fresh reviewer who did none of the earlier work. Goal: try to prove the earlier files wrong.
Files audited: `EVIDENCE.md`, `PASS1-HOWWELL.md`, `PASS2-HOWWELL.md` in this folder.
Paths are under `docs/sources/` unless they start with `feature-analysis-4/`.

Care managers are many small local firms, not one product. A report is about one firm. Whether a firm is a member of the Aging Life Care Association (ALCA) is unknown for almost all reports. I did not open `aginglifecare.org` (owner rule and its robots.txt).

Conflicts I keep in view:
- AgingCare is owned by A Place for Mom. Three forum threads (20 of the 43 new reports) come from it.
- Solace sells a rival service; its article is marketing.
- KFF Health News quotes people the writer chose; the ALCA survey in it was paid for by ALCA.
- Some Reddit comments name a business and a website (possible promotion).

Evidence states: proven, observed (I saw it myself), inferred, documented (an organization says it), reported (a person said it), not-assessed.

## Short answer (plain English)

- Quotes: no made-up quotes. All Reddit, forum and news quotes in the three files are in the cited saved files. Two quotes are cited to the wrong file.
- Counts: the arithmetic is right (43 new + 14 pass 1 = 57 as written). But 3 of the 15 reports I re-read blind carry a wrong cell label, and 6 cell labels in the F4, F5, F6, F10 rows do not match what the cell means. That changes the verdicts.
- Biggest changes: F5 "Yes" becomes LIMITED (a paid stand-in is not a relative who helps). F10 "2 WORKED" becomes 0 (a counselor is not peers). F6 gets a real report that the Figma line was based on, which `EVIDENCE.md` says it could not find.
- 12 corrections are listed with file and line.

## Check 1: do the quotes exist in the cited files?

Command (script in `cariloop/AUDIT-PASS3.md`, Appendix A): `python3 -I quotecheck.py aging-life-care/{EVIDENCE,PASS1-HOWWELL,PASS2-HOWWELL}.md`.

| File | Quotes tested | Found | Not found by script | After hand checks |
|---|---|---|---|---|
| EVIDENCE.md | 14 | 13 | 1 ("Share the Care") | Found, but in the Retirement Living Source Book file, not the Solace file the row cites. Mis-cite. |
| PASS1-HOWWELL.md | 32 | 27 | 5 | 1 is a cut-off fragment from my parser; 4 are phrases inside the same rows ("billed $3,202 in 2 weeks", "access her bank accounts", etc.). I found each in `posts_targeted.jsonl` or `posts.jsonl` by hand. 0 true misses. |
| PASS2-HOWWELL.md | 48 | 44 | 4 | 1 search string; 3 KFF phrases ("Deal with insurers, including Medicare and Medicaid", "an online Medicaid recertification form", "mediating between family members"): all found in `PASS2-kff-health-news-aging-life-care-managers-2026-10-14.txt`. |

- State: observed. Limit: proves the words are in the saved file, not that it matches the live page.
- Fabricated quotes: 0. Over 20 words: 0.
- Other facts re-checked: AARP live search excerpt (2026-11-06) still lists "Arranging for relief or respite care for stressed-out caregivers." and "Identifying social services and programs that could help the care recipient." (observed: search excerpt of `https://www.aarp.org/caregiving/basics/geriatric-care-manager/`). Cost: KFF "$150 to $350", AARP "$150 to $300", NIA says Medicare and Medicaid do not pay for care managers.

## Check 2: recount, blind reclassification, double counting

### 2a. Arithmetic (script `apfm_parse.py`, parse function reused on PASS2 rows G01 to G43)

Re-added all 43 rows by cell: `F1 9 W/1 M; F2 4 W/1 M; F3 5 W/1 D/2 M; F4 3 W/2 D; F5 4 W; F6 2 W; F8 29 W/4 D/2 M; F9 1 W/1 D; F10 2 W`, no duplicate comment IDs, no reply chains between counted comments (`chains.py`). All match PASS2 lines 20 to 30. By source: 21 Reddit (G01 to G21), 20 AgingCare forum (G22 to G41), 2 news (G42, G43). State: proven (script). Limit: proves the table matches the rows, not that the rows are right.

Pass 1 arithmetic: the F8 row (3 W, 3 D, 2 M, 1 no verdict) matches its 9 table rows.

### 2b. Blind reclassification: all 21 Reddit reports, the 20 forum reports, and a random 15

I printed each raw Reddit comment around the care-manager words with the earlier labels hidden, and read the three saved AgingCare threads in full. Limit: I had read the tables first, so I was not fully blind.

Random sample (seed 3, Python `random.sample` over all 43 IDs): G01, G05, G09, G13, G15, G16, G17, G18, G23, G24, G31, G35, G38, G42, G43.

| ID | My class and cells from raw text | Earlier | Agree? |
|---|---|---|---|
| G01 | F2 WORKED (assessment helped doctors' statements); F1 WORKED (agency found assisted living); F6: the POA step, not an account login | F2, F6, F1 WORKED | Agree on F2 and F1. F6 is not the F6 cell (account access); at most partial. |
| G05 | WORKED, but the person is an RN from a private home health agency who "acts as her case manager". Not a geriatric care manager. | F8 WORKED | Disagree on inclusion |
| G09 | F5 partly (got the family to accept the situation); F4 no: the family members who denied it were relatives, not a parent who refuses help | F5 W, F4 W | Disagree on F4 |
| G13 | F8 WORKED | same | Agree |
| G15 | F8 WORKED; F1 WORKED (agency with a licensed social worker helped land a bed) | same | Agree |
| G16 | F8 WORKED | same | Agree |
| G17 | F8 WORKED; F3 no verdict (bills quoted) | same | Agree |
| G18 | F8 WORKED | same | Agree |
| G23 | F8 WORKED. F5: a paid "concierge sibling" stands in for a missing sibling; it does not get a relative to act. | F8, F5 WORKED | Disagree on F5 |
| G24 | F8 WORKED | same | Agree |
| G31 | F8 WORKED; F6: forwards the brother's mail; the helper's own limit says she does not log into accounts | F8, F6 WORKED | Disagree on F6 |
| G35 | F3 WORKED (recommended free services); F1 WORKED | same | Agree |
| G38 | F8 WORKED; F10: "like a counselor", and she had been through the same with her mother. That is a professional, not peers or a support group. | F8, F10 WORKED | Disagree on F10 |
| G42 | WORKED (news column; person chosen by the writer) | same | Agree |
| G43 | WORKED (columnist's own experience) | same | Agree |

Result: 6 of 15 reports have a cell label I disagree with (G01-F6, G05 inclusion, G09-F4, G23-F5, G31-F6, G38-F10). Zero class flips among the 15 (all agree on WORKED).

Full read (all 43), additional disagreements:
- G04 (F5 WORKED), G19 (F5 WORKED): paid stand-ins ("eyes and ears", "basically me in my absence"), not relatives. F5 label wrong.
- G33 (F10 WORKED): "a helping sounding board for me" with a professional. Not peers. F10 label wrong. The helper's own text says "Peer support groups are a separate thing", then counts it anyway.
- G20 (F8 WORKED): the writer names a person and her business with a website ("AgeWell Options") and adds "Feel free to DM questions". Same pattern the helpers used to exclude the "Arosa" comments. Possible promotion (inferred from wording). Excluding it is consistent.
- G27 (F8 WORKED): the person who hired the manager is the 87-year-old care receiver, not a family caregiver (the row says "other"). Counted as a report. Flag.
- G22 (F8, F1 WORKED): an assessment only; no relief arranged. F1 label weak.
- G25 (F3 WORKED): quote is a contract term ("only pay for the hours actually used"), not an outcome. Weak.
- G28 (F4 WORKED): the father was "combative", not refusing help. F9 fits; F4 is a stretch.
- G07 (F8, F4 WORKED): text read is partial; the person had refused help earlier and a hospital stay was used to set up a plan. Plausible F4.
- G21 (F8 DID NOT WORK): the company sent aides and is "not an Aging Life Care firm" (helper note). Consider excluding from a care-manager count.
- Not counted but fine: second-hand reports, vendors, staff, advice-only.

Pass 1 families, my read of the raw posts (`posts.jsonl`, `posts_targeted.jsonl`):
- "14 families": p1er9pkg and p1d98a7r are probably the same writer (same mother, assisted living, 2024; the helper says "may be same author"). That makes 13.
- p1x4gtt9 ("Geriatric Caregiver... more paperwork than help"): not clearly a care manager; the helper marked "inferred".
- p1x0fqwe: the firm is "Blue Ridge Eldercare Advisors", a fiduciary firm, not shown to be a care manager firm (helper says so). But its text says "one of the BRE representatives took my mother to sign a Power of Attorney and Advanced Medical Directive without telling me beforehand" (observed, `posts_targeted.jsonl`, 8,772 characters). That is exactly the Figma F6 line "One took power of attorney without telling the family". `EVIDENCE.md` line 30 says that story was "not in the files I read" and "I did not find that story again". Wrong: PASS1 in the same folder found it (line 46).
- p1mxef8i, p1meut37, p1mht9jt: one family counted once. Correct.
- p1p1nazq ("the care manager"): unclear if a private manager or a clinic one (helper flagged). p1viweky: the post is mostly about a doctor.
- p1xgwk7r ("every option on the table was just more and more work"): vague; weak DID NOT WORK.

### 2c. Double counting, vendor, staff, promo, survey-bait

- Same comment counted twice: none. Same person across rows: none provable (no usernames). Reply chains between counted comments: none.
- The saved AgingCare file for thread 489163 says G11 was "counted as a report with limit". PASS2 line 85 and the count (8 of 19 answers) show it was not counted. The text file's own note is wrong, the count is right.
- Vendors and promo: Arosa comments excluded (consistent). G20 counted though it looks like a plug (see above).
- Care managers speaking about their own work were excluded (correct).
- Survey-bait: none. The ALCA survey (about 200 respondents; 93% say benefits outweighed costs; 99% would recommend) is documented in the KFF article as commissioned by ALCA and not representative; the helpers correctly did not count it as a report.

### 2d. My corrected counts

| Cell | Earlier combined (W/D/M) | Corrected (W/D/M) | Why |
|---|---|---|---|
| F1 | 9 / 0 / 1 | 9 / 0 / 1 (2 weak: G12, G22) | No change. Respite: 0 reports; adult day: 0. |
| F2 | 4 / 1 / 1 | 4 / 1 / 1 | No change (G03, G11, G36 W; G02 M; p16jpagx D is one line). |
| F3 | 5 / 2 / 3 | 5 / 2 / 3 (G25 weak) | No change |
| F4 | 5 / 2 / 0 | 4 / 2 / 0 | Removed G09 (family accepting, not a refusing parent) |
| F5 (relatives) | 4 / 1 / 1 | 1 / 1 / 1 | G09 W (family accepted); p1sl9uat D; the stepfather family M. G04, G19, G23 are paid stand-ins, not F5 |
| F6 (accounts) | 2 / 1 / 0 | 0 / 1 / 0, plus 2 partial (G01 POA step, G31 mail) | No report of a login. p1x0fqwe is a fiduciary firm |
| F8 | 32 / 7 / 4 | 30 / 7 / 4 | Removed G05 (not a care manager) and G20 (possible promo) |
| F9 | 1 / 1 / 0 | 1 / 1 / 0 | No change (G28 W, G37 D) |
| F10 | 2 / 0 / 0 | 0 / 0 / 0 | G33 and G38 are professional counselors, not peers |

Counts re-derived blind for 4 or more cells: F1, F2, F5, F8, F10 above (each re-added from raw text, with the changes listed).

## Check 3: try to disprove

### 3a. Searches I ran (2026-11-06; excluded: aginglifecare.org, aplaceformom.com, Trustpilot, bbb.org, yelp, glassdoor, indeed, usatoday, yespress)

| Search | Result |
|---|---|
| Firecrawl: "geriatric care manager what they do apply Medicaid application VA benefits respite care arrange family caregiver fees" | 10 results. AARP excerpt (observed): care managers "generally serve clients and families whose incomes are too high to qualify for publicly financed services"; "Neither Medicare nor Medicaid typically pays for care management services"; "Employee assistance programs may cover some care management fees"; services include "Identifying social services and programs", "Arranging for relief or respite care". A Pennsylvania agency page shows Area Agencies on Aging also assign a "care manager" to each caregiver in a caregiver support program (the page does not state a price). No source says a private care manager files applications as a standard service. |
| Firecrawl: "geriatric care manager not worth it complaints billing no plan hired care manager bad experience caregiver forum" (Reddit and AgingCare excluded) | 10 results: NIA ("Geriatric care managers charge by the hour. Medicare and Medicaid do not pay for this service."), AARP, US News, KFF, a vendor (Arosa) page, directories. No new family complaint source. |
| Re-read of the saved raw threads for "refus", "bank", "login", "support group" | The only refusal reports are G34 and G36 (fails) and G07 (works). No login report. No peer support group report. |

State: observed (search excerpts); limit: excerpts, not full pages; no new first-person reports found.

### 3b. Cells with a YES-like earlier verdict: evidence it does not work or does not reach an ordinary caregiver

- Cost and reach: families report $60 to $175 an hour (G26 $60, G32 $125, H2 $155, H1 $175); ALCA members $150 to $350 (KFF); the Figma "$150 to $300" is the older AARP range. Complaints: $3,202 in 2 weeks (p1x0fqwe, fiduciary firm), $15-20k a month with aides (G08), "he was expensive" (G30, ended the contract). Medicare and Medicaid do not pay. AARP: aimed at families "whose incomes are too high to qualify for publicly financed services". So "for a fee" is a real limit.
- F4: fails when a parent will not accept a stranger (G34: "my parents just did not get the concept") or when the caregiver will not accept help (G36). Works when the person is more willing to listen to the manager (G28, KFF K4 claim by a care manager).
- F5: p1sl9uat (brother refused the manager's calls) and the stepfather family: the manager could not make a relative help.
- F9: G37 "a waste of money" (husband kicked out of nursing homes).
- F8: G08, G14, G21 (quality of aides or the manager).
- Local reach: care managers are local firms; one reporter used two states and the second "gave only a list" (G06). Availability near the parent is not guaranteed (inferred).

### 3c. Cells with a NO or VERIFY earlier verdict: search for any evidence they DO offer it

- F6: AARP and KFF mention "Deal with insurers, including Medicare and Medicaid" and the KFF reporter's care manager "completing an online Medicaid recertification form for a client". That is an online account task done for a client. Also "Some Care Managers can be the Power of Attorney" (Private Home Care page, documented). Reports: G01 (POA step), G31 (mail forwarding), p1x0fqwe (a fiduciary firm took POA without telling the family). So some care managers act under POA and handle online forms and mail, but I found no report of helping a caregiver log in to a parent's account. LIMITED, low.
- F10: Retirement Living Source Book speaker: "Ask them about local dementia caregiver support groups, too" (advice to ask, documented, in the saved file). No firm says it connects people to groups. No report. VERIFY, leaning NO.
- F2: documented: KFF "Deal with insurers, including Medicare and Medicaid"; reports G01, G03, G11, G36 W. Not shown: filing a first Medicaid application end to end. LIMITED.

## Corrections list (errors in the earlier files)

| # | File and line | Error | Fix |
|---|---|---|---|
| G-1 | `EVIDENCE.md` line 30 | Says the Figma F6 story ("one took power of attorney without telling the family") was not found. `PASS1-HOWWELL.md` line 46 (p1x0fqwe) has it, and the post says the representative "took my mother to sign a Power of Attorney... without telling me beforehand". Caveat: the firm is a fiduciary adviser, not shown to be a care manager. | Update the note and keep the caveat. |
| G-2 | `EVIDENCE.md` line 15 (F5 row) | The quote "Share the Care" is in the Retirement Living Source Book file, not the Solace file the row cites. | Fix the citation. |
| G-3 | `PASS2-HOWWELL.md` lines 26, 115 (F5 "Yes", 4 W) | G04, G19, G23 are paid stand-ins, not relatives. Only G09 touches relatives. Summary says "The manager stands in for the missing relative", which is not what F5 asks. | F5 becomes LIMITED; counts 1 / 1 / 1. |
| G-4 | `PASS2-HOWWELL.md` lines 30, 70, 75, 112 (F10 W 2: G33, G38) | A counselor or sounding board is not peers or a support group. | F10 counts become 0. |
| G-5 | `PASS2-HOWWELL.md` lines 27, 60, 68, 111 (F6 W 2: G01, G31) | POA activation and mail forwarding are not account access. The row's own limit says so. | Show as "partial", not WORKED. |
| G-6 | `PASS2-HOWWELL.md` line 46 (G09 F4 WORKED) | The people who denied the problem were relatives. | Remove F4 from G09. |
| G-7 | `PASS2-HOWWELL.md` line 42 (G05) | Not a care manager (private home-health RN case manager). The row says "not shown to be an Aging Life Care member" but still counts it. | Remove from F8 or mark "RN case manager". |
| G-8 | `PASS2-HOWWELL.md` line 57 (G20) | Names a business and a website and invites DMs. Looks like a plug; counted, while similar "Arosa" comments were excluded. | Exclude or flag consistently. |
| G-9 | `PASS2-HOWWELL.md` line 64 (G27) | Care receiver, not a family caregiver. | Flag in the Limit or exclude. |
| G-10 | `PASS1-HOWWELL.md` line 7 ("14 families") | p1er9pkg and p1d98a7r probably one writer. | 13 families (inferred). |
| G-11 | `PASS2-agingcare-forum-question-489163-gcm-worth-it-2026-11-06.txt`, entry G11 note | Says "counted as a report with limit". It was not counted. | Fix the note. |
| G-12 | `EVIDENCE.md` line 11 (F3 row) and Figma "$150 to $300" | The $150 to $300 is the older AARP range. KFF (2026-10-14) quotes ALCA members at $150 to $350; families report $60 to $175. | Use all three with sources. |

Error count for care managers: Check 1: 0 fabricated quotes, 1 wrong citation (G-2). Check 2: 6 cell-label errors and 3 doubtful inclusions in the F4, F5, F6, F8, F10 rows (G-3 to G-9), 1 probable repeat writer (G-10), 1 wrong note (G-11). Check 3: 1 missed fact contradicting the file (G-1), 1 stale cost range (G-12).

## Final verdict table (care managers)

Reports = my corrected first-hand reports from family members or users (worked / did not work / mixed). All are reported, not observed. Documented evaluations: the ALCA-commissioned survey (about 200 respondents; 93% and 99%) is documented in KFF but not independent and not representative. No independent evaluation exists in the saved files. Care managers are local firms; one report is about one firm.

| Cell | Verdict | Confidence | Reports (W/D/M) | Plain reason | Earlier helpers | Differs from Figma? |
|---|---|---|---|---|---|---|
| F1 Relief finder | YES (for a fee, local firms): arranges aides, hospital sitters, facility tours; AARP says "arranging for relief or respite care" | medium | 9 / 0 / 1 (respite 0, adult day 0) | Reports show families get aides, visits and placements arranged; none names respite or adult day. | YES (people). Agree. | Figma "Yes, for a price". Agree. |
| F2 Eligibility and applications | LIMITED: finds programs, deals with insurers, helped with a long-term-care claim and recertification forms; no source shows it files a first Medicaid or VA application | medium-low | 4 / 1 / 1 | Real help with paperwork and insurers; the full "apply for you" is not shown. | VERIFY then "partly". Agree. | Figma has no F2 cell. |
| F3 Paying for relief | LIMITED: they explain costs and ways to pay, but you pay them $60 to $350 an hour and Medicare and Medicaid do not | medium | 5 / 2 / 3 | The advice helps; the care manager is itself the cost. | YES (fee). I downgrade to LIMITED. | Figma "Partly: advise on financial options". Agree. |
| F4 Refusing parent support | LIMITED: works when the person listens to the manager more than to the child; fails when a parent will not accept a stranger | medium-low | 4 / 2 / 0 | Mixed results in both directions. | YES (claim). I downgrade to LIMITED. | Figma "Partly... some parents still refuse them". Now supported by G34. |
| F5 Relatives cover time | LIMITED: a paid stand-in for relatives, and can mediate; cannot make a relative help | low-medium | 1 / 1 / 1 | They replace a missing sibling for pay; one brother refused the manager's calls. | YES (people). I disagree. | Figma "Partly: stand up to difficult relatives". Agree. |
| F6 Account access | LIMITED (rare): some act under POA, handle mail and online forms; no report of helping a caregiver log in; one POA complaint | low | 0 / 1 / 0 (+2 partial) | Paper and POA help, not logins. | VERIFY. Close. | Figma "One took power of attorney without telling the family": now supported by p1x0fqwe (fiduciary firm). |
| F8 Personal guidance | YES (for a fee): ongoing one-to-one expert, often a nurse or social worker | high for the existence; medium for quality | 30 / 7 / 4 | The largest set of reports. Praise: one person to call from far away. Complaints: cost, a "useless" manager, aides not showing up. | YES. Agree. | Figma agrees. |
| F9 Behavior and hard talks help | LIMITED: company and AARP text name behavior and hard talks; family reports are 1 good, 1 bad | low-medium | 1 / 1 / 0 | Mostly claims. | YES (claim). I downgrade to LIMITED. | Figma "Yes: explain hard topics". Agrees on talks. |
| F10 People who understand | VERIFY (leans NO) | low | 0 / 0 / 0 | No firm is said to connect caregivers to peers; counselor-type support is not peer support. | VERIFY "weak, 2 W". I disagree: 0 W. | Not in Figma. |

Cells where I disagree with the earlier helpers: F3, F4, F5, F9 (downgraded from YES to LIMITED), F10 (2 W becomes 0). Where the evidence differs from Figma: F6 (now has a source for the POA story), F3 range ($150 to $350 per ALCA).

## Not checked

- `aginglifecare.org` and ALCA member research (owner rule; robots.txt). Google and Yelp reviews of local firms; BBB for care manager firms; Facebook groups; Caring.com forums.
- Whether the firms in the reports are ALCA members (unknown for nearly all).
- The full AARP, NIA and US News pages (I read search excerpts only).
- Cost claims against firm price pages.
- Fresh keyword search of Reddit for care-manager words (the helpers' job timed out; I did not rerun it).
- Same-person checks across Reddit comments (no usernames saved).
- F9 and F10 with their own keywords beyond the saved threads.
