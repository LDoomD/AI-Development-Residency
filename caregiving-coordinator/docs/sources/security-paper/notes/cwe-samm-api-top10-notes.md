# Notes: three "one part only" sources (2025 CWE Top 25, OWASP SAMM v2 model page, OWASP API Security Top 10 2023)

The cite plan (`caregiving-coordinator/docs/security-paper/cite-plan-2026-11-18.md`) says to read and cite only one part of each of these three sources. These notes cover that part only. None of these pages has page numbers, so each point is tied to the page's heading or table.

## 1. 2025 CWE Top 25 Most Dangerous Software Weaknesses

- **Source:** MITRE. (2025). *2025 CWE top 25 most dangerous software weaknesses*. Common Weakness Enumeration. https://cwe.mitre.org/top25/ (the source list gives the date as Dec 11, 2025 with CISA; the saved page itself does not show a publication date, so confirm it before the bibliography).
- **Label for the paper:** official project data (tier 1, MITRE is an approved domain).
- **Local copy:** `caregiving-coordinator/docs/sources/security-paper/cwe-top25/top25-2025.html`.
- **Part read (2026-11-18):** the ranked table of 25 weaknesses with score, "CVEs in KEV" (the number of vulnerabilities from that weakness on CISA's Known Exploited Vulnerabilities list) and rank change from 2024. The "Key Insights" and "Methodology" tabs on the live page were not in the saved copy, so they were **not read** and must not be cited.

| Point | Where |
|---|---|
| The list ranks 25 weaknesses by score. Rank 1 is cross-site scripting (CWE-79, score 60.38, 7 in KEV). Rank 2 is SQL injection (CWE-89, 28.72, 4 in KEV). Rank 3 is cross-site request forgery (CWE-352, 13.64). | Table, ranks 1 to 3 |
| Missing Authorization (CWE-862) is rank 4 and moved up 5 places from 2024. Incorrect Authorization (CWE-863) is rank 17. Improper Access Control (CWE-284) is rank 19. Authorization Bypass Through User-Controlled Key (CWE-639) is rank 24 and moved up 6 places. | Table, ranks 4, 17, 19, 24 |
| Missing Authentication for Critical Function (CWE-306) is rank 21 and moved up 4 places, with 11 vulnerabilities in KEV. | Table, rank 21 |
| Exposure of Sensitive Information to an Unauthorized Actor (CWE-200) is rank 20. | Table, rank 20 |
| Improper Input Validation (CWE-20) is rank 18 and fell 6 places. | Table, rank 18 |
| Several memory-safety weaknesses are high on the list (out-of-bounds write is rank 5; use after free is rank 7). Server-side request forgery (CWE-918) is rank 22. | Table |

- **Possible use:** topic 3 (background): which weakness types are most common, with several access-control weaknesses (CWE-862, 863, 284, 639) in the list. This ties to the idea's care-circle permissions. Say "access-control weaknesses are common" and cite the table. Do not say any weakness is absent from the proposed coordinator.
- **Limits:** the page's method of scoring was not read. The scores and ranks come only from the table.

## 2. OWASP SAMM v2, the model page

- **Source:** OWASP Foundation. (n.d.). *The model*. OWASP Software Assurance Maturity Model (SAMM) v2. https://owaspsamm.org/model/
- **Label for the paper:** official project model (tier 1, `owaspsamm.org` is an approved domain). The source list says the model is v2 (2020) and the site is still active.
- **Local copy:** `caregiving-coordinator/docs/sources/security-paper/owasp-samm/model.html`.
- **Part read (2026-11-18):** the model overview page only. It names the business functions and practices. The detail pages for each practice were not downloaded and not read.

| Point | Where |
|---|---|
| SAMM defines five business functions and fifteen security practices that help an organization assess and improve its software security. | Page opening sentence |
| The five functions are Governance, Design, Implementation, Verification and Operations. Each has three practices. Governance: Strategy & Metrics, Policy & Compliance, Education & Guidance. Design: Threat Assessment, Security Requirements, Secure Architecture. Implementation: Secure Build, Secure Deployment, Defect Management. Verification: Architecture Assessment, Requirements-driven Testing, Security Testing. Operations: Incident Management, Environment Management, Operational Management. | Page list |
| The original model was written by Pravir Chandra in 2009. | Introduction |

- **Possible use:** topic 6 (what teams do) and topic 4: SAMM as one way teams organize security work across five functions. The paper may use it to show that a small project like the idea could pick only a few practices (for example threat assessment and security testing), but that is the paper's own reasoning and should be said so.
- **Limits:** only the overview was read. Do not describe what any practice contains.

## 3. OWASP API Security Top 10, 2023 edition

- **Source:** OWASP Foundation. (2023). *OWASP top 10 API security risks – 2023*. OWASP API Security Project. https://owasp.org/API-Security/editions/2023/en/0x11-t10/
- **Label for the paper:** official project list (tier 1).
- **Local copy:** `caregiving-coordinator/docs/sources/security-paper/owasp-api-security-top10/top10-2023.html` (the saved page's canonical address is the URL above).
- **Part read (2026-11-18):** the full table of the ten risks and their one-paragraph descriptions. The detail pages for each risk were not downloaded and not read. I did not confirm that 2023 is the newest edition. The page shows a 2019 edition as the earlier one.

| Risk | What the table says (my words) |
|---|---|
| API1:2023 Broken Object Level Authorization | APIs expose endpoints that take object IDs. Every function that uses an ID from the user needs an object-level permission check. |
| API2:2023 Broken Authentication | Authentication is often built wrongly, letting attackers steal tokens or take over other users' identities. |
| API3:2023 Broken Object Property Level Authorization | Combines excessive data exposure and mass assignment. The cause is missing permission checks on individual fields of an object. |
| API4:2023 Unrestricted Resource Consumption | Requests use bandwidth, CPU, memory, storage, and paid services such as email or SMS. Without limits, an attacker can run up cost or cause denial of service. |
| API5:2023 Broken Function Level Authorization | Complex roles and an unclear split between admin and ordinary functions lead to flaws that let attackers use other users' or admin functions. |
| API6:2023 Unrestricted Access to Sensitive Business Flows | A flow such as buying a ticket or posting a comment can be abused by automation if not limited. |
| API7:2023 Server Side Request Forgery | An API that fetches a remote resource from a user-supplied address can be tricked into sending a request to an unexpected place. |
| API8:2023 Security Misconfiguration | Complex settings are missed or set against best practice. |
| API9:2023 Improper Inventory Management | APIs expose many endpoints, so teams need current documentation and a list of hosts and versions to avoid forgotten old versions. |
| API10:2023 Unsafe Consumption of APIs | Developers trust data from third-party APIs more than user input, so attackers target the connected services. |

- **Possible use:** topic 5 (what it includes): the three authorization risks (API1, API3, API5) fit a product where one person's data is shared with chosen others. The proposed coordinator's server routes in Next.js are the kind of interface this list addresses. Do not call the idea's routes safe against this list.
- **Limits:** only the table was read, not the per-risk pages. The paper should cite the table's wording, not the per-risk examples.
