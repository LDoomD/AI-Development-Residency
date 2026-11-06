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

### 2f-2. Schulz et al. 2016, full text now saved (collected 2026-11-01)

`literature/schulz-2016-willingness-to-pay-PMC5019044.html` (exact page) and `.txt` (text extracted by code). Source: PubMed Central author manuscript, https://pmc.ncbi.nlm.nih.gov/articles/PMC5019044/ (the publisher's PDF returned 403 and was not retried). Schulz R, Beach SR, Matthews JT, et al. "Caregivers' Willingness to Pay for Technologies to Support Caregiving." The Gerontologist 2016;56(5):817-824.

What the full text says: national web survey, N = 512 caregivers aged 18-64 caring for an older adult; nonprobability web panel, weighted to the NAC caregiver survey; 78% care for a parent, 56% live with the care recipient, 30% income $75,000 or more. About 20% would pay nothing for kitchen and self-care technologies; among payers the mean was about $50 a month for monitoring and $70 for monitoring plus assistance; the authors say willingness is "capped at around $70 per month"; most think government or private insurance should help pay. Limit: the technologies were kitchen and personal-care monitoring and assistance for the care recipient, not coordination or information-sharing tools, and the survey is from before 2016.

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

**Privacy warning for sections 2l, 2m and 2n:** the saved `.html` and `.json` files keep the original forum and YouTube usernames (the `.txt` files replace them with [member]). The repository is private. Before making it public or sharing the folder, delete the `.html` and raw `.json` files in `forums/` and `youtube/comments-raw/` and keep only the `.txt` files.

## 2l. AgingCare caregiver forum threads (public, collected 2026-11-01; first open pass)

