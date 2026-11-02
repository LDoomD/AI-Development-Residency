# Sources index

Every cited source for the market research is saved here so it can be opened and audited. Rule (also in `CLAUDE.md`): read the full primary source, cite every claim with a link and page, and keep a copy here.

Last updated 2026-11-01.

## 1. AARP and NAC, Caregiving in the US 2025 (read in full)

Folder: `aarp-nac-caregiving-in-the-us-2025/`

| File | What it is | Original URL |
|---|---|---|
| `full-report.pdf` | The full report, 140 pages, July 2025 | https://www.aarp.org/content/dam/aarp/ppi/topics/ltss/family-caregiving/caregiving-in-us-2025.doi.10.26419-2fppi.00373.001.pdf |
| `full-report.paged.txt` | Text of the full report with a "=== PDF PAGE n ===" marker before each page (printed page = PDF page minus 6) | made from the PDF with `pdftotext -layout` |
| `executive-summary.pdf` (+ `.txt`) | 6-page executive summary | https://www.aarp.org/content/dam/aarp/ppi/topics/ltss/family-caregiving/caregiving-in-us-2025-executive-summary.doi.10.26419-2fppi.00373.003.pdf |
| `infographic.pdf` (+ `.txt`) | Infographic | https://www.aarp.org/content/dam/aarp/ppi/topics/ltss/family-caregiving/caregiving-in-us-2025-infographic.doi.10.26419-2fppi.00373.002.pdf |
| `report-page-aarp.html` | AARP's landing page for the report | https://www.aarp.org/pri/topics/ltss/family-caregiving/caregiving-in-the-us-2025/ |
| `press-release-2025-07-24.html` | AARP press release | https://www.aarp.org/press/releases/2025-07-24-new-report-reveals-crisis-point-for-americas-63-million-family-caregivers.html |
| `family-caregivers-of-adults-50-plus.html` | Companion page: caregivers of adults 50+ | https://www.aarp.org/pri/topics/ltss/family-caregiving/family-caregiving-in-us-2025/ |
| `caring-across-states.html` | Companion page: state-level data | https://www.aarp.org/pri/topics/ltss/family-caregiving/caregiving-in-the-us-2025-caring-across-states/ |
| `sandwich-generation.html` | Companion page: sandwich-generation caregivers | https://www.aarp.org/pri/topics/ltss/family-caregiving/caregiving-in-the-us-sandwich-generation/ |

The HTML companion pages were saved but have not been read in full yet. Figures in `docs/audience-segmentation.md` come only from the full report.

## 2. Apple App Store public search data (collected 2026-11-01)

Folder: `app-stores/`. Source: Apple's public iTunes Search API (`https://itunes.apple.com/search`, country US, entity software).

| File or folder | What it is |
|---|---|
| `apple/*.json` | Raw results for 10 category searches (caregiver, family caregiver, caregiver coordination, care team family, medication tracker caregiver, doctor visit notes, elder care, senior care family, aging parent, caregiver journal), up to 50 results each |
| `apple-search-merged.csv` | The 338 unique apps from those searches, ranked by rating count |
| `apple-named/*.json` | Raw results (top 5) for 36 named products (Caring Village, CaringBridge, Medisafe, Kin Health and others) |

Rating counts are reviews left, not downloads. Apple does not publish download counts.

## 2b. Google Play (collected 2026-11-01)

