# Notes: Verizon 2026 Data Breach Investigations Report (PARTLY READ, finish in the next chat)

- **Source:** Verizon. (2026). *2026 data breach investigations report*. Verizon Business. https://www.verizon.com/business/resources/reports/dbir/ (Verizon asks readers to cite it as "Verizon 2026 Data Breach Investigations Report" and to link to verizon.com/dbir, p. 9.)
- **Label for the paper:** company research (tier 3 in the source list).
- **Local copy:** the owner filled in Verizon's form and saved `2026-dbir-data-breach-investigations-report.pdf` (121 pages, created May 19, 2026). It sits in `caregiving-coordinator/docs/sources/security-paper/verizon-dbir-2026/` on the owner's computer only. It is **not in the public repository** (the folder's `.gitignore` excludes it), because Verizon asks people to link to the report and not to share the PDF. The text copy is excluded too.
- **Page numbers below are the report's page numbers.** For this report the printed page number equals the PDF page number.
- **Read so far (2026-11-18):** pages 1 to 27 (cover, introduction, how to use the report, key topics and findings, and "Results and analysis" through the AI-assisted attacks discussion).
- **Still to read:** pages 28 to 121 (the rest of the results, the incident patterns including System Intrusion and Social Engineering, the deep dives, the industry pages including Healthcare on pp. 86 to 87, small and medium businesses, regions, and the appendices).
- **Edition check:** it is the 19th edition (p. 5). It covers incidents from Nov 1, 2024 to Oct 31, 2025 (p. 9). Verizon's page lists it as the 2026 report.

## What pages 1 to 27 say (my words)

| Point | Page |
|---|---|
| The report looks at more than 31,000 incidents, including more than 22,000 confirmed data breaches in 145 countries, the most the report has examined. | p. 5 |
| Verizon's data comes from almost a hundred contributors and is normalized with the VERIS framework. Verizon says it often lacks full detail on each case. | p. 6 |
| A breach means confirmed disclosure of data to an unauthorized party. An incident is any event that harms confidentiality, integrity or availability. | p. 7 |
| The report shows uncertainty with slanted bars and similar charts. Verizon says that if two bars' slanted areas overlap you cannot call one bigger. | p. 8 |
| Exploiting a vulnerability is now the most common way in (initial access) at 31%, up from 20%. Credential abuse fell to 13% from 22%, partly because pretexting was added as its own vector. | pp. 10, 15, 16 |
| Counting credential abuse at any point in a breach, it is still the top action at 39%. | p. 16 |
| Only 26% of vulnerabilities on the CISA Known Exploited Vulnerabilities list were fully fixed in 2025, down from 38%. The median time to fully fix was 43 days, up from 32. | pp. 10, 17 |
| About 35% of known exploited vulnerabilities were still open at day 28, and 60% to 70% remain open at day 7 whatever the year or maturity. | p. 18 |
| Verizon's advice from this analysis: choosing which vulnerabilities to patch first matters, since fixing everything fast is not possible. | p. 18 |
| Ransomware was in 48% of breaches, up from 44%. 69% of victims did not pay, and the median ransom paid was USD 139,875. | p. 11 |
| Breaches involving a third party reached 48%, up 60% from 30%. | pp. 11, 20 |
| Many third-party cloud incidents came from missing MFA, poor credential rotation or too many privileges. Only 23% of third parties fully fixed missing or weak MFA on their cloud accounts. | pp. 11, 21 to 22 |
| The "human element" was in 62% of breaches. | pp. 12, 20 |
| Phishing was 16% of initial access. Pretexting (a live conversation by voice, text or email to trick someone) was 6%. Verizon says training must differ for each. | pp. 12, 16 |
| In phishing simulations, voice and text attacks had a median success rate 40% higher than email. | p. 12 |
| 88% of threat actors were external, 12% internal. Organized crime dominated the external ones. Financial gain was the main motive. | pp. 23 to 24 |
| Attackers use generative AI at many steps. The median attacker in the Anthropic data researched or used AI for 15 attack techniques. Verizon says AI use has not obviously raised the phishing success rate in its own incident data. | pp. 12, 25 to 26 |
| Shadow AI: 67% of users reach AI tools with non-corporate accounts on corporate devices. | p. 13 |
| Verizon's closing advice: the basics still matter most, including knowing your assets and third parties, disciplined patching, practiced response plans, and a culture that supports secure behavior. | p. 5 |

## Terms of use for citing (important for the paper)
- p. 9: Verizon permits statistics and figures if the source is cited as "Verizon 2026 Data Breach Investigations Report" and the content is not modified. Exact quotes are allowed. **Paraphrasing "requires review"** by Verizon. The course asks for your own words. Use exact numbers with the citation, keep any paraphrase to a plain description of a number, and ask the owner whether to contact Verizon.
- p. 9: Verizon asks readers to share the link to verizon.com/dbir, not the PDF. It forbids making pie charts from the report's data.

## Limits
- Pages 28 to 121 are not read yet, so the Healthcare, Social Engineering and System Intrusion pages are not yet used.
- Verizon's data is contributed by organizations that work incidents, so it may over-represent cases that reach investigators.
- The first-page numbers above are Verizon's own figures. The report says overlapping uncertainty means small differences (for example 60% versus 62%) are not meaningful.
