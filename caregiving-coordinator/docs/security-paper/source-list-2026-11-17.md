# Candidate sources for the Premium paper: Advanced Information Security (draft for owner approval, 2026-11-17)

**Status:** **Approved by the owner on 2026-11-18**, including the five sources added that day. Nothing in this list has been read in full yet. The reading method (me in batches in a fresh chat, or a many-agent workflow) is still to be chosen; the default is me in batches. For each source, a web search on 2026-11-17 confirmed that it exists and found its date or version. The full text is read, saved in `docs/sources/security-paper/` and logged in `docs/sources/INDEX.md` only after the owner approves the list.

**Rules for the paper (course page, requirement 3):** APA 7 citations with page numbers, a bibliography at the end, everything in my own words, no plagiarism. The Week 6 lecture notes (`Resources/Week_6/`) give direction only. They are never the evidence for a claim.

## Topic 1. Introduction to the subject

| Source | Publisher, date | Link | Used for |
|---|---|---|---|
| The Protection of Information in Computer Systems (Saltzer and Schroeder) | Proceedings of the IEEE, 1975 | Free copy to be fetched from the author's MIT page | The original design principles (least privilege, fail-safe defaults). Pages to be confirmed when read. |
| Cybersecurity Framework 2.0 (CSWP 29) | NIST, Feb 26, 2024 | https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf | Standard definitions of managing security risk |

## Topic 2. Why it matters to a career

| Source | Publisher, date | Link | Used for |
|---|---|---|---|
| Information Security Analysts, Occupational Outlook Handbook | U.S. Bureau of Labor Statistics, 2024 to 2034 projections | https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm | Job growth, pay and size of the field. Search summary says 29% growth and a $124,910 median wage. I confirm the numbers on the page itself. |
| 2025 ISC2 Cybersecurity Workforce Study | ISC2, Dec 2025 | https://www.isc2.org/insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study | Which skills the field says it needs |
| Workforce Framework for Cybersecurity (NICE), SP 800-181 Rev. 1 | NIST, Nov 2020 | https://csrc.nist.gov/pubs/sp/800/181/r1/final | Work roles and skills in the field |
| The owner's own career reasons | The owner's saved background | Saved files | Drafted from saved files and shown to the owner before saving |

## Topic 3. Background about the specialization

| Source | Publisher, date | Link | Used for |
|---|---|---|---|
| OWASP Top 10:2025 | OWASP Foundation, Nov 2025 announcement | https://owasp.org/Top10/2025/ | The current list of top web risks. Sources disagree on the final release month, so I take the date from OWASP's own page. |
| OWASP project history | OWASP Foundation | owasp.org about pages | Origin of OWASP. The lecture says 2001. I verify it. |
| IBM Cost of a Data Breach Report 2026 | IBM with Ponemon Institute, Jul 2026 | To be fetched from IBM | Cost of breaches, with healthcare figures. Only news summaries were seen so far, so the IBM report itself must be read. |
| 2026 Data Breach Investigations Report (DBIR) | Verizon, May 19, 2026 | To be fetched from Verizon | How breaches start. Only news summaries were seen so far. |

## Topic 4. How it works when building products

| Source | Publisher, date | Link | Used for |
|---|---|---|---|
| Secure Software Development Framework (SSDF) v1.1, SP 800-218 | NIST, Feb 2022 (final) | https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-218.pdf | Security practices across the build. Version 1.2 (SP 800-218 Rev. 1) was only a draft on Dec 17, 2025, so I cite 1.1 and say so. |
| Secure by Design: Shifting the Balance of Cybersecurity Risk | CISA and partners, Oct 2023 | https://cisa.gov/resources-tools/resources/secure-by-design-and-default | Building security in from design |
| OWASP Application Security Verification Standard (ASVS) 5.0.0 | OWASP Foundation, May 2025 | https://owasp.org/projects/asvs | Requirements a secure app must meet |
| OWASP Software Assurance Maturity Model (SAMM) v2 | OWASP, Jan 2020 | https://owaspsamm.org/model/ | How teams organize security work |

## Topic 5. What it includes

| Source | Publisher, date | Link | Used for |
|---|---|---|---|
| OWASP Top 10:2025 | OWASP Foundation | https://owasp.org/Top10/2025/ | The main risk categories |
| OWASP Cheat Sheet Series | OWASP Foundation | https://cheatsheetseries.owasp.org/ and https://owasp.org/www-project-cheat-sheet-series/ | Defenses by topic. The OWASP page lists 121 cheat sheets. |
| Cybersecurity Framework 2.0 | NIST, Feb 2024 | https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf | The functions of a security program |

## Topic 6. What teams do

