# PASS 1: How well Everplans features work for real families

Date: 2026-11-06. Branch feature-analysis-4. Saved data only; no website was scraped. Paths are under the repo root (docs/sources/...).
State key: observed = I saw it in a saved file; reported = a person's own account (not checked by me); documented = the company's own page; not-assessed = no usable evidence.
Rule used: a report counts only if a family caregiver or a neutral user writes about using Everplans for that feature. Mentions of the name, vendor posts, and descriptions of how it works do not count. Quotes were machine-checked against the saved text (exact match, 20 words max).

## Honest headline
The saved data holds very little independent evidence about Everplans. I found 4 counted reports in total, all for F6 (account access), all positive, and none from someone who has actually used a deputy login to get into a parent's accounts. There are 0 reports of Everplans failing, and 0 for every other cell. This is a gap in the saved data, not proof of anything.

## (a) Summary table

| Cell | Capability (EVIDENCE.md) | WORKED | DID NOT WORK | MIXED | Total independent reports | Evidence state |
|---|---|---|---|---|---|---|
| F1 Relief finder | VERIFY (leans NO) | 0 | 0 | 0 | 0 | not-assessed (0 reports found) |
| F2 Eligibility and applications | VERIFY (leans NO) | 0 | 0 | 0 | 0 | not-assessed (0 reports found) |
| F3 Paying for relief | VERIFY (leans NO) | 0 | 0 | 0 | 0 | not-assessed (0 reports found) |
| F4 Refusing parent support | VERIFY (leans NO) | 0 | 0 | 0 | 0 | not-assessed (0 reports found) |
| F5 Relatives cover time | NO (documented) | 0 | 0 | 0 | 0 | not-assessed (0 reports found) |
| F6 Account access | LIMITED (documented: paid plan, parent must set up) | 4 | 0 | 0 | 4 | reported |
| F8 Personal guidance | NO (documented) | 0 | 0 | 0 | 0 | not-assessed (0 reports found) |
| F9 Behavior and hard talks help | VERIFY (leans NO) | 0 | 0 | 0 | 0 | not-assessed (0 reports found) |
| F10 People who understand | VERIFY (leans NO) | 0 | 0 | 0 | 0 | not-assessed (0 reports found) |

## (b) Reports behind each count

#### F6

| # | Class | Audience | Source (path + id/URL) | Quote (copied exactly, 20 words max) | Limit |
|---|---|---|---|---|---|
| 1 | WORKED | adult child (caring for a parent) | docs/sources/competitive-analysis-3/grid/reddit-threads/everplans_y4q1tc.txt (comment isfovjd) https://www.reddit.com/r/personalfinance/comments/y4q1tc/im_looking_for_an_online_serviceapp_or_something/ | "I have a profile/login so that when something happens to them I can access all of their financial information" | Parents are alive; the writer has not yet used the access. Says parents are "quite happy" with it. |
| 2 | WORKED | adult child (caring for a parent) | docs/sources/app-reviews/all-reviews3.jsonl (id c-2, apple, 5 stars, 2025-04-24) | "we discovered a wealth of notes he had left for us, which significantly streamlined the process" | App Store review (5 stars, 2025). The father had filled it in. Notes, not logins; this is the best case for a prepared parent. |
| 3 | WORKED | unclear (account owner planning for self) | docs/sources/app-reviews/all-reviews3.jsonl (id c-1, apple, 5 stars, 2026-02-24) | "I absolutely feel secure in knowing that everything will be readily available to access, especially in an emergency." | Owner of the account, not a family caregiver. Feeling of security, not an access event. Same review is saved twice (c-1 and d-1). |
| 4 | WORKED | unclear (answering a husband planning for his wife) | docs/sources/competitive-analysis-3/grid/reddit-threads/everplans_sr80o8.txt (comment hwruhay) https://www.reddit.com/r/personalfinance/comments/sr80o8/is_there_an_online_service_that_lists_all_of_your/ | "articles on their site on how to prepare for something like this, which I found valuable" | Praises the planning articles, not the deputy feature. Poster says they may not use the service. |

