# Advanced Information Security: A Research Paper

**Status: Proposed draft. The owner has not approved it as a whole.** Topic 1 was approved by the owner on 2026-11-18 (the version with the title and the reader's note). Topic 2 is the owner's own words with citations added by Claude. Topics 3 to 8 are first drafts for the owner to read and change.

**Every claim comes from a saved notes file** in `caregiving-coordinator/docs/sources/security-paper/notes/`. Helper agents wrote most of those notes. They were spot-checked, not verified line by line. Page numbers are the printed page numbers in each source. Web pages have no page numbers, so they are cited by heading.

---

## 1. Introduction: Core Ideas of Information Security (Foundations, Not Current Threats)

*What you are reading: this section explains basic definitions and one framework for organizing security work. The definitions come from 1975 and 2017 sources, so the section is partly history. The framework is NIST's 2024 edition, which was the newest on NIST's page on November 18, 2026. Current attacks and the newest practices are in topics 3 to 8.*

Information security is the work of protecting information and the systems that hold it from unauthorized access, use, disclosure, disruption, modification or destruction. The goal is to keep information confidential, correct and available (Nieles et al., 2017, p. 2). Confidentiality means limiting who can see information. Integrity means guarding against improper change. Availability means people can reach information when they need it (Nieles et al., 2017, pp. 2–3). Saltzer and Schroeder (1975) named the same three failures in 1975: unauthorized release of information, unauthorized change, and unauthorized denial of use (Sec. I-A1). They also warned that the hardest case is an intruder who is otherwise a legitimate user (Sec. I-A1).

Security is not a goal by itself. NIST calls it a means to an end, and says risk can never be removed completely. Protections that are too heavy waste resources and make systems hard to use, and protections that are too light leave a system open (Nieles et al., 2017, pp. 7–8). The same document says it costs far more to add security later than to include it from the start (Nieles et al., 2017, p. 69).

The NIST Cybersecurity Framework 2.0 describes a security program through six functions: Govern, Identify, Protect, Detect, Respond and Recover (National Institute of Standards and Technology [NIST], 2024, pp. 3–5). Govern is new in version 2.0 and informs the other five. The functions are worked on at the same time, not in order (NIST, 2024, p. 5). The framework lists outcomes to reach and does not say how to reach them (NIST, 2024, p. 1).

The rest of this paper uses these ideas as a base. It follows the proposed caregiving coordinator, a product idea that has not been built. It would hold health and money notes about another adult, so it must plan for these risks. This paper does not claim that the idea is secure.

---

## 2. Why Information Security Matters for My Career

**The owner's words, unedited (written in chat on 2026-11-18):**

> This is relevant to my career because I am now learning about AI development and want to make this part of my skill set now, so I'll be doing what they call product engineering along with product design UXUI. AI development or in product engineering is the new skill for UX designers, and I want to get a job in that as well. ... Why it's valuable to me in my careers because I have to learn how to secure things as I'm using AI to develop.

**Citations added by Claude (Proposed; the owner edits or removes any of this):**

Three official sources support the point that developers need security skills. The U.S. Bureau of Labor Statistics (BLS, 2026) projects that jobs for information security analysts will grow 21 percent from 2025 to 2035, against 3 percent for all occupations, with about 14,100 openings a year ("Summary"; "Job Outlook"). The median pay in May 2025 was $129,180 ("Pay"). That figure is for people already working as analysts, and BLS calls the growth a projection. BLS also lists software developers as a similar occupation ("Similar Occupations").

NIST's workforce framework treats a software developer as part of a secure software development team, beside a security architect (Petersen et al., 2020, p. 12). It also says the cybersecurity workforce is not only people who work fully inside security (Petersen et al., 2020, p. vi).

The ISC2 (2025) workforce study is a survey of 16,029 people, and it gives no workforce size or gap number (p. 3). It reports that 59% of respondents have a critical or significant skills need (p. 11). The most named needs were AI (41%), cloud security (36%), risk assessment (29%) and application security (28%) (pp. 11, 13). ISC2 sells security certifications, so this is not an independent view of the field.

---

## 3. Background: How the Field Got Here and What the Data Says

Web security has a community history. The OWASP project launched on December 1, 2001, and became a U.S. nonprofit in 2004 (OWASP Foundation, n.d.-a, "The OWASP Foundation"). OWASP now publishes the Top 10, a list of the main web application risks. The 2025 edition is the eighth, and OWASP calls it an awareness document, not a complete list (OWASP Foundation, 2025, "Introduction"). Its ten categories are broken access control, security misconfiguration, software supply chain failures, cryptographic failures, injection, insecure design, authentication failures, software or data integrity failures, security logging and alerting failures, and mishandling of exceptional conditions (OWASP Foundation, 2025, "Introduction"). OWASP says all applications it tested had some form of broken access control ("A01:2025 Broken Access Control," "Background").

Two industry reports give numbers on how breaches happen and what they cost. Both are company research, not government data, and both state limits. IBM's 2026 report found a global average breach cost of USD 4.99 million. Healthcare was the costliest industry for the 13th year in a row at USD 6.64 million (IBM, 2026, pp. 6, 14). IBM says phishing was the top attack vector for the fourth year in a row, followed by supply chain compromise (p. 22). IBM also says its sample is not statistical and leans toward organizations with more mature security programs (p. 70).

Verizon's 2026 report covers more than 22,000 confirmed breaches (Verizon, 2026, p. 5). It says that exploiting vulnerabilities was the most common way in at 31%, up from 20% (pp. 10, 15–16). Breaches involving a third party reached 48%, up from 30% (p. 11). Verizon also warns that its percentages are shares of detected and reported breaches, not the chance that any one organization is breached (p. 114).

These sources point to the same lesson. Breaches mostly start with ordinary weaknesses: access that is not checked well, software that is not patched, and trust placed in outside parties. Newer attack waves target the tools developers use. Verizon's year in review lists a self-copying npm package worm in September 2025 that compromised more than 500 packages (Verizon, 2026, pp. 108–109). OWASP lists the same worm as an example of software supply chain failure (OWASP Foundation, 2025, "A03:2025 Software Supply Chain Failures").

---

## 4. How Security Works When Building Products

The main idea is that security belongs inside the build process, not at the end. NIST's Secure Software Development Framework says that few development models explain security, so secure practices must be added to whichever model a team uses (Souppaya et al., 2022, p. 1). It describes "shifting left": the earlier a team handles security, the less effort and cost it takes (p. 1). Its four groups are preparing the organization, protecting the software, producing well-secured software, and responding to vulnerabilities (p. 4). NIST says these practices are not a checklist and are not ranked. A team picks them by risk, cost and feasibility (p. 3).

U.S. and partner agencies make the same point about defaults. Their Secure by Design guide says makers should move the security burden from customers to the product, and that security cannot be "bolted on" later (Cybersecurity and Infrastructure Security Agency [CISA] et al., 2023, pp. 4, 8). "Secure by default" means a product is safe to use with little or no change by the customer (pp. 5, 9). OWASP's Proactive Controls say the same in developer terms: deny access by default, and start software in its most secure state (OWASP Foundation, 2024, "C1: Implement Access Control"; "C5: Secure By Default Configurations"). The OWASP Top 10 adds that a perfect implementation cannot fix a design that lacks needed controls ("A06:2025 Insecure Design").

Choices about people and identity also follow risk. NIST's digital identity guidelines promote a risk-based approach instead of a compliance-only approach (Temoshok et al., 2025b, p. 1). They set out a five-step process: define the service, assess impact, select assurance levels, tailor and document, and keep evaluating (pp. 22–24).

Two details matter for teams that build with AI coding tools. The OWASP Top 10 lists "Inappropriate Trust in AI Generated Code" as a next step. It says AI-generated code often has more vulnerabilities, and that a person should be able to read and understand every line they commit ("Next Steps," X03). IBM found that a DevSecOps approach, identity and access management and a managed security service lowered breach cost the most (IBM, 2026, pp. 50–51).

---

## 5. What Information Security Includes

NIST's CSF 2.0 gives the broadest map: Govern, Identify, Protect, Detect, Respond and Recover (NIST, 2024, pp. 3–5). It says the Core applies to all technology an organization uses, including cloud, mobile and AI systems (NIST, 2024, p. 5). A more detailed list comes from NIST's introduction to information security, which names 20 control families such as Access Control, Audit and Accountability, Identification and Authentication, and Incident Response (Nieles et al., 2017, pp. 59–70). For web applications, the OWASP Top 10 categories in topic 3 are the most-used list of risks.

Four areas matter most for a product that holds personal data.

**Access control.** OWASP says access control works only in trusted server-side code, should deny by default, and should enforce record ownership ("A01:2025 Broken Access Control," "How to prevent").

**Identity and sign-in.** NIST's identity guidelines define three assurance levels: for proving who someone is, for authenticating them, and for federation (Temoshok et al., 2025b, p. 3). NIST's authentication volume says a password used alone must be at least 15 characters, and one used as part of multi-factor sign-in at least 8. It also says sign-in services must not force people to change passwords on a schedule (Temoshok et al., 2025a, p. 14). NIST does not call 15 characters "safe"; it is a requirement of that document.

**Zero trust.** NIST describes zero trust as deciding each access request on its own, with least privilege, as if the network is already compromised (Rose et al., 2020, p. 4). That document is from 2020. NIST says its tenets apply to work inside organizations and do not apply to anonymous public use. For registered consumer users, only some policies may be possible (p. 7).

**Logging and recovery.** OWASP says to keep an audit trail with integrity controls, to log failures, and not to log sensitive data such as PII or PHI ("A09:2025 Security Logging and Alerting Failures"). NIST's incident response profile says backups should be created, protected, maintained and tested (Nelson et al., 2025, p. 22).

---

## 6. What Teams Do: Activities Security Work Involves

Teams do four kinds of work.

**They model threats.** The Threat Modeling Manifesto says a threat model asks four questions: what are we working on, what can go wrong, what are we going to do about it, and did we do a good enough job (Braiterman et al., 2020, "What is threat modeling?"). OWASP's cheat sheet describes four steps: draw the system, identify and rank threats, decide mitigations, and review. It names STRIDE (spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege) as one technique, and it says there is no universally accepted industry standard for the process (OWASP Foundation, n.d.-b, "Threat Identification"; "Addressing Each Question").

**They test.** OWASP's Web Security Testing Guide, version 4.2 from 2020, is the newest released version, and version 5.0 is not released. Its foreword says that testing alone cannot prove an application is secure, because there are endless ways to break one and no one has time to test them all (OWASP Foundation, 2020, "Foreword"). It also says automated tools find generic problems and that each finding still takes human time to check ("Foreword"). The testing tool ZAP, which is now maintained as "ZAP by Checkmarx," separates passive scanning, which only watches traffic, from active scanning, which uses known attacks and can put the target at risk (ZAP Dev Team, 2026, "Getting Started").

**They manage vulnerabilities.** A team has to decide which flaws to fix first. FIRST's scoring guide says a CVSS Base score measures severity, not risk, and should not be used alone to assess risk (Forum of Incident Response and Security Teams [FIRST], 2025, "CVSS Base Score (CVSS-B) Measures Severity, not Risk"). CISA keeps a catalog of vulnerabilities known to be exploited in real attacks and tells organizations to use it as an input to patch priority (CISA, 2026a, catalog page). Verizon found that only 26% of the vulnerabilities on that catalog were fully fixed in 2025, and the median time to fix was 43 days (Verizon, 2026, pp. 10, 17–18). Verizon says picking what to patch first is the key strategy (p. 18).

**They respond to incidents.** NIST says "another incident is inevitable" and that response belongs across the whole organization, using all six CSF functions (Nelson et al., 2025, p. 1). The 2025 edition no longer gives step-by-step procedures, because the details of response change so often (p. 3). It does say notification duties are part of response, and that laws on incident notice are evolving (pp. 30–31). NIST's older testing guide from 2008 is still the newest on NIST's page, but it is dated, so this paper uses it only for the general idea of plan, run and report (Scarfone et al., 2008).

---

## 7. Tools and Skills to Learn

**Tools for a project on GitHub and npm.** GitHub secret scanning searches the whole Git history on every branch for hardcoded credentials. GitHub says to replace (rotate) a leaked credential right away, because removing it from history is slow (GitHub, 2026a, "How secret scanning protects your code"; "Secret scanning alerts and remediation"). Dependabot alerts tell a team when a package it uses has a known weakness. GitHub states that these alerts cannot catch every issue (GitHub, 2026b, "Limitations"). The `npm audit` command checks dependencies the same way. npm's own page says "no vulnerabilities found" only means no known ones (npm, Inc., 2023, "No security vulnerabilities found"). Some GitHub features need paid plans for private repositories, so the plan choice matters (GitHub, 2026c, "About GitHub's security features"). All of these are vendor descriptions of their own tools, not tests of how well they work.

**Know who is responsible for what.** Vercel says the customer handles their data, their application and user access, while Vercel manages the infrastructure (Vercel, 2026b, "Shared Responsibility Model"). Supabase says the customer owns table access for sensitive data and the safe storage of keys (Supabase, 2026b, "You share the security responsibility").

**Skills.** ISC2's survey of 16,029 security professionals found the most-named skills needs were AI (41%), cloud security (36%), risk assessment (29%) and application security (28%) (ISC2, 2025, pp. 11, 13). When hiring managers ranked all skills together, their top five were all nontechnical: problem solving, collaboration, communication, willingness to learn and strategic thinking (pp. 18–20). Fifty-six percent of respondents entered security through IT (pp. 21–22). ISC2's entry-level Certified in Cybersecurity exam requires no work experience or degree and covers five domains, from security principles to incident response (ISC2, 2026, pp. 2–3).

---

## 8. The Proposed Caregiving Coordinator

The proposed caregiving coordinator is a product idea that has not been built. It would be a web product that family caregivers sign up for themselves, built with Next.js, hosted on Vercel, with a Supabase database. It would hold health and behavior notes about a parent or partner, money and coverage details, family member accounts and permissions, and consent records (`caregiving-coordinator/docs/risk-profile.md`, "Product facts" and "Data this product holds in MVP #1"). The research above leads to the plans below. They are plans, not features that exist. Nothing here shows the idea is secure or compliant.

**Plan 1: turn on row-level security for every table.** Supabase says the customer is responsible for table access and recommends always applying row-level security (Supabase, 2026b, "You share the security responsibility"). Its guide says a table without it can be read and written by any role with a grant (Supabase, 2026a, "Intro"). In September 2026, UpGuard reported 16,326 Supabase databases exposing readable tables and blamed configuration mistakes, not a Supabase flaw (Pollock, 2026, "A City and Its Mirror"; "Background"). That number is a count, not a rate. It is vendor research, and UpGuard sells exposure scanning. The study found 558 medical and health sites (Pollock, 2026, "Exposure by industry").

**Plan 2: check access where the data is read, not only in the web layer.** A 2025 advisory showed that Next.js access checks placed only in middleware could be skipped (Vercel, 2025). Several more advisories in 2026 showed other request paths that skip middleware or proxy checks (Vercel, 2026a). The Next.js documentation says its proxy "should not be your only line of defense" (Next.js, 2026, "Optimistic checks with Proxy"). Vercel's May 2026 notice says patching is the only complete fix and the issues cannot be reliably blocked at its firewall (Lai, 2026, "Resolution"). So the idea would check membership in a care circle in the server code that reads the data, and use the database rule as a second check. This paper does not say hosting on Vercel protects the idea.

**Plan 3: keep packages and keys under control.** The supply chain attacks in topic 3 reached developers' machines and tokens. CISA's 2026 guidance says to keep a list of all open source software in use, and to run secret scanning and dependency scans automatically (CISA, 2026b, pp. 8, 16). The idea would lock package versions, run dependency audits, and keep secret keys on the server only.

**Plan 4: do not put health data in logs, and record who looked at it.** OWASP says not to log PII or PHI and to keep audit trails with integrity controls such as append-only tables ("A09:2025 Security Logging and Alerting Failures").

**Plan 5: define who is affected before building sign-in.** NIST's guidelines separate user groups, who log in, from impacted entities, everyone who could be harmed, including people who never use the system (Temoshok et al., 2025b, pp. 26–27). In this idea, the person being cared for may never log in but would be affected most.

**Plan 6: write a breach plan before real data is stored.** The FTC says that sharing health information without a person's authorization counts as a breach under its Health Breach Notification Rule. Notice goes to each affected person without unreasonable delay and within 60 calendar days of discovery (Federal Trade Commission, 2024, "What triggers the notification requirement"; "What to do if a breach occurs"). Whether this rule or HIPAA covers the idea is an open question. The risk profile says a lawyer must answer it before launch (`caregiving-coordinator/docs/risk-profile.md`, "Open questions"). Vercel offers a HIPAA agreement to eligible customers, but its page does not say a customer's product becomes compliant by using Vercel (Vercel, 2026b, "Security & Compliance Measures").

**Limits of this paper.** Most data comes from vendor reports and vendor documents. Verizon's and IBM's samples are not random. The HHS and FTC pages could not be rechecked on the day of writing. Older sources (1975, 2008, 2017 and 2020) are used for ideas and are labeled with their year. The paper cannot show that any design is secure.

---

## References

Braiterman, Z., Shostack, A., Marcil, J., de Vries, S., Michlin, I., Wuyts, K., Hurlbut, R., Schoenfield, B. S. E., Scott, F., Coles, M., Romeo, C., Miller, A., Tarandach, I., Douglen, A., & French, M. (2020). *Threat modeling manifesto*. https://threatmodelingmanifesto.org/

Cybersecurity and Infrastructure Security Agency. (2026a). *Known exploited vulnerabilities catalog* [Data set]. U.S. Department of Homeland Security. https://www.cisa.gov/known-exploited-vulnerabilities-catalog

Cybersecurity and Infrastructure Security Agency. (2026b, July 30). *Open source software: Security principles and practices*. U.S. Department of Homeland Security. https://www.cisa.gov/resources-tools/resources/open-source-software-security-principles-and-practices

Cybersecurity and Infrastructure Security Agency, National Security Agency, Federal Bureau of Investigation, & international partners. (2023). *Shifting the balance of cybersecurity risk: Principles and approaches for secure by design software*. Cybersecurity and Infrastructure Security Agency. https://www.cisa.gov/resources-tools/resources/secure-by-design

Federal Trade Commission. (2024, July). *Complying with FTC's Health Breach Notification Rule*. https://www.ftc.gov/business-guidance/resources/complying-ftcs-health-breach-notification-rule-0

Forum of Incident Response and Security Teams. (2025, November 14). *Common Vulnerability Scoring System version 4.0: User guide* (Version 1.2). https://www.first.org/cvss/v4-0/user-guide

GitHub. (2026a). *Secret scanning*. GitHub Docs. Retrieved November 18, 2026, from https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning

GitHub. (2026b). *Dependabot alerts*. GitHub Docs. Retrieved November 18, 2026, from https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-alerts

GitHub. (2026c). *GitHub security features*. GitHub Docs. Retrieved November 18, 2026, from https://docs.github.com/en/code-security/getting-started/github-security-features

IBM. (2026). *Cost of a data breach report 2026: The AI tipping point*. IBM Corporation. https://www.ibm.com/reports/data-breach

ISC2. (2025, December 4). *2025 ISC2 cybersecurity workforce study*. ISC2, Inc. https://www.isc2.org/insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study

ISC2. (2026). *Certified in Cybersecurity (CC) certification exam outline* (Effective September 1, 2026) [Exam outline]. https://www.isc2.org/certifications/cc/cc-certification-exam-outline

Lai, J. (2026, May 7). *Next.js May 2026 security release*. Vercel changelog. https://vercel.com/changelog/next-js-may-2026-security-release

National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST Cybersecurity White Paper 29). https://doi.org/10.6028/NIST.CSWP.29

