# AUDIT PASS 3: Area Agencies on Aging (AAA)

Date: 2026-11-06. Independent auditor. Nothing was committed or edited. Evidence states: **proven** (a check that could fail ran and passed), **observed** (I saw it this session), **inferred** (follows from observed facts), **documented** (a government or published source says it), **reported** (a person said it, not verified), **not-assessed**.

Scripts live in the session scratchpad, `/private/tmp/claude-501/-Users-landodoom-Desktop-AI-Developer-Residency--caregiving-coordinator/88c39ed8-fc0d-46c0-b385-032bd23092de/scratchpad/` (`qcheck.py`, `rows.py`, `uniq.py`, `blind.py`, `dups.py`, `poolscan.py`, `pg.py`). Run them with `python3 file.py` (not `-I`).

## 1. Quote and source check (Check 1)

Method: for every table row with a quoted cell in EVIDENCE.md, PASS1-HOWWELL.md and PASS2-HOWWELL.md, find the cited source (file, Reddit post id or comment id), normalize curly quotes, HTML entities and spaces, and test that the exact words are inside that source. Rows whose post id, comment id or forum URL id disagree with the saved file are also flagged.

State: **proven** for the exact-words test. Limit: it proves the words exist in the saved copy; it does not prove the poster is telling the truth or that the class label is right.

| File | Quote rows checked | Misses |
|---|---|---|
| EVIDENCE.md | 12 | 0 |
| PASS1-HOWWELL.md | 50 | 0 |
| PASS2-HOWWELL.md | 30 | 0 |
| Total | 92 | 0 |

Extra checks, same script family: 0 quotes are longer than 20 words (the files promise 20 or fewer); 0 post, comment or forum-URL id mismatches across all 321 PASS rows of the three programs. Sanity test: changing one word ("life" to "wife") or one post id made the script report a miss, so the test can fail.

Result: **0 quote errors.**

## 2. Documented evaluation check (Check 2)

Two documents are cited in PASS2-HOWWELL.md section (c). I opened the saved copies and searched each number. Page = PDF page counted by form feeds, plus printed page where shown.

State: **observed** (I read the saved text). Source: `PASS2-doc-acl-nfcsp-outcome-evaluation-2018.txt`, `PASS2-doc-acl-nfcsp-process-evaluation-lewin-slides.txt`.

| Cited number | Found? | Page in file | Page cited by PASS2 | Verdict |
|---|---|---|---|---|
| 43% (N=522) got respite from their AAA; median 6 hours | yes | p. xviii, PDF 18 | p. xviii, PDF 18 | correct |
| 24% (N=298) got education, counseling or groups; 52% groups, 36% training, 24% counseling | yes | p. xviii, PDF 18 | same | correct |
| About one-third who skipped respite did not know of it; about half for education | yes | p. xviii, PDF 18 | same | correct |
| 709 of 1,242 (57%) used NFCSP services at baseline | yes | p. 4-1, PDF 38 | same | correct |
| Burden: Program -0.095, Comparison +0.145 for caregivers getting 4+ respite hours a week | numbers yes | p. xix PDF 19; table p. 8-7 PDF 97 | p. xix, PDF 19 | numbers correct, claim incomplete (see below) |
| 98% of respite users helpful (86% very); 99% of education users (74% very) | yes | p. xx, PDF 20 | same | correct |
| No effect on mental health, physical health or satisfaction | yes | p. xx, PDF 20 | same | correct |
| 83% get family help; 48% agency or private help | yes | p. xviii, PDF 18 | same | correct |
| Lewin slide 43: respite most requested 75%; financial help 27% | yes | slide 43 | slide 43 | correct |
| Slide 45: 41% meet respite needs all or most of the time, 52% sometimes; funding 87% of 42 | yes (chart text is jumbled but readable) | slide 45 | slide 45 | correct |
| Slide 48: 74.4% have service caps; 37% all services; 37% yearly caps | yes | slide 48 | slide 48 | correct |
| Slide 50: 30% waiting list, 43% budget cut, 24% fewer served, 51% heavier caseloads | yes | slide 50 | slide 50 | correct |
| Slide 39: info 98, respite 97, access 93, training 86, counseling 78, groups 68 | yes (bar labels line up with the six values) | slide 39 | slide 39 | correct |
| Slide 42: 77% of assessments include caregiver's health | yes | slide 42 | slide 42 | correct |
| Slide 58: 31% no evidence-based training; Powerful Tools 33, Savvy 7, REACH II 6 | yes | slide 58 | slide 58 | correct |
| Slide 65: waiting-list data not widely reported | yes | slide 65 | slide 65 | correct |

