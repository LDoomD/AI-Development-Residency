# Research checklist: law-database pass (2026-11-12)

Filled in from `docs/research-checklist.md` and shown to the owner before any search.

## 1. What this task is for

- **Task:** answer the open legal questions from `docs/sources/laws-consent-research-2026-11-12/verified-findings-2026-11-12.md` with law databases. Each "lawyer needed" row should become "the law says X, and only Y is unclear."
- **Updates:** the risk profile (`docs/risk-profile.md`, still Proposed).
- **Changes later:** the build plan's security protocol and database architecture boxes (board 576:5824), and Epic 2 (family accounts and permissions).

## 2. What the earlier deliverables already set

| Set by | What it sets | How this task uses it |
|---|---|---|
| Audience page (Figma 2378:7111, 2378:7177) | Audience 1 = adult child caring for a parent. Audience 2 = spouse or partner. | Every question is asked for both: a child entering a parent's data, and a partner entering a partner's data. Laws may treat spouses differently. |
| Market analysis (`market-analysis-review-cells-2026-11-05.md`, rows 10 and 14) | Money, accounts and legal papers is a top problem. Missing or rejected power of attorney is a named complaint. | Power of attorney is a real caregiver situation, not a guess. |
| Competitive analysis 4 (`competitive-analysis-4-updated-2026-11-07.md`, line 113) | Risk: Caring Village shows medical details to invited friends, and Everplans lets parents lock sections. | These are the 2 consent examples we have. The laws tell us which approach they require. |
| Vision and scope (`vision-and-scope-boards-2026-11-10.md`) | Direct to consumer, US, MVP #1 scope. | Fixes the product facts each question is asked about. |
| Coding challenge, requirement 6 | Vercel, Supabase, user accounts with secured data. | Fixes the stack for the data region question. |
| Open questions | Who pays (not now). | Left out. |

## 3. All saved research on the topic

Search run: `find docs -name "*.md" -not -path "docs/sources/*" -exec grep -l -i -E "power of attorney|POA|consent|HIPAA|guardian|proxy" {} \;` (39 files).

| File | What it found | Used, or left out and why |
|---|---|---|
| `verified-findings-2026-11-12.md` | 10 rules, checked today, with open questions | Used: it's the starting point. |
| `laws-consent-research-2026-11-12/sources/` (27 files) | Saved law text and guidance | Used: read before searching for anything new. |
| `risk-profile.md` | Old open questions | Used: the questions to replace. |
| `market-analysis-review-cells-2026-11-05.md` | Power of attorney complaints (rows 10, 14) | Used, as above. |
| `competitive-analysis-4-updated-2026-11-07.md` | The 2 competitor consent examples | Used, as above. |
| Older drafts (competitive 1 to 3, feature analysis, reddit findings and the rest) | Same consent and POA themes, earlier versions | Left out: replaced by the clean deliverables. |

## 4. How the research splits

- **By audience:** cared_for = parent (Audience 1) or spouse or partner (Audience 2).
- **By state:** Washington, Nevada, Connecticut, California, plus federal (FTC, HHS).
- **By question:** the 5 questions below.

## 5. The questions

| Question | Where it comes from |
|---|---|
| 1. Under the WA, NV and CT laws, who counts as the "consumer" when a caregiver types in a parent's or partner's health data? Can someone else consent for them (an authorized agent, power of attorney, guardian)? | Verified findings, open gap 1; board barrier, line 59 |
| 2. Does a general or health care power of attorney give that consent under each state's power of attorney law? | Same; market analysis rows 10 and 14 |
| 3. Is our app a "personal health record" under the FTC rule? Look at the FTC's own examples in its guide. | Verified findings, FTC breach rule row |
| 4. California: what is the CCPA size limit, and does the CMIA medical privacy law reach a consumer app? | Verified findings, open gap 2 |
| 5. Where do Vercel and Supabase store data, and can we pick a US region? | Verified findings, open gap 4 |
| Plus: any court cases or attorney general actions under the WA, NV or CT health-data laws (CourtListener, AG sites) | Checks how the laws are being enforced |

## 6. What will be produced, and how the owner can audit it

- **Files:**
  - Each new source saved in `docs/sources/laws-consent-research-2026-11-12/sources/` (numbered 28 and up) and logged in `docs/sources/INDEX.md`.
  - The answers are added to `verified-findings-2026-11-12.md` as a new dated section, so the original table stays as it is.
- **Tools:** Firecrawl government search and scrape, state legislature and attorney general sites, FTC case pages, CourtListener. No Arctic Shift or Chrome extension.
- **Checks:**
  - Every answer quotes the law's own words, with the section number.
  - Quotes are checked word for word against the saved file.
  - Each source's date is recorded, and anything not confirmed for 2025 to 2026 is marked "may be out of date."
  - Official sources first. Law firm blogs are used only to find the official source.
- **Limits:**
  - This says what the law and officials say, not how a court would rule for our exact app.
  - The state health-data laws are new (2023–2024), so few cases may exist.
  - Never says "compliant."
