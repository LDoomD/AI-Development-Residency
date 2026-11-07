# Change report: Feature Analysis 4, errors found and fixes (2026-11-06)

Status: **draft, research still running.** Sections marked "Pending" are filled in when the three research helpers finish. Branch: `feature-analysis-4`. Nothing is committed.

## 1. What this report is for

The owner asked for one place that records every error found while starting the feature comparison analysis: when each one was found, how it was found, what it caused, what is being done, where the data came from, and which other deliverables change.

## 2. The rule for this work

The owner's rule (2026-11-06): **the three updated deliverables in Figma are the source of truth.** They are the market analysis, the audience segmentation and the competitive analysis, all on page "Week 2 & 3_Updated Deliverables" (canvas 2782:15415, file `HcDDdEGAnikTImO8v7UPMp`). Feature Analysis 3 and the teacher's example are **format only**. Anything from outside Figma must be named in full sentences.

## 3. Errors found, in order

| # | What went wrong | How it was found | What it caused | Fix |
|---|---|---|---|---|
| 1 | I made a new branch and wrote a checklist file before telling the owner. | The owner said they would have wanted to be told first. | The owner did not know what I was doing. | The branch stays (owner approved). From now on I say what I will create before I create it. |
| 2 | I called the table a "competitive table" when explaining the Yes/Partly/No rule. | The owner corrected me: this is a feature comparison table. | Confusion about which table I meant. | The rule is now written for the feature table: only ✅ or 🚫. |
| 3 | I said columns 7 and 11 came from Feature Analysis 3 and "keep the table honest." | The owner asked what that meant and whether it was based on the three deliverables. | Two columns had no data reason. | Columns 7 (papers and documents) and 11 (shared care updates) were judged again from the new data only. Both overlap other columns, so both are left out. |
| 4 | I summarized the Figma deliverables without showing proof, and my first read was incomplete. | The owner said I gave no observable evidence. | The owner could not tell whether I had read the deliverables. | I re-read every section with the Figma tool and quoted node ids and numbers. See section 5. |
| 5 | The first full-page read was cut off at 100,000 characters, so I only saw the market sections' structure and took the top-problems numbers from an older handoff file. | I checked what I had actually read when the owner asked. | Some numbers in my overview did not come from Figma. | I read the remaining sections one at a time (2808:13693, 2812:14373, 2813:14661, 2834:16750). |
| 6 | The first research helper was told to use a saved markdown copy of the competitive table, not Figma. | The owner asked why I was not using Figma. | The helper could have used out-of-date data. | I copied the live Figma tables into a file and told the helper Figma comes first. The saved copy was last committed Nov 5 and marks some cells "changed." |
| 7 | The approved competitive analysis scored 5 needs, not the 9 features in the new table. | The helper reported that Figma has only the 5 needs. | No earlier report says, feature by feature, whether a company offers each feature. | New research, section 6. |
| 8 | The first grid marked many cells 🚫 only because a company's page never mentioned the feature. | I reviewed the helper's "least sure" list. The owner then said this needs fixing. | A silent page does not prove a company lacks a feature. | Those cells become "verify," then get more research. |
| 9 | The first grid gave ✅ to features offered only to employees (Cariloop) or only to veterans (the VA). | The owner said a ✅ with limits is not okay. | The ✅ hid a limit. | Those cells are held as "verify" until the owner chooses how to treat limited offers. Helpers now record the exact limit. |
| 10 | My word search for earlier feature research failed with a shell error, and I read the result as "no matches." | I re-ran the search before answering and saw the error. | I nearly told the owner nothing existed. | The search was re-run correctly: 12 files mention feature words, but none scores competitors on the 9 features. I did not read every one of them. |
| 12 | One research helper read 24 A Place for Mom pages with a plain download tool, although the site's robots.txt names ClaudeBot as blocked. It skipped the pages the site blocks for all crawlers. | The helper reported it, and I read its evidence file. | Possible disregard of the site's stated rule. | Raised with the owner, who said to delete them. The 23 saved pages were deleted. That company's verdicts from those pages are withdrawn and count as "verify." |
| 13 | Two quotes in the evidence files could not be matched to a saved page: one in the group texts file, and one care managers phrase that was the helper's own wording. | I ran a script that searches every quote against the saved pages and the Figma copy. | A paraphrase could pass as a quote. | Both are treated as unverified. |
| 11 | I used shorthand the owner could not follow ("Figma says can't be made to do that," "four pages weren't saved"). | The owner asked what I meant, twice. | Time lost, and the owner had to ask again. | I now explain in full sentences, name the file or Figma cell, and say why it matters. |

## 4. Conflicts between Figma and the saved pages

