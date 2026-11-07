# Geriatric care managers / Aging Life Care: how well do the features work for families? (PASS 1, saved data only)

Date: 2026-11-06. No website was scraped. Paths are under `docs/sources/` unless they start with `feature-analysis-4/`. States: every count is **reported** (a person said it in a post). Care managers are many local firms, so one report is about one firm.

## Short answer

- First-hand reports about hiring a care manager or elder care advisor: **14 families** (16 posts are in the table; one of the families wrote 7 posts about the same mother, and 3 of those posts are in the table). Plus 3 placement-advisor reports and 1 Solace report in separate tables. This is below the 15 target. The saved Reddit text is posts only, no replies.
- By class (families): Guidance (F8): 3 WORKED, 3 DID NOT WORK, 2 MIXED, 1 used with no verdict. Parent who refuses (F4): 2 WORKED, 0 DID NOT WORK. Relatives (F5): 1 DID NOT WORK, 1 MIXED. Eligibility (F2): 1 DID NOT WORK. Behavior help (F9) and support groups (F10): 0 reports.
- Cost complaints: 1 strong (a firm billed $3,202 in 2 weeks), 1 retainer complaint, 1 quote of $20,000 for a year (law firm program, not a care manager firm). Cost shows up in 4 posts.
- 17 more posts (16 different texts) ask "has anyone used a geriatric care manager, is it worth it?" That shows demand and doubt, but no answers were saved.

## (a) Table: one row per cell

A family counted once per cell. The 7-post family (stepfather story) is in F8 (WORKED) and F5 (MIXED) once each.

| Cell | Capability (EVIDENCE.md) | WORKED | DID NOT WORK | MIXED | USED, NO VERDICT | Total reports |
|---|---|---|---|---|---|---|
| F1 Relief finder | YES (people) | 0 | 0 | 0 | 1 | 1 |
| F2 Eligibility and applications | VERIFY | 0 | 1 | 0 | 0 | 1 |
| F3 Paying for relief | YES (fee) | 0 | 1 | 1 | 1 | 3 |
| F4 Refusing parent support | YES (marketing claim) | 2 | 0 | 0 | 0 | 2 |
| F5 Relatives cover time | YES (people, not a tool) | 0 | 1 | 1 | 0 | 2 |
| F6 Account access | VERIFY | 0 | 1 | 0 | 0 | 1 |
| F8 Personal guidance | YES | 3 | 3 | 2 | 1 | 9 |
| F9 Behavior and hard talks help | YES | 0 | 0 | 0 | 0 | 0 |
| F10 People who understand | VERIFY | 0 | 0 | 0 | 0 | 0 |

A report that names two cells is counted once in each cell. Cost (F3) rows: 1 DID NOT WORK (p1x0fqwe), 1 MIXED (p1woat2e), 1 USED NO VERDICT (p1mtvh5w).

## (b) The reports behind each count

