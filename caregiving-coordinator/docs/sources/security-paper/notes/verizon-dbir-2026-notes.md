# Notes: Verizon 2026 Data Breach Investigations Report

- **Source:** Verizon. (2026). *2026 data breach investigations report*. Verizon Business. https://www.verizon.com/business/resources/reports/dbir/ (Verizon asks readers to cite it as "Verizon 2026 Data Breach Investigations Report" and to link to verizon.com/dbir, p. 9.)
- **Label for the paper:** company research (tier 3 in the source list).
- **Local copy:** the owner filled in Verizon's form and saved `2026-dbir-data-breach-investigations-report.pdf` (121 pages, created May 19, 2026). It sits in `caregiving-coordinator/docs/sources/security-paper/verizon-dbir-2026/` on the owner's computer only. It is **not in the public repository** (that folder's `.gitignore` excludes it), because Verizon asks people to link to the report and not share the PDF.
- **Page numbers below are the report's page numbers.** For this report the printed page number equals the PDF page number.
- **Read in full (2026-11-18), the sections in the cite plan:** pages 1 to 61 (introduction, how to use the report, key findings, results and analysis, and the incident patterns: Lost and Stolen Assets, System Intrusion, Social Engineering, Basic Web Application Attacks, Miscellaneous Errors, Privilege Misuse), pages 82 to 89 (the industry pages for Education, Financial, **Healthcare on pp. 86 to 87**, and Manufacturing), pages 97 to 98 (small and medium businesses) and pages 111 to 113 (methodology and the U.S. Secret Service appendix).
- **Not read, and not cited:** pages 62 to 81 (denial of service, the deep dives on privilege escalation and North Korean IT workers, and the industry introduction), pages 90 to 96 (public administration and retail), pages 99 to 110 (regions) and pages 114 to 121 (the other appendices). These are outside the cite plan `caregiving-coordinator/docs/security-paper/cite-plan-2026-11-18.md`.
- **Edition check:** it is the 19th edition (p. 5). It covers incidents from Nov 1, 2024 to Oct 31, 2025 (p. 9). Verizon's page lists it as the 2026 report.

## What the pages say (my words)

| Point | Page |
|---|---|
| The report looks at more than 31,000 incidents, including more than 22,000 confirmed data breaches in 145 countries. | p. 5 |
| Verizon's data comes from almost a hundred contributors and is normalized with the VERIS framework. A breach means confirmed disclosure of data to an unauthorized party. | pp. 6 to 7 |
| Exploiting vulnerabilities is now the most common way in (initial access) at 31%, up from 20%. Credential abuse fell to 13% from 22%, partly because pretexting was added as its own vector. Counting credential abuse at any point in a breach, it is still the top action at 39%. | pp. 10, 15, 16 |
| Only 26% of vulnerabilities on the CISA Known Exploited Vulnerabilities list were fully fixed in 2025, down from 38%. The median time to fix was 43 days, up from 32. About 35% were still open at day 28. | pp. 10, 17, 18 |
| Verizon says picking which vulnerabilities to patch first is the key strategy, because only 30% to 40% of known exploited ones get fixed in the first week even at best. | p. 18 |
| Ransomware was in 48% of breaches. 69% of victims did not pay, and the median ransom paid was USD 139,875. The reported share of victims who paid, per ransomware group, was about 9%. | pp. 11, 29, 42 to 43 |
| Breaches with a third party involved reached 48%, up from 30%. Many third-party cloud incidents trace to missing multi-factor authentication, poor credential rotation or too many privileges. Only 23% of third parties fully fixed missing or weak MFA on cloud accounts. | pp. 11, 20 to 22 |
| The "human element" was in 62% of breaches. 88% of threat actors were external and 12% internal. Financial gain was the main motive. | pp. 20, 23 to 24 |
| Stolen credentials were used in 36% of breaches and exploiting vulnerabilities in 32%. Hacking was in 64% of breaches and malware in 63%. | p. 29 |
| Credentials were in 28% of breaches. Personal data was taken in 23%, and sensitive personal information such as Social Security numbers in 1.7%. | p. 36 |
| System Intrusion is the top pattern, 60% of breaches. Ransomware is in 77% of System Intrusion breaches, with stolen credentials and exploited vulnerabilities each the way in for 39%. Attackers increasingly use legitimate remote management software. | p. 40 to 41 |
| 50% of ransomware victims that had an infostealer or credential leak had one within 95 days before the attack. Admin accounts sold by access brokers at about USD 1,300 against about USD 700 for a regular account. | pp. 44, 46 |
| Social Engineering is 16% of breaches. Email is still the main way in, but 41% of social breaches involve other vectors. In simulations the median click rate was about 2% for phone-centric attacks and 1.4% for email (a 40% higher rate). Pretexting means a live conversation; Verizon says training must differ from email phishing training. | pp. 48 to 50 |
| Basic Web Application Attacks: driven by stolen credentials and unpatched vulnerabilities. Credentials were taken in 52% of these breaches. | pp. 54 to 55 |
| Miscellaneous Errors (about 9% of breaches): Misdelivery, Misconfiguration and Loss were the most common. Verizon says developers, system administrators and end users top the list of people who cause them, and suggests limiting who has access to the most critical data. | pp. 56 to 57 |
| Privilege Misuse (just under 4% of breaches): the main motive was convenience (60%), for example emailing company data to a personal account. Verizon suggests an activity review when someone with sensitive access leaves. | pp. 58 to 60 |
| Shadow AI: 67% of users reach AI tools with non-corporate accounts, and 45% of employees are now regular AI users on corporate devices. | p. 60 |
| **Healthcare:** 1,492 incidents and 1,438 confirmed breaches. System Intrusion, Miscellaneous Errors and Social Engineering are 81% of breaches. Miscellaneous Errors has been in the top three every year in the report's tracking, which Verizon says goes back to the 2014 report. Errors were Misdelivery, Loss (often unencrypted devices) and Misconfiguration. 99% of the actors had a financial motive. Third parties were involved in 32%. | pp. 86 to 87 |
| Verizon says security fundamentals "must be baked into the contracts" with business associates and suppliers. | p. 87 |
| **Small and medium businesses** (fewer than 1,000 employees): 7,256 incidents. About 96% of the ransomware victims whose size is known were small or medium businesses. Third parties were involved in 55%. | pp. 97 to 98 |
| Verizon's closing advice: know your assets and third parties, patch with discipline, practice response plans, and support secure behavior. | p. 5 |
| Methods: three data collection routes, non-incident data analyzed separately, confidence intervals shown in charts. Verizon says it does not claim the findings represent all breaches. Its sample is a convenience sample with sampling bias, and ransomware may be overrepresented. | pp. 111 to 112 |

## Terms of use for citing (important for the paper)
- p. 9: Verizon permits statistics and figures if the source is cited as "Verizon 2026 Data Breach Investigations Report" and the content is not modified. Exact quotes are allowed. **Paraphrasing "requires review"** by Verizon. The course asks for your own words. Use exact numbers with the citation, keep any wording a plain description of a number, and ask the owner whether to contact Verizon.
- p. 9: Verizon asks readers to share the link to verizon.com/dbir, not the PDF. It forbids making pie charts from the report's data.

## Possible use in the paper
- Topic 3 (background): how breaches start (vulnerabilities, stolen credentials), ransomware, third parties and the human element.
- Topic 6 (what teams do): vulnerability management and its limits (pp. 15 to 20), incident patterns, and the offboarding review for insiders (p. 60).
- Topic 8: healthcare errors (misdelivery, misconfiguration, loss), third-party risk, and small-organization ransomware. These support general points only. The report does not mention caregiver or consumer health apps, and nothing here says the proposed coordinator is secure or compliant.

## Limits
- It is a convenience sample of breaches that reached investigators and contributors (pp. 111 to 112), so rates are not population rates.
- Verizon's own data skews to organizations; it says individuals not tied to an organization are excluded (p. 112).
- Parts of the report were not read (see above), so the paper must not describe the whole report.
- AI sections beyond one line are not used because the proposed coordinator uses no AI service (task T3.2.3).