These are the cells where a saved company page and the Figma competitive analysis point different ways. The helper listed them in `docs/sources/feature-analysis-4/first-pass-grid-and-evidence-2026-11-06.md`.

| Cell | Saved page says | Figma says |
|---|---|---|
| Behavior and hard talks help, six companies | Several pages describe help with hard conversations, but none describes a dementia-behavior service. | The problem table says no competitor covers dementia behavior, but need 1 gives Yes or Partly to several. |
| Caring Village, relatives cover time | `competitors/caring-village/pages-2026-11-03/app.txt`: to-do lists "let people claim tasks" and give tasks "a named owner." | Need 5: "Partly: relatives join free with their own login. Can't make them do tasks." |
| A Place for Mom, refusing parent | A "tough conversation" guide exists. | Need 4: No. An advisor told one family to lie to the parent. |
| Respite and adult day, refusing parent | The Alzheimer's Association adult day page says some people resist going at first and suggests giving the center a chance. | Need 4: No. |
| Area Agencies, personal guidance | The program lists "individual counseling." | Agencies "mostly give referrals." |
| Group texts, relatives cover time | Saved Reddit themes show a few posts asking for shift cover and more posts about requests being ignored. | Need 5: Partly. |

## 5. Data collected and where it came from

**Figma (read 2026-11-06 with the Figma tool, file `HcDDdEGAnikTImO8v7UPMp`):**

| Node | What it is | What I used |
|---|---|---|
| 5:638 | The format example (titled "EXAMPLE FEATURE COMPARISON ANALYSIS": 21 columns, a question row, a green OUR COMPANY row, ✅ or 🚫 cells) | Layout and titles only |
| 2808:13693 | Market analysis, main research table | Sizes, competitors, funding |
| 2812:14373 | Possible market segments (15) | Segments and examples |
| 2813:14661 | Market size | Sizes and confidence |
| 2815:15035 | Market opportunity | The approved answer (relief) |
| 2834:2844 | Audience segmentation definition | Who the caregivers are |
| 2834:2867 | Motivations, goals and use cases | Use case counts per audience |
| 2834:16750 | Top problems | Mentions per source |
| 2843:15117 | Competitive analysis, all tables | 9 competitors, 5 needs, 4 gaps |

Saved copy of the competitive tables: `docs/sources/feature-analysis-4/figma-competitive-tables-2026-11-06.md`.

**Saved company pages (already in the repo):** `docs/sources/competitors/`, `competitors-3/pages/`, `competitors-4/` (with `save_log*.json` showing which pages were blocked by robots.txt), `competitive-analysis-3/`, and Reddit data in `reddit/arctic-shift-2026-11-03/`.

**First-pass grid:** 81 cells (9 companies × 9 features). Result: 29 "verify." The helper's quotes were spot-checked by searching the saved files: 10 of 10 quotes exist. Evidence file: `docs/sources/feature-analysis-4/first-pass-grid-and-evidence-2026-11-06.md`.

**Pages that were never saved (found 2026-11-06):**
- Caring Village's "Marketplace" page.
- The ARCH respite pages "Apply for State Lifespan Respite Voucher Programs" and "How to Pay for Respite" (only menu labels were saved).
- A VA page about behavior or dementia help.
- The Area Agencies on Aging folder is empty. The federal page (acl.gov) is blocked by robots.txt. Its text was saved by hand in `competitors-4/manual-saves/acl_gov_nfcsp.txt`.

## 6. New research (started with the owner's yes)

Three helpers read each company's own site and independent sources (reviews, BBB, Reddit, forums). Rules given to them:
- Respect robots.txt. Blocked pages are listed, not scraped.
- Each cell is **YES, LIMITED (limit named), NO (named source) or VERIFY**. A page that never mentions a feature is never a NO.
- Every page used is saved under `docs/sources/feature-analysis-4/<company>/`, with the URL and date at the top, and an `EVIDENCE.md` with exact quotes.

| Helper | Companies |
|---|---|
| 1 | Caring Village, Everplans, group texts and notebooks |
| 2 | Cariloop, A Place for Mom, geriatric care managers |
| 3 | Area Agencies on Aging, respite and adult day services, VA caregiver programs |

**Results (all three helpers finished 2026-11-06).** Every quote in every `EVIDENCE.md` was checked against the saved pages and the Figma copy. Of about 160 quotes, all match except one in the group texts file (the wording appears only in the evidence file) and one phrase in the care managers file that is the helper's own paraphrase, not a quote. Both are treated as unverified.