Nelson, A., Rekhi, S., Souppaya, M., & Scarfone, K. (2025). *Incident response recommendations and considerations for cybersecurity risk management: A CSF 2.0 community profile* (NIST Special Publication 800-61 Rev. 3). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-61r3

Next.js. (2026, September 16). *Authentication*. Next.js documentation. https://nextjs.org/docs/app/guides/authentication

Nieles, M., Dempsey, K., & Pillitteri, V. Y. (2017). *An introduction to information security* (NIST Special Publication 800-12 Rev. 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-12r1

npm, Inc. (2023). *Auditing package dependencies for security vulnerabilities*. npm Docs. Retrieved November 18, 2026, from https://docs.npmjs.com/auditing-package-dependencies-for-security-vulnerabilities/

OWASP Foundation. (n.d.-a). *About OWASP Foundation*. Retrieved November 18, 2026, from https://owasp.org/about/

OWASP Foundation. (n.d.-b). *Threat modeling cheat sheet*. Retrieved November 18, 2026, from https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html

OWASP Foundation. (2020). *Web security testing guide* (Version 4.2). https://github.com/OWASP/wstg/tree/v4.2

OWASP Foundation. (2024). *OWASP top 10 proactive controls 2024*. https://top10proactive.owasp.org/archive/2024/the-top-10/

OWASP Foundation. (2025). *OWASP Top 10:2025*. https://owasp.org/Top10/2025/

Petersen, R., Santos, D., Smith, M. C., Wetzel, K. A., & Witte, G. (2020). *Workforce framework for cybersecurity (NICE Framework)* (NIST Special Publication 800-181 Rev. 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-181r1

Pollock, G. (2026, September 23). *Everything everywhere: Systemic data exposure in Supabase apps*. UpGuard. https://www.upguard.com/blog/everything-everywhere-systemic-data-exposure-in-supabase-apps

Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST Special Publication 800-207). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-207

Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*. https://web.mit.edu/Saltzer/www/publications/protection/ **[Volume, issue and page range still to confirm on IEEE's page.]**

Scarfone, K., Souppaya, M., Cody, A., & Orebaugh, A. (2008). *Technical guide to information security testing and assessment* (NIST Special Publication 800-115). National Institute of Standards and Technology. https://csrc.nist.gov/pubs/sp/800/115/final

Souppaya, M., Scarfone, K., & Dodson, D. (2022). *Secure software development framework (SSDF) version 1.1: Recommendations for mitigating the risk of software vulnerabilities* (NIST Special Publication 800-218). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-218

Supabase. (2026a, November 3). *Row level security*. Supabase Docs. https://supabase.com/docs/guides/database/postgres/row-level-security

Supabase. (2026b, October 6). *Shared responsibility model*. Supabase Docs. https://supabase.com/docs/guides/deployment/shared-responsibility-model

Temoshok, D., Fenton, J. L., Choong, Y. Y., Lefkovitz, N., Regenscheid, A., Galluzzo, R., & Richer, J. P. (2025a). *Digital identity guidelines: Authentication and authenticator management* (NIST Special Publication 800-63B-4). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-63B-4

Temoshok, D., Galluzzo, R., LaSalle, C., Lefkovitz, N., Regenscheid, A., Choong, Y. Y., Proud-Madruga, D., & Gupta, S. (2025b). *Digital identity guidelines* (NIST Special Publication 800-63-4). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-63-4

U.S. Bureau of Labor Statistics. (2026, August 27). *Information security analysts*. In *Occupational outlook handbook*. U.S. Department of Labor. Retrieved November 18, 2026, from https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm

Vercel. (2025, March 21). *Authorization bypass in Next.js middleware* (GHSA-f82v-jwr5-mffw; CVE-2025-29927) [Security advisory]. GitHub. https://github.com/vercel/next.js/security/advisories/GHSA-f82v-jwr5-mffw

Vercel. (2026a, May 6). *Middleware / Proxy bypass advisories* (GHSA-36qx-fr4f-26g5, GHSA-492v-c6pp-mqqv, GHSA-267c-6grr-h53f, GHSA-26hh-7cqf-hhc6, GHSA-6gpp-xcg3-4w24) [Security advisories]. GitHub. https://github.com/vercel/next.js/security/advisories

Vercel. (2026b, August 11). *Vercel documentation: Shared responsibility model; Security and compliance measures*. Retrieved November 18, 2026, from https://vercel.com/docs/security/shared-responsibility

Verizon. (2026). *2026 data breach investigations report*. Verizon Business. https://www.verizon.com/business/resources/reports/dbir/

ZAP Dev Team. (2026). *ZAP* [Software documentation]. ZAP by Checkmarx. Retrieved November 18, 2026, from https://www.zaproxy.org/

---

## Check list for the owner (not part of the paper)
- **Verizon rule:** Verizon allows exact numbers with citation and says paraphrasing "requires review." This draft uses exact numbers with plain descriptions. The owner decides whether to contact Verizon.
- **To fix before submission:** the Saltzer and Schroeder volume and pages; the 2026a/2026b/n.d. letters in the reference list were checked by eye only; the Vercel (2026a) entry groups four advisories and should be split into four entries.
- **Not checked:** each claim was matched to its notes file, not to the original source. The final Vercel page cited in topic 8 ("Security & Compliance Measures") is one of the 21 pages read; the reference list gives only the first page's address.