Folder: `google-play/`. Source: public Google Play pages (`https://play.google.com/store/search?q=...&c=apps&gl=us` and each app's `https://play.google.com/store/apps/details?id=...` page). There is no official API, so ratings, install bands and developer names were read from each page's own metadata.

| File | What it is |
|---|---|
| `play-apps.csv` | 121 unique apps from 8 category searches and 23 named-product searches: name, developer, install band (for example 10K+), rating, rating count, and the URL of each app page |
| `search-caregiver.html` | The raw Google Play search page for "caregiver" |

Install counts are bands set by Google (10K+, 500K+, 5M+), not exact numbers. Raw HTML for each app page was not kept (about 1 MB each); the CSV has the URL for each so it can be reopened.

## 2c. GitHub (collected 2026-11-01)

Folder: `github/`. Source: GitHub repository search through the `gh` command line, 12 queries, up to 50 repos each, sorted by stars (caregiver, caregiving app, care coordination, family caregiver, elder care, senior care, medication reminder, medication tracker, dementia caregiver, caregiver coordination, doctor visit notes, eldercare family). `*.json` are the raw results; `github-merged.csv` has the 445 unique repos with stars, language, licence, dates and URL. Many results are unrelated (for example Chinese school-project elderly-care systems and baby trackers).

## 2d. Hacker News "Show HN" posts, a source for indie launches (collected 2026-11-01)

Folder: `hackernews/`. Source: the public Hacker News search API (`https://hn.algolia.com/api/v1/search?tags=show_hn`), 8 queries. `*.json` are the raw results; `hn-show-merged.csv` has the 124 unique posts with points, date, title and link.

Not yet collected: Product Hunt (needs an API token), Indie Hackers, and indie developer sites outside Hacker News.

## 2e. Official NAICS 2022 codes and 2022 Economic Census revenue (primary, collected 2026-11-01)

Folder: `census-naics/`. Source: US Census Bureau.

| File | What it is | Original URL |
|---|---|---|
| `2022_NAICS_Descriptions.xlsx` | Official 2022 NAICS code titles and definitions | https://www.census.gov/naics/2022NAICS/2022_NAICS_Descriptions.xlsx |
| `2022_NAICS_Index_File.xlsx` | Official index of activities and the code each belongs to (used to find where "referral services", alarm monitoring and home care of the elderly sit) | https://www.census.gov/naics/2022NAICS/2022_NAICS_Index_File.xlsx |
| `2-6_digit_2022_Codes.xlsx` | Official code list | https://www.census.gov/naics/2022NAICS/2-6%20digit_2022_Codes.xlsx |
| `ec2022-51/`, `ec2022-44/`, `ec2022-62/`, `ec2022-56/`, `ec2022-52/` | 2022 Economic Census "BASIC" tables (revenue, firms, establishments, employees by NAICS code) for sectors 51 (information), 44-45 (retail), 62 (health care and social assistance), 56 (administrative and support), 52 (finance and insurance). Each folder has the data file, a field list and a README. | https://www2.census.gov/programs-surveys/economic-census/data/2022/sector{51,44,62,56,52}/EC22{sector}BASIC.zip |
| `naics-revenue-2022.json` | The US all-establishments rows I extracted for the codes used in the market table | made from the files above |
| `sector-*.html` | The Census landing pages that list those downloads | https://www.census.gov/data/tables/2022/econ/economic-census/naics-sector-62.html (and 51, 44-45, 56, 52) |

**Local only:** the raw `.dat` and `.zip` files in `ec2022-*/` are not in git (up to 175 MB each; GitHub rejects files over 100 MB). Re-download them from the links above. The numbers we use are in `naics-revenue-2022.json` and `ecnbasic-*.json`, which are in git.

Limits: revenue by NAICS code covers the whole industry, not caregiving. The Census data API now needs a free key, so the files were downloaded instead.

## 2f. Academic and survey literature on caregiver technology (collected 2026-11-01)

Folder: `literature/`. Eleven sources, each saved as `.html` or `.pdf` plus a `.txt` copy. Six were read in full except the reference lists; five were read in part (the agent's notes: Chen 2024, Lin 2026, Espirito-Santo 2024, Barr 2024 and Malden 2025 were partial). I checked 12 key quotes against the saved text.

| File prefix | Citation | URL |
|---|---|---|
| `kelley-2024-...` | Kelley et al., J Med Internet Res 2024;26:e46108, DOI 10.2196/46108 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11157180/ |
| `salagonzalez-2021-...` | Sala-Gonzalez et al., IJERPH 2021;18(4):1702, DOI 10.3390/ijerph18041702 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7916631/ |
| `zou-2024-...` | Zou et al., JMIR Aging 2024;7:e58517, DOI 10.2196/58517 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11617330/ |
| `chen-2024-...` | Chen, Lee, Ma, JMIR Form Res 2024;8:e51076, DOI 10.2196/51076 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11091808/ |
| `desormeaux-2021-...` | Desormeaux-Moreau et al., JMIR Aging 2021;4(2):e21808, DOI 10.2196/21808 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8087965/ |
| `lin-2026-...` | Lin et al., JMIR Aging 2026;9:e76115, DOI 10.2196/76115 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13256489/ |
| `espiritosanto-2024-...` | Espirito-Santo et al., Pharmacy 2024;12(1):20, DOI 10.3390/pharmacy12010020 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10893508/ |
| `geneva-co-caregiving.*` | Kaboha et al., AH2021 (ACM), DOI 10.1145/3460881.3460886 | https://access.archive-ouverte.unige.ch (unige:158901) |
| `audio-recording-feasibility-...` | Barr et al., Patient Educ Couns 2024;131:108574, DOI 10.1016/j.pec.2024.108574 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11701810/ |
| `assistive-tech-barriers-...` | Malden et al., JMIR Aging 2025;8:e73917, DOI 10.2196/73917 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12661617/ |
| `aarp-2022-...` | Keenan, US Caregivers' Use of Technology, AARP Research 2022, DOI 10.26419/res.00566.001 | https://www.aarp.org/pri/topics/ltss/family-caregiving/caregiving-technology-survey/ |

Not found: any study of siblings coordinating care through an app, and any caregiver-specific study of AI visit summaries. Two AARP and NAC older technology reports were seen only as search snippets and were not used.

## 2g. Competitor sites and App Store reviews (collected 2026-11-01)

Folder: `competitors/`. One subfolder per company with the pages read (`.html` plus `.txt`): Caring Village, CaringBridge, Lotsa Helping Hands, ianacare, Kin Health (meetkin.com), Cariloop, Wellthy, Papa, Honor, Medisafe, MyTherapy, Cozi, TimeTree, FamilyWall, Everplans, Trustworthy, A Place for Mom, Caring.com, Capsule, Amazon Pharmacy and PillPack. `carallel/` holds nothing useful: carallel.com returned HTTP 403.

`app-store-reviews/` holds 24 raw JSON files from Apple's public review feed (3 pages for each of 8 apps), and `app-store-listings/` holds the store listing JSON. I recounted the stars per app from the JSON and checked 13 quotes: all matched. Counts read: CaringBridge 150, Medisafe 150, Cozi 150, MyTherapy 150, Caring Village 54, Lotsa 56, Kin 46, ianacare 15.

Limits: Apple reviews only (the most recent per app); Google Play reviews were not read. Company statements about HIPAA, security and user counts are the companies' own claims and were not verified.

## 2h. Market-research firms' own report pages (opened 2026-11-01)

Folder: `market-reports/`. The publisher's own landing page for each report whose figure appears in the market table, saved as `.html` with a `.txt` copy. I read the surrounding sentence for each cited figure on the saved page. Findings: Wise Guy Reports, HTF Market Intelligence, Credence Research, Fact.MR, SNS Insider, MarketIntelo, Kenresearch, Verified Market Research and Transparency Market Research matched what I had cited. The Insight Partners page says CAGR 4.6% to $11.86B by 2034, which corrected my 5.19%. Grand View Research was seen only through a reseller's copy (`gii-gvr`). Data Bridge Market Research returned HTTP 403 (`databridge.html` holds only the error page).

| File | Publisher page |
|---|---|
| `wiseguy.html` | https://www.wiseguyreports.com/reports/caregiver-app-market |
| `htf.html` | https://www.htfmarketintelligence.com/report/global-pill-reminder-app-market |
| `credence.html` | https://www.credenceresearch.com/report/elderly-care-services-market |
| `insight.html` | https://www.theinsightpartners.com/reports/personal-emergency-response-system-market |
| `factmr.html` | https://www.factmr.com/report/digital-caregiver-platforms-market |
| `sns.html` | https://www.snsinsider.com/reports/ai-medical-scribing-market-10467/segmentation |
| `marketintelo.html` | https://marketintelo.com/report/password-manager-market/amp |
| `kenresearch.html` | https://www.kenresearch.com/industry-reports/global-digital-legacy-market |
| `vmr.html` | https://www.verifiedmarketresearch.com/product/caregiver-app-market/ |
| `tmr.html` | https://www.transparencymarketresearch.com/medication-adherence-packaging-market.html |
| `gii-gvr.html` | https://www.gii.tw/report/grvi2089724-non-medical-home-care-market-size-share-trends.html (reseller copy of Grand View) |
| `databridge.html` | https://www.databridgemarketresearch.com/reports/global-patient-portal-market (HTTP 403) |

Retried 2026-11-01 with normal requests: the Lotsa Helping Hands help center loaded (`competitors/lotsa-helping-hands/helpcenter-home.*`, a short index page only); carallel.com still returns 403; papa.com/faq is a Notion page that needs JavaScript; the Medisafe pricing and TimeTree privacy URLs I guessed do not exist. These need a real browser.

## 2i. Audience data gaps (collected 2026-11-01)

Folder: `audience/`. Each saved as `.html` or `.pdf` plus `.txt`. Quotes checked against the saved text.

| File | Source | What it gave |
|---|---|---|
| `can-cic-survey-2026.pdf` | Caregiver Action Network, Caregiver Tech Insights Survey 2026. https://www.caregiveraction.org/wp-content/uploads/2026/05/CIC-Survey-2026.pdf | Willingness to pay: 32% say a helpful tool should be free, 28% would pay $11 to $25 a month, "Only 12% said they would personally pay out of pocket", 64% say insurance should cover it. 272 respondents from CAN's email list (self-selected). |
| `pubmed-schulz-2016.html` | Schulz et al., The Gerontologist 2016, abstract on PubMed. https://pubmed.ncbi.nlm.nih.gov/26035899/ | About 20% would pay nothing for kitchen and self-care technologies; willing payers averaged about $50 a month for monitoring technology. Full text was blocked (403), so abstract only. |
| `pmc-digital-proxy-behavior.html` | JMIR 2025, digital proxy behavior in the US. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12360674/ | 657 US adults: 49% had digital proxy duties; about one-third of proxies used informal access; about 10% logged on by knowing the owner's credentials. All adults, not only caregivers. |
| `pmc7199170.html` | JAMA Internal Medicine, hospital portal password sharing (PMC copy). | In 94 hospitals asked, 42 (45%) endorsed password sharing between patient and caregiver. About hospital staff, not caregivers. |
| `northwestern-mutual-2019-care-study.html` | Northwestern Mutual 2019 C.A.R.E. study press release. https://news.northwesternmutual.com/2019-04-03-Northwestern-Mutual-Study-Caring-for-Aging-Parents-is-Not-a-Family-Affair | 83% have siblings; one in 10 say siblings share equally; 40% say siblings do not help; 41% say they are the primary caregiver. A company press release, 2019, no method shown. |

Blocked and not used: jamanetwork.com, beckershospitalreview.com, academic.oup.com (all 403), dataintelo.com (403).

## 2j. More market-research pages and store data for segments 11 to 14 and the size gaps (collected 2026-11-01)

- `market-reports/`: added the research firms' own pages for adult day care (Grand View, Polaris, IBISWorld), mental health apps (Grand View, Global Market Insights), telehealth (Grand View, Global Market Insights, IMARC), healthcare navigation (Grand View, Global Market Insights), benefits navigation (Verified Market Research, The Business Research Company, Marketintelo, Data Horizzon), family calendar and parenting apps (Market Intelo, SkyQuest, Congruence, Verified Market Research, DataHorizzon), and senior living (Towards Healthcare, Technavio). `segments-11-14.json` and `missing-sizes.json` hold the agents' structured notes. Two 403 pages were kept as evidence of the block: `alliedmr-telehealth.html`, `marketsandmarkets-mental-health-apps.html`.
- Opened in Chrome through the Claude extension on 2026-11-01 (no file copy except the Grand View excerpt): Data Bridge's patient portal page (USD 6.43B in 2025, USD 18.13B in 2033, CAGR 13.84%) and Grand View's non-medical home care page. Excerpt: `market-reports/grandview-non-medical-home-care-EXCERPT.txt`.
- `app-stores/apple-segments-11-14/` and `google-play/segments-11-14/`: store data for the apps in segments 11 to 14. I checked 15 of the Apple rating counts against the saved JSON; all matched.
- Searched, not found: a research-firm size for senior care referral and placement services; a dedicated size for employer caregiver benefits; a dedicated size for family organizer apps (only adjacent categories).

## 2k. Indie and launch-site results (collected 2026-11-01)

Folder: `indie/`. `producthunt-searches-2026-11-01.txt` holds the names and taglines returned by Product Hunt searches for caregiver, aging parents, eldercare and doctor visit notes, opened in Chrome through the Claude extension. A bot-check page appeared on some loads; I waited without interacting and did not solve it. The search "family caregiver" stayed behind it and returned nothing. Indie Hackers retired its search in 2026 (its page returns HTTP 410). GitHub and Hacker News results are in `github/` and `hackernews/` (sections 2c and 2d).

Sources I could not open, with what I need from you: `from-user/README.md`.

## 3. Earlier research (secondary sources; not yet re-read at the primary source)

`docs/market-research-prompt2-results.md`, `docs/market-size-table.md`, `docs/possible-market-segments-table.md` and `docs/market-opportunity.md` rely on market-report publisher summaries, press releases and vendor pages found by web search. Their links are in those files. They have not been re-checked against the full primary reports, and the paid reports are not available. Treat them as first-pass until redone.

`docs/qualitative-research-findings.md` summarizes about 86 Reddit and forum pages collected through NotebookLM. The notebook sources are not saved in this repo.