| Post id | Cell | Class | Quote (exact, max 20 words) | Audience | Source file and link | Limit |
|---|---|---|---|---|---|---|
| p1sl9uat | F5 | DID NOT WORK | "I hired a Geriatric Care Manager. He lost his mind on me." | adult child | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/CaregiverSupport/comments/1sl9uat/ | Brother refused the GCM; the GCM could not make him help. Brother also "won't return the GCM's calls". |
| p1x4gtt9 | F8 | DID NOT WORK | "it just feels like more paperwork than help" | adult child | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/CaregiverSupport/comments/1x4gtt9/ | Post says "Geriatric Caregiver"; assumed to mean care manager (inferred). |
| p1woat2e | F8+F3 | MIXED | "They were an absolute godsend when my mom, who died last year, careened from crisis to crisis" | adult child | docs/sources/reddit/arctic-shift-2026-11-03/posts_targeted.jsonl https://www.reddit.com/r/eldercare/comments/1woat2e/ | Now pays "a retainer" for monthly check-ins and is "dissatisfied with a number of things". |
| p1er9pkg | F8 | WORKED | "I even have a private care manager assisting me to take some of the burden off of myself." | adult child | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/CaregiverSupport/comments/1er9pkg/ | No detail on what the manager does. May be the same author as p1d98a7r (inferred from wording). |
| p1d98a7r | F8 | MIXED | "The social worker is encouraging me to let me my mom's son again" | adult child | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/CaregiverSupport/comments/1d98a7r/ | Hired a social worker at a "care management company"; poster still cannot relax. May be same author as p1er9pkg. |
| p1p1nazq | F4+F8 | WORKED | "The care manager talked to me for a long time and was super helpful and sympathetic." | adult child | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/AgingParents/comments/1p1nazq/ | Title says the care manager's advice ("Prove me wrong") worked. Unclear if private GCM or clinic care manager. |
| p1viweky | F4 | WORKED | "so I send her with a care manager instead, who talks to me after" | adult child | docs/sources/reddit/arctic-shift-2026-11-03/posts_targeted.jsonl https://www.reddit.com/r/dementia/comments/1viweky/ | Mother is angry at daughters; care manager goes to doctor visits instead. Post is mostly about a doctor, not the manager. |
| p1mxef8i | F8 | WORKED | "I have a care manager who is at the hospital with my mom" | adult child (stepfather in the story) | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/AgingParents/comments/1mxef8i/ | Likely same family as p1meut37, p1mht9jt, p1mj5yyg, p1mbdkw4, p1n3ht5l, p1nlgdmz (inferred from story). Counted as ONE family. |
| p1meut37 | F5 | MIXED | "He avoided her calls. Which made her decide there was no way my mom could go home." | adult child (stepfather in the story) | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/AgingParents/comments/1meut37/ | Same family as p1mxef8i. Advisor still gave a verdict; the stepfather would not talk to her. |
| p1mht9jt | F5 | MIXED | "I called my elder care advisor. She was speechless." | adult child (stepfather in the story) | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/AgingParents/comments/1mht9jt/ | Same family. Advisor could not stop the stepfather from taking mom home; she "said she'd try to get through to him". |
| p1kxe3qv | F1 | USED, NO VERDICT | "I hired a care manager to help her with dr appts" | adult child | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/AgingParents/comments/1kxe3qv/ | Manager also tours assisted living places; no judgment of how it went. |
| p16jpagx | F2 | DID NOT WORK | "Elder Care Manager who told me that there are no options until she needs nursing home care" | adult child | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/AgingParents/comments/16jpagx/ | Short; no detail on what was asked. |
| p1x0fqwe | F3+F8+F6 | DID NOT WORK | "took POA of my mother, billed $3,202 in 2 weeks, and pushed assisted living" | adult child | docs/sources/reddit/arctic-shift-2026-11-03/posts_targeted.jsonl https://www.reddit.com/r/eldercare/comments/1x0fqwe/ | Eldercare advisors/fiduciary firm, not shown to be an Aging Life Care member. Strongest cost and account-access complaint. |
| p1xgwk7r | F8 | DID NOT WORK | "every option on the table was just more and more work for me" | adult child | docs/sources/reddit/arctic-shift-2026-11-03/posts_targeted.jsonl https://www.reddit.com/r/dementia/comments/1xgwk7r/ | "Consults" with lawyers, social workers and GCMs; unclear which advice failed. |
| p1cp6hth | F8 | USED, NO VERDICT | "an elder care management company said why not get her back in her own home for a 60 day trial" | other (legal guardian of a friend) | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/CaregiverSupport/comments/1cp6hth/ | Poster is overwhelmed afterward but does not blame the company. |
| p1mtvh5w | F3 | USED, NO VERDICT | "The fee is $20,000 for the first year and then $4,500 annually." | adult child | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/AgingParents/comments/1mtvh5w/ | A law firm "elder care coordinator" program is only being considered; poster asks if it is worth it. |

### Placement-style senior advisors (APFM-type, not care managers)

| Post id | Cell | Class | Quote | Audience | Source | Limit |
|---|---|---|---|---|---|---|
| p1cr1bvr | F1+F3 | MIXED | "she was nice but it felt a little scammy that she is free to use" | unclear | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/AgingParents/comments/1cr1bvr/ | Local "care advisor" paid by facility referral fees; not a care manager. |
| p1piot7c | F1 | MIXED | "summarized the visit to me via email, capturing well what I believe her desires are" | adult child | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/AgingParents/comments/1piot7c/ | Advisor also sent her to a financial advisor; poster asks if that is a red flag. |
| p1l7p30b | F1 | DID NOT WORK | "Coastal Senior Advisors – Possible Scam Alert (Port St. Lucie, FL)" | unclear | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/AgingParents/comments/1l7p30b/ | Title only; the post body is empty. |
| p1r08qm4 | F3 | USED, NO VERDICT | "I spoke to a Solace advocate that we gave in place now, she thinks medical bankruptcy may be an option." | adult child | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl https://www.reddit.com/r/CaregiverSupport/comments/1r08qm4/ | Solace is a rival service, not a care manager firm. |

### Read but NOT counted

