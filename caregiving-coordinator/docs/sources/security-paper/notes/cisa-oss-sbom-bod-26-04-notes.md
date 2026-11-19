# Notes: CISA open source guidance, 2026 SBOM minimum elements, and BOD 26-04

Retrieval date for all three: 2026-11-18. All three are on cisa.gov. Label for the paper: official U.S. government guidance (tier 1). Page numbers are the printed "Page N of N" numbers, which match the PDF page numbers (offset 0). BOD 26-04 is a web page with no page numbers, so I cite its section names.

---

## Source 1: Open Source Software: Security Principles and Practices

- **Source:** Cybersecurity and Infrastructure Security Agency. (2026, July 30). *Open source software: Security principles and practices*. U.S. Department of Homeland Security. https://www.cisa.gov/resources-tools/resources/open-source-software-security-principles-and-practices
- **Date check:** The PDF cover says "Publication: July 30, 2026". The cisa.gov landing page says "Publish Date July 30, 2026". They match. (The PDF file's internal creation date is Aug 11, 2026; I treat the printed date as the publication date.) The PDF shows no version number.
- **Label:** tier 1, U.S. government guidance, marked TLP:CLEAR (free to share).
- **Local copy:** `caregiving-coordinator/docs/sources/security-paper/cisa-oss-security-principles/` holds `page.html`, `page.page.txt`, `open-source-software-security-principles-and-practices.pdf` (31 pages) and the `.txt` made with pdftotext -layout.
- **Read in full (2026-11-18):** all 31 pages, including footnotes, the references, Appendix A (C4 Framework), and Appendices B and C (federal metadata examples; read, few notes).
- **Who it is for:** "Federal agencies" (p. 2). It is guidance, not a law.

| Point | Page |
|---|---|
| Today's software is mostly built from existing parts, and many of those parts are open source. People who use open source are responsible for security updates themselves. | p. 4 |
| Open source maintainers are not the same as a company that sells software. Updates are "best effort," and the people using the code must keep their own dependencies up to date. | p. 6 |
| Before approving an open source part, check how trustworthy the project is. Check again on a schedule, and also when a trigger happens, such as a new version. Use automated tools to help. | pp. 7-8 |
| Check the license to make sure the intended use is allowed. | p. 8 |
| Keep a list of all open source software in use. Without that list you cannot tell whether a new vulnerability (CVE) affects you. | p. 8 |
| Log4Shell and the xz Utils backdoor show why you need to know what is inside your software. A software bill of materials (SBOM) shows the parts and their dependencies. You can make one yourself for open source with SBOM tools. | p. 8 |
| One challenge is getting enough view into the supply chain to find and watch dependencies. Tools, including AI tools, can help with security checks. | p. 9 |
| Known Exploited Vulnerabilities (KEV) and CVE apply to open source too. Two patch principles: "collaborate, don't demand" and push fixes upstream. | p. 9 |
| When a patch ships, you must apply it and test that it does not break your app. | p. 9 |
| If a project has a security policy (often SECURITY.md), report problems the way it says. If maintainers do not answer, re-check the part. Silence may mean the project is no longer supported. If it is unsuitable, replace it. Keeping your own fork is the last resort. | p. 10 |
| In 2026, new tools (including AI) found more vulnerabilities faster and sped up patches. So automate dependency and patch work, for example in a CI/CD pipeline, which can also produce SBOMs. | p. 10 |
| Review anything you publish for secrets before it goes public, such as keys, passwords, host names and credentials. Test data built from real sensitive data should not be committed. | pp. 12, 15-16 |
| Use automated checks in CI: secret scanning to stop leaks, and a dependency scan to find vulnerabilities. Squashing git history is not a reliable fix for leaked secrets, because forks keep the old history. | p. 16 |
| For published projects: include README, LICENSE, CONTRIBUTING, SECURITY.md (with a way to report problems), and an SBOM with each release. | pp. 16-17 |
| A project is "actively maintained" if none of its dependencies are end-of-support and security patches are applied on the BOD 26-04 timeline. If you stop maintaining a project, say so clearly (for example, archive it on GitHub). | p. 17 |
| Follow secure development practices such as NIST SP 800-218 (SSDF). | p. 18 |
| "Open source" AI models may not share their training data, so you cannot judge them the way you judge code. Treat a model with no training data access as proprietary software with incomplete provenance. | pp. 18-20 |
| "All software carries risk, and OSS is no more or less risky than other software." Open source lets you check the code yourself. | p. 21 |
| C4 Framework: judge a project by four groups: Codebase (last commit, known CVEs, out-of-date dependencies), Community (number of maintainers, foundation), Conduct (security policy, code review, license) and Configuration (is the default setup secure). Judge how it was made, not who made it. | p. 24 |
| C4 in five steps: pick measurable criteria, set how much risk is acceptable, collect facts, check each criterion, compare to the risk you accept. Example: a part that touches personal data should have a low risk tolerance. Pick some "red flag" criteria where one failure rules the part out. | pp. 25-26 |
| Example criterion: "the project includes a software bill of materials (SBOM) for each version." The Scorecard tool can check that an SBOM exists, but not what is in it. | p. 25 |

**Useful for the paper**
- **Topic 7 (best practices):** a plain method to choose and re-check open source parts (C4), plus automation in CI (secret scan, dependency scan, SBOM) (pp. 10, 16, 24-26).
- **Topic 8 (application):** for the proposed coordinator, every npm package is an open source part. The C4 questions (recent commits, number of maintainers, security policy, known CVEs, license) can be asked of each important package. Keep a list of dependencies (the lockfile is the practical record) so a new CVE can be matched to what is installed (p. 8).
- **Topic 5 (risks):** unmaintained packages and silent maintainers are a risk; replace or re-check (p. 10). Leaked secrets in a public repo are a risk (p. 16). A health-data product would set a low risk tolerance for any package that touches personal data (p. 25).
- **Patch priority:** points to BOD 26-04 as the timeline example (p. 17).

**Limits and cautions**
- It is written for U.S. federal agencies. Most of it (source code inventory, OMB M-16-21, DHS metadata, government reuse) does not apply to a private product. I used the general sections only.
- It is guidance, not law, and it does not say any practice makes software "secure."
- It tells agencies to "default to open source" for their own code. That is an agency policy, not advice for a private startup.
- The claim about AI speeding up vulnerability discovery (p. 10) is stated without a citation in the text I read.

**Not read:** nothing in the PDF. I did not open the outside links it cites (Hipcheck, CHAOSS, Scorecard, OpenSSF, OMB M-16-21).

---

## Source 2: 2026 Minimum Elements for a Software Bill of Materials (SBOM)

- **Source:** Cybersecurity and Infrastructure Security Agency, National Security Agency, Federal Bureau of Investigation, and international partners. (2026, July 29). *2026 minimum elements for a software bill of materials (SBOM)* (Version 2.1). Cybersecurity and Infrastructure Security Agency. https://www.cisa.gov/resources-tools/resources/2026-minimum-elements-software-bill-materials-sbom
- **Date and version check:** The PDF cover says "Publication: July 29, 2026". The version table on p. 2 lists 1.0 (July 12, 2021, initial), 2.0 (August 22, 2025, draft) and 2.1 (July 29, 2026, update after public comments). The cisa.gov landing page says "Publish Date July 29, 2026". They match. The PDF does not label itself "Version 2.1" on the cover; I took that from the p. 2 table, so confirm the APA version wording before use.
- **Label:** tier 1, U.S. government plus allied agencies' joint guidance, TLP:CLEAR. Co-authors include NSA, FBI and agencies from Australia, Canada, Czechia, France, Germany, India, Italy, Japan, Korea, the Netherlands, New Zealand, Poland and Slovakia (p. 4). The landing page lists the audience as federal government, industry, small and medium businesses and state, local, tribal and territorial government.
- **Local copy:** `caregiving-coordinator/docs/sources/security-paper/cisa-sbom-minimum-elements-2026/` holds `page.html`, `page.page.txt`, `2026_cisa_sbom_minimum_elements_508c.pdf` (23 pages) and the `.txt`.
- **Read in full (2026-11-18):** all 23 pages, including footnotes, the references, Appendix A and Appendix B.

| Point | Page |
|---|---|
| An SBOM is a nested list of the "ingredients" of software. This document "updates and replaces" the 2021 minimum elements from NTIA (a U.S. Commerce Department agency). | p. 4 |
| Tools have improved a lot since 2021, so buyers can now ask for more detail. | pp. 2, 4 |
| The EU Cyber Resilience Act requires makers of products with digital parts to give an SBOM in their technical documents (the document says so; I did not check the EU law). | p. 5 |
| The minimum elements apply to all software, including open source. AI software and cloud (SaaS) may need extra elements. | pp. 5, 7 |
| New data fields in 2026: SBOM Author Signature, Data Format Name and Version, Generation Context, Tool Name and Version, SBOM Version, Component Hash Value and Algorithm, Component License. | p. 5 |
| Changed fields: SBOM Author, Component Identifiers, Component Producer, Component Version, plus practices Accommodation of Updates, Coverage, Explicitly Identifying Unknown Information, Machine-Processable Data. Access Controls was removed and folded into Distribution and Delivery. | pp. 5-6 |
| SBOM data can be matched to security advisories or lists of approved software. SBOMs do not solve all problems, but are "a necessary step." | p. 6 |
| People cannot track modern software by hand, so automation matters. | p. 6 |
| The minimum elements "do not create new requirements"; they refine how to generate and request SBOMs. | p. 7 |
| Data fields about the SBOM file: author (a full name, not the tool), signature (shows it was not changed), format name and version, generation context (before build, build, after build), timestamp (RFC 9557), tool name and version, SBOM version. | pp. 8-10 |
| Data fields about each component: producer (one organization; if unclear, say "unknown provenance"), dependency relationship, hash value and algorithm, identifiers (for example Package-URL, "PURL"; CPE), license (for example SPDX identifiers), name, version. | pp. 10-13 |
| Coverage: list all components, including transitive dependencies. "There is no minimum depth." If the list does not include a component, the reader can conclude a new vulnerability in that component does not affect them. | p. 13 |
| Distribution: share the SBOM promptly with those who need it; access controls must not block trusted sharing or use in security tools. | p. 13 |
| If a field is missing, say whether it is unknown or withheld. | pp. 13-14 |
| Frequency: each release or build should have its own SBOM, and a corrected one when errors are found. | p. 14 |
| Machine-readable data: the two widely used formats are SPDX and CycloneDX. Do not accept deprecated format versions. | p. 14 |
| SBOM plus advisories such as VEX and CSAF shows which known vulnerabilities actually matter, and speeds response. | p. 16 |
| Appendix A lists 18 data fields with one-line definitions. | p. 19 |
| **Difference from 2021 (Appendix B):** "Depth" (top-level dependencies only) became "Coverage" (all components, including transitive); "Supplier Name" became "Component Producer"; "Other Unique Identifiers" became "Component Identifiers"; "Known Unknowns" became "Explicitly Identifying Unknown Information"; "Automation Support" became "Machine-Processable Data" and SWID tags were dropped from the formats list; "Access Control" was removed; and hash, license, signature, format, context, tool and SBOM-version fields were added. | pp. 20-23 |
| Disclaimer: the publication is "general" and "does not constitute advice for compliance, regulatory, or legal purposes." | p. 17 |

**Useful for the paper**
- **Topic 7:** a clear definition of a baseline SBOM and why to regenerate it with each release (p. 14). Dependency lockfiles feed this: a lockfile lists exact versions of direct and transitive packages, which is the raw material for the "Coverage" idea (p. 13). (The link between npm lockfiles and these fields is my reading; the document does not name npm.)
- **Topic 8:** for a small team, a practical path is to generate an SBOM automatically in CI at each release in SPDX or CycloneDX, with Package-URL identifiers (pp. 11-14). This is my suggestion built on the document, not something the document says about small teams.
- **Topic 5:** an SBOM lets a team answer "does this new CVE affect us?" quickly (p. 13, p. 16).
- **Patch priority:** SBOM data plus advisories (VEX) can narrow which alerts matter (p. 16); pair it with the BOD 26-04 priority table below.

**Limits and cautions**
- It says what an SBOM should contain. It does not say any software is safe, and an SBOM is only data about parts (p. 16).
- It says the document is not compliance advice (p. 17).
- It does not give a small-team or startup walk-through, and it does not cover npm tooling. Data management and exact encoding are out of scope (p. 7).
- Accuracy, completeness and validation of SBOMs are out of scope here (pp. 15-16), so a tool-made SBOM is not proof it is correct.
- The document admits ambiguity remains in naming producers (p. 11).

**Not read:** nothing in the PDF. I did not open the cited outside references (SPDX, CycloneDX, RFCs, EU Cyber Resilience Act text, G7 SBOM for AI document).

---

## Source 3: BOD 26-04, Prioritizing Security Updates Based on Risk

- **Source:** Cybersecurity and Infrastructure Security Agency. (2026, June 10). *BOD 26-04: Prioritizing security updates based on risk* [Binding operational directive]. U.S. Department of Homeland Security. https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk
- **Companion:** Cybersecurity and Infrastructure Security Agency. (2026, June 10; updated 2026, August 25). *BOD 26-04: Implementation guidance for prioritizing security updates based on risk*. https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk
- **Date check:** Both cisa.gov pages show "June 10, 2026". The guidance page also shows "Updated: August 25, 2026". The related-directives lists on both pages show June 10, 2026. The directive page shows no version number and no separate effective date; its deadlines are written as "within 60 days of issuance" and "within 180 days of issuance." I did not compute calendar dates for them.
- **Label:** tier 1, U.S. government directive. This is a web page with no PDF. A "web-friendly version" of the directive is what cisa.gov publishes, per its own text.
- **Local copy:** `caregiving-coordinator/docs/sources/security-paper/cisa-bod-26-04/` holds `page.html` (directive), `page.page.txt` (its text), `implementation-guidance.html`, `implementation-guidance.page.txt`, `table-1-remediation-timelines.png` and `graphic-remediation-timelines.png`. I did not download the standardized data schema spreadsheet (XLSX) the page links.
- **Read in full (2026-11-18):** the whole text of both pages. Table 1 on the directive page is an image, so I opened the saved PNG and read all 16 rows, and I opened the flowchart graphic (it agrees with the table). I did not open the linked outside documents (SSVC guide, NIST documents, OMB M-24-15).

| Point | Section |
|---|---|
| A Binding Operational Directive is "a compulsory direction" to federal executive branch agencies. It does not apply to national security systems. | Directive intro |
| It replaces and revokes BOD 19-02 (April 2019) and BOD 22-01 (Nov. 2021), the older rules for internet-facing patching and for the KEV catalog. | Background |
| Reason: attackers exploit unpatched vulnerabilities, and AI "may further narrow the time defenders have to react." The aim is to focus patching on the highest risk instead of treating everything the same. | Background |
| Four questions set the deadline: (1) Is the asset publicly exposed? (2) Is the CVE on the KEV catalog? (3) Can an attacker automate all steps? (4) Does the attacker gain partial or total control? | Background |
| CISA publishes the KEV, automatable and technical impact answers for each CVE (through its Vulnrichment program). The agency answers the exposure question for its own assets. | Background |
| Scope: federal civilian agencies' systems. It does not apply to contractors unless the contract says so. | Scope |
| Phases: Phase I immediately (update policies, monitor the KEV, report KEV status through the CDM dashboard or every two weeks by hand); Phase II within 60 days (process updates based on CVE data and KEV); Phase III within 180 days (meet the Table 1 timelines and tag exposed assets, reporting every 7 days if not automated). | Required Actions |
| Timeline clock starts when CISA adds the CVE to the KEV, or when the agency finds the vulnerability on an asset, whichever happens first. Days are calendar days. | Appendix A |
| "Remediated" means eliminated by patching, decommissioning the system, or another action. Removing a system from the internet can change the required timeline. | Appendix A |
| **Table 1 (16 rows), in my words.** Publicly exposed + on the KEV + automatable + total control: 3 days and forensic triage. Same but partial control: 3 days. Exposed + on KEV + not automatable: total control 3 days and forensic triage; partial control 14 days. Exposed + not on KEV + automatable: total control 3 days; partial 14 days. Exposed + not on KEV + not automatable: total 14 days; partial 60 days. Not exposed + on KEV + automatable: total 3 days and forensic triage; partial 14 days. Not exposed + on KEV + not automatable: 14 days either way. Not exposed + not on KEV + automatable: 60 days either way. Not exposed + not on KEV + not automatable: "fix on system upgrade" (next scheduled major upgrade or rebuild). | Appendix A, Table 1 (image) |
| "Forensic triage" means finishing the fix within three days and also checking whether the system was already compromised. | Appendix A |
| The table is "informed by" SSVC (a decision method). "Technical impact" is "similar to" the CVSS base score's idea of severity. | Appendix A |
| **KEV:** CISA adds a vulnerability when it has a CVE ID, reliable evidence of active exploitation, a clear fix or mitigation, and significant risk to U.S. government systems. CISA aims to update the KEV within 24 hours. Old CVEs can be added. Removal is rare. | Guidance, KEV FAQ |
| The KEV is not the only list to worry about. Agencies "should track and prioritize all vulnerabilities," and longer timelines are acceptable for those not on the KEV or without a CVE ID. | Guidance, KEV FAQ |
| **CVSS:** by revoking BOD 19-02, federal agencies "no longer require CVSS use for vulnerability prioritization." CVSS labels like "critical" or "high" do not say what action to take, so CISA replaces them with explicit timelines. The guidance quotes the CVSS user guide: base scores "should not be used alone to assess risk." | Guidance, FAQ on CVSS and critical/high vs KEV |
| Technical impact is "total" if, for example, the attacker can run arbitrary software, gets a full-privilege account, or reliably gets login credentials. Otherwise it is "partial" (for example, denial of service). | Guidance, FAQ |
| Automatable example: a public proof-of-concept that reliably gives remote code execution. | Guidance, FAQ |
| If data is missing, CISA assumes "not automatable" and "total" for a non-KEV CVE until data is supplied. | Guidance, FAQ |
| The timelines are maximums. Agencies may patch faster. CISA does not issue waivers. If an asset cannot be fixed in time, remove it from the network. | Guidance, FAQs |
| Forensic triage in six steps with suggested hours (scope within about 2 hours; collect evidence 2-24 hours; patch 2-24; contain 6-24; analyze 24-48; report and decide escalation 48-72). The timelines are "recommended best practices"; the requirement is that adequate triage is done. | Guidance, Forensic Triage Steps |
| Not every vulnerability gets a CVE ID, including many web application and configuration problems. Agencies should still fix them. | Guidance, Vulnrichment FAQ |
| Shared responsibility: for SaaS, the cloud provider handles web application security; for IaaS the agency keeps full responsibility. CISA recommends remediation timelines in service-level agreements. | Guidance, Vendors FAQ |

**Useful for the paper**
- **Patch priority (topic 7):** a worked example of ranking by real-world risk rather than by a score alone: exposed to the internet, known to be exploited, easy to automate, and how much control the attacker gets. A proposed coordinator that is public on the web would sit in the "publicly exposed" rows of Table 1.
- **Topic 8:** a small team could borrow the four questions as a plain triage rule for `npm audit` findings and Dependabot alerts (this is my suggestion; the directive does not address private products). The KEV catalog is free to check (the guidance describes the catalog but I did not test any tool).
- **Topic 5:** shows that old, known-exploited flaws matter, and that a CVSS label alone is not a full risk answer.
- **Cross-link:** the OSS guidance (p. 17) uses this BOD's timeline to define "actively maintained."

**Limits and cautions**
- The directive binds U.S. federal civilian agencies only. It does not bind private companies and is not law for a private product. Say so in the paper.
- The 3, 14 and 60 day numbers are federal maximums chosen by CISA for agency assets. They are an example, not a rule a small team must follow.
- It covers vulnerabilities with CVE IDs most directly. It says many problems have no CVE ID, so it is not complete (Guidance, Vulnrichment FAQ).
- CISA says it will review Table 1 each fiscal year and may shorten the timelines (Directive, CISA Actions), so the numbers may change. The guidance page was updated Aug 25, 2026, so re-check before final submission.
- The guidance says CISA relies on sources it describes (vendors, researchers, intelligence feeds) to decide what is "actively exploited." I did not check that independently.
- It does not mention npm, lockfiles or SBOM data directly.

**Not read:** the linked CISA SSVC guide PDF, the BOD 26-04 standardized data schema (XLSX, which I did not download), NIST SP 800-40 Rev. 4, OMB Circular A-130, OMB M-24-15, the FedRAMP response, and the CISA Internet Exposure Reduction Guidance. I read the glossary only as a list of acronyms.