Folder: `forums/agingcare/<topic>/<thread-id>.html` (exact page, saved byte for byte) and `.txt` (text extracted from that page by code). List of every thread: `forums/agingcare/manifest.csv`. Tool: `forums/fetch_agingcare.py` (plain HTTP request, 10 second delay, as the site's robots.txt asks; only thread pages).

| Item | Detail |
|---|---|
| Source | AgingCare.com caregiver forum, https://www.agingcare.com/caregiver-forum |
| Threads | 41, dated 2026-03-13 to 2026-10-31. Topics: Family Caregiver 7, Relationships 6, Caregiver Support 4, Financial Planning 4, Medications 4, New to Caregiving 4, Working Caregiver 4, Paying for Care 3, Power of Attorney 3, Care Decisions 2 |
| How chosen | Recent threads from each topic's listing page, picked by agents with no keyword filter. Older "most popular" threads were skipped because they were dated before 2024 or undated. |
| Handles | Member usernames are replaced with [member] in the .txt files. The .html files are untouched. |
| Check run | 121 random lines from the 41 .txt files were searched for in the matching .html: all 121 found. |

Limits: 5 of 41 threads show more answers on the page than the HTML holds (replies behind "See all" are not in the saved page). A first pass by model agents retyped the text and one typo was found, so those files were replaced by the code-made versions above. Forum posters skew toward frequent posters and dementia care. Not a representative sample. Facebook groups were not used (private; terms forbid scraping). Reddit: not yet collected (Firecrawl does not support it).

## 2m. ALZConnected community threads (Alzheimer's Association; public; collected 2026-11-01; first open pass)

Folder: `forums/alzconnected/discussions-recent/<thread-id>.html` (exact page) and `.txt` (text extracted from it by code). List: `forums/alzconnected/manifest.csv`. Tool: `forums/fetch_alzconnected.py` (plain HTTP request, 10 second delay; only `/discussions`, `/discussions/p<N>` and `/discussion/<id>/<slug>`, which the site's robots.txt allows).

| Item | Detail |
|---|---|
| Source | https://alzconnected.org/discussions |
| Threads | 101, the first four pages of "recent activity" on 2026-11-01; thread dates 2021-12-05 to 2026-11-01 (2 are older than 2024) |
| Who they are about | By category: caring for a spouse or partner 45, caring for a parent 26, general caregiver topics 16, living with dementia 8, long distance 2, other 4. Mostly spouses, unlike AgingCare (mostly parents). |
| How chosen | Page order only, no keyword filter |
| Handles | Member usernames replaced with [member] in the .txt files; .html untouched |
| Check run | 382 random lines from the .txt files searched for in the matching .html: 381 found; the one miss differs only by a non-breaking space |

Limits: long threads show only page one of replies (later pages not fetched); no thread reached 50 messages. People in a dementia-focused community, so it skews to dementia care. Not a representative sample.

## 2n. YouTube caregiver videos and comments (YouTube Data API v3; collected 2026-11-01)

Folder: `youtube/`. `search-raw/` = Google's search answers saved byte for byte (7 topic searches); `candidates.csv` = the videos that passed the filters; `comments-raw/<video-id>/` = Google's comment answers (.json, exact) and `comments-raw/<video-id>.txt` = text extracted from them by code. Tool: `youtube/fetch_youtube.py`. The API key is in `.env` (not in git).

| Item | Detail |
|---|---|
| Source | https://www.googleapis.com/youtube/v3/ (official API; terms: https://developers.google.com/youtube/terms/api-services-terms-of-service) |
| Videos | 12 of the 13 that passed the filters (video 9, a video for mothers of estranged adult children, cut as off topic). Topics searched: caring for an aging parent, siblings not helping, caregiver burnout, long-distance caregiving, a parent's medications, power of attorney, dementia caregiving. |
| Filters | Posted after 2023-11-01, English, 100+ comments, at most 2 per channel, top results by YouTube's relevance order. The long-distance and medications searches returned nothing with 100+ comments, and nothing at 50+, so those two topics are not covered. |
| Comments | About 3,500 top-level threads (up to the first 500 by YouTube's "relevance" order per video) plus the replies shown with them |
| Handles | Commenter names replaced with [member] in the .txt files; .json untouched |
| Check run | 180 random lines from the .txt files searched for in the saved .json: all 180 found |

Limits: comments are short and react to a video; commenters are the audience of each creator (many are coaches or self-help channels). Order is YouTube's "relevance," not a random sample. Firecrawl's YouTube reader was also tested (2 calls, 10 credits) but its output was not used: it cannot save to a file.

## 2o. Academic papers on coordination, siblings, technology, cost and distance (collected 2026-11-01)

Folder: `literature/papers/` (exact copy as `.html` or `.pdf`, plus `.txt` extracted by code; `status.csv` lists all 18). Found with `literature/search_openalex.py` (OpenAlex answers saved byte for byte in `literature/openalex-raw/`; all 89 results in `literature/openalex-candidates.csv`); copies fetched with `literature/fetch_papers.py` (PubMed Central first, then the open-access link; blocks are recorded, not worked around). 18 papers were picked by title and journal and approved by the project owner; 15 saved.

| Paper | Year | Saved from |
|---|---|---|
| Family Caregiver Experiences Coordinating Care of Older Adults | 2025 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12631485/ |
| Caring in the Information Age: Personal Online Networks to Improve Caregiver Support | 2017 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5495540/ |
| Family Care Partners and Paid Caregivers: National Estimates of Role-Sharing in Home Care | 2024 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11772859/ |
| Designing Interactive Systems to Mediate Communication Between Formal and Informal Caregivers in Aged Care | 2019 | https://ieeexplore.ieee.org/ielx7/6287639/8600701/08906121.pdf |
| “It made me feel like I wasn’t alone in the darkness”: exploring dementia care network communication and coordination through a digital health platform | 2022 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9667183/ |
| Designing trustworthy, low-threshold care coordination: co-creating a hybrid CareCompass with rural informal caregivers | 2026 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13478116/ |
| Division of Parent Care Among Adult Children | 2019 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7751154/ |
| Paid Leave Mandates and Care for Older Parents | 2024 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11576588/ |
| Factors Predicting Decisions About Technology Adoption Among Older Adults | 2017 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6177084/ |
| Sex and gender differences in technology needs and preferences among informal caregivers of persons with dementia | 2020 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7236350/ |
| The burden of family caregiving in the United States: work productivity, health care resource utilization, and mental health among employed adults | 2017 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5723115/ |
| Economic Spillover Effects of Intensive Unpaid Caregiving | 2019 | https://link.springer.com/content/pdf/10.1007/s40273-019-00784-7.pdf |
| Close enough? Adult child-to-parent caregiving and residential proximity | 2021 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8806164/ |
| Spatial Distance Between Parents and Adult Children in the United States | 2019 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7537569/ |
| Caregiving across distances: residential proximity, care activities, and mental health | 2026 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13418846/ |

Not saved (publisher returned 403; not retried): Technology Use among Family Caregivers of People with Dementia (2020); Patterns of help and care by adult only children and children with siblings (2022); Family caregiver readiness to adopt smart home technology to monitor care—Dependent older adults: A qualitative exploratory study (2023). If you can open them from your library, drop the PDFs in `docs/sources/from-user/`.

Limits: PubMed Central slows requests that come too fast (a bot-check page appeared and cleared when requests were spaced 30 seconds apart). Findings from these papers are in `docs/academic-findings.md`, marked by what was read (abstract so far).

## 2p. App-store reviews, what users say (Apple public review feed; collected 2026-11-02)

Folder: `app-reviews/`. This is user voice, kept apart from the competitor material in `competitors/` (which is parked until a problem is chosen). Source: Apple's public customer-reviews RSS/JSON feed, up to 10 pages of 50 most recent reviews per app and country. No login; no page scraping. `fetch_apple_reviews.py` saved the exact feed JSON in `raw/<country>/` and extracted the text by code into `reviews.csv` (9,448 reviews, 44 apps, 2013 to 2026). `search_apple.py` and `lookups/` hold the app searches used to choose the apps.

Groups: family coordination and organizers (Caring Village, CaringBridge, Lotsa, ianacare, Cozi, TimeTree, FamilyWall, John Hancock CareGiver, tendercare), medication (Medisafe, MyTherapy), visit notes (Kin), safety and alerts (Lively, MyMedicalGuardian, Aloe Care, Life360, Snug, FallCall), watches and health devices (Apple Watch app, Fitbit, Garmin, Samsung Health, Samsung Galaxy Watch, Wear OS, Fossil, Omron, Withings, Kardia, a seizure-alert watch app), and apps from the UK, Australia, Germany, India, Japan and Canada, read in their home storefronts for learning only (the market stays US).

Limits: this feed is iPhone reviews only. The "Android watch" apps in that feed (Samsung, Wear OS, Fossil) are their iPhone companions.

Android: `app-reviews/google-play/` holds 4,777 reviews from 10 Google Play apps (Galaxy Wearable, Wear OS, Medisafe, MyTherapy, Caring Village, CaringBridge, Life360, MyMedicalGuardian, OMRON connect, Withings), collected 2026-11-02 in the project owner's Chrome, with permission, by opening each app's Play page, loading "See all reviews" and reading the page. Google Play has no public review feed. Chrome blocked repeated file downloads, so the page text was sent to a local script (`receive_reviews.py`, 127.0.0.1 only, since stopped) that wrote the bytes to the JSON files. Reviewer names are not saved. Limits: about 540 reviews per app (820 for Galaxy Wearable; 42 for Caring Village), in the page's default order, not a complete or random set; each file's note gives the share of 1 and 2 star reviews. Not collected: Fossil, Fitbit and Garmin (judged not caregiving apps). Apps with many ratings are capped at the 500 most recent written reviews; several international apps have few or no written reviews. `raw/` keeps reviewer usernames (same privacy warning as above); `reviews.csv` leaves them out. `raw/` is NOT in git (it keeps reviewer usernames; see `.gitignore`): regenerate it with `fetch_apple_reviews.py`, or rely on `reviews.csv`, whose `source_file` column names the raw file each review came from. No theme reading has been done yet.

## 2q. Company funding and value (collected 2026-11-02)

Folder: `funding/` (one subfolder per company, plus `group-a.json`, `group-b.json`, `group-c.json`, `build_funding_outputs.py`), and the combined list `docs/company-funding.md`. 66 companies were searched; 41 have a sourced figure, 25 are NOT FOUND (reasons in the JSON `tried` field). Figures are different measures (funding raised, valuation, acquisition price, annual revenue, franchise system sales) and are not comparable. Aggregator estimates (PitchBook, Tracxn, Caplight, GetLatka, CB Insights snippets) were not used because they disagree.

Each figure comes from a page a research agent opened and saved; the supporting sentence was extracted from the saved file by code, and I re-checked that each figure appears in its saved file. Limits: press releases and news pages were read, not full annual reports or franchise documents. The websites of 24 of the 41 blocked normal downloads, so their saved files are short Firecrawl text excerpts, not exact page copies (file names contain `firecrawl` or `extract`). For six of them, the page was opened in Chrome on 2026-11-02 and a highlighted screenshot saved (`chrome-verification.md`); the Papa page showed a Cloudflare human-verification check and is still unsaved. Most "latest round" entries were not checked for later rounds. Two saved pages were edited to replace a third party's public site key with `REDACTED-PUBLIC-KEY` before committing (`abridge/series-e.html`: an analytics script key; `caring-village/press.html`: a Google Maps embed key); the rest of each page is unchanged.

## 2r. App-review problem reading (2026-11-02)

Folder: `app-reviews/analysis/`. Output: `docs/app-review-findings.md`. 1,475 of the 14,225 reviews in 2p matched an English caregiving or family word list (`make_slices.py`) and were read by four reader agents (`slices/`, `slice-N-tags.json`). `verify_tags.py` checked every quote as an exact substring of the original review (1,312 verified, 0 dropped; I also re-checked 12 random quotes against `reviews.csv` and the Google Play JSON files by hand: 12 of 12). `build_findings.py` generates the findings file from `verified-tags.json`, so no count or quote in it is typed by hand. Limits: the other 12,750 reviews were not read; one reader and one category per review; the apps were chosen by the project team, which shapes the counts (location and alert complaints come mostly from Lively and Life360).

## 2s. Competitive analysis inputs (2026-11-02)

Folder: `competitive-analysis/` and `competitors-2/`. Output: `docs/competitive-analysis.md` and the Figma section (node `2322:9639`). `competitors-2/` holds exact HTML copies and extracted text of public company pages saved on 2026-11-02 by `save_pages.py` (respects robots.txt: Life360, OMRON, Withings and 1Password disallow automated fetching and were not fetched; 404 and tiny pages are logged in `save_log.json`), plus the three companies' own App Store descriptions (`appstore-description.txt`, from the iTunes lookup JSON). `competitive-analysis/` has `manifest.json` (which saved pages each company uses), `extract-1..4.json` (exact quotes picked by four readers from the saved text), `assemble.py` and `assemble-log.json` (script check that every quote is an exact substring of its file; removals and price expansions logged), `urls.json` (the live URL for each page and how it was confirmed), `compose.py` and `table-rows.json` (the table rows), `gaps-draft.txt` (the draft summary box). Limits: quotes were chosen by readers (judgement); several saved pages are mostly navigation or testimonials; the Caring Village FAQ link is unverified; the Chrome checks were done by loading each page and testing for a snippet of each quote (results not saved as screenshots).

## 3. Earlier research (secondary sources; not yet re-read at the primary source)

`docs/market-research-prompt2-results.md`, `docs/market-size-table.md`, `docs/possible-market-segments-table.md` and `docs/market-opportunity.md` rely on market-report publisher summaries, press releases and vendor pages found by web search. Their links are in those files. They have not been re-checked against the full primary reports, and the paid reports are not available. Treat them as first-pass until redone.

`docs/qualitative-research-findings.md` summarizes about 86 Reddit and forum pages collected through NotebookLM. The notebook sources are not saved in this repo.

## 2t. Classmate Notion page, Market Research (outline only)
- Copy: `docs/sources/classmate-notion/market-research-page-outline.md`; source https://app.notion.com/p/Market-Research-401e2016f74880be8e31cebffcf7e37f; read 2026-11-02 via Firecrawl; headings only, tables and images not returned.

## 2u. Small Apple review samples for Everplans and Epic MyChart (2026-11-02)
- Fetched with `app-reviews/fetch_apple_reviews3.py` (public feed; Everplans 8 reviews = all it returns, Epic MyChart 200 most recent); `reviews3.csv`, `all-reviews3.jsonl` (ids c-N); my reading of the 13 that mention a family word is in `app-reviews/analysis/sample3-tags.json` (every evidence quote checked as an exact substring). Raw files with usernames are in the gitignored `raw/`. Not part of the 439 caregiving count.

## 2v. Guides on questions to ask about competitors (2026-11-02)
- Folder `competitor-questions/`: saved copies (`.html` and `.txt`) of Aha! (https://www.aha.io/roadmapping/guide/product-strategy/how-should-product-managers-research-competitors), Productboard (https://www.productboard.com/glossary/competitor-analysis/), Coursera (https://www.coursera.org/articles/competitor-analysis) and Salesforce (https://www.salesforce.com/blog/small-business/what-is-competitor-anaylsis/). Fetched 2026-11-02 after a robots.txt check (all allowed). Text versions are tag-stripped by script. Used in `docs/competitor-questions.md`. Salesforce: the article is lines 14-70 of the text copy (the rest is a sign-up form and a country list); its product, cost and place questions are cited.

## 2w. Instructor NotebookLM notebook, two questions (2026-11-02)
- Folder `instructor-notebook/`: the question sent and the notebook's full answer text for each (`answer-1-order-of-steps.txt`, `answer-2-followup.txt`). Asked in the owner's signed-in Chrome session with the owner's OK. The notebook is the instructor's ("AI Development Residency - Learning Materials", 93 sources). Limit: the notebook's own words and quotes; I could not open the underlying documents, so its quotes are reported, not verified by me. The two answers differ on whether a segment is chosen early (see the answers).

## 2x. Audience Segmentation, Goals, Motivations, and Use Cases Workshop template (2026-11-02)
- `audience-workshop-template/template-text.md`: text copy of all 7 sections of the community template the owner linked (https://www.figma.com/board/Q5jRpN3MbONqFQF6KTS70j/). Read-only. Used to set the order of work for audience goals and use cases.

## 2y. Instructor notebook, check of the audience segmentation work (2026-11-02)
- `instructor-notebook/answer-3-check-of-audience-work.txt`: the question (a summary of the audience work and six questions) and the notebook's full answer. Asked in the owner's signed-in Chrome session at the owner's request. Limit: the notebook's own words and quotes; I could not open the underlying course files, so its quotes are reported, not verified by me. Differences from the Community template board are noted in the chat reply.

## 2z. Exhaustion and dementia behavior: demand, market size, existing offerings (2026-11-02)
- `alz-facts-figures-2026/facts-and-figures-2026.pdf`: Alzheimer's Association 2026 Alzheimer's Disease Facts and Figures, full PDF (https://www.alz.org/getmedia/ef8f48f9-ad36-48ea-87f9-b74034635c1e/alzheimers-facts-and-figures.pdf), downloaded directly; `raw.txt` is the text (reading order). Pages cited in `docs/exhaustion-dementia-research.md` are PDF pages (49, 52, 55). Limit: report figures are the Association's own estimates.
- `market-reports/respite-coherent-2026.{html,txt}` and `respite-researchandmarkets-2026.txt`: the free pages of two paid respite-care market reports (https://www.coherentmarketinsights.com/industry-reports/respite-care-for-the-elderly-market and https://www.researchandmarkets.com/reports/6055528/respite-care-the-elderly-market-global). Limit: summaries only; method not seen; scope is care services.
- `competitors-3/pages/`: text of 10 offering pages, directly downloaded 2026-11-02 (HTML tags removed). `competitors-3/offerings.json`: the quotes, who-pays notes and a "verified" field per quote. 28 of 41 quotes were re-checked by script against these copies. Torchlight, Positive Approach to Care and Savvy Caregiver returned 403 to direct download, so their 12 quotes came from a Firecrawl scrape and are NOT re-checked; no workaround was tried. The research agent first saved hand-copied excerpts; those were deleted and replaced.

## 3a. Instructor notebook, how to choose the problem (2026-11-02)
- `instructor-notebook/answer-5-choosing-the-problem.txt`: the question (with a summary of where the project stands) and the notebook's full answer. Asked in the owner's signed-in Chrome session at the owner's request. Limit: the notebook's own words; its quotes are reported, not verified by me against the course files.

## 2026-11-03 additions (source fixes after the board review)

| File | What it is | Original URL | Used for |
|---|---|---|---|
| `market-reports/cnn-2024-10-06-mercer-caregiving-benefits.md` | CNN article (Jeanne Sahadi, 2024-10-06, WRAL copy) quoting Mercer's survey of employers with 500+ staff. Read in full. Secondary: journalist quoting Mercer; the survey report itself is gated and was not opened. | https://www.wral.com/archive/21660040/ | The "34% offer or plan elder care referrals, 10% offer digital tools for caregivers" line in the market analysis. |
| `market-reports/mercer-2023-next-frontier-caregiving.md` | Mercer's own article "The next frontier: Caregiving of adults" (March 2023). Read in full. Primary for the 2023 figure: one-third of large employers offer elder-care referral services; 28% facility search; 19% backup elder care; 13% elder-care leave. | https://www.mercer.com/en-us/insights/us-health-news/ushn-202303-02/ | Confirms the order of magnitude of the CNN figure. |
| `competitors/caring-village/www_caringvillage_com_faq.LIVE-CHECK-2026-11-03.md` | Fresh fetch of the Caring Village FAQ (HTTP 200, page last modified 2026-06-01) with the four quoted lines checked word for word. | https://caringvillage.com/faq/ | Clears the four "page link not verified" cells in the competitive analysis table. |

Also resolved the same day without new files: the second pill-reminder market figure ($628M in 2025 to $2,068M in 2034, CAGR 14.2%) traces to a Topflight Apps blog post quoting an unnamed report, https://topflightapps.com/ideas/how-to-create-a-medication-reminder-app/ (recorded in `docs/market-research-prompt2-results.md`); it stays labelled "blog, publisher unnamed" and the HTF figure remains the main one.
| `fleety/answer-1-feature-analysis-and-next-steps.md` | Fleety (Tech Fleet helper bot, TAL 9000) answer, asked 2026-11-03 in the owner's signed-in session with his approved question. Word for word, with the 6 guide.techfleet.org pages it cites. A bot answer, not a primary source; the cited guide pages were not opened. | https://techfleet.network/tal-9000 (sign-in required) | What a feature comparison must include, how to fill the "our company" row, and the order feature analysis, UVP, positioning, Vision Board. |

## 2026-11-03 feature analysis: missing competitor pages found

Why: several earlier saved pages were empty or 404. Checked 2026-11-03 in the built-in browser: most were guessed addresses that do not exist on the sites (Caring Village /features and /security, CaringBridge /how-it-works and /features, Lotsa /faq/ and /features/, Medisafe /medfriend and /pricing); Lively moved its pages to shop.lively.com. The real pages were found from each site's own menu and copied as text with the date and URL at the top of each file. Used in `docs/feature-analysis.md` (steps 2 and 3).

| File or folder | What it is | Original URL | Used for |
|---|---|---|---|
| `competitors/caring-village/pages-2026-11-03/app.txt` | Caring Village "The App" page: seven tools, Julia, role-based invites, plans | https://caringvillage.com/app/ | Caring Village features |
| `competitors/caringbridge/help-center-2026-11-03/` (7 files + README) | CaringBridge help center: Requests (replaced the Planner in Dec 2023), Meal Train, privacy settings, Ways to Help and Page Settings article lists | https://caringbridge.my.site.com/help/s/ (from www.caringbridge.org/help) | CaringBridge features |
| `competitors/lotsa-helping-hands/pages-2026-11-03/` (2 files) | Lotsa help center: create groups (who sees what), announcements and emailing | https://lotsa.helpscoutdocs.com/ | Lotsa features |
| `competitors/medisafe/pages-2026-11-03/features.txt` | Medisafe "App Features" page: Medfriend, refill and appointment reminders, 90+ trackers | https://medisafeapp.com/features/ | Medisafe features |
| `competitors-2/lively/shop-pages-2026-11-03/` (4 files + README) | Lively caregivers, services, medical alert plans ($24.99/$34.99 per month; fall detection +$9.99), Everyday Support for Caregivers ($99/yr, Wellthy care coordinator, invite family) | https://shop.lively.com/pages/caregivers, /services, /medical-alert-compare-plan, /everyday-support-for-caregivers | Lively features |

Not re-fetched: Everplans, Epic MyChart and Medical Guardian (their saved main pages had full text). Limit: copied page text, not full HTML; demo-screen text, product listings and repeated quotes were trimmed and marked as trimmed in each file.

## 2026-11-03 feature analysis: more reviews

Why: the owner asked to fill feature boxes that had too few reviews. Collected in the built-in browser. Google Play has no public feed; reviews were read through the Play Store page's own review data request (the same data the "See all reviews" window loads), newest first. Reviewer names are not saved. Big apps were filtered by keyword, so these are not random samples.

| File | What it is | Original URL | Used for |
|---|---|---|---|
| `app-reviews/google-play/google-play-reviews-lotsa.json` | All 20 written Lotsa reviews on Google Play (page shows 51 ratings) | https://play.google.com/store/apps/details?id=com.lotsahelpinghands.android.lotsa | Lotsa row (none tagged: no reviewer clearly caring for a relative) |
| `app-reviews/google-play/google-play-reviews-lively-link-family-access.json` | 66 of 1,451 Lively Link reviews: family word plus invite/access/log-in words | https://play.google.com/store/apps/details?id=com.greatcall.link | Lively columns 2, 3, 7 |
| `app-reviews/google-play/google-play-reviews-caringbridge-family-help.json` | 36 of 2,080 CaringBridge reviews: family word plus help/requests/privacy/access words | https://play.google.com/store/apps/details?id=com.caringbridge.app | CaringBridge columns 1, 2, 3 |
| `app-reviews/google-play/google-play-reviews-mychart-family.json` | 58 of the 6,169 newest MyChart reviews (2026-07-15 to 2026-11-02) with a family or caregiving word | https://play.google.com/store/apps/details?id=epic.mychart.android | MyChart columns 3 and 6 |
| `forums/app-mentions-2026-11-03/agingcare.json` | AgingCare thread paragraphs naming the apps, word for word | thread URLs inside the file | Lively and Medical Guardian column 7 |
| `forums/app-mentions-2026-11-03/alzconnected.json` | ALZConnected sentences naming the apps; none usable for counts | thread URLs inside the file | Not counted (see note in file) |
| `app-reviews/analysis/extra-tags-2026-11-03.json` | Claude's column tags for the new reviews (one pass, not double-checked) | — | `feature_ratings.py` |
| `app-reviews/analysis/feature_ratings.py`, `feature-ratings.json` | Script that counts every feature box, and its output | — | Feature table on the board and in `docs/feature-analysis.md` |

Not found: Everplans has no Google Play reviews; Reddit is blocked in the built-in browser (not worked around); `app-reviews/save_play_2026_11_03.py` saved the Play files.

## 2026-11-03 feature analysis: Reddit caregiver posts (Arctic Shift archive)

Why: the owner asked for more qualitative evidence for the empty and vague boxes (documents, caregiver support, "Mixed"). Reddit itself is blocked in the built-in browser, so posts came from the Arctic Shift archive API (https://arctic-shift.photon-reddit.com/api, project https://github.com/ArthurHeitmann/arctic_shift), which is public and needs no login. Usernames were never requested. Report: `docs/reddit-caregiver-findings-2026-11-03.md`.

| File | What it is | Original URL | Used for |
|---|---|---|---|
| `reddit/arctic-shift-2026-11-03/posts.jsonl` | 43,665 posts since 2023-01-01: all of r/CaregiverSupport, r/AgingParents to Feb 2026 (stopped once there was enough data) | each line has its reddit.com link | Search and tagging |
| `reddit/arctic-shift-2026-11-03/posts_targeted.jsonl` | Newest ~500 posts from each of 11 other communities (dementia, Alzheimer's, caregivers, CaregiversOfReddit, eldercare, Parkinson's, stroke, ALS, MS, COPD, disability), plus 178 dementia posts from an early word search | each line has its link | Other-communities section of the report |
| `reddit/arctic-shift-2026-11-03/collect.py`, `collect_targeted.py`, `collect_recent.py`, `log*.txt` | Download scripts and their logs (rate-limit retries, why each was stopped) | — | Re-running the download |
| `reddit/arctic-shift-2026-11-03/build_candidates.py`, `tagging/` | Picks posts by topic words, splits them for reading; `INSTRUCTIONS.md` is the tag rule; `tags-*.jsonl` are the tags (Claude helpers, one pass, quotes checked word for word) | — | Counts in the report |
| `reddit/arctic-shift-2026-11-03/analyze_tags.py`, `reddit-findings.json` | Counts per feature, problem groups, quotes, wishes; removes app-maker posts and copies (list kept in the file) | — | Report numbers |
| `reddit/arctic-shift-2026-11-03/app-mentions.json` | 37 posts that name a competitor and say how it worked | links inside | Added to `feature_ratings.py` through `extra-tags-2026-11-03.json` |

## 2026-11-04 additions: Competitive Analysis 2

- `competitive-analysis-2/packs/*.json`: one evidence pack per competitor (1,101 items) built from saved app reviews, Reddit downloads and forum mentions by `build_packs.py`. No new web fetching.
- `competitive-analysis-2/themes/*.json`: the themes counted from every pack item read in full (577 caregiving items kept). Rules: `READER-INSTRUCTIONS.md`. Check: `verify_themes.py`.
- `competitive-analysis-2/facts/*.json`: company answers drawn from every saved company page (`competitors/`, `competitors-2/`, app store listings, `docs/company-funding.md`). Check: `verify_facts.py`.
- `competitive-analysis-2/answers-v2.json`, `figma-grid.json`: the table text. Checks: `audit_answers.py`, `audit_gaps_uvo.py` and Figma hash matches (220 of 220 table cells, 42 of 42 gaps and opportunities texts). Readable copy: `docs/competitive-analysis-2.md`.
- `competitive-analysis-2/feature-analysis-3/`: Feature Comparison Analysis 3 in the teacher's format. `theme-to-feature.json` (which counted theme belongs to which feature), `build_howwell.py` → `howwell-counts.json`, `fa3-text.json` (table text), `assemble_fa3.py` (builds `figma-fa3.json` and checks every number). Readable copy: `docs/feature-analysis-3.md`. Figma section `2584:10359`, hash-matched.

## 2026-11-04 additions: market analysis updated with Reddit

- `market-analysis-3/sample/`: random sample of 500 Reddit posts (no keyword filter) drawn by `build_sample.py` from the Arctic Shift downloads in `reddit/arctic-shift-2026-11-03/` (seed 20261104). No new web fetching.
- `market-analysis-3/CODING-INSTRUCTIONS.md`, `codes/part-1..4.json`: each post coded with the 14 forum themes (Claude readers, one pass, quotes checked word for word).
- `market-analysis-3/count_themes.py` → `reddit-sample-theme-counts.json`; `other_groups.py` → `other-groups.json`; `count_by_audience.py` → `reddit-sample-by-audience.json`.
- `market-analysis-3/ma3-text.json` → `build_ma3.py` → `ma3-filled.json` (every number filled from the counts). Readable copy: `docs/market-analysis-3.md`. Figma: market page section `2598:10950`, Audience page section `2605:638`. Hash-checked.

## 2026-11-04: Audience page in the teacher's format (`market-analysis-3/audience-v2/`)

- `build_packs.py` → `pack-1..6.json`: the 304 Reddit parent and spouse posts (from `goals/posts-*.json`) and the 109 forum threads the audience page was built from (full text from `forums/`).
- `MOMENTS-INSTRUCTIONS.md` → `codes-1..6.json`: for each problem in each item, when it happens, what the writer wants, and one exact quote (Claude readers, one pass). `verify_codes.py` checks the quotes and names (777 codes, 0 problems).
- `count_moments.py` → `moments-by-usecase.json`. `GROUPING-INSTRUCTIONS.md` → `groups-A1.json` and `groups-A2.json`.
- `uc-A1.json` and `uc-A2.json` hold the table rows. `check_uc.py` checks that every line is a top group, in order. `boxes.json` holds the box lists. `check_boxes.py` checks them against `goals/audience-tables.json`.
- `TABLE-RULES.md`: the readability and accessibility rules. `figma-teacher-format.json`: the data used in Figma section 2623:76. Readable copy: `docs/audience-teacher-format-2026-11-04.md`.

## 2026-11-04: Competitive Analysis 3, step 3 research (`competitors-4/`)

- `save_pages.py` saves each page byte for byte (`.html`) plus its text (`.txt`). It follows each site's robots.txt and logs blocked pages in `save_log.json` instead of working around them.
- Saved: an AARP article on geriatric care managers (updated August 05, 2026), a PMC study on Trualta (PMC8293668), the Eldercare Locator pages (eldercare.acl.gov, usaging.org), and two Aeroflow Urology pages.
- Blocked by robots.txt, so not saved: aginglifecare.org, trualta.com, aging.ny.gov (Trualta page), teepasnow.com.
- `evidence.json`: each competitor's claims, with the exact quote, URL, saved file and limits. It also reuses 4 earlier saved pages (A Place for Mom, the Alzheimer's helpline, Cariloop, Medicare GUIDE).
- `verify_quotes.py` proves every quote is in its saved page: 22 found, 0 not found (Calm and Headspace added from the 2026-11-02 saved pages).
- **Step 5a (basics for all 15 competitors):**
  - `basics-5a.json`: 10 new competitors, 6 fields each (segment, website, features, how they stand out, business model, who pays and the cost), each with exact quotes.
  - `verify_basics_5a.py`: 119 quotes found, 0 not found.
  - `basics-5a-kept.json`: the 5 kept competitors, copied from `docs/competitive-analysis-2.md`.
  - New pages saved by `save_pages_5a.py`:
    - an AgeWays page (an Area Agency on Aging, Michigan) saying Trualta is free to caregivers there
    - Calm's plans page
    - an Everyday Health review of Calm
    - a lifestack.ai blog on Headspace prices (third-party, weaker)
    - a Headspace page
  - Blocked by robots.txt: trualta.com/getting-started, coaaa.org. Returned bot-check pages (files deleted, still logged): areaagencyonaging.org, hr.msu.edu.
  - The step 3 log is kept as `save_log_step3.json`.
- **Fixes 2026-11-04 (Firecrawl, which renders JavaScript):**
  - `competitors-4/headspace/firecrawl_headspace_subscriptions.txt`: Headspace's official price, $69.99 a year or $12.99 a month. This replaces the third-party blog.
  - `competitors-4/medisafe/firecrawl_appstore_medisafe.txt`: Medisafe's App Store in-app prices, $2.99 to $9.99 a month or $27.99 to $39.99 a year.
  - Proof checks after the fixes: `verify_basics_5a.py` 120 found, 0 not found; `verify_quotes.py` 25 found, 0 not found.
  - Still open: the robots.txt-blocked and bot-check pages (Trualta, Aging Life Care, coaaa.org, the Cariloop individual price). Chrome wasn't available this session.
- **Fixes 2026-11-04 (read in the desktop app's built-in browser; the Chrome extension showed no connected browsers for this account):** in `competitors-4/manual-saves/`:
  - `aginglifecare_org_home.txt`: the care managers' own site
  - `coaaa_org_trualta.txt`: Central Ohio AAA, where Trualta is free to caregivers in 8 counties
  - `hr_msu_edu_cariloop_faqs.txt`: Cariloop is free to MSU employees, with extended coaching at $249 a month
  - trualta.com returned HTTP 500 (server error) in a real browser, so it can't be read today. Trualta's facts rest on two agency pages and the PMC study.
  - Proof checks: `verify_basics_5a.py` 125 found, 0 not found, 0 answers too long; `verify_quotes.py` 30 found, 0 not found.
  - Update: `manual-saves/trualta_com_for_caregivers.txt` is Trualta's own site, saved after the owner opened it in the built-in browser ("Offered at no cost through local partnerships"). Proof checks: 130 found and 32 found, 0 not found.

## 2026-11-04: Competitive Analysis 3, step 5b (`competitive-analysis-3/5b/`)

- `count_new_mentions.py` → `mentions.json`: every saved Reddit post (49,315) naming a new competitor.
- `build_packs.py` → `pack-1.json` and `pack-2.json` (207 items): the Reddit posts in full, plus forum threads (the text around each mention). For the Alzheimer's Association, forum matches count only if they name the helpline, because ALZConnected is run by the Association.
- `READING-INSTRUCTIONS.md` → `codes-1.json` and `codes-2.json`, written by two Claude readers, one pass each.
- `verify_and_count.py` → `counts-5b.json`: 207 coded, 135 relevant, 0 problems (every quote exact).
- `group_themes.py` → `themes-5b.json`: themes counted by distinct post. Unmatched labels are printed; none were left.

## 2026-11-04: Competitive Analysis 3 grid (`competitive-analysis-3/grid/`)

- `build_grid.py` → `grid.json`: 7 competitors × 13 columns (the teacher's template columns plus the 5 criteria). Every cell has a source: an exact quote in a saved file, exact text in Competitive Analysis 2, a 5b theme, a count, or "no evidence found" stated as such. The script checks them all: 91 cells, 125 sources, 0 problems.
- `competitive-analysis-3/count_segment_candidates.py` → `segment-candidate-mentions.json`: Reddit mentions for every company the market analysis names in the relevant segments.
- `competitors-4/manual-saves/acl_gov_nfcsp.txt`: the National Family Caregiver Support Program page (the federal program behind Area Agencies on Aging' caregiver services). robots.txt blocked the save script, so it was read in the built-in browser.
- **Grid fix (same day): more review sources, and every cell answers its question.**
  - `app-reviews/fetch_apple_reviews4.py` → `reviews4.csv`: Everplans App Store reviews (8). Cariloop had no written App Store reviews.
  - `competitors-4/manual-saves/google_play_cariloop.txt`: Cariloop's Google Play listing and its 2 written reviews.
  - `competitors-4/review-sites/bbb_2026-11-04.txt`: BBB records. Cariloop has 0 complaints and 0 reviews. A Place for Mom has 272 reviews (3.95 stars) and 109 complaints in 3 years. Excerpts are copied word for word.
  - `competitors-4/review-sites/trustpilot_everplans_2026-11-04.txt`: Everplans' only Trustpilot review.
  - Checked but no reviews: Shortlister (Cariloop, "Reviews pending").
  - After the rewrite: 91 cells, 131 sources, 0 problems.

## 2026-11-04 Competitive Analysis 3 grid, version 2 (cells rewritten as direct answers)

| File | What it is | Link | Used for |
|---|---|---|---|
| `competitive-analysis-3/grid/build_grid_v2.py` → `grid-v2.json` | Grid version 2: every cell rewritten to answer its column's question. Checker: 91 cells, 0 problems (each source found word for word, no cell over 16 words, no semicolons or research words, no "no data" sources). Version 1 (`build_grid.py`, `grid.json`) unchanged | — | The grid |
| `competitive-analysis-3/grid/fetch_threads.py` → `reddit-threads/*_<id>.txt` | 6 Reddit threads naming Everplans (5) or Cariloop (1), from the public Arctic Shift archive (Reddit is blocked for Firecrawl and the built-in browser). Usernames removed | reddit.com link at the top of each file | Everplans and Cariloop "do well" cells |
| `competitive-analysis-3/grid/search_comments.py` → `reddit-threads/search_everplans.json`, `search_cariloop.json` | Archive word search in 12 communities. Most searches were refused by the archive (HTTP 422 and 429), so this found only 5 Everplans items and 0 Cariloop | links inside | Not used in cells; kept to show what was tried |
| `competitors-4/manual-saves/google_play_cariloop_full_2026-11-04.txt` | Full Cariloop Google Play page text (the earlier save was missing part of the description), read in the built-in browser. Reviewer names removed | https://play.google.com/store/apps/details?id=com.cariloop.member | Cariloop cells |

| `competitive-analysis-3/grid/build_business.py` → `business.json` | Business questions table (how they make money, who pays, how they keep customers, customer experience, getting started) for the 7 competitors. Checker: 35 cells, 57 sources, 0 problems | — | Step 5, fourth table |

## 2026-11-04 Market analysis update: segments 11 (respite, adult day) and 12 (burnout support)

Why: exhaustion is the #1 caregiver problem, but segments 11 and 12 were never researched, so the competitive analysis had no competitors for it. No new web fetching in this pass.

| File | What it is | Link | Used for |
|---|---|---|---|
| `market-analysis-3/segments-11-12/search_saved_posts.py` | Searches the 49,315 saved Arctic Shift Reddit posts (`reddit/arctic-shift-2026-11-03/posts.jsonl`, `posts_targeted.jsonl`) with the word patterns listed in the script | — | Counts below |
| `market-analysis-3/segments-11-12/term-counts.json` | Posts matching each term, with the exact patterns used | — | Sizing segments 11 and 12 |
| `market-analysis-3/segments-11-12/matches.jsonl` | Every matching post: reddit.com link, community, date, terms, and an excerpt around each match | links inside | Auditing the counts; reading pass next |
| `market-analysis-3/segments-11-12/search_named_programs.py` → `named-counts.json`, `named-matches.jsonl` | Second search of the same saved posts for named offerings and payers (VA, Medicaid waivers, hospice respite, Area Agencies on Aging, the 10 offerings in `exhaustion-dementia-research.md`). 115 posts not already matched | links inside | Reading set |
| `market-analysis-3/segments-11-12/build_reading_packs.py` → `packs/pack-1..11.json`, `packs/manifest.json` | 1,086 items: all 632 respite or adult day posts, 115 named-program posts, random 150 support-group and 150 therapist posts (seed 20261104), 39 forum threads (text around each mention) | links inside | Reading pass |
| `market-analysis-3/segments-11-12/READING-INSTRUCTIONS.md`, `codes/codes-1..11.json`, `verify_codes.py` | Reader rules, the 11 readers' codes, and the checker (every item coded once, every quote exact: 0 problems) | — | Counts |
| `market-analysis-3/segments-11-12/count_results.py` → `results.json` | Counts per kind of help, barriers (with grouping rules for free-text barriers), providers, payers and costs, each with the post ids behind it | — | `docs/market-analysis-segments-11-12-findings.md` |
| `market-analysis-3/segments-11-12/research-checklist-audience-split.md` | Checklist filled in and shown to the owner before the audience split | — | Rule #1 |
| `market-analysis-3/segments-11-12/label_audience.py` → `audience-script.json`, `audience-packs/`; `AUDIENCE-INSTRUCTIONS.md`, `audience-codes/acodes-1..5.json`, `verify_audience.py` | Labels each relief post with the "cared_for" labels: script for clear posts, readers for the rest, and a 40-post spot check (38 agree) | — | Audience split |
| `market-analysis-3/segments-11-12/count_by_audience.py` → `audience-labels.json`, `results-by-audience.json` | Merged labels and every relief count split by Audience 1, Audience 2 and other | — | Findings, "split by audience" |

## 2026-11-04 Competitive Analysis 3, version 2: exhaustion competitors

Checklist: `docs/research-checklist-ca3-exhaustion.md`. Reader version 2: `docs/competitive-analysis-3-reader-v2.md` (version 1 kept).

| File | What it is | Link | Used for |
|---|---|---|---|
| `competitors-4/save_pages_exhaustion.py`, `save_pages_exhaustion_2.py` → `save_log_exhaustion.json` | Saved pages, robots.txt respected. NADSA (nadsa.org) is disallowed by robots.txt and was not saved; one ACL fact sheet URL returned 404 | — | New rows |
| `competitors-4/va-caregiver/*` | VA caregiver program pages (caregiver.va.gov home and support services, VA respite care, Program of Comprehensive Assistance for Family Caregivers) | https://www.caregiver.va.gov/ ; https://www.va.gov/family-and-caregiver-benefits/health-and-disability/comprehensive-assistance-for-family-caregivers/ | VA row |
| `competitors-4/hospice-respite/*` | Medicare hospice coverage page (inpatient respite, 5% copay) | https://www.medicare.gov/coverage/hospice-care | Respite row |
| `competitors-4/adult-day/*` | Alzheimer's Association adult day centers page (hours, activities, sliding scales, Medicaid) | https://www.alz.org/help-support/caregiving/care-options/adult-day-centers | Respite row |
| `competitors-4/respite-arch/*` | ARCH National Respite Network home page | https://archrespite.org/ | Respite row |
| `competitive-analysis-3/grid/build_grid_v3.py` → `grid-v3.json`, `business-v2.json` | Grid version 3 and business table version 2: version 2 rows unchanged plus the 2 new rows. New source types check relief reader codes and relief barrier counts. Grid 117 cells, 214 sources; business 45 cells, 82 sources; 0 problems | — | Reader version 2, Figma |

## 2026-11-05 Audit and corrections

| File | What it is | Used for |
|---|---|---|
| `audit-2026-11-05/` | 6-agent audit: blind re-reads (`build_samples.py`, `recode-codes.json`, `relevance-check.json`, `audience-check.json`, `compare.py` → `compare-results.json`) and reports `audit-4-market.md`, `audit-5-audience.md`, `audit-6-competitive.md` | `docs/reports/audit-2026-11-05-results.md` |
| `market-analysis-3/segments-11-12/count_results.py` (grouping rule corrected 2026-11-05) → `results.json`, `results-by-audience.json` | "Family won't help" recount (93 → 83) | Market and audience corrected sections |
| `competitive-analysis-3/grid/build_grid_v4.py` → `grid-v4.json`, `business-v3.json` | Grid version 4 and business table version 3 with the audit fixes; 0 problems (grid 117 cells and 217 sources; business 45 cells and 85 sources) | `docs/competitive-analysis-3-reader-v2.md`, Figma 2645:12741 |
| `competitors-4/adult-day/`, `va-caregiver/`, `hospice-respite/` | Quotes added: adult day counseling and behavior help, VA 70% disability rating, VA respite copay, hospice "terminally ill" | Corrected respite and VA cells |

## VA row fix, Competitive Analysis 3 version 3 (2026-11-05)

- `competitive-analysis-3/grid/build_grid_v5.py` → `grid-v5.json`, `business-v4.json`: four VA cells fixed; older versions' files are not rewritten (0 problems).
- `competitive-analysis-3/va-check/va-cells-change-2026-11-05.md`: what changed and why, with the post ids.
- `competitive-analysis-3/va-check/research-checklist-va-2026-11-05.md`: checklist for a 187-post VA reading, not run (kept for the feature analysis).
- `competitive-analysis-3/va-check/va_ids.json`, `va_archive_ids.json`: the post lists.
- Repo copy: `docs/competitive-analysis-3-reader-v3.md` (version 2 marked superseded).

## GitHub practices (2026-11-06, for the wrap-up skill audit)
Saved from the GitHub Docs article API (`https://docs.github.com/api/article/body?pathname=...`) on 2026-11-06. Audit: `docs/reports/wrap-up-github-audit-2026-11-06.md`.
- `github-practices/github-flow.md`: GitHub flow (branch, commit, PR, merge, delete branch). https://docs.github.com/en/get-started/using-github/github-flow
- `github-practices/helping-others-review.md`: small PRs, context, self-review, security review.
- `github-practices/repo-best-practices.md`: minimum security features; protected branches.
- `github-practices/merge-methods.md`, `protected-branches.md`, `rulesets.md`, `auto-delete-branches.md`, `deleting-branches.md`, `status-checks.md`, `reviewing-changes.md`, `ignoring-files.md`, `about-ci.md`.
- `github-practices/push-protection.md`, `secret-scanning.md`, `dependabot-alerts.md`, `github-plans.md`: what each plan and repo type includes.
- `github-practices/git-book-contributing.html`: Pro Git 2nd ed., "Contributing to a Project" (Commit Guidelines). https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project

## INVEST and skill writing (2026-11-06, for the full invest-task-scoping skill)
- `invest/agile-alliance-invest.md`: Agile Alliance glossary entry on INVEST (extract). https://agilealliance.org/glossary/invest/
- `invest/bill-wake-invest.md`: Bill Wake's 2003 INVEST article (extract). https://xp123.com/invest-in-good-stories-and-smart-tasks/
- `invest/cucumber-gherkin-reference-text.txt`: Cucumber Gherkin reference, text of the whole page (Given/When/Then meanings). https://cucumber.io/docs/gherkin/reference/
- `invest/anthropic-skill-best-practices-text.txt`: Anthropic, Skill authoring best practices, text of the whole page. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