- p1nzzmq3: praises Oasis Senior Advisors; same brand name appears in vendor post p1lhl80l, so possible promotion (excluded as suspect).
- p1lhl80l: VENDOR (Oasis Senior Advisors).
- p1pl1cbv: VENDOR (hellohera).
- p1xhyhx7: VENDOR (care app).
- p1x45aze: news article excerpt about an aging life care manager (not a family).
- 77278.txt: forum: recommends an ALCA and elder law attorney (advice, no use).
- 499305.txt: forum: recommends a GCM (advice, no use).
- p17kp1k8: says aging consultants "won't do this sort of thing" (advice, no use).
- p13spwzv: paid caregiver, not family.
- p1mnznot: home health agency care manager, not a GCM.
- p1c9n0q9: "Healthcare consultant" suggested a psych ward; no verdict.
- a-1387: a care manager reviewing an app, not a family report.

Ask-only posts (no outcome saved): p19ax1dy, p1liu3zd, p1n9bqwm, p1n9bovr, p1qv1kmo, p1q62c27, p1qldy9o, p1wbrom7, p1jqxo6a, p1agdhv9, p1lpvr2z, p1nyaqna, p1hkgbf3, p15sol5v, p1sa7kcp, p1msan1e, p1mf6sfe (17 posts; p1n9bqwm and p1n9bovr are the same text posted twice).

## Cost report list

| Post | Amount or complaint | Class |
|---|---|---|
| p1x0fqwe | "billed $3,202 in 2 weeks" with no agreed plan | DID NOT WORK |
| p1woat2e | pays "a retainer" for monthly check-ins and is dissatisfied | MIXED |
| p1mtvh5w | law firm program quoted $20,000 first year, then $4,500 a year | no verdict |
| p1cr1bvr | placement advisor "free to use" but takes referral fees; feels "scammy" | MIXED (placement advisor) |
| AARP page (company-neutral, documented, not a family report) | $150 to $300 an hour | not a report |

## (c) Search filters and raw hits

| Filter | Raw hits |
|---|---|
| `care manager|geriatric care|aging life care|elder care consultant/advisor/advocate|senior advisor|private advocate|hired advocate` in Reddit, forums, app reviews (85 raw hits; all read) | 85 |
|    of which: describe real use (main table has 16 posts: 14 from this filter, 2 from the 'care management' filter) | 14 |
|    of which: placement-style senior advisors (APFM-type, separate table) | 3 |
|    of which: asks like 'has anyone used a GCM?' (no answer saved) | 17 |
|    of which: vendors, 'removed', plain words, job or study notes | rest not tallied: vendors, removed posts, plain words, and passing mentions of the role |
| `care management` without the other words (read all 20: 2 describe real use, p1d98a7r and p1cp6hth, both in the main table; p1anobar is advice) | 20 |
| `\bsolace\b` (the word, read all 35; 1 real Solace use: p1r08qm4, 3 asks) | 35 |
| `patient advocate|healthcare advocate|medical advocate` (116 raw with first filter; read in a first pass; almost all are the caregiver's own role) | 116 |
| Existing extract `feature-analysis-4/aging-life-care/reddit_posts_mentioning_care_manager_2026-11-06.txt` (60 posts; all are inside the 85) | 60 |
| Forum threads: 3 hits (499305, 77278 recommend a GCM or ALCA; neither reports use) | 3 |

Raw hits come from the same 49,315 Reddit posts, 142 forum threads and 17,956 app reviews as the other companies.

## (d) Cells that are VERIFY: does the saved data settle them?

| Cell | Settled? | Evidence |
|---|---|---|
| F2 Eligibility and applications | No | 1 report (p16jpagx): an elder care manager said "no options" (DID NOT WORK). 1 law firm program lists Medicaid enrollment (p1mtvh5w, reported by the family, not verified). No report shows a care manager filing an application. |
| F6 Account access | No | 1 report (p1x0fqwe) that a fiduciary firm took power of attorney and asked a mother to sign for "access her bank accounts" (DID NOT WORK). p1mxef8i: a care manager stood in the hospital while the family got account access, but did not do it. No report shows a care manager helping a caregiver into a parent's login. |
| F10 People who understand | No | 0 reports. 1 post (p1q0iemb) only plans to suggest a support group and a care manager. |
| F9 Behavior help | No | Capability YES rests on company and AARP text only. 0 family reports of a care manager helping with dementia behavior. |
| F4 Refusing parent support | Partly supports YES | p1p1nazq and p1viweky say it worked. The claim "some parents still refuse" has 0 reports in either direction for the GCM themselves (p1sl9uat is a brother refusing). |

## (e) Not checked

- Reddit replies (not saved); Facebook groups; Aging Life Care Association member reviews; Google and Yelp reviews of local firms; BBB for care manager firms (none saved).
- Whether firms named in posts are Aging Life Care members: unknown for all.
- F1 (respite), F9, F10: no family report of a care manager doing these.
- Same-author checks: Reddit files hold no usernames, so same-family grouping is inferred from the story.
