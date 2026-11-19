# Notes: NIST SP 800-207 (Zero Trust Architecture) and NIST SP 800-100 Rev. 1 (DRAFT)

Retrieved 2026-11-18 with plain `curl -L` from nist.gov servers. Page numbers below are the printed page numbers.

---

## Source 1: NIST SP 800-207, Zero Trust Architecture

- **Source:** Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST Special Publication 800-207). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-207
- **Label for the paper:** official government guidance (tier 1), final, dated August 2020. It is about six years old on the retrieval date.
- **Status page (checked 2026-11-18):** https://csrc.nist.gov/pubs/sp/800/207/final shows "Date Published: August 2020". The saved copy shows no "superseded" or "withdrawn" notice and does not name a newer edition or SP 1800-35. Its "Related NIST Publications" list is empty in the saved file (that list may load by script, so I cannot say what a browser shows). It lists only two unofficial translations (Spanish and Japanese).
- **Local copies:** `caregiving-coordinator/docs/sources/security-paper/nist-sp-800-207/nist-sp-800-207.pdf` (59 PDF pages), `.../nist-sp-800-207.txt` (text from `pdftotext -layout`), `.../status.html`.
- **Page offset:** printed page 1 (Introduction) is PDF page 10. PDF page = printed page + 9. Front pages are Roman numerals (ii to vii). Last printed page is 50 (PDF page 59).
- **Read in full:** all 59 PDF pages of text (cover, abstract, audience, contents, Sections 1 to 7, References, Appendices A and B). I also looked at the PDF image of printed page 9 (Figure 2). Figures 1, 3 to 12 were read through their captions and the text that describes them; I did not view their images.

### What the pages say (my words)

| Point | Printed page |
|---|---|
| NIST says zero trust is a set of ideas, not one product. It assumes an attacker may already be on the network. Trust is not given because of where a device sits. | pp. 1 to 2 |
| The guide is written for enterprise security architects working with civilian federal systems. NIST says it is "not intended to be a single deployment plan." | p. iii |
| Working definition: zero trust means making each access decision per request, with least privilege, as if the network is already compromised. | p. 4 |
| Access is decided by a policy decision point (PDP) and carried out by a policy enforcement point (PEP). The idea is to keep the "implicit trust zone" as small as possible and move these checks close to the resource. | p. 5 |
| **The seven tenets:** (1) all data sources and services count as resources; (2) all communication is protected no matter where it comes from; (3) access is granted per session, with least privilege; (4) access follows dynamic policy (who is asking, what device, other context); (5) the organization watches the health of every asset it owns; (6) authentication and authorization happen, and are checked again, before access; (7) the organization collects data about assets, traffic and requests to improve policy. NIST says these are the ideal and may not all be fully met. | pp. 6 to 7 |
| The tenets apply to work inside an organization or with partners. They do not apply to anonymous public or consumer-facing use. For registered users (such as customers or employee dependents) some zero trust policies may be possible. | p. 7 |
| Network assumptions: the whole private network is not a trusted zone; no resource is trusted by default; credentials of a person alone are not enough to trust a device; remote users should treat their local network as hostile. | p. 8 |
| **Policy engine (PE):** makes the final decision to allow, deny or revoke access, using policy and outside inputs, and logs the decision. | p. 9 |
| **Policy administrator (PA):** carries out the PE's decision by opening or closing the connection through the PEPs, and can create a session-specific token or credential. | pp. 9 to 10 |
| **Policy enforcement point (PEP):** turns the connection on, watches it, and shuts it off. Everything behind the PEP is the trust zone. | p. 10 |
| Data sources the PE uses: a device-health system (CDM), a compliance system, threat feeds, activity logs, data access policies, a public key system, an identity management system, and a SIEM (security log analysis). | pp. 10 to 11 |
| Three ways to build a ZTA: driven by identity governance, by micro-segmentation, or by network software-defined perimeters. A full solution uses parts of all three. NIST notes that identity-driven setups still leave basic network access open, so attackers could scan or try denial of service. | pp. 11 to 13 |
| **Deployment variations:** device agent and gateway; enclave gateway; resource portal; device application sandboxing. The portal model needs no software on the user's device, but it can only check a device while it is connected and may see little about it. | pp. 13 to 17 |
| **Trust algorithm:** the PE's decision process. Inputs: the access request, a subject database, an asset database, resource requirements, and threat intelligence. It can be criteria-based or score-based, and singular (each request alone) or contextual (considers recent history). NIST says ideally it should be contextual. It also warns that repeated re-prompting can hurt usability, and that an early "tuning" phase will wrongly deny some valid requests. | pp. 17 to 21 |
| The control plane (decisions and setup) is kept separate from the data plane (real traffic). Resources should not be reachable except through a PEP. The decision components must scale, because delay or loss of a PEP hurts the whole workflow. | pp. 21 to 22 |
| Use cases: remote or satellite offices; several clouds; contractors and visitors; working with another organization; public or customer-facing services. For public-facing services NIST says the tenets do not directly apply to anonymous pages and that the organization can only apply limited policy to registered users. | pp. 23 to 27 |
| **Threats to a ZTA:** (5.1) the decision process is subverted, because the PE and PA are the key parts, so their configuration must be logged and audited; (5.2) denial of service or outage of the PE, PA or PEP; (5.3) stolen credentials or insiders. Even with ZTA, a person with valid credentials can still reach what that account may reach; (5.4) poor visibility into encrypted or non-enterprise traffic; (5.5) stored logs and policy data become a target; (5.6) lock-in to proprietary formats; (5.7) software or AI agents that administer the system could be tricked or have their credentials stolen. | pp. 28 to 31 |
| ZTA depends on exact identity management. Weak identity setup and incomplete asset knowledge make the PE deny valid requests. | pp. 33, 37 |
| Privacy: logging and inspecting traffic can capture private data. NIST points to the NIST Privacy Framework and says organizations may need to inform users or get consent. | p. 32 |
| **Migration:** it is a journey, not a one-step replacement. Most organizations will run a hybrid of zero trust and perimeter for a long time. A new system can be built on zero trust from the start ("greenfield"), though NIST calls this rarely possible for existing networks. | pp. 36 to 37 |
| Migration steps: identify actors; identify assets; identify and rank key processes and risks; write policies for a first candidate; choose solutions; deploy first in a watch-and-report mode (basic rules such as denying failed MFA still enforced); then expand and re-check after changes. Start with a low-risk process. | pp. 37 to 41 |
| Appendix B: NIST says the ZTA product market was "not mature enough for widespread adoption" in 2020. It names open questions: no common terms, vendor lock-in, how attackers will adapt (for example, going after MFA or after the parts that are not yet zero trust), user experience and "security fatigue," and what happens when a decision component is unreachable. | pp. 46 to 50 |