Report dates: Westat/ACL outcome evaluation is dated December 5, 2018 (file p. 1). The Lewin deck's surveys ran Jan to Dec 2015 (slide 9); the deck itself has no date in the saved text. No date looks wrong for today (2026-11-06). Both are old: 2018 and 2015 data.

**Error found (C2-1).** PASS2-HOWWELL.md line 115 reports the burden drop as a finding. The same report says the difference "was not statistically significant" (p. 8-7, PDF 97, and again p. 8-8, PDF 98: "Although the result was not statistically significant..."). The executive summary (p. xix) leaves that out. The line must carry the caveat. The 4+ hour group is also a restricted subgroup the authors chose (p. 8-6, PDF 96).

Other limits that PASS2 did not state: the 98% and 99% helpful figures come from people still in the program (PASS2 does say this). Slide 65 also says local providers reported "low rates of inability to accept NFCSP clients", which cuts against the waiting-list story and was left out.

## 3. Recount (Check 3)

### 3a. Arithmetic recount from the saved rows

I parsed every report row in the two PASS files and rebuilt the cell tables.

| Test | Result | State |
|---|---|---|
| Per-cell W / D / M counts rebuilt from rows vs the tables in section (a) | all 22 cell-pass counts match | proven (script `rows.py`) |
| Headline "42 unique" (pass 1) | 42 distinct quotes: 8 / 28 / 6, matches | proven |
| Headline "19 unique" (pass 2) | 24 distinct quotes minus 5 flagged "same writer" = 19, matches | proven |
| Same post or comment in both passes | none by id or by quote | proven |
| Same text posted twice under two ids | none among counted rows (8-word shingle test, `dups.py`) | proven |

### 3b. Double counting I found that the files did not flag

| ID | Where | What | Effect |
|---|---|---|---|
| D-1 | PASS2 lines 59 and 69 (comment kyc2wnb, F2 and F3) vs PASS1 line 72 (post 1bx5ch2, F2) | The comment is by the thread opener. The post says "We've had the department of aging come to the apartment. My mom doesn't qualify for help. There a minimum wait or 2 years for an aide." The comment repeats the same facts and ends "Thank you for your suggestion though." Same family counted in both passes. | F2 and F3 each lose 1 DID NOT WORK in the combined count. Pass-2 unique count 19 becomes 18. |
| D-2 | PASS2 line 46 (CCSWA row) says "same writer as the row above" | The row above is from a different thread (440844). The writer cetman91 is the writer of line 95 (thread 445160), not of the line above. The note is wrong; the count is not affected. | note error only |
| D-3 | PASS2 lines 60 and 71 (comment jxbmjw4) | A former Council on Aging employee states a rule ("clients are required to exhaust all resources..."). That is a staff statement, not a family experience. It is counted as a family report in F2 and F3. | remove from family counts (-1 D in F2, -1 D in F3) |
| D-4 | PASS2 line 79 (comment js009lv, F4) | The row's own note says "neutral advice, not own experience." It is still counted as DID NOT WORK. | remove (-1 D in F4) |

State of D-1: **inferred** (same facts, same thread, reply addressed to a helper; Reddit usernames were not saved so identity is not proven). Source: `PASS2-reddit-comments-aaa.jsonl` comment kyc2wnb; `reddit/arctic-shift-2026-11-03/posts.jsonl` post p1bx5ch2. Limit: no author field.

