# Notes: NIST SP 800-115, Technical Guide to Information Security Testing and Assessment

- **Source:** Scarfone, K., Souppaya, M., Cody, A., & Orebaugh, A. (2008). *Technical guide to information security testing and assessment* (NIST Special Publication 800-115). National Institute of Standards and Technology. (The PDF cover and page ii give the title, authors and date: September 2008, 80 pages. The PDF shows no DOI. Confirm the URL for the bibliography from NIST's page: https://csrc.nist.gov/pubs/sp/800/115/final.)
- **Label for the paper:** official government guidance (tier 1), but **old**: September 2008. It replaced SP 800-42 (10/15/2003). NIST's status page (checked 2026-11-18) shows "Date Published: September 2008", "Supersedes: SP 800-42" and no newer edition. The paper must say the guide is from 2008 and that tools named in it (for example BackTrack and Knoppix) are dated.
- **Local copy:** `caregiving-coordinator/docs/sources/security-paper/nist-sp-800-115/nistspecialpublication800-115.pdf` (80 PDF pages) and `caregiving-coordinator/docs/sources/security-paper/nist-sp-800-115/status.html`.
- **Page numbers below are the printed page numbers.** The guide numbers pages by section (ES-1, 1-1, 2-1 and so on, then A-1, B-1 and so on for appendices). Cite them as, for example, "p. 5-2". Front pages use Roman numerals.
- **Read in full (2026-11-18):** front matter, Executive Summary, Sections 1 to 8 including Tables 3-1 to 3-2, 4-1 to 4-2 and 5-1 to 5-2 (and Figures 5-1 and 5-2 as text), and Appendices A to G. Appendices A, E and G are tool, link and acronym lists; I read them and took few notes.
- **Scope:** written for federal agencies; nongovernmental organizations may use it on a voluntary basis (p. 1-1). It is about technical testing of hosts and networks. Application security testing is covered in about one page (Appendix C) and the guide says it is "outside the scope" to give specific techniques (p. C-2).

## What the pages say (my words)

| Point | Page |
|---|---|
| An information security assessment checks how well something (a host, system, network, procedure or person) meets security objectives. There are three methods: testing, examination and interviewing. | p. ES-1 |
| Assessments "are not meant to take the place of implementing security controls and maintaining system security." | p. ES-1 |
| NIST recommends four things: a written assessment policy; a repeatable, documented method; objectives set for each assessment; and root cause analysis after it, so findings become actions. Findings may point to weak processes as well as weak technology. | pp. ES-1 to ES-2 |
| No single technique gives a complete picture, so organizations should combine techniques. | pp. ES-2, 2-3 |
| A phased method has at least three phases: planning, execution and post-execution. A security assessment should be run like any other project. | pp. 2-1 to 2-2 |
| Three groups of technical techniques: review (examination), target identification and analysis, and target vulnerability validation. The guide says it does not say which technique to use in which case. | pp. 2-2 to 2-3 |
| Examinations (reading documents, logs, rulesets) rarely affect the systems. Testing is more intrusive and can cause outages or denial of service, so each organization must decide how much intrusion it accepts. | pp. 2-3 to 2-4 |
| Testing is narrow because time is limited, while attackers "can take whatever time they need" and are not limited to safe techniques. | p. 2-4 |
| External testing starts from outside the perimeter; internal testing assumes an insider or an attacker already inside. If both are done, do external first. | pp. 2-4 to 2-5 |
| Overt testing is done with the IT staff's knowledge. Covert testing is done without the IT staff's knowledge but with management's permission; it shows the damage an adversary could do, but not every vulnerability, and is time-consuming and costly. | pp. 2-5 to 2-6 |
| Review techniques: documentation review (checks that policies exist and are current; it does not show controls are implemented), log review, ruleset review, system configuration review, network sniffing and file integrity checking. | pp. 3-1 to 3-5 |
| Configuration review: automated checks are quicker and "provide consistent, repeatable results"; checking thousands of settings by hand is "tedious and error-prone". | p. 3-3 |
| Network sniffing cannot read encrypted content. File integrity checking needs a trusted reference database stored offline. | pp. 3-4 to 3-5 |
| Target identification: network discovery (passive and active), port and service identification, vulnerability scanning and wireless scanning. Port scanners find hosts and services but "do not identify vulnerabilities". | pp. 4-1 to 4-4 |
| Vulnerability scanners match what they find against known weaknesses. They have high false positive rates, miss problems that only show up in combinations, use their own risk scales, and depend on signature updates. The assessor must set the real risk level and not accept the scanner's label. | pp. 4-4 to 4-6 |
| A "surface vulnerability" is one that exists on its own. Several low-risk findings can together be a higher risk; penetration testing is a more reliable way to see risk in combination. | p. 4-5 |
| Common practice is to use multiple scanners and compare results. | p. 4-6 |
| Validation techniques: password cracking, penetration testing and social engineering. These carry the most risk to the target. | p. 5-1 |
| Password cracking: dictionary, hybrid, brute force and rainbow tables. Salted hashing defeats rainbow tables. NIST notes that brute force "usually takes far less time than most password policies specify for password changing", so such passwords are still too weak. | pp. 5-1 to 5-2 |
| Penetration testing means mimicking real attacks, often with real tools on real systems. It has four phases: planning, discovery, attack, reporting. It can damage systems and "should be performed only after careful consideration, notification, and planning." | pp. 5-2 to 5-3 |
| The guide lists typical weaknesses that penetration tests exploit: misconfigurations (especially insecure defaults), kernel flaws, buffer overflows, insufficient input validation (such as SQL injection), symbolic links, file descriptor attacks, race conditions and incorrect file permissions. | pp. 5-4 to 5-5 |
| NIST says annual penetration testing may be enough because of its cost and risk, and that regular scanning plus periodic penetration tests "can help prevent many types of attacks". | p. 5-6 |
| Social engineering tests (including phishing) check people. Results should be used to improve security and "not to single out individuals". | p. 5-6 |
| Planning: write an assessment policy; review it at least annually; prioritize systems by impact and last test date; consider when to test (for example, delay until a known weakness is fixed or a planned upgrade is done). | pp. 6-1 to 6-3 |
| When choosing techniques, consider risk: use a non-production copy if a test could cause denial of service, and use fake data instead of real personal information where tests could expose it. The guide notes test and live systems often differ, so a non-production test can miss problems. | p. 6-3 |
| Assessors should be vetted and skilled. The person who assesses a system should not be the one responsible for fixing the findings (conflict of interest). Outside assessors should be vetted and may be asked to share liability for damage. | pp. 6-5 to 6-6 |
| Give each assessor a separate administrator account that can be monitored and then disabled; never share administrator accounts. | p. 6-7 |
| Every assessment needs a written plan (or "rules of engagement"). It states scope, who may test, logistics, how sensitive data is handled and what to do if an incident occurs. It lists systems that must NOT be tested. If part of the network is a third party's, that party must also agree in writing. | pp. 6-10 to 6-12 |
| Legal teams should be involved for intrusive tests such as penetration testing, and should address privacy: captured data may include sensitive data that does not belong to the organization. | p. 6-12 |
| Execution: stop testing the affected systems if an incident (or a real intruder) is found, until the organization has responded. Keep a time-stamped log of every test. Do not apply immediate fixes outside change management. | pp. 7-1 to 7-3 |
| Analysis: remove false positives, group findings by control family, and find root causes. The listed root causes are weak patch management, weak threat management, no security baselines, poor security in the development life cycle, architecture weaknesses, weak incident response, weak training, and missing policy or enforcement. | pp. 7-3 to 7-4 |
| The National Vulnerability Database lists CVE entries and scores them with CVSS. | p. 7-4 |
| Assessment data is itself sensitive. In the wrong hands, architecture and vulnerability data "would provide a blueprint and roadmap" for exploiting systems. Store it isolated, encrypted and with limited access. Destroy it by the right method when no longer needed (disposal, clearing, purging or destruction, from SP 800-88). | pp. 7-4 to 7-7 |
| Post-testing: write mitigation advice for each finding with root cause; write a report; track fixes in a Plan of Action and Milestones. Test a fix on a copy first; get approval; verify the fix by retesting; keep the plan updated. | pp. 8-1 to 8-3 |
| NIST says verifying a fix by a signed statement is cheaper but risky, because the change is not technically verified. | pp. 8-2 to 8-3 |
| Appendix B gives a template for rules of engagement. Appendix C separates white box (source code) from black box testing and says white box is usually more efficient for custom applications. Appendix D covers remote access testing, including testing authentication and self-service password reset. | pp. B-1 to B-3, C-1 to C-2, D-1 to D-2 |

## Possible use in the paper
- **Topic 5 (what it includes) and topic 6 (what teams do):** the three groups of techniques (review, identification and analysis, validation) and the three phases (plan, execute, report) are a plain picture of how a security team tests a system. The point that a scanner's risk label must be checked by a person is a useful, honest limit on tools.
- **Topic 7 (tools and skills):** the guide lists the skills assessors need and warns against relying on one tool. It is dated, so use it for the method and not for the tool names.
- **Topic 8:** a plan for the proposed coordinator can say it would test with fake care-circle data and never real health or money notes, keep a written scope before any outside test, and store test findings with limited access. The paper must label this as a plan.

## Limits
- The guide is from 2008. It names tools such as BackTrack and Knoppix STD that are no longer current (the guide itself says Knoppix STD had not been updated since 2004's 0.1 release). It has no mention of cloud services, APIs, containers or modern web application stacks. It recommends SHA-1 (p. 3-5) which is no longer treated as strong. Do not cite it for tools or algorithms.
- It is written for large organizations with networks, firewalls and staff. It does not describe a one-person project or a hosted web app.
- Application security testing gets one page (Appendix C). The OWASP Web Security Testing Guide is the better source for that.
- I did not open the older documents it replaced or the NIST documents it points to.
