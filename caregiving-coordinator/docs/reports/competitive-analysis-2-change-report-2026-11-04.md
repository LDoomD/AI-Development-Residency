# REPORT: What changed in the competitive analysis, why, and what caused it (2026-11-04)

## How to use this report with Claude
Paste this whole report into a chat, or point Claude at `docs/reports/competitive-analysis-2-change-report-2026-11-04.md` in the caregiving-coordinator folder. The new table is `docs/competitive-analysis-2.md` and the Figma section "CAREGIVING — Competitive Analysis 2" (Section 8). The data and check scripts are in `docs/sources/competitive-analysis-2/`, and each file is listed in `docs/sources/INDEX.md`. Commit 4e56d3a, branch feature-analysis, PR #23.

## 1. What happened
Reviewing the competitive analysis table, the owner found that "What do they not do well?" for Caring Village was one user's comment, not an answer. Claude then checked all ten rows and found the same problem almost everywhere.
- "Do well" and "not do well" had one quote per company. Some quotes didn't even answer the question. Medisafe's "does well" quote describes a struggle ("My mom takes 20+ different medications…"). Caring Village's "not well" is a question a reviewer asked. MyChart's "not well" is about a child's chart, not caring for a parent.
- "What market gaps have they NOT filled?" was filler text Claude generated automatically, for example "its saved pages state all three of: how it differs, sharing, price." It answered nothing.
- The company columns (business model, keeping customers, customer experience, data and consent, emergencies, setup, relatives joining) pasted two company quotes each and never said what they meant.
- Everplans, Group texts and Paper notebook were mostly "Not assessed."
- The gaps box and the unique value opportunities table had the same quote-first style.

## 2. What was changed
A second version was built next to the first. Version 1 is unchanged, so before and after can be compared.
1. **Evidence gathered:** every caregiving app review, every Reddit post in both downloads that names a competitor, and every forum mention. That is 1,101 items for the 10 competitors.
2. **Read in full and themed:** readers read every item, kept the 577 written by someone caring for another person that say something about the product, and counted themes from what people wrote. They didn't start from a list.
3. **Company facts:** every saved company page was read in full for the business model, price, privacy, setup and the other company questions. All 273 backing quotes were found in the saved pages.
4. **New answers:** every box is now a short plain-words answer with counts. For example: "the daily care plan resets or is too rigid (3), bugs and lost entries (3)". The last column says what the evidence is and where it's thin.
5. **Gaps and value opportunities redone** the same way: six gaps and seven opportunity areas. All 97 numbers cited there were matched to the theme they describe.
6. **Checked by script:**
   - every count against its list of items (0 errors)
   - every quote word for word (0 errors)
   - every number in the answers
   - Figma text against the source (220 of 220 table cells, 42 of 42 gap and opportunity texts)

**Biggest differences in the findings:**
- MyChart: "once a caregiver gets in, it works; getting in is the problem."
- Lively and Medical Guardian: "the button works, the family app fails." Lively has wrong location in 58 items and alerts to family late or never in 27.
- Group texts: details get buried, causing missed appointments and near double doses (10).
- Everplans: too thin to judge (1 caregiving review).

## 3. Why it happened (the causes)
1. **Claude set the wrong rule.** When building version 1, Claude wrote the question rules as "review or forum quotes only." That told every step to paste quotes instead of drawing a conclusion.
2. **Text filled boxes automatically.** The gaps column was filled by a script that stitched labels together. It looked finished but said nothing.
3. **The first counting was narrow.** Version 1 counted reviews by keyword categories in one pass. MyChart's 200 Apple reviews were never filtered for caregiving, and the workarounds were never read.
4. **No one checked whether each box answered its question.** The checks confirmed that quotes were real, not that the box answered the question. A table can be accurate and still useless.
5. **Claude didn't audit its own output before handing it over,** even though the same kind of problem (unfiltered reviews, vague labels) had happened before.

## 4. What it affects next
- **Feature analysis:** it was counted from the older, narrower tags, so every box needs recounting. Group texts and Paper notebook rows need adding, and its gaps step needs updating. Feature Analysis 2 is planned and waiting for the owner's go.
- **Template note:** on the board template, "Summarize the unique value opportunities" and "Summarize the gaps" are one box. The opportunities table covers both.
- **Still open:** the Reddit research read posts through the 8 feature columns, after keyword filtering. An open read of caregiver posts, with no feature list, hasn't been done. It could show a big problem that doesn't fit the 8 features.

## 5. What Claude will do differently
1. Answer the question in every box with a conclusion and counts. Quotes only back it up.
2. Read all the relevant evidence in full and count themes from it, not one example.
3. Never let a script write answer text. Scripts count and check; answers are written from the counts.
4. Run an audit before handing anything over: does each box answer its question? Is the data filtered to caregivers? Are any boxes empty or vague, and why? Then say the gaps out loud.
5. Check numbers by script against the raw data, and check that each number belongs to the theme it describes.
6. State thin evidence plainly instead of filling the box.

## 6. What the owner can do
1. Spot-check one row. Open a box, then open the theme file it cites (`docs/sources/competitive-analysis-2/themes/<company>.json`) and see whether the counts and themes match.
2. Ask "is this a conclusion or a quote?" for any box. If it's a quote, send it back.
3. Ask Claude to state the question each column answers before it fills the table, and check that the rule matches the template.
4. Ask for the audit result (what was checked, what's thin) before accepting any table.
5. Decide which gaps to go after. Claude gives evidence but doesn't choose.
