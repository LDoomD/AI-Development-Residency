# Notes: NIST SP 800-218, Secure Software Development Framework (SSDF) Version 1.1

- **Source:** Souppaya, M., Scarfone, K., & Dodson, D. (2022). *Secure software development framework (SSDF) version 1.1: Recommendations for mitigating the risk of software vulnerabilities* (NIST Special Publication 800-218). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-218
- **Label for the paper:** official government standard (tier 1 in the source list).
- **Local copy:** `caregiving-coordinator/docs/sources/security-paper/nist-ssdf-800-218/NIST.SP.800-218.pdf` (36 PDF pages) and NIST's status page `caregiving-coordinator/docs/sources/security-paper/nist-ssdf-800-218/status.html`.
- **Page numbers below are the printed page numbers.** The front pages are numbered with Roman numerals (ii to vii). Body pages start at printed page 1, which is PDF page 10, so PDF page = printed page + 9.
- **Read in full (2026-11-18):** the front matter, the executive summary, sections 1 and 2, the practice and task columns of Table 1 (printed pp. 5 to 19), the references list headings, Appendix A (the Executive Order 14028 table, p. 24), the acronyms and the change log (p. 27). In Table 1 I read each practice, task and the lead "notional implementation examples". I did not read every reference code in the right-hand column (for example the BSIMM, BSAFSS and IEC 62443 code lists).
- **Currency check (2026-11-18):** NIST's page lists the final of 02/03/22 and a draft of 09/30/21, and no newer edition. It shows "Potential updates" and a related part, SP 800-218A. SP 800-218A is a separate publication and is not read.

## What the pages say (my words)

| Point | Page |
|---|---|
| Few software development models explain security in detail, so secure practices have to be added to whichever model a team uses (waterfall, agile, DevOps). | p. 1 |
| Vulnerabilities are not only coding bugs. NIST also counts weak configuration settings, wrong trust assumptions and out-of-date risk analysis. | p. 1 |
| "Shifting left": the earlier in development security is handled, the less effort and cost it takes, and the less technical debt builds up. | p. 1 |
| The SSDF adds no new practices. It collects high-level practices from existing standards and describes outcomes, not tools. | pp. 1 to 2 |
| The SSDF is for software makers of any size and for software buyers. It can fit any sector or technology. | pp. vi, 2 |
| NIST says the SSDF practices may help support the Cybersecurity Framework but do not map to it. The practices are usually done by different people. | p. 2 (footnote 2) |
| The practices are "not prioritized". NIST says the aim is not a checklist but a base for a risk-based plan. Which practices apply, and how far, depends on risk, cost, feasibility and applicability. | p. 3 |
| When software is delivered as a service (infrastructure, platform or software as a service), NIST says responsibility likely follows a shared responsibility model. The customer should agree with the provider in writing on who is responsible for each practice and how the provider will show it. | p. 3 |
| The four groups: Prepare the Organization (PO), Protect the Software (PS), Produce Well-Secured Software (PW), Respond to Vulnerabilities (RV). | p. 4 |
| Each practice has tasks, optional notional implementation examples, and references. No example is required. | p. 4 |
| **PO** has five practices: define security requirements (PO.1), implement roles and responsibilities (PO.2), implement supporting toolchains (PO.3), define and use criteria for software security checks (PO.4), and implement and maintain secure environments for development (PO.5). | pp. 5 to 9 |
| PO.5.1 says to separate and protect each development environment. NIST's examples include multi-factor, risk-based authentication for each environment and separating environments from production. | p. 8 to 9 |
| **PS** has three practices: protect all forms of code from unauthorized access and tampering (PS.1), provide a way to verify software release integrity (PS.2), and archive and protect each software release (PS.3). PS.1.1 says to restrict access to code by least privilege and to track every change with version control. | pp. 9 to 10 |
| **PW** covers design (PW.1 risk modeling such as threat modeling, PW.2 design review), reusing well-secured software (PW.4), secure coding (PW.5), build tools (PW.6), code review (PW.7), executable-code testing (PW.8) and secure default settings (PW.9). PW.1.1 names threat modeling, attack modeling and attack surface mapping. PW.5.1 includes validating all inputs and properly encoding all outputs as an example. | pp. 11 to 16 |
| PW.4.4 asks teams to verify that bought, open-source and other third-party components meet the organization's requirements through their life. Example: check regularly for publicly known vulnerabilities in the components, and build automatic detection into the toolchain. | p. 13 |
| PW.9.1 says to define a secure baseline so the default settings are secure and do not weaken what the platform provides. | p. 16 |
| **RV** has three practices: identify and confirm vulnerabilities on an ongoing basis (RV.1), assess, prioritize and remediate (RV.2) and analyze root causes (RV.3). RV.1.3 asks for a policy on vulnerability disclosure and response. Example: a disclosure program that makes it easy for researchers to report. | pp. 16 to 18 |
| PW.3, PW.4.3 and PW.5.2 were retired and merged into other tasks, so some identifiers are not used. | pp. 12, 27 |
| The framework was a response to Executive Order 14028 (May 12, 2021) on software supply chain security. Appendix A maps its Section 4e to SSDF tasks. | p. 24 |
| A June 2021 NIST workshop produced more than 150 position papers. The final version was published February 2022; the original white paper was April 2020. | pp. iii, 27 |

## Possible use in the paper
- **Topic 4 (how it works when building products):** the four groups as the frame for "security inside the build process"; shifting left; vulnerability handling and disclosure; protecting source code; checking third-party packages (PW.4.4).
- **Topic 7 (tools and skills):** PW.4.4 supports dependency checking (`npm audit`) and PS.1.1 supports repository access rules.
- **Topic 8:** which SSDF tasks the proposed coordinator would plan to follow (threat modeling PW.1.1, least privilege on code PS.1.1, third-party component checks PW.4.4, secure defaults PW.9.1, a plan for vulnerability reports RV.1.3).

## Limits
- The SSDF is written for software producers and federal buyers. NIST says it gives outcomes, not methods (p. 1 to 2), and that practices are not prioritized (p. 3). It does not say the proposed coordinator is secure and it cannot be used to claim compliance.
- NIST's "shared responsibility" language on p. 3 is general. It does not describe the Vercel or Supabase agreements. Those are covered by their own documents.
- The right-hand reference codes were not read in detail.
- The edition is from 2022. A newer draft is not shown on NIST's page as of 2026-11-18.