| Company | Evidence folder | Main finding |
|---|---|---|
| Caring Village | `docs/sources/feature-analysis-4/caring-village/` | Relatives can claim tasks and a named person is shown as done. A respite search link and a cost guide exist. Behavior guides are on its blog only. Six cells stay "verify." |
| Everplans | `.../everplans/` | Relatives can only view. Account access works only on the paid plan and only if the parent set it up. Personal guidance is no. |
| Group texts and notebooks | `.../group-texts-notebooks/` | No way to assign or confirm tasks. A few families still set shifts, without crediting a tool. |
| Cariloop | `.../cariloop/` | Every feature is employer-paid only. Only price found: $249 a month at one university after leaving a job. |
| A Place for Mom | `.../a-place-for-mom/` | Guides on a refusing parent and on hard talks, plus a cost calculator. One BBB review says an advisor suggested lying. **23 pages were read although robots.txt names ClaudeBot as blocked. The owner had them deleted; this row is back to "verify."** |
| Geriatric care managers | `.../aging-life-care/` | Mostly marketing claims. The Figma claim about a care manager taking power of attorney could not be found in saved sources. |
| Area Agencies on Aging | `.../area-agencies-on-aging/` | What a family gets depends on the local agency. Care manager, dementia classes and groups exist in some places only. 17 local and national pages saved. |
| Respite and adult day services | `.../respite-adult-day/` | Real ARCH voucher and "how to pay" pages saved. Nothing helps a parent who refuses. Some state vouchers pay a relative. |
| VA caregiver programs | `.../va-caregiver/` | The 70% rating applies only to the comprehensive program. The general program has no rating and is free. Everything is veterans only. |

**Where the new research differs from the Figma competitive analysis** (the owner decides; nothing in Figma was changed):
- Caring Village, relatives share: Figma says the app can't make relatives do tasks. No saved source says that. The app assigns, lets people claim and shows who finished. It cannot force anyone.
- Caring Village, relief and paying: Figma says no relief and only partial money help. The research found a respite search link and a cost guide.
- Everplans, relatives share: Figma says "Partly." Evidence says viewing only.
- Group texts, relatives share: Figma says "Partly." Evidence says no way to assign or confirm.
- Cariloop, understand: Figma says Yes on eligibility help. No page says coaches help file applications.
- A Place for Mom, refusing parent: Figma says No, based on one complaint. Guides exist.
- VA: the 70% rule applies to one program, not all.
- Area Agencies: "can't act without the parent's consent" has no saved source.

## 7. How the research feeds the feature table

1. Every ✅ or 🚫 in Feature Analysis 4 must trace to a saved source. Cells with no source say "verify."
2. A cell takes the Figma competitive analysis as its starting point. Where a company page disagrees with Figma, the owner decides which wins.
3. The owner decides how limited offers are shown, because a ✅ with limits is not allowed.
4. The first six columns (company, website, pricing, market, segment, customers) are already drawn from Figma tables 2843:15145 and 2843:15146 and were approved.
5. The nine feature columns were approved by the owner. Their evidence row names the deliverable each came from.

## 8. Which deliverables change

| Deliverable | Change | Why | How it is saved |
|---|---|---|---|
| Market analysis | None expected | The research only covers what each company offers | n/a |
| Audience segmentation | None expected | Same | n/a |
| Competitive analysis | **Pending.** Possibly the Caring Village need 5 cell, "dementia behavior: no one covers it" versus the need 1 cells, and the A Place for Mom need 4 cell. | Conflicts in section 4 | Its own branch and pull request, only if the owner approves a change |
| Feature analysis | New (Feature Analysis 4) | The table we are building | Branch `feature-analysis-4`, then its own pull request |
| `docs/research-checklist-feature-analysis-4-2026-11-06.md` | To be updated: Figma is the source of truth, and the new evidence files are inputs | Its section 3 and 6 predate this research | Same branch |

## 9. How the outcomes were reached

- **Which columns:** each of the 11 proposed columns was checked against the market analysis, audience segmentation and competitive analysis. Columns 7 and 11 had no data reason of their own, so they were left out. Nine remain.
- **Which cells are "verify":** the helper used ✅ only when a saved page showed the feature, 🚫 only when a source said no, and "verify" when sources were silent or conflicted. I then tightened it: a silent page is never a 🚫.
- **Spot check:** 10 of the helper's quotes were searched for in the saved files, and all were found.
- **Not checked yet:** the new research results, whether Figma was edited after 2026-11-06, and any company page not saved.

## 10. Open decisions for the owner

1. How a feature offered only to some people (employees, veterans) should appear in a ✅ or 🚫 cell.
2. Whether help with hard talks alone counts as ✅ for the behavior and hard talks column.
3. For Caring Village: is "claim tasks" ✅ for relatives cover time, or 🚫 because the app can't make relatives follow through?
4. Whether to change the competitive analysis once the research is in.
