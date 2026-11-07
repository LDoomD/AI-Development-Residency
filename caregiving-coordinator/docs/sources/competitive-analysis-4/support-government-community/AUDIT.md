# Independent audit: support groups, government programs, online communities

Date: 2026-11-06. Auditor did not do the earlier work. Goal: try to prove `SYNTHESIS.md` and `MENTIONS-READ.jsonl` wrong.
Method: `skeptical-audit`. Every claim has a state, a source you can re-open, and a limit.
States: **proven** (a check that could fail ran and passed) / **observed** (I saw it directly) / **inferred** / **documented** / **reported** / **not-assessed**.
Skills applied: `skeptical-audit`. Judged not relevant: `security-review`, `accessibility-check`, `ux-ui-design-review`, `judge-arch`, `engineering-quality-check` (no code or UI changed). I did not fetch any web page, so robots.txt did not come up.
Nothing existing was edited. New files are only this file and `audit-scripts/`.

Paths below are relative to this folder (`docs/sources/competitive-analysis-4/support-government-community/`).
Raw data used: `../../reddit/arctic-shift-2026-11-03/posts.jsonl` and `posts_targeted.jsonl`, `../../forums/agingcare`, `../../forums/alzconnected`, `../../market-analysis-3/segments-11-12/{packs,codes}`.

## How to re-run

```
python3 -I audit-scripts/a_corpus.py      # builds my own copy of the 50,547 items (writes a pickle in the scratchpad)
python3 -I audit-scripts/a_quotes.py      # check 1
python3 -I audit-scripts/a_table.py ; a_dups.py ; a_medicaid.py ; a_sample.py ; a_blind_labels.py   # check 2
python3 -I audit-scripts/a_counts.py ; a_missed.py ; a_missed2.py ; a_break_fb.py ; a_namecounts.py ; a_headline.py   # checks 3 and 4
```
Saved outputs: `audit-scripts/out_*.txt`. Saved reading data: `audit-scripts/data_*`.
My corpus has 50,547 items (49,315 Reddit posts, 873 ALZConnected and 359 AgingCare thread parts) and 831 relevant coded posts. These match the helper's numbers, so we read the same data. (observed, `a_corpus.py`)

---

## Summary in plain words

| Area | Result |
|---|---|
| Quotes | All 447 quotes are real and 20 words or less. **0 errors.** |
| Table math | Section 4 table matches the jsonl for all 34 rows. **0 errors.** |
| Blind re-label (50) | Same label 82%. Same "caregiver report or not" 92%. Same outcome 95%. Same person cared for 89%. **1 clear error** (an app maker counted as a user). |
| 48 of 78 Medicaid reports are one NY event | **Wrong number.** 48 mention CDPAP. Only **30** are from March or April 2025. SYNTHESIS contradicts itself (line 241 says 30). The idea (a big NY cluster) holds. |
| Counts for PACE 41, IHSS 77, Facebook 21, Support group 37 | Reproduce from raw data. |
| Hospice respite 23 | **Undercount.** At least **9 more** real reports exist (so 32 or more). |
| Alzheimer's Association 19 (7 used) | Reproduces, but 9 of 19 come from the Association's own forum, and "5 worked" is really 3. |
| "Break only in hospice, PACE, IHSS" | **Fails.** The VA caregiver programs also give breaks. IHSS "break" is mostly cleaning help. |
| VA caregiver programs | **Left out of the candidates.** At least 19 real caregiver posts. |
| Meals on Wheels "6 reports" | **Fails.** About 45 real caregiver mentions; about 12 say the person refused or canceled. "Food, not relief" probably still holds. |
| Discord and WhatsApp "12 asks" | **Fails.** About 7 or 8 distinct asks. Three WhatsApp posts look like one person. Supply cannot be measured from this data. |
| Facebook "only community with mostly bad reports" | **Fails** as worded (WhatsApp family chat is 4 of 5 bad). Also biased: the writers are on Reddit or ALZConnected. |

---

## Check 1. Quotes

