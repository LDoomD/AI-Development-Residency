# Notes: NIST SP 800-61 Revision 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management

- **Source:** Nelson, A., Rekhi, S., Souppaya, M., & Scarfone, K. (2025). *Incident response recommendations and considerations for cybersecurity risk management: A CSF 2.0 community profile* (NIST Special Publication 800-61r3). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-61r3
- **Label for the paper:** official government guidance (tier 1). It supersedes SP 800-61 Rev. 2 (August 2012).
- **Local copy:** `caregiving-coordinator/docs/sources/security-paper/nist-sp-800-61r3/NIST.SP.800-61r3.pdf` (48 PDF pages) and NIST's status page `caregiving-coordinator/docs/sources/security-paper/nist-sp-800-61r3/status.html`. The status page lists the draft of 04/03/24 and the final of 04/03/25 and nothing newer (checked 2026-11-19). The PDF says it was approved by the NIST Editorial Review Board on 2025-03-25.
- **Page numbers below are the printed page numbers.** Front pages use Roman numerals. The Executive Summary is printed page 1, which is PDF page 9, so PDF page = printed page + 8.
- **Read in full (2026-11-19):** front matter, Executive Summary, sections 1 to 3 including Table 2 (preparation and lessons learned) and Table 3 (incident response), the references list, and Appendices A to C. I read every row of Tables 2 and 3. Table 2 mostly repeats CSF 2.0 text with low priority and few notes.

## What the pages say (my words)