### 3c. Blind re-reading: 15 random reports (seed 11)

Method: `blind.py area-agencies-on-aging 11 15` picked 15 rows at random from all unique (source, quote, cell) rows and printed the quote plus about 500 characters on each side, with no class label. I classified each, then compared.

| # | Cell | Source | My class | Earlier class | Agree? | Note |
|---|---|---|---|---|---|---|
| 1 | F1 | forum 445160 opener | D (weak) | D | yes | complaint is mostly about a home care agency |
| 2 | F3 | comment kzz7uqj | not a payment report | D | NO | about an aide shortage and 8 to 10 affordable hours; says nothing about AAA payment |
| 3 | F1 | comment pdoulmm | D | D | yes | wrong cell: "suggested the crisis line" is behavior help (F9), not a relief finder |
| 4 | F9 | comment pdoulmm | D | D | yes | |
| 5 | F2 | comment kyc2wnb | D | D | yes | duplicate family, see D-1 |
| 6 | F2 | post 15nym3h | D | D | yes | |
| 7 | F2 | post 11awqmt | M | M | yes | wait list for the wait list |
| 8 | F4 | comment js009lv | not a report | D | NO | advice, not experience (D-4) |
| 9 | F1 | comment pdoomaw | W (weak) | W | yes | one line, no detail |
| 10 | F4 | forum 440844, writer Val3rie | W (weak) | M | NO | writer says "I found everyone very helpful"; the social worker met the parent alone |
| 11 | F1 | post 1726a3n | D (mild M) | D | yes | |
| 12 | F8 | forum 463104, Llamalover47 | W | W | yes | town-run Council on Aging in Massachusetts style, may not be a federally funded AAA |
| 13 | F4 | post 12hnruv | D | M | NO | writer: agency "do not have the ability to do anything without my mom's consent"; they gave resources but could not act |
| 14 | F1 | post 18yfm7u | D | D | yes | phone never connects (Dallas ADRC) |
| 15 | F1 | post 130ibg9 | D | D | yes | |