### Useful for the paper

- Gives a cited, official base for the idea "every request is checked, nothing is trusted by default": tenets 3, 4 and 6 (pp. 6 to 7) and the definition on p. 4.
- The PE / PA / PEP split (pp. 9 to 10) is a clear way to describe where a request check lives in the proposed coordinator. The proposed idea would only borrow the concept; it would not need the enterprise network parts.
- Section 5 (pp. 28 to 31) is a ready list of risks for topic 5: a subverted decision point, outage, stolen credentials, log storage as a target, and automated agents.
- Section 5.3 (p. 29) is useful for a caregiving case: even strong checks do not stop a person who legitimately holds a valid account from using what that account may see.
- Section 7 (pp. 36 to 41) supports a staged, start-small approach for topic 8.
- The note on registered non-employee users (pp. 7, 27) fits caregivers and family members who are not employees.

### Limits and cautions

- Written for **enterprise networks and U.S. federal agencies** (p. iii). It talks about devices, gateways, VPNs, CDM and federal programs (TIC, EINSTEIN, FICAM). A small web product with no company network does not map one-to-one; the paper should say it borrows principles only.
- It says the tenets do **not** apply to anonymous or consumer-facing use (p. 7). Caregiver sign-in is closer to a registered-user case (p. 27), where NIST says only limited policy can be applied.
- Dated August 2020. Its sources (for example NIST SP 800-63-3) have since been replaced by newer editions. I did not check the 800-63 edition here.
- Describes ideas and options, not a test or a certification. It does not make any system "secure."
- The status page shows no newer edition, but I could not see its "Related" list (see above), so do not state that NIST has published no later ZTA material.

### Not read

- Documents cited by 800-207 (for example SP 800-63, SP 800-162, SP 800-37, OMB memos). Figures 1 and 3 to 12 images (text and captions only). The unofficial Spanish and Japanese translations. I did not look for NIST SP 1800-35 beyond checking the status page.

---

## Source 2: NIST SP 800-100 Rev. 1, Information Security Handbook (DRAFT)