| Claim | State | Source | Limit |
|---|---|---|---|
| All 447 non-empty quotes in `MENTIONS-READ.jsonl` appear word for word (after fixing curly quotes and spacing) in the saved item with that same id. 444 in `posts.jsonl` or forum files, 3 only in the market-analysis pack text. | proven | `python3 -I audit-scripts/a_quotes.py`, output `audit-scripts/out_check1_quotes.txt`: `tiers: item 444, pack 3, thread 0, corpus 0, none 0, noquote 309`; `MISSES 0` | Proves the words exist. Does not prove the label fits. Case ignored. |
| No quote is over 20 words | proven | same run: `quotes >20 words 0` | Counts by spaces. |
| All 756 ids exist in the saved data and every url matches | proven | same run: `ids not in corpus/packs 0`, `url mismatches 0` | none |
| The 309 rows with no quote are exactly labels 4 and 5 | observed | `quote_checked=False` count 309 = labels 4 + 5 (102 + 207) | none |
| SYNTHESIS.md has 51 quoted strings. 36 are real caregiver words found in the data. 15 are not caregiver quotes. | observed | same run, "SYNTHESIS quoted strings" | 14 of the 15 are labels or scare quotes. **One is a made-up quote:** line 153 puts "this forum saved me" in quote marks, but it is not in any post. No SYNTHESIS quote is over 20 words. |

Misses: **none in the jsonl. One in SYNTHESIS (line 153, a paraphrase in quote marks).**

---

## Check 2. Blind re-label, duplicates, and the 48 of 78 claim

### 2a. Sample and method
Seed 20261106. I took **one random mention from every one of the 34 candidates**, topped up so each label has at least 6, then added random label 1 to 3 posts from the 9 big candidates, for 50. Label counts in the sample: 1:14, 2:16, 3:8, 4:6, 5:6. (observed, `audit-scripts/out_sample.txt`)
I read each post's text without the helper's labels (`audit-scripts/data_blind50_reading_file.txt`), wrote my labels in `a_blind_labels.py`, and only then compared. For 7 posts the snippet hid the key word, so I searched the full text.
State: observed. Limit: one reader (me). Long posts were shown as the first 350 characters plus the passages around the keyword, then checked in full when unclear.

### 2b. Agreement (from `audit-scripts/out_check2_blind.txt`)

| Field | Agree | Rate |
|---|---|---|
| Label 1 to 5 (exact) | 41 of 50 | 82% |
| "Caregiver report (1 to 3)" versus "not (4 or 5)" | 46 of 50 | 92% |
| Outcome (where both say 1 to 3) | 35 of 37 | 95% |
| Who is cared for (where both say 1 to 3) | 33 of 37 | 89% |

### 2c. Every disagreement (15 items; I judged each)

