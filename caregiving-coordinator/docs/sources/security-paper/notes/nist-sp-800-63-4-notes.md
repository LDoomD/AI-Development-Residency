# Notes: NIST SP 800-63-4, Digital Identity Guidelines (main volume)

- **Source:** Temoshok, D., Galluzzo, R., LaSalle, C., Lefkovitz, N., Regenscheid, A., Choong, Y. Y., Proud-Madruga, D., & Gupta, S. (2025). *Digital identity guidelines* (NIST Special Publication 800-63-4). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-63-4 (the "How to Cite" box on the PDF, p. i, gives this author order).
- **Label for the paper:** official government guidance (tier 1). Final, July 2025. It supersedes SP 800-63-3. Approved by the NIST Editorial Review Board on 2025-04-28.
- **Local copy:** `caregiving-coordinator/docs/sources/security-paper/nist-sp-800-63-4/NIST.SP.800-63-4.pdf` (96 PDF pages) and NIST's status page `caregiving-coordinator/docs/sources/security-paper/nist-sp-800-63-4/status.html`. The status page (checked 2026-11-18) says: published July 2025; supersedes SP 800-63-3 (03/02/2020); final posted 07/31/25; a planning note dated 10/06/2026 says an "Implementation Resource Hub" is available. It lists no newer edition.
- **Page numbers below are the printed page numbers.** Front pages use Roman numerals. Printed page 1 is PDF page 11, so PDF page = printed page + 10.
- **Read in full (2026-11-18):** front matter, Table of Contents, Preface, Sections 1 to 3 (including Tables 1 to 4), References, Appendix A (acronyms), Appendix B (glossary) and Appendix C (change log).
- **Important limit:** this is the main volume only. The three companion volumes (SP 800-63A-4 on identity proofing, 63B-4 on authentication and passwords, 63C-4 on federation) are separate documents. They hold the detailed rules on passwords, MFA, recovery and sessions. They were **not read** (open decision 10 in report 9). Do not cite this volume for password length, rotation or recovery rules.
- **Scope:** the guidelines are written for government online services. They say private-sector organizations "may consider the use of these standards where appropriate" (p. 3). They say machine-to-machine authentication, IoT devices and API access are not explicitly addressed (p. 3).

## What the pages say (my words)