| Point | Page |
|---|---|
| Incident response is "a critical part of cybersecurity risk management" and should be woven through the whole organization. All six CSF 2.0 Functions (Govern, Identify, Protect, Detect, Respond, Recover) play a part: Govern, Identify and Protect help prevent and prepare; Detect, Respond and Recover find, contain, remove and recover from incidents. | p. 1 |
| NIST says organizations cannot control attackers' methods and that "another incident is inevitable". | p. 1 |
| An event is any observable occurrence. A cybersecurity incident is an occurrence that actually or imminently jeopardizes the integrity, confidentiality or availability of information or an information system, or violates law or policy (NIST quotes FISMA 2014). The listed examples include ransomware with data theft, phishing used to take over accounts, and an attacker obtaining administrative credentials at a software-as-a-service provider. | p. 2 |
| Scope change from Revision 2: because the details of how to respond change so often, this revision no longer holds step-by-step procedures. It gives recommendations organized as a CSF 2.0 Community Profile. | p. 3 |
| The old model (Revision 2) was a circle: preparation, detection and analysis, containment and recovery, and post-incident activity. NIST says that fit a time when incidents were rarer, narrower and fixed in a day or two. Today incidents are frequent and recovery can take weeks or months. | p. 4 |
| The new life cycle puts Detect, Respond and Recover as the response, with Govern, Identify and Protect underneath as preparation and "Improvement" feeding lessons into all Functions at any time. Table 1 maps the old phases to CSF 2.0 Functions. | pp. 5 to 6 |
| NIST says to "use the incident response life cycle framework or model that suits them best". | p. 6 |
| Roles named: leadership, incident handlers (on staff, on contract, or on call), technology professionals, legal, public affairs, human resources, physical security, and asset owners. | pp. 6 to 8 |
| Third parties (managed security providers, cloud providers) may do part of the response. NIST calls this a shared responsibility model and says the responsibilities, information flows and limits must be written in a contract. A provider may spot an attack sooner because it sees many customers, and has privileged access, so the risk of its own compromise must also be considered. | p. 8 |
| An incident response policy should state management commitment, purpose, scope, definitions, roles and authority, how to prioritize incidents and measure performance. Playbooks (step lists for common scenarios) make procedures easier to use; CISA publishes examples. | pp. 8 to 9 |
| The Community Profile gives each CSF element a priority (High, Medium, Low) for incident response, plus recommendations ("R", something the organization should do), considerations ("C") and notes ("N"). | p. 10 |
| GV.OC-03 (Medium): cybersecurity requirements should include all requirements on incident notification and data breach reporting. | pp. 11 to 12 |
| GV.SC-05 (Medium): supplier agreements should cover cybersecurity performance, vulnerability, threat and incident disclosure and information sharing. GV.SC-08 (Medium): include suppliers in incident planning, response and recovery. | p. 15 |
| ID.AM-01 to ID.AM-04 (Medium): keep current, automatically updated inventories of hardware, software and services, including those from suppliers, to find vulnerabilities, detect adverse events and spot "shadow IT". ID.AM-07: keep a data inventory with classifications, owners and locations, since it shows what data may have been involved in an incident. | pp. 15 to 16 |
| ID.RA-05 (High) suggests considering threat modeling to understand attack vectors and attack surfaces. ID.RA-06 (High) lists four risk responses: accept, mitigate, transfer, avoid. ID.RA-08 (Medium) calls for a process to receive and respond to vulnerability disclosures. | pp. 17 to 18 |
| ID.IM-02 (High): improvements come from exercises and tests, including with suppliers. ID.IM-04 (High): keep incident response, vulnerability management and business continuity plans in sync and review them periodically. | pp. 19 to 20 |
| PR.DS-11 (High): backups are created, protected, maintained and tested. PR.PS-04: log records are generated and available for continuous monitoring. | p. 22 |
| Detect (High): monitor networks, personnel activity, external service providers and computing assets; monitor authentication attempts for attacks against credentials. DE.AE-02 to DE.AE-08: analyze events, correlate logs from several sources, estimate impact, alert staff and declare an incident when criteria are met. | pp. 23 to 26 |
| Respond (High): do not handle incidents "first-come, first-served"; triage and prioritize using risk factors such as asset criticality, data impact and recoverability (RS.MA). Keep a record of each incident's status. Third parties should have a way to report possible incidents. | pp. 26 to 28 |
| RS.AN-03: determine the sequence of events and root causes. RS.AN-06 and RS.AN-07: record actions, protect those records and preserve evidence. RS.AN-08: estimate how large the incident is, looking for signs on other possible targets too. | pp. 28 to 30 |
| RS.CO-02 (High): coordinate notifications as the law, regulations and contracts require (the text says incident notification laws are "evolving" and new ones are "established frequently"), notify affected third parties and tell law enforcement or regulators based on the plan. | pp. 30 to 31 |
| RS.MI-01 and RS.MI-02 (High): contain the incident, then remove its causes (for example disabling breached accounts and fixing exploited vulnerabilities). The text cautions that letting an attacker continue so that they can be watched delays containment and is risky; discuss with legal first. | pp. 32 to 33 |
| Recover (High): restore from clean backups, check integrity before use, restore in the right order, confirm normal operations and write an after-action report (RC.RP-01 to RC.RP-06). RC.CO-04: follow breach notification procedures and explain what is being done to prevent a repeat. | pp. 33 to 35 |
| The glossary defines "threat", "vulnerability", "incident" and "indicators of compromise". | p. 39 |
| Appendix C: this edition is a full rewrite of Revision 2. | p. 40 |

## Possible use in the paper
- **Topic 6 (what teams do):** the new life cycle and the idea that response is not a separate step; the roles list; playbooks; notification duties.
- **Topic 8:** a plan for the proposed coordinator can say it would name who handles an incident, keep backups and test them, keep an inventory of data (the care-circle notes) and its outside services (the host, the database and the email service), and follow a breach notice rule. The 60-day breach plan (FTC Health Breach Notification Rule) is a legal rule and comes from the saved FTC pages, not from this document.

## Limits
- It is written for organizations of any size but gives no steps for a one-person project. The Community Profile does not tell a team which rows to pick; NIST says to customize it.
- It contains no legal analysis. It says new notification laws appear often and that organizations must follow the ones that apply to them (p. 30).
- Most of Table 2 has no recommendations.