- **Source (DRAFT, initial public draft):** Van Wyk, I., Brewer, J., Marron, J., & Licata, J. (2026). *Information security handbook: A guide for executive leadership* (NIST Special Publication 800-100r1 ipd, initial public draft). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800.100r1.ipd (the DOI as printed in the PDF; the status page links https://doi.org/10.6028/NIST.SP.800-100r1.ipd).
- **Label for the paper:** official government guidance (tier 1) but **a DRAFT, not final**. The PDF and status page say October 2026. Public comment period: October 21 to December 4, 2026 (unnumbered page before the abstract). The status page gives "October 12 to December 4, 2026" in its announcement text, so the start date differs between the two; the end date, December 4, 2026, matches. It may change before it is final. The paper must say "draft" every time it is cited, and must not present it as the final edition.
- **Status page (checked 2026-11-18):** https://csrc.nist.gov/pubs/sp/800/100/r1/ipd. "Date Published: October 21, 2026"; "Comments Due: December 4, 2026". Document history lists two drafts: 01/09/24 "SP 800-100 Rev. 1 (Draft)" and 10/21/26 "SP 800-100 Rev. 1 (Draft)". The final field ("Supersedes") in the PDF is an unfilled placeholder. I did not open the 2024 draft.
- **Local copies:** `caregiving-coordinator/docs/sources/security-paper/nist-sp-800-100r1-draft/nist-sp-800-100r1-ipd.pdf` (52 PDF pages), `.../nist-sp-800-100r1-ipd.txt`, `.../status.html`.
- **Page offset:** printed page 1 (Introduction) is PDF page 11. PDF page = printed page + 10. Front pages are Roman numerals (i to vi). Last printed page is 42 (PDF page 52). The draft also prints line numbers down the left side.
- **Read in full:** all 52 PDF pages of text (front matter, Sections 1 to 7, References, Appendices A to C). I looked at the PDF images of printed pages 13 (Fig. 2), 26 (Fig. 3) and 29 (Fig. 4). Fig. 1 (NICE building blocks) was read by caption and text only.
- **Draft defects I saw in the text:** "Error! Reference source not found" appears in Section 2's opening list (p. 4); a stray reference entry is mixed into the text at the end of Sec. 3.4 (pp. 16 to 17) and in Sec. 4.4 (p. 20); the text version of the table of contents omits subsection lines. These show it is unfinished.

### What the pages say (my words)

| Point | Printed page |
|---|---|
| The handbook gives executives short summaries of key cybersecurity topics and points to other NIST publications for detail. It follows the layout of the NIST Cybersecurity Framework (CSF) 2.0. It says it is not a companion to the CSF. | pp. 1, 3 |
| Audience: senior leaders, CIOs and CISOs, program managers, system owners, and managers without technical depth. | p. ii |
| NIST says the 2006 original is "two decades" old and out of step with current practice, so the revision restructures it. | p. ii |
| Structure: 1 Introduction (roles); 2 NIST Frameworks; 3 Governance; 4 Identify; 5 Protect; 6 Continuous Monitoring; 7 Detect, Respond and Recover. | p. 3 |
| Section 1.2 lists leadership roles: agency head, CIO, CISO, chief enterprise architect, and the privacy officer. | pp. 1 to 3 |
| Section 2 summarizes seven NIST frameworks and how they fit: Risk Management Framework (7 steps), CSF 2.0, NICE workforce framework, Privacy Framework, SSDF (secure software development), AI Risk Management Framework, and supply chain risk management. | pp. 4 to 10 |
| Governance: how leaders frame, assess, respond to and monitor risk; risk appetite and risk tolerance; three levels of risk management (organization, mission or process, system); written policy with rules of behavior. | pp. 11 to 16 |
| Identify: asset inventory (kept up to date, not one time), risk assessment (4 steps), information exchange between systems, and measurement and metrics. | pp. 18 to 20 |
| Protect: zero trust architecture, awareness and training, IT contingency planning (types of plans), configuration management (baselines and change control). | pp. 21 to 25 |
| **Zero trust in the draft (Sec. 5.1):** describes ZTA as removing implicit trust, with per-request authentication and authorization, continuous checks and least privilege, and lists seven tenets in short form that match SP 800-207's tenets. It sends readers to SP 800-207 for detail. | pp. 21 to 22 |
| Continuous monitoring: a six-stage process (define, establish, implement, analyze, respond, review or update) and roles. | pp. 26 to 27 |
| Detect, respond, recover: incident response life cycle with lessons learned feeding preparation; an incident response plan (purpose, roles, incident types, communication, playbooks). | pp. 28 to 30 |
| **New versus old edition:** the change log says the revision follows the CSF 2.0 layout, reduces the focus on federal executives, adds risk management strategy and supply chain risk to governance, and adds short descriptions of the RMF, CSF 2.0, NICE and Privacy frameworks. | p. 42 |

### Useful for the paper

- A recent (October 2026) official statement that zero trust sits inside NIST's wider set of frameworks (p. 21), and that SP 800-207 remains the detailed source. This can show the paper is not relying on SP 800-207 alone, but it must be marked as a draft.
- The Section 7 incident-response ideas (pp. 28 to 30) and the asset-inventory point (p. 18) can support topic 8 at a high level.
- The "NIST frameworks" overview (pp. 4 to 10) helps explain how risk, privacy and secure development fit together in one sentence.

### Limits and cautions

- **It is a draft** (initial public draft, comments open to December 4, 2026). Wording, section numbers and page numbers can change. Re-check before submitting the paper and cite the final edition if one appears.
- It is a high-level executive summary, not a technical or testing guide. It adds little new detail on zero trust beyond pointing to SP 800-207.
- Much of it is aimed at federal agencies (laws, OMB circulars, authorizing officials), though NIST says private organizations can use it.
- The draft has visible errors (see above), so quote it only from the text I read and check the final text later.
- It does not describe any product like the proposed coordinator and says nothing about home caregiving or health data.

### Not read

- The January 2024 earlier draft of SP 800-100r1 (named in the history list). The original 2006 SP 800-100. The comment template (xlsx). Any publication cited by the draft (SP 800-37, SP 800-53, CSF 2.0 and others). The NICE Fig. 1 image.