| Point | Page |
|---|---|
| A digital identity is unique within one online service. A person can hold several. When a service does not need to know who someone really is, it can use anonymous or pseudonymous accounts. | p. 1 |
| NIST promotes "a risk-based approach to digital identity solution implementation rather than a compliance-oriented approach". Assurance levels are a starting point, not a full answer. | p. 1 |
| The guidelines say risks go beyond the organization: they must account for risks to individuals, communities and other organizations. Privacy and customer experience are considered along with security. | pp. 1 to 2 |
| Three assurance levels, each with three levels: IAL (identity proofing), AAL (authentication), FAL (federation). | p. 3 |
| NIST recommends that non-federal organizations follow comparable standards (for example ISO/IEC 27001) for secure operation. The assurance levels "augment but do not replace" the controls required under FISMA and the Risk Management Framework. | p. 5 |
| This version improves defenses against identity fraud: IAL1 is repurposed, the threat models are updated, there are new options for phishing-resistant authentication, and new requirements to prevent automated attacks against enrollment. | p. 5 |
| Privacy: if a breach occurs, privacy notices must say in plain language what was released and, if known, how it was exploited. Each volume has its own privacy section with rules on data collection, retention and minimization. | pp. 5 to 6 |
| Two new ideas for customer experience: control tailoring, and continuous improvement programs. Systems should make it "easy for users to do the right thing, hard to do the wrong thing, and easy to recover when the wrong thing happens". | p. 7 |
| Notation: SHALL means required; SHOULD means recommended; MAY means permitted. Section 3 is normative (mandatory for compliance); Sections 1 and 2 are informative. | p. 8 |
| Roles: applicant, subscriber, claimant (the person); credential service provider (CSP), relying party (RP), verifier and identity provider (IdP). One entity can play several roles or they can be spread across entities. | pp. 9 to 10 |
| Three kinds of authentication factor: something you know, something you have, something you are. Two things of the same kind (a PIN and a password) are still single-factor. | p. 11 |
| Knowledge-based authentication (security questions) is not an acceptable secret. A biometric is not a secret and cannot be used alone. | p. 12 |
| Well-designed authentication protocols help limit damage from an attacker pretending to be the real verifier (phishing). | p. 13 |
| Benefits of federation: better user experience, lower cost, and less data exposed to each service through pseudonymous identifiers and derived values. NIST lists situations where federation may fit, including when an organization lacks infrastructure for account recovery, authenticator issuance and help desks. | p. 14 |
| Accept federated attributes when, among other cases, pseudonymity matters, or when attributes are needed only temporarily and need not be kept. | p. 15 |
| Three models are shown: non-federated, federated with a general-purpose identity provider, and federated with a subscriber-controlled wallet. | pp. 15 to 20 |
| The Digital Identity Risk Management (DIRM) process looks at two kinds of risk: (1) harm if the online service is compromised, which sets the first assurance levels, and (2) harm caused by the identity system itself, which drives tailoring. | p. 21 |
| Examples of harm from the identity system itself: a legitimate person blocked by barriers, a breach of the data collected to prove identity, or a control that fails to stop a known attack. | p. 22 |
| Five DIRM steps: (1) define the online service; (2) conduct an initial impact assessment; (3) select initial assurance levels; (4) tailor and document; (5) continuously evaluate and improve. The steps can be repeated when new rules, features, data uses or threats appear. Federal relying parties must run the process for all online services. | pp. 22 to 24 |
| Step 1: the description must list mission, partner dependencies, legal and privacy duties, functions and data, user groups, and everyone who could be affected. It must separate *user groups* (who logs in) from *impacted entities* (everyone who could suffer harm, including people who never use the system). | pp. 26 to 27 |
| Step 2: at least five impact categories must be assessed: degraded mission delivery; damage to trust, standing or reputation; unauthorized access to information; financial loss or liability; loss of life or danger to human safety, health or environmental health. Each user group is assessed separately. | pp. 27 to 28 |
| Impact levels are Low (limited adverse effect), Moderate (serious) and High (severe or catastrophic). Organizations should set documented thresholds. Combined levels can use a high-water mark, weights or other logic, but the method must be documented and applied consistently. | pp. 29 to 33 |
| Step 3 mapping: Low impact gives IAL1, AAL1 and FAL1; Moderate gives IAL2, AAL2 and FAL2; High gives IAL3, AAL3 and FAL2 or FAL3. Identity proofing is not needed if the service needs no personal information. The levels can differ from each other. Executive Order 13681 requires multiple factors where personal data is made accessible to citizens, which sets AAL2 as the minimum for those services. | pp. 38 to 40 |
| Table 2 (AAL): AAL1 deters password-focused attacks and expects multi-factor options to be offered. AAL2 requires multi-factor authentication and offers phishing-resistant options. AAL3 requires phishing resistance and protection against a compromised verifier, using a non-exportable private key. | pp. 35 to 36 |
| Table 1 (IAL): IAL1 limits highly scalable attacks and synthetic identity; IAL2 limits scaled and targeted attacks; IAL3 requires an in-person or attended session and a biometric. | pp. 34 to 35 |
| A service does not have to run every control itself. Some or all can be done by an outside CSP or IdP. | p. 40 |
| Step 4 (tailoring): organizations must assess privacy, customer experience and threat resistance, and may raise or lower an assurance level or add compensating or supplemental controls, but must document and justify each decision in a Digital Identity Acceptance Statement. Tailoring does not require any change to the initial levels. | pp. 41 to 46 |
| Customer experience assessment must make sure controls do not cause undue burden and that there are paths to service for people of all capabilities, resources, technology access and economic statuses. | p. 43 |
| Threat assessments must consider known threat actors; the text gives the example that certain benefit programs may be more subject to "familial threats or collusion". | p. 43 |
| Compensating controls stand in for a required control; supplemental controls add protection (for example, restricting users to phishing-resistant authentication at AAL2, or risk scoring with re-proofing). | pp. 44 to 45 |
| The Digital Identity Acceptance Statement must also be written for each outside service the organization uses, including software-as-a-service such as email and social media. | p. 45 |
| Step 5: organizations must run a documented continuous evaluation program using user feedback and performance metrics, and must monitor the threat landscape and regularly assess security and fraud measures. | pp. 46 to 47 |
| Table 4 lists recommended metrics: proofing pass, fail and abandonment rates; authenticator type usage; authentication failures; account recovery attempts; confirmed, suspected and reported fraud; help desk calls and resolution times; satisfaction surveys; redress requests and resolution times. | pp. 47 to 49 |
| Where possible, evaluation should avoid collecting more personal information and use proxy data instead. | p. 50 |
| Redress: relying parties and CSPs must offer a documented, accessible, trackable way to raise grievances, with a governance model, a dedicated function, human staff who can override algorithmic decisions, and training. | pp. 50 to 51 |
| Security, fraud and identity teams must exchange information. Data shared by an identity provider must get a privacy and legal assessment. | pp. 51 to 52 |
| AI and machine learning in identity systems: all uses must be documented and disclosed to relying parties; training methods and data and test results must be shared; NIST says to follow the NIST AI Risk Management Framework; privacy risk assessments are required. | pp. 52 to 53 |
| The glossary defines terms used by the OWASP and ASVS notes: phishing resistance ("without reliance on the vigilance of the claimant"), password, passphrase, account recovery, session, session hijack attack, replay attack, and CSRF and XSS. | pp. 62 to 84 |
| Change log: SP 800-63-3 removed email as a valid channel for out-of-band authenticators and added account recovery requirements; SP 800-63-4 adds the wallet model, an expanded risk process, performance metrics, a redress section and an AI/ML section. | pp. 85 to 86 |

## Possible use in the paper
- **Topic 4 (how it works when building products) and topic 5 (what it includes):** the three assurance levels (IAL, AAL, FAL) and the five-step risk process are a clear way to show that identity decisions follow a risk assessment, not a checklist.
- **Topic 6 (what teams do):** the idea of listing "impacted entities", not only users, fits a caregiving product where the person being cared for may never log in. The customer experience and redress points show security teams working with support and design.
- **Topic 8:** a plan for the proposed coordinator can say the idea would define its user groups (the account owner, care circle members, an invited helper) and its impacted entities (including the person being cared for), assess impact by group, and record the decision. The paper must label this as a plan. It must not say the coordinator meets any assurance level.

## Limits
- The volume is mainly a risk-management method. It does not give password, MFA, recovery or session rules; those are in SP 800-63B-4, which was not read.
- It is written for government services. Use of it by a private product is voluntary (p. 3).
- It does not discuss caregiving or health data specifically.
- I did not read the Implementation Resource Hub, the draft versions or the public comments.