| Source | Publisher, date | Link | Used for |
|---|---|---|---|
| Threat Modeling Manifesto | Threat modeling practitioners, 2020 | https://threatmodelingmanifesto.org/ | The four questions of threat modeling |
| Threat Modeling Cheat Sheet | OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html | How teams run a threat model |
| Technical Guide to Information Security Testing and Assessment, SP 800-115 | NIST, 2008 | https://nvlpubs.nist.gov/nistpubs/legacy/SP/nistspecialpublication800-115.pdf | How security tests are planned and run. It is old, so I say so. |
| OWASP Web Security Testing Guide (WSTG) v4.2 | OWASP, Dec 3, 2020 (stable). v5.0 is still in development. | https://owasp.org/wstg | Test methods for web apps |

## Topic 7. Tools and skills

| Source | Publisher, date | Link | Used for |
|---|---|---|---|
| OWASP Cheat Sheet Series | OWASP | https://cheatsheetseries.owasp.org/ | Skills a developer needs, by topic |
| NICE Framework | NIST | https://csrc.nist.gov/pubs/sp/800/181/r1/final | Skills by work role |
| Tool documentation (secret scanning, dependency checks, code scanners) | Each tool's own docs | To be chosen with the owner | What the pipeline checks do. Only official docs, no vendor blogs. |

## Topic 8. The proposed caregiving coordinator (a product idea, not built yet)

The course asks the paper to propose the vision for the product. The coordinator is a **hypothesis**, so this topic describes how the field would apply to it. It does not describe a finished product.

These are already saved in `docs/sources/` (2026-11-12 research, listed in `INDEX.md`). I reuse them and add the field sources above.

| Source | Publisher, date | Where saved | Used for |
|---|---|---|---|
| Row-level security | Supabase docs, updated Nov 3, 2026 | `docs/sources/` (Supabase section of `INDEX.md`) | Access rules on the database tables |
| Shared responsibility model | Supabase docs, updated Oct 6, 2026 | `17-supabase-shared-responsibility.html` | Who protects what |
| Health Breach Notification Rule, 16 CFR 318, 2024 final rule | FTC, May 30, 2024 | Files 38 and 39 in the laws folder | The 60-day breach notice (task T4.3.3) |
| Complying with the Health Breach Notification Rule | FTC, Jul 2024 | `04-ftc-complying-with-hbnr.md` | Plain guidance on the rule |
| Health apps and HIPAA | HHS | `02-hhs-health-apps.md` | Where the app likely sits. No conclusions. |
| The owner's approved files | `non-functional-epics-features-tasks-2026-11-15.md` (T4), `docs/risk-profile.md` | In the project | The app's own security tasks |

## Source quality rules (added 2026-11-17 at the owner's request)

The course page sets no number of sources. It only asks for APA citations with a bibliography. I cite only what I read and use, and every source must pass these rules.

| Tier | What counts | Official addresses I accept |
|---|---|---|
| 1. Standards, governments and official projects | Standards bodies, government agencies, and the projects' own sites | OWASP: owasp.org, cheatsheetseries.owasp.org, owaspsamm.org, asvs.owasp.org, genai.owasp.org, and the official github.com/OWASP organization. NIST: csrc.nist.gov, nvlpubs.nist.gov, nist.gov, nvd.nist.gov. CISA: cisa.gov. MITRE: cwe.mitre.org. FIRST: first.org. Also bls.gov, ftc.gov, hhs.gov, supabase.com/docs, vercel.com/docs, github.com/advisories, and (added 2026-11-18) docs.github.com, docs.npmjs.com and zaproxy.org (the OWASP ZAP project's own site). |
| 2. Peer-reviewed and professional bodies | Journals and professional groups | IEEE, ACM, ISC2 (isc2.org) |
| 3. Primary company reports | The company's own report or advisory, never news about it | verizon.com (Data Breach Investigations Report), ibm.com (Cost of a Data Breach), and for incidents only the researchers' own advisories (Socket, Aikido, Palo Alto Unit 42, UpGuard, Wiz). I label these "company research". |
| Leads only, never cited | News sites, blogs, Medium, Wikipedia, vendor marketing, forums, AI summaries, copies on other domains | Used only to find the primary source, then dropped |

Before citing an OWASP page I confirm the address is on an OWASP domain above. A page that merely copies OWASP content on another site is not accepted.

## Currency check, run 2026-11-17 on each project's own official page

The owner's rule: security changes fast, so the newest published material comes first. For each older-looking source, I opened the official page (not a news summary) to see whether something newer exists.