### Category context (read, NOT counted)
These show the need and the "parent must fill it in" risk. None names Everplans as the tool used, so they stay out of the counts.

| Cell | Source | Quote | Why not counted |
|---|---|---|---|
| F6 | LifeProTips thread, post by an adult child (docs/sources/competitive-analysis-3/grid/reddit-threads/everplans_1eaenyg.txt, https://www.reddit.com/r/LifeProTips/comments/1eaenyg/) | "I didn't have access to her computer or cell phone passwords" | Could not pay a dead mother's bills without passwords. The thread is saved as an Everplans thread, but the writer did not use Everplans. Shows the need, not the product. |
| F6 | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl (key p1pb8snh) https://www.reddit.com/r/AgingParents/comments/1pb8snh/ | "we didn't even know the password to his phone" | Title of a post by a family member locked out when a father was in hospital. No product named. |
| F6 | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl (key p1ijdg4c) https://www.reddit.com/r/AgingParents/comments/1ijdg4c/ | "I still cannot access her email account as she can't remember the password" | Adult child cannot get into a mother's email. No product named. |
| F6 | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl (key p1xdkg46) https://www.reddit.com/r/dementia/comments/1xdkg46/ | "Her password book I got her is a jumbled, scribbled out mess" | Child of a mother with dementia. Paper password book failed. No product named. |
| F4 | docs/sources/reddit/arctic-shift-2026-11-03/posts.jsonl (key p1i9rvrr) https://www.reddit.com/r/AgingParents/comments/1i9rvrr/ | "Both refuse to touch it." | Parents refused to use a planner and binder for documents. Shows the "parent must fill it in" risk that Everplans has. No product named. |
| F4 | docs/sources/competitive-analysis-3/grid/reddit-threads/everplans_1i5704g.txt (comment m81m1jv) https://www.reddit.com/r/GenXWomen/comments/1i5704g/ | "My parents do not want to think about death, do not want to talk about death" | Comment under a post that lists Everplans among end-of-life tools. About tools in general. |

### Everplans named but not counted (and why)
| Source | What it says | Why not counted |
|---|---|---|
| everplans_1eaenyg.txt comment lel5klc | Describes how deputies and locked areas work | A description of the product, not an experience. |
| everplans_1eaenyg.txt comment lergxsb | Pastes Everplans' FAQ on waiting time (3 hours to 30 days) | Company text, copied. |
| everplans_s6gxn7.txt comment ht8bqhy | "My step mom's attorney uses an online portal ... Everplans" | Name only. |
| everplans_y4q1tc.txt comment ishktln | "My folks use everplans." | Name only; no feature, no outcome. |
| everplans_1i5704g.txt (post) | Lists Everplans among tools and asks why people do not adopt them | Name only; no saved comment on it describes using Everplans. |
| search_everplans.json posts 1tmpm3i and 1r7scv7 | A person asks which of Everplans or Trustworthy to buy; another lists Everplans among digital estate tools | Questions and name-only. No comments are saved for them. Post 3e3log is a vendor post (a discount code), excluded. Post 1i56ze6 is a copy of the 1i5704g question (name-only). Post mb0o23 says the writer will "definitely" check out Everplans: intent, no experience. |
| App Store reviews c-0, c-3, c-4, c-5, c-6 (also saved as d-0, d-3 to d-6) | Complaints that the iPad app is a phone-size app; praise for the website | Not about any of the nine features. |
| App Store review c-7 | "I need to get organized. Thank you" | Not about a feature. |
| Trustpilot (docs/sources/competitors-4/review-sites/trustpilot_everplans_2026-11-04.txt) | 1 review, 1 star, 2022, about an upsell to buy a book | Not about a feature. |

## (c) Filters used and raw hit counts
| Filter | Where | Raw hits | What I did |
|---|---|---|---|
| "everplan" (any case) | Reddit posts.jsonl (43,665 posts) and posts_targeted.jsonl (5,650 posts) | 0 and 0 | Nothing to read. Note: the saved posts file has post text only, no comments. |
| Saved Everplans threads with comments | docs/sources/competitive-analysis-3/grid/reddit-threads/ everplans_1eaenyg, 1i5704g, s6gxn7, sr80o8, y4q1tc (about 1,100 saved lines) | 5 threads; 6 comments and 1 post name Everplans | Read every one of the 7. Counted 2 (isfovjd, hwruhay). |
| Extra search file | docs/sources/competitive-analysis-3/grid/reddit-threads/search_everplans.json | 5 posts (4 name Everplans in the text, 1 is a vendor post; 0 with comments saved) | Read all 5; counted 0. |
| "deputy" | Reddit posts | 2 | Both read: a UK legal deputy for a woman with dementia (p1chuki6) and a sheriff's deputy (p1h5aoyh). Neither is about Everplans. |
| "legacy contact" | Reddit posts and the 5 threads | 0 in posts; 1 thread (y4q1tc) uses the words about another tool (LastPass emergency access, comment ishlgtf) | Not Everplans; not counted. |
| "digital executor", "digital estate/vault/legacy" | Reddit posts | 1 and 1 | The first is a user who is their mother's digital executor (p1h5yu22); the second is a removed promo post (p1l9j1k8). Not counted. |
| "password manager", LastPass, Bitwarden, 1Password, Dashlane | Reddit posts | 10 | Read all 10. They are about families helping parents with passwords; none names Everplans. Used only as context. |
| written password lists or books near "mom, dad, parent..." | Reddit posts | 30 | Read all 30 snippets. 3 used as context above (p1pb8snh, p1ijdg4c, p1xdkg46); the rest are in the group-texts file. |
| "everplan", "deputy", "caring village" | docs/sources/forums/agingcare and alzconnected (142 .txt files) | 0 | Nothing to count. |
| app name = everplans | docs/sources/app-reviews/all-reviews3.jsonl and all-reviews4.jsonl | 8 unique reviews (c-0 to c-7); all-reviews4 repeats the same 8 as d-0 to d-7 | Read all 8. Counted 2 (c-1, c-2). |
| Trustpilot, BBB | docs/sources/competitors-4/review-sites/ | Trustpilot 1 review; BBB file has Cariloop and A Place for Mom only | Read; counted 0. |
| Everplans in docs/sources/competitive-analysis-2/themes/everplans.json | earlier reader pass | kept 1 review (c-2) | Cross-check only. Matches my count for c-2. |

## (d) Cells still marked VERIFY: does the saved data settle them?
| Cell | Settled? | Evidence |
|---|---|---|
| F1 Relief finder | No | No review or post says anyone looked for respite in Everplans. Silence. |
| F2 Eligibility and applications | No | Silence. |
| F3 Paying for relief | No | Silence. The one price mention is Everplans' own $99.99 a year (c-1). |
| F4 Refusing parent support | No (supports "leans NO") | Context posts show parents refusing to fill in planners (p1i9rvrr, comment m81m1jv). That is about tools in general. Everplans' own help page already says the parent must enter the information. |
| F9 Behavior and hard talks | No | Silence. Only hwruhay praises the planning articles (not hard-talk help). |
| F10 People who understand | No | Silence. |
| F6 (already LIMITED) | Supported, not proven | 4 positive reports, all consistent with "works if the parent set it up". 0 reports of a deputy actually getting in. 0 reports of it failing. |

## (e) Not checked
- No saved Reddit comments exist for the Everplans search results, so the number of people who tried Everplans may be larger than what is saved.
- Apple App Store and Google Play listing text and any Google Play reviews for Everplans: only 8 Apple reviews are saved; no Google Play file for Everplans was found in docs/sources/app-reviews/google-play/.
- Other review sites (Reddit r/EstatePlanning comments, Capterra, G2, Better Business Bureau for Everplans): not saved, not searched in this pass.
- Whether a deputy can actually see passwords or log in to a bank (documented limit in EVIDENCE.md; no independent report either way).
- Whether the partner-firm (free) version works differently for families.
- No website was scraped in this pass.