| # | id | Candidate | Me versus helper | Who is right |
|---|---|---|---|---|
| 3 | p1uf0jsd | NAMI | label 3 vs 5 | Judgment call. A link-list post. |
| 4 | p1dg490a | PACE | cared for parent vs unclear | Me (post says "mom"). Small. |
| 5 | alzconnected-77086-COMMENT3 | Eldercare Locator | 3 vs 5 | Helper (pasted search result). |
| 7 | p1r8ob9p | IHSS | used vs asking | Judgment call ("in the process of enrolling"). |
| 13 | p1xgi8wh | Medicaid | outcome none vs did not work | Judgment call. Helper's own rule: "could not get in" counts as did not work. On a waitlist is not the same as denied. |
| 17 | p1dxh2xf | Medicaid | used vs asking | Judgment call. |
| 18 | p1uod3tm | Subreddit | parent vs unclear | Me. Small. |
| 24 | alzconnected-77414-COMMENT15 | Facebook | used vs recommends-or-warns | Both fit. |
| 30 | p1xgi8wh | SHIP counselor | asking vs used | Judgment call. Note: the **same post** is also counted under Medicaid (#13). |
| 36 | **p158bctp** | Subreddit | **vendor vs "1 caregiver used it", outcome worked** | **Me. Helper error.** The author says "We JUST launched the first version of our app". An app maker was counted as a caregiver user. |
| 42 | p1d89ew3 | Medicaid | did not work vs mixed | Judgment call. |
| 47 | p1n1ottl | WhatsApp family chat | used vs vendor | Judgment call. Looks like survey bait, so the helper may be right. |
| 49 | p1kb5v1a | Support group | asking vs recommends | Judgment call. Writer is not the caregiver. |
| 49 | p1kb5v1a | Support group | spouse vs parent | Me. Small. |
| 50 | p1hp30b0 | Meal Train | unclear vs other relative | Judgment call. |

Result: **1 clear error in 50 (2%)**. The other 14 are judgment calls or small labeling slips. State: observed. Limit: 50 of 756, one reader; a 2% rate has a wide range.
I then scanned all 55 "Subreddit" reports for app-maker words. Only p158bctp matched (`audit-scripts/a_subreddit_vendor_va.py`, output `audit-scripts/out_subreddit_vendor_va.txt`). So the Subreddit row should read **54 reports, 33 worked**, not 55 and 34 (SYNTHESIS lines 12, 77, 147, 148). State: observed. Limit: keyword scan only.

### 2d. Is any person counted twice?

| Claim | State | Source | Limit |
|---|---|---|---|
| No exact duplicate text inside any candidate (first 300 and first 120 characters compared) | proven | `a_counts.py`, `a_table.py`, `a_dups.py`, outputs `out_check3a_counts.txt`, `out_table_recompute.txt`, `out_check2c_dups.txt`: 0 groups | Catches copies only. |
| **Three WhatsApp "asks" are probably one person.** p1x3k3jd (11 Oct 2026), p1x49fv6 (12 Oct, same title, empty body) and p1x4ejkv (12 Oct, "spouse-caregiver burnout... private WhatsApp group"). All in r/CaregiverSupport within 2 days. Helper flagged only the pharmacist crosspost. | observed | `audit-scripts/out_check3cd.txt`, text in `audit-scripts/out_check2c_dups.txt` | Same-writer is inferred (same title, same sub, same days). No author names in the data. |
| 15 posts count as a report under more than one candidate. 3 are in both IHSS and PACE (p1ti6pdq, p1ha4nnh, p1oskbnd); p1ha4nnh is really a PACE complaint filed under IHSS. | observed | `out_check3a_counts.txt` | The per-candidate table stays valid. Adding candidates together would double count. Medicaid plus IHSS = 155 unique posts, no overlap (checked). |
| ALZConnected: 28 reports in 23 threads, so 4 threads have 2 or 3 comments. Same member twice is possible. | observed | `out_table_recompute.txt` | Member names are hidden in the saved files. |

### 2e. The "48 of 78 Medicaid reports are one NY CDPAP to PPL event in March and April 2025" claim

Re-derived from the 78 Medicaid reports (`a_medicaid.py`, `audit-scripts/out_medicaid_NY.txt`):

| What I counted | Number |
|---|---|
| Medicaid reports (labels 1 to 3) | 78 (matches) |
| Text mentions CDPAP or PPL | **48** (matches the helper's 48) |
| ...and post dated March or April 2025 | **30** (10 in March, 20 in April) |
| ...dated March to June 2025 | 33 |
| CDPAP or PPL posts from other dates (Dec 2023 up to June 2026) | 18 |
| Strict version: CDPAP or PPL, plus "payroll" or "transition" words, dated March or April 2025 | 25 |

- **The claim as written is wrong.** 48 is the count of posts that mention CDPAP in any year. Only 30 are from March or April 2025. The helper's own claims table (line 241) says 30, which contradicts lines 11 and 118. State: proven (script printed 30 and 48).
- **The idea holds.** Raw data check (`audit-scripts/out_medicaid_raw255.txt`): of all 255 Medicaid-filter hits, 151 mention CDPAP or PPL and 78 of those are dated March or April 2025. So the NY cluster is real and is larger in the full pool (about 31% of hits), not smaller. State: observed. Limit: whether each of the 30 is about the PPL switch was judged by keyword, not by reading each one.
- **Fix:** "30 of 78 Medicaid reports are CDPAP posts from March and April 2025 (the NY switch to PPL). 48 of 78 mention CDPAP at all. The other 30 reports (no CDPAP or PPL) cover other states."

---

## Check 3. Try to disprove

### 3a. Re-derived counts (my own regexes on all 50,547 items; `a_counts.py`, `out_check3a_counts.txt`)

| Candidate | Helper claim | My raw hits | Helper's caregiver reports | My finding | State |
|---|---|---|---|---|---|
| PACE | 62 hits, 41 reports | 62 (same ids) | 41 | Reproduces. 19 of the other 21 are one weekly link-list post (I read all 62 snippets; list confirmed). | proven (raw), observed (labels) |
| IHSS | 101 hits, 77 reports | 101 (same ids) | 77 | Reproduces. Used-for is 73 pay and 4 break. | proven (raw), observed (labels) |
| Hospice respite | 27 hits, 23 reports | **30** (3 not read) | 23 | **Undercount.** See 3b. | proven (30 vs 27) |
| Alzheimer's Association | 22 hits, 19 reports, 7 used | 22 | 19 | Count reproduces. Source and outcome problems below. | observed |
| Facebook groups | 64 narrow hits, 21 reports | 63 | 21 | Reproduces (one hit differs by regex wording). | observed |
| Support group (any) | 347 hits, 37 reports from 41 read | 347 | 37 | Reproduces, but 37 is **only the 41 the helper read**. 308 hits were not read; 175 are in the 831 relief set and 114 were coded earlier. The true number is much bigger. | proven (347), observed (limit) |

Details that change a conclusion:
- **Alzheimer's Association.** 9 of the 19 reports are ALZConnected comments. ALZConnected is the Association's own forum, so those are members pointing to their host, not independent proof of use. **Reddit-only: 10 reports (6 used it).** State: observed (`audit-scripts/out_check3a_counts.txt`: "9 in 9 threads"). The "5 worked" holds for only 3: alzconnected-77005-COMMENT2 and alzconnected-77348-COMMENT3 only say "good resource" with no outcome of their own (`audit-scripts/out_check4_headline.txt`). Fix: **3 worked, 3 did not, 11 no outcome, 2 recommendation-only.**
- **Support group.** The 37 reports mix very different things (hospital groups, Association groups, Zoom groups, online groups). Section 6 says "7 of 15" worked and the table says 8 worked overall (7 users plus 1 recommender). Both are right, but they should be labeled.

### 3b. Real mentions the helper missed

Search over all 50,547 items (`a_missed.py`, `a_missed2.py`; saved contexts in `audit-scripts/data_missed_contexts_*.txt`). "Not read" means the id is not in `MENTIONS-READ.jsonl`. I read the 240-to-300-character snippets for the groups I list as "observed". I did not read every post.

| Search | Items found | Not read by helper | What I saw | State |
|---|---|---|---|---|
| **VA caregiver programs** (PCAFC, Veteran Directed Care, VA caregiver stipend, VA respite or aide hours) | 18 strict (`a_missed2.py`), 26 loose (`a_subreddit_vendor_va.py`; p1l0d9o5 and p1w4oijc were found by a wider "VA ... respite" search I ran inline and did not save) | 17 strict | At least **19 distinct caregiver posts**: p13njcjy, p1k58bpy, p1l0d9o5, p1lwgcii, p1mbxwso, p1n2nhns, p1r7iv1m, p1r8g2fz, p1ry7qkt, p1s5mbcr (p1s5mg96 is a repeat), p1sto9oj, p1u10o61, p1umpacb, p1uwf30x, p1vfh78m, p1xmgzdg, p1hnx5ix, p1l9w918, p1w4oijc. Real breaks in them: p1l0d9o5 ("15 hours of respite in-home caregiving a week" through the VA), p1l9w918 (30 days of respite plus 20 hours a week), p1w4oijc (VA respite stay). The helper's own Part B ranks VA programs at **39 posts (rank 12)**, above Alzheimer's Association (13) and Facebook (7), yet VA is not in Part C or the include table. | observed (snippets); count approximate |
| **Hospice respite, missed by the 60-character window** | 30 vs 27; 81 posts have both words | 50 of the 81 | At least **9 more real hospice respite reports**: p16pk4wd, p1cbmszm, p1cgw0j9, p1e0vg7a, p1h9xsuw, p1igixmj, p1mym2av, p1jmpdxc, p1bo2sz0 (p1xcuw96 is a tenth, weaker). Offered then declined (p1igixmj, p1mym2av), stay used and went badly (p1jmpdxc, p1cgw0j9), offered and held back (p1e0vg7a, p1cbmszm). The three 30-vs-27 posts (p1amhy8v, p1mym2av, p1v3ycpw) are one reason: the regex stops at a line break. **Corrected total: 32 or more.** | observed |
| **Meals on Wheels** | 64 | 58 | About **45 real caregiver mentions** ("I set up Meals on Wheels", "she cancelled it because she hates the food"). About **12 say the person refused, disliked or canceled** (examples: p14vy96q, p18auy7o, p1ax69gc, p1mdnc54, p13ponu0, p145fo9f, p1e3840b, p1f2brol, p1faj4hy, p1jp1bhn, p1vi9585). About 6 say it helps (p10isd97, p1ieh671, p1r2l8f5, p1lfiqzm). Helper says "6 reports... 1 parent refused". | observed (snippets only) |
| Respite voucher, Lifespan Respite, ARCH, NFCSP | 2 strict | 1 | One real mention: p1tu60qx ("applied for a caregiver respite voucher"). The other is a copied article (p15cg7fl). Helper's "once" holds. | observed |
| Paid family caregiver / stipend (strict wording) | 93 | 84 | Many real posts (examples p10l8wam, p15b1ue4, p1rs0ge5). Not classified. These are mostly the same pay-for-care theme the helper found in Medicaid and IHSS. The helper's note "covered inside the Medicaid and IHSS reading" is **not true for 84 of 93**. | observed (existence), not-assessed (counts) |
| PCA, CDPAS, self-directed, cash and counseling (strict) | 25 | 21 | Other-state paid-care programs exist in the data. Not classified. | observed (existence), not-assessed |
| Structured Family Caregiving | 6 | 4 | p15b1ue4, p1ddk3co, p1t6wlq5, p1rs0ge5 are real. | observed |
| Medicare Advantage in-home benefit | 2 strict | 2 | Two asks. Too thin. Helper's "no users" holds. | observed |
| Church or faith group | 88 | 84 | Mixed: church friends helped (p17dcrwd), church "could not help" (p14uf7ds, p17sfjlq). Helper's "mostly passing" is plausible but not proven. | observed (sample), not-assessed (count) |
| Senior center | 100 | 98 | Not read. Helper's text contradicts itself: line 196 says 5 posts, line 232 says 8. | not-assessed |
| Caregiver coaching or care navigator | 25 | 25 | Mostly employer benefits and job posts. Too thin to judge. | observed (sample) |
| Hospital caregiver program | 2 strict | 1 | Too thin. | observed |
| AgingCare forum as support | 11 items | 9 | 3 caregivers say they use or used AgingCare (p1aijjhb, agingcare-499298, p125uikq). The rest are PDF file names in ALZConnected. Too thin. | observed |
| Well Spouse Association | 2 to 3 | 0 | Confirmed 1 caregiver (an online summit, p1lg4oxs). p1atw6p5 uses "wellspouse" as a word, not the group. | observed |
| Caregiver Action Network / Savvy Caregiver | 0 / 0 | 0 | Confirmed zero. National Alliance for Caregiving appears twice (a copied list and a news item). | proven (0 hits) |
| Lotsa, Meal Train, Cozi, CaringBridge, Teepa, NAMI, Wellthy | 3, 4, 2, 7, 4, 7, 2 | 0 | Counts reproduce (NAMI 7 versus the helper's 8, regex wording). | proven |
| Area Agency on Aging / council on aging | 96 to 120 | 89 | Not a candidate and not read. The helper's Part B ranks it at 32 posts (rank 13), above several included names. | not-assessed |

### 3c. "A real break appears only in hospice respite, PACE and IHSS"

| Claim | State | Source | Limit |
|---|---|---|---|
| By the helper's own tags, "break" appears in 11 candidates, not 3 (hospice 18, PACE 12, IHSS 4, franchise home care 3, Medicare GUIDE 3, Regional Center 3, named respite facilities 2, Meal Train 2, hospice hotline 1, Meetup 1, Papa Pals 1). | observed | `out_check3cd.txt` | Several are asks, not breaks. |
| **Fails.** The VA caregiver programs give breaks (see 3b) and are not in the claim. | observed | 3b VA row | Snippets only. |
| **IHSS "break" is weak.** The 4 break reports are: a father who turned the workers away (did not work), an "occasional caretaker", an IHSS worker who "mainly cleans the house", and a mother asking where to get respite. At most 1 or 2 are a break. | observed | p1jd8q64, p1pk41yo, p1ubklew, p1ssqrqc (read in full) | Judgment on what a "break" means. |
| PACE "12 break reports" is generous. 10 are label 1. Real rest (respite stay or day-center days): about 5 or 6 (p1bahk0o, p1b4mm45, p1buxxon, p1c28i82, p14t1yn1, p14pgf4l). Two are only plans (p1hvc21c, p1u8ryhm). | observed | `out_check4_headline.txt`, snippets | Judgment. |

### 3d. Facebook and Discord / WhatsApp

| Claim | State | Source | Limit |
|---|---|---|---|
| Facebook: of 12 support users, 2 worked, 4 mixed, 5 did not, 1 no outcome | proven | `out_check3cd.txt` | Counts of the helper's labels, which I did not re-read one by one. |
| "Another 6 used Facebook to find help and **none got it**" | observed, **overstated** | same file: 4 did not work, 2 no outcome | "none said they got it" is accurate; "none got it" is not. |
| "Facebook is the **only** community type with mostly bad reports" | **fails** | WhatsApp family chat: 4 of 5 did not work (`out_check3cd.txt`) | The helper does not count a family chat as a community. Say so, or drop "only". |
| The Facebook reports are biased. Most of these writers are posting on Reddit or ALZConnected and comparing it to Facebook ("I don't recommend FB any more. The people on this forum are..."). SYNTHESIS says Reddit praise is circular but does not say the Facebook complaints are the same effect. | inferred | alzconnected-77414-COMMENT15 and others | Not measured. |
| Discord: "8 asked". 2 of the 8 are asking for the link or the way into an **existing** server (p14w2jm7, p1ghdx77). 1 is a general ask (p1rlva01). About **5 distinct asks for a new group**. | observed | text of each, `out_check3cd.txt` | Judgment. |
| WhatsApp: "4 asked". 3 look like one writer (see 2d). 1 (p1s54boa) is for hospital sitters to share jokes. About **1 or 2 distinct asks**. | observed | 2d | Same-writer is inferred. |
| "Demand for Discord and WhatsApp groups is more than supply" | **not proven** | The data has no server or group sizes. The sidebar Discord for r/CaregiverSupport exists (p15upsyi, p1lmwx2m "enjoying it"). | A real supply count needs web research. |
| Corrected: **about 7 or 8 distinct asks (not 12)**; 2 users (Discord) and 1 organizer (WhatsApp). | observed | above | Same limits. |

---

## Check 4. Corrections list

Line numbers are in `SYNTHESIS.md` unless noted.

| # | File and line | What it says | What the evidence says | Size |
|---|---|---|---|---|
| 1 | L11, L118 (also L71 note) | "48 of 78 Medicaid reports are one NY CDPAP to PPL change in March and April 2025" | 48 mention CDPAP; **30** are dated Mar to Apr 2025. L241 already says 30. | **High** |
| 2 | L10, L25, L52, L74, L132 to L136, L240, L260 | Hospice respite: 23 reports, 27 hits all read | At least 9 more reports exist; 30 raw hits; **32 or more**. | High |
| 3 | L10 | "A real break appears only in hospice respite, PACE and IHSS (4)" | VA programs also; IHSS break is mostly cleaning. | High |
| 4 | L21 to L29, L84, Part C table | Candidates omit VA caregiver programs | **At least 19 posts**. Add a row (federal government program). | High |
| 5 | L33, L39, L84, L280, L290 | Meals on Wheels: 6 reports, 1 parent refused | About 45 real mentions, about 12 refused or canceled. Count is a read of 6 of 64 hits. | Medium (conclusion likely holds) |
| 6 | L14, L40, L157 | 12 asks for Discord or WhatsApp; supply "tiny" | About 7 or 8 distinct asks; 3 WhatsApp posts look like one person; supply not measured. | Medium |
| 7 | L12 | Facebook is "the only" community with mostly bad reports; "none got it" | WhatsApp family chat is 4 of 5 bad; 4 of 6 did not work and 2 said nothing; writers are biased toward Reddit or ALZConnected. | Medium |
| 8 | L26, L75, L137 to L139 | Alzheimer's Association: 19 reports, 5 worked | 9 of 19 are from the Association's own forum (Reddit-only 10); 3 worked, 2 are recommendations only. | Medium |
| 9 | L12, L28, L77, L147 to L148 | Reddit: 55 reports, 34 worked | p158bctp is an app maker. **54 and 33.** | Low |
| 10 | L64 | "Never the same person twice" with a short exceptions list | Add the 3 WhatsApp posts (p1x3k3jd, p1x49fv6, p1x4ejkv). | Low |
| 11 | L153 | Quote marks around "this forum saved me" | Not a real quote. Remove the marks. | Low |
| 12 | L196 vs L232 | Senior center 5 posts versus 8 posts | Pick one. | Low |
| 13 | L76, L142 to L145 | "37 support-group reports" | It is a count of the 41 read, out of at least 114 coded and 347 raw hits. Say "37 read". | Low |
| 14 | L282 (filters table) | Stipend and paid-caregiver hits "covered inside the Medicaid and IHSS reading" | 84 of 93 strict hits were not read. | Medium |
| 15 | L134 | Hospice quote "I am glad they offered respite..." shown as a good example | The same post says she did not take it until a social worker pushed. Fine as a quote, but it is "used under pressure". | Low |

Items I checked and found **correct**: the section 4 table math (34 of 34 rows), Medicaid plus IHSS 155 with 151 about pay, 7 worked, PACE 8/7/6 and 7 spouses, hospice 1/3/8 and 18 of 23 about a break, Facebook 2/4/5, Alzheimer's 7 used, support group 16 asking, the 255 Medicaid raw hits, FCA 1 / CAN 0 / Savvy 0, Lotsa 3, Cozi 2, Meal Train 4, CaringBridge 7, Wellthy 2, Teepa 4.

---

## Verdict table

"Reports" means caregiver posts labeled 1 to 3. The target is 15 or more independent reports. "Independent" cannot be proven because the data has no author names (limit for every row).

| Candidate | Kind | Helper count | Count after audit | Verdict | Confidence | Enough to include (15 or more)? |
|---|---|---|---|---|---|---|
| Medicaid waiver and state paid-family-caregiver programs (HCBS, CDPAP, others) | Government program | 78 (48 NY) | 78 read; **30 dated Mar-Apr 2025 CDPAP**, 30 with no CDPAP/PPL text | HOLD WITH CORRECTIONS (#1) | Medium-high on count, medium on labels | **Yes: 78, and 30 outside CDPAP.** Pay, not rest. |
| IHSS (California) | Government program | 77 | 77 (3 shared with PACE) | HOLD (break claim corrected, #3) | High on count | **Yes: 77** |
| PACE | Government program | 41 | 41 | HOLD | High | **Yes: 41** |
| Hospice respite (Medicare benefit) | Government benefit, run by hospices | 23 | **32 or more** | HOLD WITH CORRECTIONS (#2) | Medium | **Yes: 32+** |
| Alzheimer's Association | Nonprofit | 19 (7 used) | 19 (7 used; **10 Reddit-only**); 3 worked | HOLD WITH CORRECTIONS (#8) | Medium | **Yes at 19 total. No at 10 if its own forum is excluded.** Owner decides. |
| Support groups (any sponsor) | Mixed: nonprofits, hospitals, peers | 37 | 37 read of 114+ | HOLD WITH CORRECTIONS (#13) | Medium | **Yes: 37 read** |
| Facebook caregiver groups | Workaround (Meta platform) | 21 | 21 | HOLD WITH CORRECTIONS (#7) | Medium | **Yes: 21** (with the bias note) |
| Reddit communities | Workaround (circular) | 55, 34 worked | **54, 33** | HOLD WITH CORRECTIONS (#9) | High | Description only. Not independent. |
| ALZConnected | Nonprofit forum (circular) | 28, 19 worked | 28 (4 threads repeat) | HOLD | Medium | Description only. |
| **VA caregiver programs** (new) | Government program | not counted | **19 or more** | NEW: helper omitted it (#4) | Medium (snippets only) | **Yes: 19+** |
| Discord caregiver servers | Workaround | 10 reports, 8 asks | about 5 distinct asks, 2 users | HOLD WITH CORRECTIONS (#6) | Medium | **No: 10 (5 distinct asks)** |
| WhatsApp caregiver groups | Workaround | 5 reports | 2 to 3 distinct | HOLD WITH CORRECTIONS (#6, #10) | Medium | **No: 5, about 3 people** |
| Meals on Wheels | Nonprofit network | 6 | **about 45** | FAIL on count (#5); "not a relief competitor" probably holds | Medium | Count would pass, but the need is food, not relief. The helper's reason still stands. |
| CaringBridge 6, Meal Train 3, Lotsa 0, Cozi 0, Teepa 4, NAMI 4, Al-Anon 3, Wellthy 2, Torchlight 1, Papa Pals 1, Medicare GUIDE 3, Regional Center 4, FCA 0, CAN 0, Savvy 0, Well Spouse 1 | Nonprofits, businesses, programs | as listed | Counts reproduce for those I re-searched | HOLD | High (raw counts), medium (labels) | **No for all.** Largest is 6. |
| Area Agency on Aging, adult day programs, senior center, church groups | Government program, generic type, generic, workaround | not carried to Part C | Not assessed (96, 35 to 101, 100, 88 hits) | **Not assessed** | n/a | Unknown. The helper's own Part B ranks Area Agency on Aging and adult day above several included names. |

Plain answer to "is the evidence enough to include each as a competitor of 'help for worn-out caregivers'?":
- **Yes (15 or more reports):** Medicaid and state paid-family programs, IHSS, PACE, hospice respite, VA caregiver programs, Facebook groups, support groups (any sponsor). The Alzheimer's Association passes only if ALZConnected members count.
- **Include, but describe only:** Reddit and ALZConnected (circular).
- **No (fewer than 15):** Discord, WhatsApp, CaringBridge, Meal Train, Teepa, NAMI, Al-Anon, Wellthy, Torchlight, Papa Pals, Medicare GUIDE, Regional Center, FCA, CAN, Savvy, Well Spouse, Lotsa, Cozi.
- **Count enough, need says no:** Meals on Wheels (food).
- **Pay versus rest:** none of the government pay programs (Medicaid, IHSS) give rest as their main use. Rest appears in hospice respite, PACE (day center and respite) and the VA programs.

---

## Not checked

- I read **one reader's** 50 posts. I did not re-label all 756. The 2% error rate has a wide range.
- Meals on Wheels, VA, church and hospice-missed numbers come from 240-to-300-character snippets, not full posts. Counts are approximate ("about", "at least").
- I did not classify the 84 unread "paid family caregiver" hits, the 21 PCA/CDPAS hits, the 100 senior center hits, the 96 Area Agency on Aging hits, or the 35 adult day hits.
- I did not re-check the helper's other label fields (`used_for`, `blockers`) except where a claim leaned on them. Section 6 details such as "18 of 39 IHSS asks are denials" and "24 IHSS hits are not caregiver use" were not re-derived.
- I did not check the 73 support-group posts coded by earlier readers, or the 859 unread Subreddit-praise posts.
- Dates: I used the post date in the saved data. I did not check it against the live site.
- Whether any program is still running, its cost, or its rules. I used no web pages. The NY CDPAP-to-PPL change dates come only from the posts themselves.
- "Independent person" cannot be proven in any row (no author names in Reddit data; forum names hidden).
- The helper's decision files (`decisions/*.txt`) and its scripts were not run. I rebuilt the counts from raw data with my own scripts.
