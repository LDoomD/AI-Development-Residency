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