| Source | Newest published edition (official page) | Newer work in progress | What the paper does |
|---|---|---|---|
| OWASP Web Security Testing Guide | 4.2 (Dec 2020). Page says "Latest Version 4.2". | v5.0 is in development on GitHub (about 46% of its milestone done; draft notes list new multi-factor, JWT and clickjacking tests). It is not released. | Cite 4.2 as the stable edition. Read the draft 5.0 notes and say they are drafts. |
| NIST SP 800-115, security testing | Final, Sep 2008. No revision or draft listed on NIST's page. | None found | Cite it as the standing NIST testing guide and label it 2008. Pair it with newer sources below. |
| NIST SSDF, SP 800-218 | 1.1, Feb 2022 (final) | 1.2 (Rev. 1) initial public draft, Dec 17, 2025. No final version found. | Cite 1.1. Read the 1.2 draft and label it as a draft. |
| OWASP ASVS | 5.0.0 (May 2025). No 5.0.1 listed on the page. | Check the project's GitHub before final draft | Cite 5.0.0 |
| OWASP Top 10 | 2025 is "the most current released version" | None | Cite 2025 |
| OWASP SAMM | v2 (2020). The site shows 2026 activity (an Oct 14, 2026 post on AI and software development). | Check SAMM docs before final draft | Cite v2 and say it is still active |
| OWASP Cheat Sheet Series | Continuously updated (121 sheets on OWASP's page) | Live | Cite each sheet with the date I read it |

**Why some picks are older:** they are still the newest edition. The official pages say so. I should have shown that check in the first list instead of leaving it as search summaries.

## Added after the check: newer sources (all 2023 to 2026)

| Source | Publisher, date | Link | Used for |
|---|---|---|---|
| 2026 Data Breach Investigations Report | Verizon, May 19, 2026 | To be fetched from Verizon | Newest data on how attacks start. News coverage says exploiting software flaws overtook stolen logins as the top entry point. I confirm in the report. |
| Cost of a Data Breach Report 2026 | IBM with Ponemon, Jul 2026 | To be fetched from IBM | Newest breach cost data |
| 2025 CWE Top 25 Most Dangerous Software Weaknesses | MITRE with CISA, Dec 11, 2025 | https://cwe.mitre.org/top25/ | Newest ranked list of weaknesses |
| Known Exploited Vulnerabilities Catalog | CISA, live list | cisa.gov | Flaws attackers use right now. I record the date I read it. |
| SP 800-63-4, Digital Identity Guidelines | NIST, Jul 2025 (final) | https://csrc.nist.gov/pubs/sp/800/63/4/final | Current rules for logins, passkeys and identity proofing |
| SP 800-61 Rev. 3, Incident Response | NIST, Apr 3, 2025 (final) | https://csrc.nist.gov/pubs/sp/800/61/r3/final | Current incident response guidance, ties to the breach plan (T4.3.3) |
| CVSS v4.0 | FIRST, Nov 2023 | first.org | Current way to rate how serious a finding is, for PenTest findings |
| OWASP Top 10 Proactive Controls 2024 | OWASP, Oct 2024 | https://owasp.org/www-project-proactive-controls/ | Current secure coding techniques |
| OWASP API Security Top 10 (2023 edition) | OWASP | owasp.org (official page not yet confirmed) | Risks for the app's server routes. I confirm it is the newest edition. |

## Newest items found on 2026-11-17 (Mar to Oct 2026), added after a second search

These come from searches for what was published or disclosed recently. Search results are only leads. I read the primary page of each before citing anything. Figures differ between news outlets, so I use only numbers from the primary advisory or report.

| Item | Date | Primary source to read | Why it matters for the paper and the app |
|---|---|---|---|
| CISA, Open Source Software: Security Principles and Practices | Jul 30, 2026 | cisa.gov (PDF, 31 pages) | Newest U.S. government guidance on using open source packages. It points to NIST's Secure Software Development Framework. Ties to T4.3.2. |
| CISA, 2026 Minimum Elements for a Software Bill of Materials | Jul 29, 2026 | CISA SBOM PDF | Newest rules for listing a product's components |
| NIST SP 1347, CSF 2.0 Informative References Quick-Start Guide | Aug 2026 (final) | csrc.nist.gov / nist.gov news | Newest NIST help for using the Cybersecurity Framework |
| NIST SP 800-100 Rev. 1 draft, Information Security Handbook | Draft, Oct 2026. Comments open to Dec 4, 2026. | csrc.nist.gov | Newest NIST draft for security leaders. Use only as a labeled draft. |
| NIST post-quantum cryptography transition report | Oct 27, 2026 | nist.gov news | Where encryption standards are heading. It applies to T4.2.4. Series number not confirmed. |
| 2026 wave of self-spreading npm package attacks (CanisterWorm in March, CanisterSprawl in April, a May attack on 323 packages, the TeamPCP and Mini Shai-Hulud attacks in May to June, IronWorm in June, ChainDrop in August) | Mar to Aug 2026 | The researchers' own advisories (Socket, Aikido, Palo Alto Unit 42) and the npm and GitHub notices | Stolen publish tokens and CI accounts were the common cause. Directly tied to T4.3.2 (locked versions, `npm audit`) and T4.2.2 (replace leaked keys). Package counts differ by source. |
| Next.js middleware authorization bypasses (CVE-2026-44573, CVE-2026-44574, CVE-2026-44575, CVE-2026-45109, others) | May to Jul 2026 | NVD entries and the GitHub advisories (GHSA IDs) | Shows why access checks must not rest on middleware alone. This applies only if the app uses Next.js, which I confirm from the Week 4 stack. One later CVE number from a single source is unconfirmed. |
| UpGuard study of more than 16,000 Supabase databases readable by anyone because row-level security was off | Sep 2026 | UpGuard's own report, the Wiz research on Moltbook, and Supabase's Security Advisor docs | Directly tied to the risk profile's rule that every table with health, money or consent data has row-level security. Reports say the cause was developer settings, not a Supabase flaw. I confirm in the primary report. |

**A claim I am not using:** some outlets say OWASP published a web "Top 10 2026". OWASP's own page says 2025 is "the most current released version", and the "2026" stories list the same categories as the 2025 list. One site argues there is no 2026 list. The OWASP LLM Top 10 for 2026 (Sep 2026) is real but concerns AI chat apps, so it is out of scope while MVP #1 uses no outside AI service.

## Added 2026-11-18 to fill gaps (Proposed, awaiting owner approval)

The owner asked whether the list is enough for the course page's requirements. Topics 1 and 5 had only a framework and no plain introduction, and Topic 7 had the row "tool documentation, to be chosen". A search on 2026-11-18, limited to official domains, found these. Only search summaries have been seen so far. I read each page before citing it.

| Source | Publisher, date | Link | Topic | Why added |
|---|---|---|---|---|
| SP 800-12 Rev. 1, An Introduction to Information Security | NIST, June 2017 (final) | https://csrc.nist.gov/pubs/sp/800/12/r1/final | 1, 5 | A plain introduction for newcomers, with eight core principles. It is from 2017, so I label it as the newest final edition once I confirm that on NIST's page. |
| About secret scanning; GitHub security features (secret scanning, Dependabot alerts, code scanning) | GitHub Docs | https://docs.github.com/code-security/secret-scanning/about-secret-scanning and https://docs.github.com/en/code-security/getting-started/github-security-features | 7 | Official docs for the tools that catch leaked keys, vulnerable packages and code flaws. The docs say code scanning and secret scanning are on by default for public repositories. |
| Auditing package dependencies for security vulnerabilities (npm audit) | npm Docs | https://docs.npmjs.com/auditing-package-dependencies-for-security-vulnerabilities/ | 7 | The official way to check a project's packages for known flaws. I confirm the current npm version when I read it. |
| ZAP (Zed Attack Proxy) | OWASP project; the search found release 2.17.0 of Dec 15, 2025 | https://www.zaproxy.org/ | 6, 7 | A free testing tool teams use. I confirm the newest release on the project's download page. |
| Certified in Cybersecurity exam outline | ISC2, effective Sep 1, 2026 | https://www.isc2.org/certifications/cc/cc-certification-exam-outline | 2, 7 | The skills an entry-level person is expected to have. I use the outline only, not the fees, which are ISC2's marketing. |

With these, Topic 7 has real tool and skill sources and the optional "tool docs" row above is resolved. Count after this addition: about 44 sources.

**Optional cuts if the owner wants a shorter list:** NIST post-quantum report (series number unconfirmed), NIST SP 800-100 Rev. 1 draft, NIST SP 1347.

## Rules for keeping the paper current

1. When I read each source, I re-check the project's official page and write the version and the date I checked in `INDEX.md`.
2. Live sources (CISA catalog, cheat sheets, CWE) are cited with an access date.
3. Draft or in-development versions are used only as labeled drafts. Final editions carry the claims.
4. I re-run the version check once more before the final draft, so nothing published during the work is missed.
5. For threats, I use 2025 to 2026 reports first and older reports only for background.

## Flags

1. **The lecture's "30 times more" cost claim has no confirmed source.** The lecture attributes it to a NIST study. A search found it only in blogs with no origin. Other numbers (3x, 15x) are attributed to NIST, and 4 to 5x to IBM, all from secondary pages. I will not use the 30x figure unless the NIST report itself supports it.
2. **Newer editions exist for two reports.** I use IBM 2026, not 2025, and Verizon 2026.
3. **Older sources are labeled old, and only used where they are still the newest official edition.** SP 800-115 is from 2008 and WSTG 4.2 is from 2020. See the currency check above.
4. **No Wikipedia, no vendor blogs** (Aikido, Semgrep and similar) as evidence. I used them only to find the primary source.
5. **No legal conclusions.** Law sources describe what the rule says. They never claim that the product idea would be safe or compliant.
