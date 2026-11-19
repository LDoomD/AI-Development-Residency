# Notes: CISA and partners, Secure by Design (Shifting the Balance of Cybersecurity Risk)

- **Source:** Cybersecurity and Infrastructure Security Agency, National Security Agency, Federal Bureau of Investigation, and international partners. (2023). *Shifting the balance of cybersecurity risk: Principles and approaches for secure by design software*. CISA. https://www.cisa.gov/resources-tools/resources/secure-by-design
- **Label for the paper:** joint government guidance (tier 1 in the source list). The guide says it does not automatically serve as a regulatory document (p. 34).
- **Local copy:** `caregiving-coordinator/docs/sources/security-paper/cisa-secure-by-design/SecureByDesign_1025_508c.pdf` (36 pages, created Oct 17, 2023) and CISA's landing page `caregiving-coordinator/docs/sources/security-paper/cisa-secure-by-design/page.html` (revision date October 25, 2023). The landing page saved earlier was only a short summary. The real guidance is the PDF, which I downloaded on 2026-11-18 from https://www.cisa.gov/sites/default/files/2023-10/SecureByDesign_1025_508c.pdf (an approved domain).
- **Page numbers below are the printed page numbers.** They match the PDF page numbers.
- **Read in full (2026-11-18):** pages 4 to 34 (overview, the three principles with their tactics, the tactics lists, the guide for customers and the disclaimer). Pages 1 to 3 (cover and contents) and the resource and reference lists on pages 35 and 36 were skimmed, not read in detail.
- **Currency check (2026-11-18):** CISA's page shows this as the October 25, 2023 update of the April 2023 original. The page shows no newer edition. The text of the PDF drops periods in places, so I paraphrase and do not quote.

## What the pages say (my words)

| Point | Page |
|---|---|
| The authors say makers should shift the security burden from customers to manufacturers. Past practice was to fix flaws after customers had deployed the product, at the customers' cost. | p. 4 |
| "Secure by design" means a product is built so it reasonably protects against attackers. "Secure by default" means a product is safe to use right out of the box with little or no change by the customer, and with security features at no extra cost. Secure by default is a form of secure by design. | pp. 5, 8, 9 |
| The guide recommends a risk assessment, a threat model made for the product and defense-in-depth (several layers, so one failure does not break everything). The authors say security cannot be "bolted on" later. | p. 8 |
| The three principles are: take ownership of customer security outcomes; embrace radical transparency and accountability; lead from the top. | p. 10 |
| Principle 1 says makers should invest in three things: application hardening, security features (for example TLS, single sign-on, multi-factor authentication, audit logging and role-based access control) and secure default settings. | pp. 11 to 12 |
| The guide gives sample tactics: validate input and use parameterized queries, not input placed directly in code. | p. 11 |
| The guide warns about making customers follow a long "hardening guide". It says guides are hard to find, hard to follow and do not scale. A short phrase captures it: the industry needs more secure products, not more security products. | p. 13 |
| Small and medium organizations usually lack the expertise, money and time to add security tools themselves. | p. 13 |
| Practices that make a product secure by default include eliminating default passwords, field-testing how real users use security features, and alerts that repeat when users or admins are in an unsafe state. | pp. 15 to 16 |
| Practices for development include documenting conformance to a secure development framework (the guide names NIST SSDF), a vulnerability management program that finds root causes, responsible use of open source, safe defaults for developers ("paved roads"), and testing that logs help incident responders. | pp. 17 to 18 |
| The guide says businesses should not charge extra for security logging, single sign-on or multi-factor authentication. It calls this the "SSO tax". | p. 19 |
| Transparency practices include publishing high-level threat models, a software bill of materials, and a vulnerability disclosure policy with legal safe harbor for researchers. | pp. 23 to 24 |
| The guide says not to treat a count of public vulnerability records as only a bad sign, since it can also show that a team finds and reports flaws. | pp. 10, 23 |
| Principle 3 says security is a business priority that must start with senior leaders, not only technical staff. | p. 26 |
| The "tactics" list names memory safe languages, secure software components, web template frameworks that escape input automatically, parameterized queries, static and dynamic testing, code review, software bills of materials, vulnerability disclosure programs, and defense-in-depth. | pp. 28 to 29 |
| Secure-by-default tactics include removing default passwords, making multi-factor authentication required for privileged users, single sign-on at no extra cost, audit logs by default, and an authorization profile that limits roles (the guide's example is a medical scheduler who sees less than a doctor). | p. 30 |
| Each added setting adds a burden on users. The guide says the most secure setting should be built in by default. | p. 31 |
| The guide recommends "loosening guides" instead of hardening guides: they list which changes weaken security and explain the risk in plain words. | p. 32 |
| For customers: hold suppliers accountable, write purchase rules that require secure by design, and for cloud systems understand the shared responsibility model and prefer providers that are transparent about their controls. | pp. 33 to 34 |

## Possible use in the paper
- **Topic 4 (building products):** the idea that security is built in from the start, "secure by default", threat modeling at design time, and that customers should not carry the burden. These support the stance that the proposed coordinator should use safe defaults (for example, turn on row-level security and keep access private by default).
- **Topic 5 (what it includes):** defense-in-depth, least-privilege roles, audit logs, multi-factor authentication.
- **Topic 8:** the guide's own role example (p. 30) shows people with different roles seeing different amounts of health information. This supports the idea of limited roles in care circles in a general way. It is not a claim about the coordinator.

## Limits
- This guidance is addressed to software manufacturers and their customers, mostly larger ones. It does not say how a student or a very small team should apply it. The authors say smaller manufacturers may struggle (p. 6).
- The guide is voluntary. It is not a compliance standard (p. 34).
- Some of the suggestions (board reports, financial reports, executive sponsors) do not apply to a one-person project. Do not claim the coordinator meets them.
- The document is from 2023. It does not mention Vercel or Supabase.