Result: **11 of 15 agree on class; 4 disagree** (#2, #8, #10, #13). Two more agreed on class but sit in the wrong cell or are duplicates (#3, #5). State: **observed**. Limit: 15 reads, one auditor, no second rater.

### 3d. Independent raw re-scan for cells (not looking at earlier labels first)

Pool: `posts.jsonl` + `posts_targeted.jsonl` (43,665 + 5,650 posts) and all saved comment files. Agency words (area agency on aging, AAA, council or office or department on aging, ADRC, elder services and others).

| Cell | What I did | Result |
|---|---|---|
| F1 / F2 (completeness) | 144 post hits and 67 comment hits; read 106 post hits not used as rows | About 7 more thin first-person mentions exist (for example 1fnxry0, 1s6suej, 1xemgi5, 1dsv8r1, 1tc3u7d); none changes a conclusion. Counts are a slight undercount, not an overcount. |
| F4 (refusing parent) | agency word within 200 characters of refuse, consent, resist, voluntary | 17 hits; 6 are rows; 1 missed valid first-person report (post 1fnxry0: family called elder affairs; grandparents refuse entry; D). My count: 1 W / 11 D / 0 M (12) after fixes, vs 0 / 10 / 2 (12) claimed. Direction unchanged. |
| F5 (relatives) | agency word within 100 characters of sibling, relatives, schedule | 6 hits. None is a tool for giving tasks to relatives. Two matter: the Florida paid-caregiver family (grandchild paid through a Medicaid waiver with AAA involved), and comment o3e1bb0: "Without CDS the caregiver must come from an agency. With CDS family members can be paid. ADRC ... does NOT pay caregivers." |
| F6 (accounts) | agency word within 130 characters of bank, bills, POA, accounts | 20 hits; 0 describe an agency getting a caregiver into a parent's accounts. 1 existing row (1ihp8rc, "So far I haven't gotten anything from them"). |

State: **observed**. Source: scripts `aaa_scan.py`, `near.py`, `poolscan.py`.

### 3e. Counts after my corrections (combined pass 1 + pass 2)

"Earlier" is the combined column in PASS2 section (a). "Adjusted" removes D-1 to D-4, the cell misfit (#3), and applies my blind class changes (#2 removed from F3, #10 to W, #13 to D) and adds 1fnxry0. Weak rows stay in. Reports that are staff or advice are excluded.

| Cell | Earlier W / D / M (total) | Adjusted W / D / M (total) |
|---|---|---|
| F1 | 12 / 14 / 6 (32) | 12 / 13 / 6 (31) |
| F2 | 3 / 11 / 3 (17) | 3 / 9 / 3 (15) |
| F3 | 2 / 6 / 4 (12) | 2 / 3 / 4 (9) |
| F4 | 0 / 10 / 2 (12) | 1 / 11 / 0 (12) |
| F5 | 0 / 0 / 0 | 0 / 0 / 0 |
| F6 | 0 / 1 / 0 (1) | 0 / 1 / 0 (1) |
| F8 | 2 / 1 / 0 (3) | 2 / 1 / 0 (3) |
| F9 | 0 / 2 / 0 (2) | 0 / 2 / 0 (2) |
| F10 | 1 / 0 / 0 (1) | 1 / 0 / 0 (1) |
| Pass 2 headline | 19 (7 / 9 / 3) | 16 (7 / 6 / 3) |
| Pass 1 headline | 42 (8 / 28 / 6) | 43 (8 / 30 / 5) |

Scope flags: pass 2 counts 3 "unclear" non-family voices (former staff, friend, advice). 1 pass-1 row (1c0e35g) is APS rather than an AAA. Several rows are named "Council on Aging" or "department of aging" and may be town or state offices rather than federally funded AAAs (the files say this too).

Vendor, promo or survey-bait: scanned the full text of all counted rows for survey, app, DM, research study and similar words. 0 true hits (hits on "our app" were the word "application"). State: **observed**. Limit: keyword scan, not a human read of all 66 sources.

## 4. Try to disprove (Check 4)

Tools: saved pages, Firecrawl search and scrape. robots.txt: I read `ilaging.illinois.gov` (general agents allowed; paths used are not disallowed), `www.va.gov` (the paths used are not disallowed). `www.mass.gov` returned no readable robots.txt to curl; I fetched the single public page anyway and say so here. I did not fetch aplaceformom.com, gao.gov or Trustpilot.

| Search | Source | Found | Effect |
|---|---|---|---|
| "Area Agency on Aging money management program volunteers pay bills" | Firecrawl, 2026-11-06 | Illinois Department on Aging Money Management Program: volunteers help low-income older people "paying bills; ... keeping track of banking records; intervening with creditors"; volunteers can be Representative Payees. Only for Community Care Program participants and people with a substantiated APS case, in listed counties (`ilaging.illinois.gov/programs/money-mgmt.html`, scraped). Massachusetts: free for income-eligible people 60 and over, run by local Aging Services Access Points, helps with "creating budgets and paying bills" (`mass.gov/info-details/money-management-program`, scraped). | **F6 is not a flat NO.** Some state aging networks help an older person with bills and banking. The older person is the client; it is not a caregiver login to a parent's accounts. |
| "AAA family caregiver respite provider may be a family member consumer-directed" | Firecrawl, 2026-11-06 | NY State Office for the Aging technical memo on caregiver-directed respite under the NFCSP: caregivers hire, schedule and supervise respite workers, "whether to hire family members"; "Family members may be hired as respite providers under both the Voucher Model and the FI Model" (not the primary caregiver); timesheets are required (search excerpt of `aging.ny.gov/26-tam-01-implementing-caregiver-directed-respite-care-service-delivery-model-under-nfcsp`). Arizona's Lifespan Respite lets a family member be the provider except spouse, child, parent or guardian or someone in the home. | **F5 is not a flat NO.** A relative can be paid or hired in some AAA and state programs. No tool assigns or tracks relatives' tasks. |
| "AAA ... parent who refuses services ... family consultation, mediation, coaching" | Firecrawl, 2026-11-06 | 8 results, none documents an agency program for a refusing parent. East Arkansas family mediation (already saved) is the only related item. | nothing found that changes F4 |
| Saved pages grep for "family member", "consent", "accounts" | saved `.txt` files | nothing new | no change |
| Reddit raw scans (section 3d) | Arctic Shift saved data | see 3d | F4 backed by 12 reports; F6 and F5 show no agency tool |

For every earlier YES, I looked for evidence it is not available to an ordinary family caregiver: Lewin slide 45 (only 41% of AAAs meet respite needs all or most of the time), slide 48 (74.4% use caps), slide 50 (30% added a waiting list), ACL outcome p. xviii (about a third did not know the service existed), and families who report waits of 2 years or 6 months (saved Reddit and forum rows). That is why F1, F2 and F3 come down from YES to LIMITED below.

State: **documented** for the web pages (search excerpt or scraped page, date read 2026-11-06; these pages were not saved to docs/sources because this audit may write only the AUDIT file). Limit: web pages change; one state per example.

## 5. Corrections list (earlier files)

| # | File : line | Error | Fix |
|---|---|---|---|
| 1 | PASS2-HOWWELL.md : 115 | Burden drop stated without "not statistically significant" (report p. 8-7, 8-8; PDF 97, 98) | add the caveat |
| 2 | PASS2-HOWWELL.md : 59, 69 | comment kyc2wnb is the thread opener whose post is PASS1 line 72; double count across passes | remove from pass 2 F2 and F3 |
| 3 | PASS2-HOWWELL.md : 46 | note "same writer as the row above" points to a different thread | change note |
| 4 | PASS2-HOWWELL.md : 60, 71 | staff rule statement counted as a family report | move to documented-context list |
| 5 | PASS2-HOWWELL.md : 79 | advice counted as DID NOT WORK (own note says it is advice) | remove from counts |
| 6 | PASS2-HOWWELL.md : 70 | aide-shortage comment counted as an F3 payment failure | remove from F3 |
| 7 | PASS2-HOWWELL.md : 48 | "suggested the crisis line" counted in F1 relief finder; it fits F9 only | remove from F1 |
| 8 | PASS1-HOWWELL.md : 43 and 91 | post 12hnruv classed MIXED; the writer says the agency could not act without consent | class D in F4 (M in F1 is fine) |
| 9 | PASS2-HOWWELL.md : 77 | Val3rie "I found everyone very helpful" classed M in F4 | class W (weak) |
| 10 | EVIDENCE.md : F5 and F6 rows | VERIFY, "leans NO" | F5 LIMITED, F6 LIMITED (section 4); EVIDENCE says "No page offers help getting into a parent's accounts", true for the saved pages, false for state money management programs |
| 11 | PASS2-HOWWELL.md : header, section (c) | no mention that Lewin slide 65 says local providers report low inability to accept clients | add as a limit |
| 12 | PASS1-HOWWELL.md : section (e) | "Nothing was fetched from the web" is correct for pass 1; but 1fnxry0 (F4) and about 6 thin agency reports were missed | add or note as undercount |

## 6. Final verdict per cell

Confidence: high, medium, low. Counts are my adjusted combined family reports (W worked / D did not work / M mixed). "Disagree" means I differ from the earlier helpers' verdict. "Figma" means the Figma 4c cell is the source of truth and I say where evidence differs.

| Cell | Final | Conf. | Family reports W/D/M | Documented evaluations | One sentence | Disagree with earlier? | Differs from Figma? |
|---|---|---|---|---|---|---|---|
| F1 Relief finder | LIMITED (local referral plus some funded respite; waits and caps) | medium | 12 / 13 / 6 | ACL outcome 2018 (43% got respite); Lewin 2015 (97% offer respite, 41% meet need) | Agencies find and sometimes pay for relief, but few families get it fast. | yes (was YES) | no, Figma "Partly" |
| F2 Eligibility and applications | LIMITED (agencies assess and help apply; strict rules, waits of months to years) | medium | 3 / 9 / 3 | Lewin (93% give access help; waiting lists at 30%) | They do the paperwork step, but most reports end in no or long wait. | yes (was YES) | no |
| F3 Paying for relief | LIMITED (depends on state and agency; caps; funding runs out) | medium | 2 / 3 / 4 | Lewin (74.4% caps, funding top reason); PA table (200% FPL gets 100%) | Some agencies pay or reimburse, many cap hours, and no national price exists. | yes (was YES) | no, Figma "Partly" |
| F4 Refusing parent support | NO (agency offers services but cannot act without the parent's consent; no feature for persuading) | medium | 1 / 11 / 0 | none found | Twelve families describe agencies stopping when the parent says no, and nothing documented contradicts them. | no (VERIFY, reported NO) | agrees with Figma "No" (EVIDENCE.md set VERIFY) |
| F5 Relatives cover time | LIMITED (a relative can be hired or paid in some NFCSP or waiver programs; nothing assigns or tracks tasks) | low | 0 / 0 / 0 | NY TAM (documented via search excerpt) | The only link is paying a relative as respite worker; no tool splits tasks. | yes (was VERIFY, leans NO) | differs: Figma "No" |
| F6 Account access | LIMITED (some state money-management programs pay bills for low-income older adults; no caregiver login to a parent's accounts) | low | 0 / 1 / 0 | none | It helps the older person with bills in a few states, not a caregiver getting in. | yes (was VERIFY, leans NO) | differs: Figma "Partly: Medicare counseling" (Medicare help is real but is not account access) |
| F8 Personal guidance | LIMITED (care manager or TCARE coach at some agencies) | low | 2 / 1 / 0 | Lewin (78% offer counseling; 77% assess caregiver health) | One-to-one help exists in many agencies, with uneven quality. | no | no |
| F9 Behavior and hard-talk help | LIMITED (dementia classes at some agencies; most list none) | low | 0 / 2 / 0 | Lewin (31% of local providers offer no evidence-based training; Savvy Caregiver 7%) | A few agencies teach it; one family was told to call a crisis line. | no | no |
| F10 People who understand | LIMITED (about two in three agencies run groups; thin family evidence) | low | 1 / 0 / 0 | Lewin (68% offer groups); ACL (52% of education users used groups) | Groups are common but not everywhere, and only one family said so. | yes (was YES) | no, Figma "Partly" |

State of the verdict column: **inferred** from the documented and reported evidence above. Counts: **proven** arithmetic on **reported** rows.

Cells where I and the earlier helpers disagree: F1, F2, F3, F5, F6, F10. Cells where evidence differs from Figma: F5, F6 (and F4 only in that EVIDENCE.md had it as VERIFY).

## 7. Not checked

- Whether the Reddit and forum people are who they say they are; no usernames saved on Reddit.
- Replies under most Reddit posts (the keyword search of comments failed; only 81 threads were fetched).
- Every one of the 188 unused agency hits was read only as a 300-character window, not as a full post.
- The Illinois and Massachusetts program pages and the NY memo were not saved to docs/sources; read live on 2026-11-06. `www.mass.gov` robots.txt could not be read.
- Whether "Council on Aging" and "Office on Aging" rows are federally funded AAAs.
- Current (2026) AAA waiting lists and caps; the best documents are 2015 and 2018.
- GAO reports and state auditor reports on AAAs (gao.gov blocked by instruction; Ohio unreachable).
- Skills: skeptical-audit applied. security-review, accessibility-check, engineering-quality-check, judge-arch, architectural-decision-records, enterprise-architecture-standards, owasp-secure-coding-bdd, test-strategy, operational-readiness, release-deployment-safety, data-lifecycle-compliance, ux-ui-design-review, writing-security-tests: not relevant (no code, UI or personal-data system was reviewed).
