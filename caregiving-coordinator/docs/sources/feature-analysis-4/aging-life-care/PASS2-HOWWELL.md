# Geriatric care managers / Aging Life Care: how well do the features work for families? (PASS 2)

Date: 2026-11-06. PASS 2 (new independent evidence). Evidence states: reported = a person said it (all counts below); documented = published text; observed/inferred are not used for any count. Paths start at docs/sources/ unless shown in full. Reddit usernames were never saved (so two comments could come from one person; assumed different). Pass 1 counts are read from PASS1-HOWWELL.md in the same folder; this pass adds only people NOT in pass 1 (comments, forums, review pages). Comments by the original poster of a thread are left out when pass 1 already counted that post.

Care managers are many local firms; one report is about one firm. Some posters named firms that are not Aging Life Care Association (ALCA) members; those are flagged. AgingCare (owner: A Place for Mom) hosts three of the threads; flagged.

## Short answer

- **NEW independent reports: 43** (21 Reddit comments, 20 AgingCare forum answers, 2 news-column families). Pass 1 had 14 families (plus 4 other). Combined: **57** care-manager reports. The 15 target is met only for F8 (35 new, 43 combined with pass 1). Other cells, new reports: F1 10, F3 10, F2 5, F4 5, F5 4, F6 2 (neither is a login), F9 2, F10 2.
- F8 Personal guidance (new): 29 WORKED, 4 DID NOT WORK, 2 MIXED. Praise is about one phone number to call when the family lives far away: appointments, hospital visits, weekly checks. Complaints: cost, a manager who "was pretty useless", aides who did not show up.
- F4 Refusing parent: 3 new WORKED, 2 DID NOT WORK. It works when a parent accepts the person (a father who talks more easily to the manager than to his child). It fails when parents will not accept a stranger (G34) or the caregiver will not accept help (G36).
- F2: 4 WORKED, 1 MIXED. Examples: assessment report used with a long-term-care insurance company (G03); in-home assessment used to start a POA (G01); help with insurance (G11). One mixed case: slow on a pooled-trust request that turned out not needed (G02).
- F3 cost: 5 families say it was worth the price; 1 says too costly; 2 give bills only. Hourly rates quoted by families: $60 to $175. ALCA says $150 to $350 (KFF).
- F6 Account access: no report of a manager logging into a parent's accounts. 2 reports about powers of attorney and mail (G01, G31).
- F9 Behavior: 1 WORKED (father combative with his child, G28), 1 DID NOT WORK (husband kicked out of nursing homes, G37).
- F10: 2 WORKED (sounding board G33; a manager who went through the same with her own mother G38). Peer support groups are a separate thing.

## (a) Table: one row per cell

| Cell | Capability state (from EVIDENCE.md / pass 1) | NEW WORKED | NEW DID NOT WORK | NEW MIXED | NEW NO VERDICT | NEW total | Pass 1 (W / D / M) | COMBINED (W / D / M) |
|---|---|---|---|---|---|---|---|---|
| F1 Relief finder | YES (people) | 9 | 0 | 1 | 0 | 10 | 0 / 0 / 0 | 9 / 0 / 1 |
| F2 Eligibility and applications | VERIFY -> now supported | 4 | 0 | 1 | 0 | 5 | 0 / 1 / 0 | 4 / 1 / 1 |
| F3 Paying for relief | YES (fee) | 5 | 1 | 2 | 2 | 10 | 0 / 1 / 1 | 5 / 2 / 3 |
| F4 Refusing parent support | YES (claim) | 3 | 2 | 0 | 0 | 5 | 2 / 0 / 0 | 5 / 2 / 0 |
| F5 Relatives cover time | YES (people) | 4 | 0 | 0 | 0 | 4 | 0 / 1 / 1 | 4 / 1 / 1 |
| F6 Account access | VERIFY -> partly | 2 | 0 | 0 | 0 | 2 | 0 / 1 / 0 | 2 / 1 / 0 |
| F8 Personal guidance | YES | 29 | 4 | 2 | 0 | 35 | 3 / 3 / 2 | 32 / 7 / 4 |
| F9 Behavior and hard talks help | YES (claim) | 1 | 1 | 0 | 0 | 2 | 0 / 0 / 0 | 1 / 1 / 0 |
| F10 People who understand | VERIFY -> weak | 2 | 0 | 0 | 0 | 2 | 0 / 0 / 0 | 2 / 0 / 0 |

