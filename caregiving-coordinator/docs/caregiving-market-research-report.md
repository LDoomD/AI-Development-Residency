# Caregiving Coordinator: Market Research Report

**Project:** caregiving-coordinator (Tech Fleet AI Development Residency, Premium track)
**Prepared:** 2026-10-29
**Status:** Draft for review. Not yet placed into the FigJam board.
**Builds on:** `docs/market-research-segments.md` (segment survey, 2026-10-28) and `docs/figjam-market-research-review.md`.

---

## 1. Summary

1. **The market is real and growing, but the numbers are soft.** Digital caregiver support and coordination platforms are sized at $4.80B in 2026 growing to $16.90B by 2034 (16.9% CAGR) by one firm. Other firms size neighbouring segments between $0.64B and $2.8B. Estimates for the same segment differ by 2 to 10 times depending on how each firm draws the boundary.
2. **No segment is a clean match for the product.** Coordination, medication management, visit documentation, benefits navigation and credential sharing are each served by a different category of company. The product sits across several of them.
3. **The closest existing products are older and narrow.** CareZone (medication list, acquired for its technology by Walmart in 2020), CaringBridge (updates and support for a patient's circle, nonprofit) and Lotsa Helping Hands (free task and meal calendar) each cover one slice. Caring Village covers shared calendar, to-dos, messaging and documents. None of the sources I found describe AI-generated notes from a recorded doctor visit as a feature of these products. That is a finding from limited search, not proof that nobody offers it.
4. **The strongest differentiator is also the most regulated.** Recording a doctor visit triggers state recording-consent laws (about a dozen "all-party consent" states). Storing visit content and medication lists puts the product under the FTC Health Breach Notification Rule if it is not covered by HIPAA.
5. **The shared credential vault is the highest-risk feature.** It holds pharmacy and insurance logins. It should be scoped, delayed or replaced by guidance to use an existing password manager.

**Recommended direction (analyst opinion, for discussion):** lead with visit capture and structured notes, add a shared medication list that the notes update, and treat siblings' shared access as the coordination layer. Defer the credential vault.

---

## 2. Method and how far to trust each number

- **Market sizes** come from public summaries of paid research reports (Strategy MRC, Fact.MR, MarketIntelo, Verified Market Research, Fortune Business Insights, Research Nester, Coherent Market Insights, Dataintelo, Mordor Intelligence and others). I read search summaries, not the full reports. These firms use different definitions, so figures for "the same" market disagree.
- **Competitor facts** come from company pages and news. Where only one source supports a claim, I say so.
- **Legal facts** come from law-firm and vendor summaries. They are not the statutes or the Federal Register text. Check the primary source before relying on any of them.
- **Labels used below:** *Sourced* means a source states it. *Analyst judgment* means my reasoning, with no source. *Not verified* means I found conflicting or thin evidence.

---

## 3. Market segments

Ten segments were surveyed across the whole caregiving landscape, not only apps like this one.

| # | Segment | 2026 size (as sourced) | Projection | Source |
|---|---|---|---|---|
| 1 | Digital caregiver support / coordination platforms | $4.80B | $16.90B by 2034, 16.9% CAGR | StrategyMRC |
| 1a | Narrower: digital caregiver platforms (matching and scheduling) | $640.0M | $3,050.0M by 2036, 16.9% CAGR | Fact.MR |
| 1b | AI-powered caregiver support platforms | $2.8B (2025) | about $15.6B by 2034, 19.5% CAGR | MarketIntelo |
| 2 | Medication management software | $9.11B | $23.29B by 2034, 12.45% CAGR | Fortune Business Insights |
| 2a | Medication management apps | $3.5B (2025) | not stated | Verified Market Research |
| 2b | Alternate software estimate | $6B | $26.3B by 2035, 17.9% CAGR | Research Nester |
| 3 | Respite care services (broad) | $25.20B | $49.3B by 2034, 8.17% CAGR | MarketResearch.com / OG Analysis |
| 3a | Respite care for the elderly (narrow) | $374.1M | $562.5M by 2033, 6.0% CAGR | Coherent Market Insights |
| 4 | Senior care marketplaces / advisory | $23.6B (2025) | $46.4B by 2034, 7.8% CAGR | Dataintelo |
| 5 | Home care agencies and staffing marketplaces | about $173.6B (US providers) | +4.1% year over year | IBISWorld via AveeCare |
| 5a | Global home care services | $658.20B | not stated | Coherent Market Insights |
| 6 | Remote patient monitoring / wearables | $30.9B to $67.3B depending on firm | not stated | GMI Insights, Research and Markets |
| 6a | US RPM wearables | $8.58B | not stated | MedQuantivo |
| 7 | Caregiver mental health / burnout support | no dedicated figure found | n/a | n/a |
| 8 | Telehealth / virtual care | $118.8B to $219.31B | $1,272.81B by 2034, 24.60% CAGR (one firm) | MarketsandMarkets |
| 8a | Virtual care (narrow) | $13.9B | not stated | Persistence Market Research |
| 9 | Insurance / benefits navigation | $12.25B | $17.61B by 2031, 7.52% CAGR | Mordor Intelligence |
| 9a | Medicare AI navigation sub-segment | $1.2B (2025) | about $8.1B by 2034, 23.0% CAGR | via search summary |
| 10 | Adult day care services and finders | $9.33B (2025) | $15.0B by 2035, 4.9% CAGR | WiseGuy Reports |

### Segment notes

**1. Digital caregiver support / coordination platforms.** Closest segment. A cited National Alliance for Caregiving figure says 68% of family caregivers aged 35 to 54 actively seek technology for care management, up from 41% in 2020. The same source set projects the family-caregiver end-user revenue segment at 26.4% CAGR through 2034. I reached the 68% figure through a Grand View Research summary, not the original report.

**2. Medication management.** The widest spread of any segment. A consumer app ($3.5B), software ($9.11B), and a full clinical and pharmacy system ($8.78B per Research and Markets) are different things. Only the consumer-app definition resembles this product's medication list.

**3 and 10. Respite care and adult day care.** These are services delivered by people. They are context for who the user is (a family caregiver under strain) but not competitors.

**4 and 5. Marketplaces and home care agencies.** A Place for Mom reports 500,000+ family reviews, 20M+ family visits a year, and a network of 15,000+ senior living communities and home care agencies. Care.com reported FY2025 revenue of $347M (company-reported, found in a search summary). These companies help families *find* care. They do not coordinate day-to-day care between siblings.

**6. Remote patient monitoring.** The segment is large but the buyer is usually a health system or insurer. The device and data integrations are a different product. Treat it as a later integration, not a competitor.

**7. Caregiver mental health.** Roughly 40% of family caregivers report burnout symptoms and 70% report at least one physical health issue linked to caregiving (WorldMetrics). Named tools: Sanvello, Talkspace, Calm, Insight Timer, ianacare. No firm tracks this as its own market. That is a finding.

**8. Telehealth.** Adults 65 and older have a 43.3% telehealth utilization rate. *Not verified:* this came through as an unattributed figure in a search summary. Do not use it downstream until a source is found.

**9. Insurance and benefits navigation.** Chapter is the named leader in Medicare navigation, with a reported $3B valuation after a $100M Series E in April 2026 (search summary, company funding data). KFF notes Medicare care-management billing codes expanded on January 1, 2026 to cover more caregiver-support personnel and visit types.

### How the segments fit the product (analyst judgment)

| Segment | Role for this product | Fit |
|---|---|---|
| 1 Coordination platforms | Home market and direct comparison set | High |
| 2 Medication management | Secondary feature set and indirect competitors | High |
| 9 Insurance / benefits navigation | Pharmacy and insurance portal pain is real, but navigation as a service is a different business | Medium |
| 7 Caregiver mental health | Adjacent need, not a market with its own data | Low to medium |
| 8 Telehealth | Context, and a source of recordings and visit summaries | Low to medium |
| 4 and 5 Marketplaces, home care | Different job: finding care | Low |
| 6 RPM | Possible future integration | Low |
| 3 and 10 Respite, adult day care | Services, not software | Low |

---

## 4. Competitor landscape

Only facts I could source are listed. Pricing and feature gaps are marked.

### CareZone
- In June 2020 Walmart bought CareZone's technology platform, patents and key intellectual property, and took on 25 to 30 product and engineering staff. CareZone's CEO said the apps had about 3.5 million members. Reported price was about $200M per CNBC's health technology reporter, undisclosed by Walmart.
- CareZone kept its pharmacy business and remained a separate company (2020 reporting). Walmart did not buy the pharmacy, which sorted medications into pill packs and delivered by mail.
- *Not verified:* a single aggregator (Dealroom) says the pharmacy and app were later wound down. It conflicts with the 2020 reporting. I found no official notice or date.
- **Why it matters here:** CareZone proves a medication-list product can reach millions of users and still end in an asset sale. I have not found *why* it ended. This is the open question that matters most for the project.

### CaringBridge
- A 501(c)(3) nonprofit since 2002, founded to avoid depending on advertisers. Over 90% of funding comes from people who have used it. Says it never sells personal data and runs no outside advertising.
- Authors choose among three privacy options per site.
- *Not verified:* HIPAA status. No authoritative source found. A press-release-style page claims HIPAA and GDPR compliant storage and looks unreliable. CaringBridge is a consumer platform, so HIPAA may not apply directly. That is my inference.
- **Role:** broadcasting health updates to a circle of friends and family. It is not a medication or visit-note tool.

### Lotsa Helping Hands
- Free for coordinators and team members per its own FAQ.
- Help Calendar for meals, rides and visits. A Vital Information feature keeps key information in one place. Coordinators invite others to help manage.
- *Not verified:* owner and business model. No result named a parent company.
- **Role:** organizing volunteer help from a community. Different job from sibling coordination of a parent's care.

### Caring Village
- Free tier: one village, up to two members. Paid plans start from $14.99 a month in a 2025 comparison.
- Features: shared calendar, to-dos, messaging, documents. Calendar sync is Google Calendar only. Data is described as encrypted with role-based access.
- *Conflicting:* plan member limits differ between the FAQ (5 and 25) and the pricing page (50 for the top tier). Medication dose alerts are listed as present in one place and absent in another.
- **Source caution:** most comparison content is on Caring Village's own blog, which ranks itself first.
- **Role:** the closest feature overlap with a "one place for the family" product.

### Carely, ianacare, Cozi
- **Carely:** described as an app to coordinate and plan care and share memories. No pricing or feature detail found.
- **ianacare:** founded 2017, based in Newton, Massachusetts, offers tools and resources for home-based care, with peer support and coaching named in one source. No app pricing found.
- **Cozi:** no results found in this pass.

### Other named players
Sanvello, Talkspace, Calm and Insight Timer (caregiver mental health), A Place for Mom, Caring.com and Care.com (marketplaces), Chapter (Medicare navigation). Not analyzed further.

### What I could not establish
- Whether any competitor above generates structured notes from a recorded visit. I did not find one in these searches. A direct check of each product is needed before claiming this is unmet.
- Current pricing for Carely, ianacare and Cozi.
- Why CareZone's consumer app ended.
- How any of these companies handled HIPAA-adjacent obligations in practice.

---

## 5. Feature-by-feature view of the problem

These map to the founder's lived experience caring for a parent after surgery. The "what exists" column reflects only what I found.

| Need from the founder's account | What exists (sourced) | Gap (analyst judgment) |
|---|---|---|
| Clear notes from recorded doctor visits: what was said, suggested, warned | No competitor found that does this | Likely the main differentiator. Needs verification. |
| One current medication list, with changes and stops | Medication apps ($3.5B segment). Caring Village's dose alerts are disputed. | A list built *from* visit notes, shared by siblings, is the combination. |
| Shared place for three siblings to coordinate | Caring Village, Lotsa Helping Hands | Exists. Not the wedge. |
| Shared pharmacy and insurance logins | General password managers. No caregiving product found. | Real need, high liability. See section 7. |
| Notes readable by siblings, or as an audio overview | Not found | Depends on the note feature working first. |

---

## 6. Regulation and consent

This is not legal advice. It lists what to check with a lawyer or a compliance professional.

### HIPAA and the FTC Health Breach Notification Rule
- HIPAA covers "covered entities" and their "business associates." Many consumer apps that handle health data are outside it, especially apps a person downloads on their own with no link to a provider.
- Apps in that position generally fall under the FTC Health Breach Notification Rule. The FTC's 2021 policy statement confirmed health apps must comply. The 2024 amendments made the application to health apps explicit.
- An app can be within the rule if it draws data from several sources, such as user input combined with APIs.
- A covered vendor must notify affected people without unreasonable delay and no later than 60 calendar days after discovering a breach. A breach affecting 500 or more people also triggers notice to the FTC.
- Gray area: connecting to a provider's or pharmacy's systems through APIs can change the HIPAA analysis.
- *Check before relying:* the final rule text at 16 CFR Part 318, and whether the amendments are unchanged today.

### Recording a doctor visit
- About a dozen US states require every person recorded to consent. Commonly listed: California, Connecticut, Delaware, Florida, Illinois, Maryland, Massachusetts, Montana, New Hampshire, Oregon, Pennsylvania and Washington. Sources disagree on the list, and Oregon and Hawaii are described as nuanced.
- A caregiver or relative in the room counts as a recorded person. In an all-party state, consent may be needed from everyone present, including interpreters and other clinicians.
- One source cites $5,000 per violation under California's Invasion of Privacy Act. This is from a secondary source.
- Only a small number of states require providers to disclose ambient AI tools. A California case argues that general notices and implied consent may not be enough. It is early and untested.
- **Product implication (analyst judgment):** the app needs a consent step before each recording that works for the doctor's office, not only for the user. Expect some clinics to refuse. The feature may need an "I'm taking notes myself, then dictating a summary afterward" mode as a fallback.

---

## 7. Risks

| Risk | Why it matters | Mitigation to consider |
|---|---|---|
| Recording-consent law | Fines and refused visits in all-party states | Per-visit consent prompt, state-aware guidance, post-visit dictation mode |
| FTC breach rule and state privacy law | Health data held outside HIPAA still carries breach duties | Encrypt at rest, minimise data, written breach plan |
| Shared credential vault | A breach exposes pharmacy and insurance logins for every family | Defer. Recommend an existing password manager's family sharing instead. |
| AI note errors | A wrong dose or instruction in a summary can harm someone | Show the transcript next to every summary, label notes as AI-generated, require human confirmation for medication changes |
| Market definitions | Sizes vary 2 to 10 times | Quote ranges, never one number |
| Prior products ending | CareZone ended in an asset sale and the reason is unknown | Find out why before claiming demand |
| Login-gated product vs. search visibility | Week 8 SEO work needs a public surface | Plan a thin public landing page (see `PLANNING-NOTES.md`) |

---

## 8. Open questions

1. Why did CareZone's consumer app end, and what does that say about willingness to pay?
2. Does any competitor offer AI visit notes? Check Caring Village, Carely and ianacare directly.
3. Who is the paying user: the adult child caregiver, a family plan, or an employer benefit? No evidence gathered yet.
4. Which states matter for launch, given the recording-consent split?
5. Does the project need HIPAA-grade handling anyway, to work with clinics later?
6. Which 10 (or fewer) segments go into the FigJam board?

---

## 9. Next steps

1. Review this report and mark which segments to carry forward.
2. Fill the FigJam "Possible Market Segments" and "Market Size" tables (ask before using the browser or Figma).
3. Run the competitor pass with the Prompt 2 structure from the template: channels, five direct and indirect competitors each, market size, CAGR, sources.
4. Check each competitor's own site for visit-note features and pricing.
5. Rewrite Section 8 of the research paper for this project (author's own writing).

---

## 10. Sources

**Market size**
- StrategyMRC, digital caregiver support platforms: https://www.strategymrc.com/report/digital-caregiver-support-platforms-market
- Fact.MR, digital caregiver platforms: https://www.factmr.com/report/digital-caregiver-platforms-market
- MarketIntelo, AI-powered caregiver support: https://marketintelo.com/report/ai-powered-caregiver-support-platform-market
- Verified Market Research, medication management app: https://www.verifiedmarketreports.com/product/medication-management-app-market/
- Fortune Business Insights, medication management software: https://www.fortunebusinessinsights.com/medication-management-software-market-115703
- Research Nester, medication management system: https://www.researchnester.com/reports/medication-management-system-market/6718
- Research and Markets, medication management system: https://www.researchandmarkets.com/reports/5752020/medication-management-system-market-report
- MarketResearch.com / OG Analysis, respite care: https://www.marketresearch.com/OG-Analysis-v3922/Respite-Care-Elderly-Outlook-Share-44742043/
- Coherent Market Insights, respite care for the elderly: https://www.coherentmarketinsights.com/industry-reports/respite-care-for-the-elderly-market
- Dataintelo, caregiver marketplace: https://dataintelo.com/report/caregiver-marketplace-market
- A Place for Mom (Yahoo Finance): https://finance.yahoo.com/healthcare/articles/place-mom-reaches-500-000-130000660.html
- AveeCare, home care statistics (IBISWorld): https://www.aveecare.com/resources/home-care-industry-statistics-2026
- Coherent Market Insights, home care service: https://www.coherentmarketinsights.com/industry-reports/home-care-service-market
- GMI Insights, RPM devices: https://www.gminsights.com/industry-analysis/remote-patient-monitoring-devices-market
- Research and Markets, RPM: https://www.researchandmarkets.com/reports/6226093/remote-patient-monitoring-market-report
- MedQuantivo, US RPM wearables: https://medquantivo.com/wearable/us-remote-patient-monitoring-wearable-devices-market/
- Grand View Research, RPM devices: https://www.grandviewresearch.com/industry-analysis/remote-patient-monitoring-devices-market
- WorldMetrics, caregiver burnout: https://worldmetrics.org/caregiver-burnout-statistics/
- Caring Senior Service, caregiver apps: https://caringseniorservice.com/blog/most-useful-caregiver-apps/
- MarketsandMarkets, telehealth: https://www.marketsandmarkets.com/Market-Reports/telehealth-market-201868927.html
- Persistence Market Research, virtual care: https://www.persistencemarketresearch.com/market-research/virtual-care-market.asp
- Mordor Intelligence, healthcare navigation: https://www.mordorintelligence.com/industry-reports/healthcare-navigation-platform-market
- KFF, Medicare Advantage 2026: https://www.kff.org/medicare/medicare-advantage-2026-spotlight-a-first-look-at-plan-premiums-and-benefits/
- WiseGuy Reports, adult day care: https://www.wiseguyreports.com/reports/adult-day-care-service-market

**Competitors**
- CNBC, Walmart buys CareZone technology: https://www.cnbc.com/2020/06/15/walmart-buys-tech-from-carezone-to-help-people-manage-prescriptions.html
- Healthcare Dive, Walmart and CareZone: https://healthcaredive.com/news/walmart-buys-medication-management-tech-from-startup-carezone/579875
- Fierce Healthcare, Walmart and CareZone: https://www.fiercehealthcare.com/tech/walmart-buys-medication-management-technology-from-startup-carezone
- Dealroom, CareZone (single source for wind-down claim): https://dealroom.co/companies/carezone/
- CaringBridge, how it works: https://caringbridge.org/how-it-works
- CaringBridge, private and protected spaces: https://www.caringbridge.org/resources/private-and-protected-spaces
- Lotsa Helping Hands, how it works: https://lotsahelpinghands.com/?p=81
- Caring Village, pricing: https://caringvillage.com/pricing/
- Caring Village, FAQ: https://caringvillage.com/faq/
- Caring Village, features: https://www.caringvillage.com/product/features/
- CB Insights, ianacare: https://www.cbinsights.com/company/ianacare/financials

**Regulation**
- Foley Hoag, FTC updated Health Breach Notification Rule: https://foleyhoag.com/news-and-insights/blogs/security-privacy-and-the-law/2024/april/ftc-s-updated-health-data-breach-rule-covers-apps-other-new-tech/
- Hunton, FTC guidance on the rule: https://www.hunton.com/privacy-and-cybersecurity-law-blog/2021/09/21/ftc-issues-guidance-clarifying-scope-of-its-health-breach-notification-rule-for-health-apps-and-connected-devices/
- Holland and Knight, FTC rules for health apps outside HIPAA: https://www.hklaw.com/en/insights/publications/2021/09/important-ftc-rules-for-health-apps-outside-of-hipaa
- McDermott, legal risks for AI scribes: https://www.mcdermottlaw.com/insights/all-about-ai-scribes-faqs-for-health-systems-and-providers/
- JD Supra, legal risks before recording with an AI scribe: https://www.jdsupra.com/legalnews/ready-set-press-pause-legal-risks-and-5352318/
- JUCM, states adopt varied AI scribe laws: https://www.jucm.com/states-adopt-varied-ai-scribe-laws/