Pass 1 also had F1 1 no-verdict and F8 1 no-verdict; not repeated in the table. A report with two cells is counted once in each cell.

## (b) Every new report (exact quote, source file, class, audience)

| ID | Cells (class) | Exact quote (max 20 words) | Audience | Source file | Limit |
|---|---|---|---|---|---|
| G01 | F2: WORKED; F6: WORKED; F1: WORKED | "in order to activate the POAs Mom had already set up a few years prior" | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-raw.jsonl (thread 13wp1no, comment jmjrllo); https://www.reddit.com/comments/13wp1no/ | Care manager's in-home assessment backed doctor statements needed to activate POAs. F6 is the power-of-attorney step, not logging into accounts. |
| G02 | F2: MIXED; F3: MIXED | "Care manager didn’t seem to prioritize this request and took a very long time" | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-raw.jsonl (thread 19ax1dy, comment kiuijn6); https://www.reddit.com/comments/19ax1dy/ | Found through Aging Life Care Association. Pooled trust effort ended up not needed. |
| G03 | F2: WORKED; F3: WORKED; F8: WORKED | "wrote a report that we used with the LTC company" | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-firecrawl-found-raw.jsonl (thread 1liu3zd, comment mzetcop); https://www.reddit.com/comments/1liu3zd/ | Report used for a long-term-care insurance claim; text ends mid-sentence in the saved copy. |
| G04 | F8: WORKED; F1: WORKED; F5: WORKED | "She's my eyes and ears when I can't be there." | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-raw.jsonl (thread 1qldy9o, comment o1gb9tv); https://www.reddit.com/comments/1qldy9o/ | Lives 8 hours away; pays about $500 a month, range $250 to $1500. |
| G05 | F8: WORKED | "a wonderful RN who visits our LO in her assisted living facility weekly" | unclear | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-raw.jsonl (thread 1qldy9o, comment o1dqu0m); https://www.reddit.com/comments/1qldy9o/ | RN from a private home health agency, not shown to be an Aging Life Care member. |
| G06 | F1: MIXED; F8: MIXED | "I would have loved more help but basically got a list of places to call for facility openings." | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-firecrawl-found-raw.jsonl (thread 1mtlwms, comment n9f5u68); https://www.reddit.com/comments/1mtlwms/ | Used managers in 2 states; the first was 'great', the second gave only a list. |
| G07 | F8: WORKED; F4: WORKED | "Yes, it was a game changer." | unclear | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-firecrawl-found-raw.jsonl (thread 1mtlwms, comment n9dwhmk); https://www.reddit.com/comments/1mtlwms/ | Person had earlier refused help; manager used a hospital stay to get a plan in place. Text read is partial. |
| G08 | F8: DID NOT WORK; F3: DID NOT WORK | "They were pretty useless, but it was more about how they didn’t have reliable help themselves." | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-firecrawl-found-raw.jsonl (thread 1mtlwms, comment n9deqbx); https://www.reddit.com/comments/1mtlwms/ | Care manager plus aides cost $15-20k a month; memory care $9k. Writer thinks it is due to location. |
| G09 | F5: WORKED; F4: WORKED | "She was super helpful in getting all family members to accept the reality of the situation" | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-firecrawl-found-raw.jsonl (thread 1mtlwms, comment n9dcmis); https://www.reddit.com/comments/1mtlwms/ | An 'elder care consultant', not shown to be an Aging Life Care member. |
| G10 | F3: USED, NO VERDICT | "Sitting with my mom in the ER, $100/hr." | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-firecrawl-found-raw.jsonl (thread 1mtlwms, comment n9dho2m); https://www.reddit.com/comments/1mtlwms/ | Cost report only; has not seen the first bill; no verdict. |
| G11 | F8: WORKED; F2: WORKED | "It’s really helped a lot." | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-firecrawl-found-raw.jsonl (thread 19aogut, comment kirra1b); https://www.reddit.com/comments/19aogut/ | Mom in assisted living with dementia; manager visits weekly and helps sort insurance. |
| G12 | F8: WORKED; F1: WORKED | "Our GCM put me in touch with resources that I wouldn't have found on my own" | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-firecrawl-found-raw.jsonl (thread 1onj30l, comment nmyip7r); https://www.reddit.com/comments/1onj30l/ | Also says assessment showed mom was worse than they thought. |
| G13 | F8: WORKED | "I used a Geriatric care manager who was my lifeline." | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-firecrawl-found-raw.jsonl (thread 1onj30l, comment nmyel6u); https://www.reddit.com/comments/1onj30l/ | Independent, hourly, 5 years until mom died. |
| G14 | F8: DID NOT WORK | "We worked with one who wasn’t worth his weight" | unclear | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-firecrawl-found-raw.jsonl (thread 1onj30l, comment nmya5v8); https://www.reddit.com/comments/1onj30l/ | Quote cut before a swear word. |
| G15 | F8: WORKED; F1: WORKED | "for us, it's worth every cent." | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-firecrawl-found-raw.jsonl (thread 1onj30l, comment nmx9t26); https://www.reddit.com/comments/1onj30l/ | Agency with a licensed social worker; helped land a memory care bed. Not shown to be an Aging Life Care member. |
| G16 | F8: WORKED | "honestly, we were a little shocked at her findings." | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-firecrawl-found-raw.jsonl (thread 1fp4zmt, comment low02sl); https://www.reddit.com/comments/1fp4zmt/ | Assessment from across the country found the parents less safe than thought. |
| G17 | F8: WORKED; F3: USED, NO VERDICT | "the care manager allows us to keep our lives" | adult child (in-law) | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-firecrawl-found-raw.jsonl (thread 1fp4zmt, comment louyh8p); https://www.reddit.com/comments/1fp4zmt/ | MIL lives 1000 miles away; monthly bills $1500 to $9000. |
| G18 | F8: WORKED | "I hired a GCM to manage my moms care for 2 years" | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-firecrawl-found-raw.jsonl (thread 1jgq2n8, comment mjkfmyj); https://www.reddit.com/comments/1jgq2n8/ | Mom stayed at home until death. |
| G19 | F8: WORKED; F5: WORKED | "It was very helpful for me, as there was enough work to do behind the scenes" | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-firecrawl-found-raw.jsonl (thread 1tttk40, comment op4xfn6); https://www.reddit.com/comments/1tttk40/ | Manager is a licensed social worker; visited Mom weekly. |
| G20 | F8: WORKED | "She helped me through all stages of my mom's care until she passed in 2025." | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-firecrawl-found-raw.jsonl (thread 1xm1580, comment 19s1iwgjc95id); https://www.reddit.com/comments/1xm1580/ | Found from the Aging Life Care Association list. |
| G21 | F8: DID NOT WORK | "the staffing was not good and we constantly had issues we had to discuss with them" | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-reddit-threads-gcm-firecrawl-found-raw.jsonl (thread 1ri1fkn, comment o82t99i); https://www.reddit.com/comments/1ri1fkn/ | A 'care management company' that sent aides; not an Aging Life Care firm. |
| G22 | F8: WORKED; F1: WORKED | "We were satisfied with the assessment and the recommendations she made." | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-489163-gcm-worth-it-2026-11-06.txt | AgingCare forum (owned by A Place for Mom). Answer 'Alva'. |
| G23 | F5: WORKED; F8: WORKED | "but she has seriously saved my bacon a few times." | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-489163-gcm-worth-it-2026-11-06.txt | Answer posted 08/14/2024 15:16; GCM called a 'concierge sibling'. |
| G24 | F8: WORKED | "knowing I can call her in an emergency is critical to my mental health" | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-489163-gcm-worth-it-2026-11-06.txt | Answer posted 08/12/2024; lives 4 hours away. |
| G25 | F3: WORKED | "only pay for the hours actually used" | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-489163-gcm-worth-it-2026-11-06.txt | Contract term; answer posted 08/11/2024 12:57. |
| G26 | F8: WORKED; F3: WORKED | "and have very glad we did" | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-489163-gcm-worth-it-2026-11-06.txt | $60 an hour; picked by elder attorney. |
| G27 | F8: WORKED | "I think it was worth the cost" | other (older adult, for self) | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-489163-gcm-worth-it-2026-11-06.txt | Care receiver herself, aged 87. |
| G28 | F4: WORKED; F9: WORKED; F8: WORKED | "It has been a huge life-saver for me and has helped reduce a lot of the stress I was feeling." | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-489163-gcm-worth-it-2026-11-06.txt | Father was combative with the writer; manager handles his medical care. |
| G29 | F8: WORKED | "I have found its worth it." | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-489163-gcm-worth-it-2026-11-06.txt | Manager also acts as bridge to assisted living. |
| G30 | F8: MIXED; F3: MIXED | "BUT, and here is the BUT, he was expensive" | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-485228-gcm-difficult-parents-2026-11-06.txt | Great manager; ended contract in 2020 because of cost. |
| G31 | F8: WORKED; F6: WORKED | "she has been invaluable in visiting him" | other (sibling and fiduciary) | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-485228-gcm-difficult-parents-2026-11-06.txt | Manager goes through brother's mail and forwards it; does not log into accounts. |
| G32 | F8: WORKED | "and it's worth it; she is very helpful." | spouse | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-485228-gcm-difficult-parents-2026-11-06.txt | Used for sister then husband with dementia; $125 an hour. |
| G33 | F8: WORKED; F10: WORKED | "The GCM has also been a helping sounding board for me" | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-485228-gcm-difficult-parents-2026-11-06.txt | Manager also handles hospital decisions; writer has a difficult father. |
| G34 | F4: DID NOT WORK | "my parents just did not get the concept" | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-442693-gcm-worth-it-2026-11-06.txt | Parents did not accept a manager; hired before they were frail. |
| G35 | F1: WORKED; F3: WORKED | "The specialist we ended up hiring often recommended services that were free." | unclear | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-442693-gcm-worth-it-2026-11-06.txt | Interviewed three; one partly paid by services she recommended. |
| G36 | F8: WORKED; F3: WORKED; F2: WORKED; F4: DID NOT WORK | "has helped arrange a way to pay for the help" / "getting the caregiver to accept help" | unclear | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-442693-gcm-worth-it-2026-11-06.txt | 'Aging Care Specialist', 6 hours away. She could not get the caregiver to accept help. |
| G37 | F8: DID NOT WORK; F9: DID NOT WORK | "In our case, it was a waste of money." | spouse | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-442693-gcm-worth-it-2026-11-06.txt | Husband was being asked to leave nursing homes for bad behavior. |
| G38 | F8: WORKED; F10: WORKED | "she had gone through similar situations with her own mother" | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-442693-gcm-worth-it-2026-11-06.txt | Manager also 'like a counselor'. |
| G39 | F8: WORKED | "They can be immensely helpful in a variety of areas where help is needed." | adult child (in-law) | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-442693-gcm-worth-it-2026-11-06.txt | Hired one years ago for MIL; brief. |
| G40 | F8: WORKED; F1: WORKED | "It's been a huge help to me." | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-442693-gcm-worth-it-2026-11-06.txt | Manager works for the same company as the home care team. |
| G41 | F1: WORKED | "the care manager had all the experience (of options and costs) that they didn't have" | other (ex-spouse's family) | docs/sources/feature-analysis-4/aging-life-care/PASS2-agingcare-forum-question-442693-gcm-worth-it-2026-11-06.txt | Emergency placement fixed in three days. |
| G42 | F8: WORKED | "they knew what to do when I wouldn't have" | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-kff-health-news-aging-life-care-managers-2026-10-14.txt | News column; person chosen by the writer. Bernstein, Aging Well Eldercare. |
| G43 | F1: WORKED; F8: WORKED | "and eased my fears that something urgent might strike the moment I left on a vacation or a work trip" | adult child | docs/sources/feature-analysis-4/aging-life-care/PASS2-kff-health-news-aging-life-care-managers-2026-10-14.txt | News column; the writer's own experience; shared cost with her sister. |

### Read but NOT counted (and why)
- Vendors or suspected promotion: three comments praising "Arosa" with similar wording (1liu3zd/ncn0bzx, 1mtlwms/of2ztpo, 1plo268/nu2sdyh); an Arosa staff reply (1n9bovr/nq1ausv); Alenta Service (1mtlwms/p09hvdc); Ability Link staff (several); a comment 1q62c27/ny8qhcx written like an advert. Arosa-linked comments are excluded because the same brand appears in a company reply.
- Care managers speaking about their own work (not family): 1mtlwms/ni60dwu, 1mtlwms/neqzixj, 19aogut/l4xpn8q, 19aogut/neqvff2, 1onj30l/nmxb7r4, 1mtlwms/n9d3ebh, 6xbth2/dmexu3b, ghwpry (several).
- Second-hand (friend, in-law, neighbor): 1mtlwms (friend story ipw4vzn in xmuolb), AgingCare G11 and G12 in 489163, H4 in 485228, G6 research only.
- Advice only or asks: 1464e7r/jnq1phl (still working with one, no verdict), 1mtlwms/n9cyjkb and n9cvirx (planning), 1lpvr2z/n0xy5hr, 1q62c27/ny4jkbz, 1xgwk7r, 13wp1no/jmd9o3k and jmcvfci (advice), 19ax1dy/kiod2wi (medical group's own care manager phoned for blood pressure; not a care manager firm).
- OP replies already counted in pass 1: 1sl9uat, 1viweky, 1woat2e.
- A gerontologist (doctor) is not a care manager: AgingCare 489163 answer 'As a caregiver for my husband', 442693 gerontologist answer.
- 17 ask-only Reddit posts from pass 1 remain ask-only.

## (c) Searches, filters, raw hits, and what was blocked

| Step | Raw hits |
|---|---|
| Pass 1 archive posts that name care managers or similar words, thread comments fetched by link_id | 102 posts with comments -> 1,392 comments; 54 name a care-manager term; 6 first-hand reports kept |
| Firecrawl web search (reddit.com only): "geriatric care manager hired worth it experience mom dementia" | 25 results; 16 post ids fetched (others not about GCMs) |
| Those 16 posts, comments by link_id | 343 comments; ~60 mention care managers; 15 first-hand reports kept |
| Firecrawl web search, forums and news (excluding aginglifecare.org, aplaceformom, reddit, trustpilot, usatoday, glassdoor, yelp, bbb) | 20 results: used 3 AgingCare question pages (442693, 485228, 489163) and KFF Health News; skipped vendor and blog pages |
| Firecrawl web search restricted to agingcare.com, alzconnected.org, dailycaring.com, caregiver.org, carepatrol.com | 15 results; used 2 more AgingCare threads |
| AgingCare 489163 / 485228 / 442693 | 19 + 10 + 14 answers; 8 + 4 + 8 counted (20 total) |
| KFF Health News, Oct. 14, 2026 | 2 family accounts counted; ALCA survey (about 200 respondents, 93% / 99%) recorded as documented, NOT independent |
| Arctic Shift keyword search (body/post text, year windows) | timeouts; the output files were empty (deleted) and I stopped the job; no log kept |

**Blocked or skipped (robots.txt read 2026-11-06):** aginglifecare.org (owner rule; ALCA research blog not read); caring.com forums (robots.txt returned 403; skipped); bbb.org (ClaudeBot group); nytimes.com archive (not fetched); AARP page (not fetched; pass 1 has it); Glassdoor, Yelp, USA Today (ClaudeBot disallowed); Reddit pages directly (not fetched); Facebook groups (not fetched).

## (d) Which VERIFY cells are now settled, and by what

| Cell | Settled? | Evidence |
|---|---|---|
| F2 Eligibility and applications | Yes, partly | Documented (KFF): care managers "Deal with insurers, including Medicare and Medicaid" and one starts the day on "an online Medicaid recertification form". Reported: G01, G03, G11, G36 WORKED; G02 MIXED. Not shown: a care manager filing a first Medicaid application end to end. |
| F6 Account access | Partly | G01 (POA step) and G31 (forwards mail). 0 reports of logging into a parent's bank, insurer or portal. State: no evidence either way for logins. |
| F10 People who understand | Weak | 2 reports (G33, G38). No report of a care manager connecting people to peers. |
| F9 Behavior help | Weak | 1 W (G28) and 1 D (G37). Capability claim from pass 1 text stays company text. |
| F4 Refusing parent support | Settled as "sometimes" | 3 W and 2 D new; plus 2 W in pass 1. Fails when the parent or caregiver will not accept the person. |
| F5 Relatives cover time | Yes | 4 W (G04, G09, G19, G23) plus KFF text "mediating between family members". The manager stands in for the missing relative. Pass 1 has 1 D and 1 M where a relative would not cooperate. |
| F1 Relief finder | Yes | 9 W, 1 M. Respite: 0 reports; adult day: 0. |

## (e) Not checked

- Aging Life Care Association member research (blocked by owner rule), Google and Yelp reviews of local firms, BBB for care manager firms, Facebook groups, Caring.com forums.
- Whether any firm named is an ALCA member (unknown for most; G01 G02 G20 G22 mention ALCA lists).
- Reddit comments that do not name a care manager but answer care-manager threads. Fresh Arctic Shift keyword search (timeouts).
- F9 and F10 with their own keywords (for example "dementia behavior" plus care manager).
- Cost claims were not verified against firm price pages.
