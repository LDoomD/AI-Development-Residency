# Notes: BLS Information Security Analysts profile and ISC2 CC exam outline

Two official sources for Topic 2 (career relevance) and Topics 1, 3, 4 and 8 of the paper. The paper discusses a proposed caregiving coordinator (a product idea, not built). Nothing here says anything is secure or compliant.

**Important correction to the task brief:** the live BLS page I saved is the **2025 to 2035** projection (page last modified August 27, 2026), not 2024 to 2034. All numbers below come from the saved 2025 to 2035 page.

---

## Source 1: U.S. Bureau of Labor Statistics, Information Security Analysts

- **Reference (APA 7):** U.S. Bureau of Labor Statistics. (2026, August 27). *Information security analysts*. In *Occupational outlook handbook*. U.S. Department of Labor. https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm (Retrieved November 18, 2026.)
- **Label / tier:** official U.S. government statistics (tier 1). A projection, not a measurement of the future.
- **Local copy:** `caregiving-coordinator/docs/sources/security-paper/bls-information-security-analysts/main.htm` (raw page, saved with curl -L, HTTP 200, 114,225 bytes) and `main.txt` (plain text I extracted from it to read).
- **How the page is built:** all nine tabs (Summary, What They Do, Work Environment, How to Become One, Pay, Job Outlook, State & Area Data, Similar Occupations, More Info) are inside this one HTML file as `tab-1` to `tab-9`. There are no separate tab URLs, so one file holds every tab. I did not make nine copies.
- **Read in full (2026-11-18):** all nine tabs, the Quick Facts box, the three bar charts' data, the projections table, and the page's glossary text at the bottom.
- **Retrieval date:** 2026-11-18. **Page "Last modified date":** August 27, 2026. The page's suggested citation says "visited October 29, 2026". I did not find out why it shows that date; it is not my retrieval date.
- **Page numbers:** none (web page). I cite the tab or heading.

### What the pages say (my words)

| Point | Tab or heading |
|---|---|
| Analysts plan and carry out security measures to protect an organization's computer networks and systems. | Summary; What They Do |
| 2025 median pay was $129,180 per year ($62.11 per hour). | Summary, Quick Facts; Pay |
| Typical entry education is a bachelor's degree. Related work experience: less than 5 years. On-the-job training: none. | Summary, Quick Facts |
| There were 192,900 jobs in 2025. | Summary, Quick Facts; Work Environment |
| Jobs are projected to grow 21 percent from 2025 to 2035 (labeled "Much faster than average"). The average for all occupations is 3 percent. | Summary; Job Outlook |
| The projected change is 40,600 more jobs, from 192,900 in 2025 to 233,400 in 2035 (SOC code 15-1212). Values are rounded to the nearest 100. | Summary; Job Outlook, projections table |
| About 14,100 openings per year are projected on average over the decade. Many come from people leaving the job for another or retiring, not only from new jobs. | Summary; Job Outlook |
| Duties include monitoring networks for breaches and investigating them, using and maintaining tools such as firewalls and data encryption programs, checking for vulnerabilities, researching security trends, writing reports on metrics, attempted attacks and breaches, developing security standards and best practices, and recommending improvements to management. | What They Do |
| Analysts help create the organization's disaster recovery plan, including regular offsite copies of data, and they keep testing the plan. | What They Do |
| Analysts must keep up with the methods attackers use and research new security technology. | What They Do |
| Largest employers by share: computer systems design and related services 22%, finance and insurance 17%, management of companies and enterprises 9%, information 9%, management, scientific, and technical consulting services 6%. Health care is not on the list shown. | Work Environment |
| Most work full time; some work more than 40 hours a week; some are on call outside normal hours for emergencies. | Work Environment; Pay |
| Most need a bachelor's degree in computer and information technology or a related field such as engineering or math. Some enter with a high school diploma plus industry training and certifications. | How to Become One, Education |
| Many analysts come from IT departments, often as network and computer systems administrators. | How to Become One, Work Experience |
| Many employers prefer candidates with a security certification. Some are entry level, some for experienced workers. | How to Become One, Licenses, Certifications |
| Analysts can advance to chief security officer or another computer and information systems manager role, lead a team, or become an expert in one area. | How to Become One, Advancement |
| Five qualities listed: analytical, communication (explain threats to technical and nontechnical people), creative, detail oriented, problem solving. | How to Become One, Important Qualities |
| May 2025 median annual wage: analysts $129,180; computer occupations $109,470; all occupations $50,980. | Pay, chart |
| Lowest 10 percent earned less than $75,090; highest 10 percent earned more than $199,850. | Pay |
| Median wage by industry, May 2025: information $138,650; computer systems design $132,410; finance and insurance $130,630; management of companies $128,950; consulting $125,420. | Pay |
| Projected growth: analysts 21%, computer occupations 6%, all occupations 3%. | Job Outlook, chart |
| Reasons given for demand: cyberattacks have become more frequent; businesses need to protect new technologies; "increased use of artificial intelligence (AI) and the rise of e-commerce" raise the need for security. | Job Outlook, Employment |
| Similar jobs with 2025 median pay: software developers, QA analysts and testers $134,040; computer network architects $134,050; database administrators and architects $126,760; computer systems analysts $105,850; web developers and digital designers $99,520; network and computer systems administrators $99,130; computer programmers $100,390. | Similar Occupations |
| State and local data live in other BLS tools (OEWS), Projections Central and CareerOneStop. The page itself holds no state numbers. | State & Area Data |
| For certification details, the page points to CareerOneStop and O*NET. | More Info |

### Useful for the paper

- **Topic 1 (intro to the field):** the one-sentence definition and the duties list in What They Do.
- **Topic 2 (career relevance):** 21 percent growth against 3 percent for all jobs, 14,100 openings a year, a $129,180 median, and the "AI use raises the need for security" line. Also: software developers are listed as a similar occupation with a $134,040 median, which supports a developer moving toward security-aware work. The page itself says certifications are preferred by many employers (links to Source 2).
- **Topic 3 (what the field covers):** monitoring, vulnerability checks, reporting, standards, disaster recovery.
- **Topic 5 (risks and challenges):** analysts may be on call after hours; attackers' methods keep changing.
- **Topic 6 (trends):** the Job Outlook reasons (more cyberattacks, new technologies, AI, e-commerce).
- **Topic 7 (best practices):** "develop security standards and best practices" and offsite backups with tested recovery plans.
- Topics 4 and 8: only thin support (firewalls and encryption programs are named; nothing on health data).

### Limits and cautions

- This is a **projection** from BLS, not a promise of jobs. It is about the whole U.S. occupation, not about the author's own chances.
- The $129,180 is a **U.S. median for people already working as analysts**, in May 2025. A new graduate or career changer should not expect it. Half of analysts earned less; the bottom 10 percent earned under $75,090.
- The pay data exclude self-employed workers (the page's Pay glossary says so).
- The page says "less than 5 years" of related experience is typical and a bachelor's is typical; it also says some people enter with a high school diploma. It does not say how many.
- The page is about "information security analysts" only. It says nothing about AI developers or caregiving products.
- The retrieved page says it was last modified August 27, 2026, but my copy shows a "visited October 29, 2026" citation date. I did not resolve why; cite the Last modified date and my retrieval date.
- Numbers could change at the next BLS update. Re-check before final submission.

### Not read

- Linked pages the tabs point to (OEWS data maps, Projections Central, CareerOneStop, O*NET, the Employment Projections skills page, the YouTube video). I read only the text of this page. The video transcript was not read.

---

## Source 2: ISC2 Certified in Cybersecurity (CC) exam outline

- **Reference (APA 7):** ISC2. (2026). *Certified in Cybersecurity (CC) certification exam outline* (effective September 1, 2026; document version v01/2026) [Exam outline]. https://www.isc2.org/certifications/cc/cc-certification-exam-outline (PDF: https://edge.sitecorecloud.io/internationf173-xmc4e73-prodbc0f-9660/media/Project/ISC2/Main/Media/documents/exam-outlines/2026/EXAMS-CC_Exam_Outline-English-Revised-01-2026-Final.pdf). (Retrieved November 18, 2026.)
- **Label / tier:** the certifying body's own official document (primary source for what the exam covers). It is a trade-body document, not a government source.
- **Local copy:** `caregiving-coordinator/docs/sources/security-paper/isc2-cc-exam-outline/CC_Exam_Outline_English_01-2026.pdf` (HTTP 200, 256,171 bytes, 8 printed pages) and `page.htm` (the web page, which links the PDF in five languages; I saved the English one).
- **Read in full (2026-11-18):** all 8 pages of the English PDF (extracted with pdftotext) and the text of the web page. The web page itself has almost no content beyond the PDF; most of its body loads by script ("Loading component...").
- **Retrieval date:** 2026-11-18. **Dates:** effective September 1, 2026; the PDF footer reads "v01/2026". The web page shows no "last modified" date.
- **Scope used:** outline only (domains, weights, task statements). I did not use fees or marketing.
- **Page numbers below are the printed numbers in the PDF.**

### What the pages say (my words)

| Point | Page |
|---|---|
| The CC certification is meant to show employers foundational knowledge for an **entry- or junior-level** cybersecurity role, plus willingness to keep learning. | p. 2 |
| Five domains are on the exam: Security Principles; Security Governance; Identity and Access Management (IAM) Concepts; Networking and Cloud Security Concepts; Security Operations and Incident Response. | p. 2 |
| No prerequisites. Basic IT knowledge is recommended. No cybersecurity work experience or degree is required. | p. 2 |
| ISC2 says CC meets ANAB accreditation under ISO/IEC 17024. (This is ISC2's own statement; I did not check it with ANAB.) | p. 2 |
| ISC2 updates the exam from a Job Task Analysis, a regular review of tasks that working security professionals do. | p. 2 |
| Exam format: 2 hours, 100 to 125 items, multiple choice and advanced item types, computerized adaptive testing, pass mark 700 out of 1000, at a Pearson VUE center. | p. 3 |
| Average weights: Security Principles 24%; Security Governance 17.3%; IAM 20%; Networking and Cloud 21.3%; Security Operations and Incident Response 17.3%. The page prints "Total: 100%" although these add to 99.9 (rounding). | p. 3 |
| Domain 1 topics: confidentiality, integrity, availability; authentication, authorization, accounting; non-repudiation; privacy; risk management lifecycle; regulations, laws, frameworks, policies; technical, administrative and physical controls; professional ethics, due care and due diligence, the ISC2 Code of Ethics. | p. 4 |
| Domain 2 topics: governance, risk and compliance; business continuity and disaster recovery; security awareness (social engineering, password protection, phishing); measuring security with metrics, key risk indicators, dashboards and reports. | p. 5 |
| Domain 3 topics: identity life cycle (define roles, provision, review, deprovision); least privilege; separation of duties; access control models. | p. 5 |
| Domain 4 topics: network basics (OSI and TCP/IP models, IPv4/IPv6, VPN, firewalls, wireless, IoT and embedded systems); network segmentation, defense in depth, zero trust; cloud characteristics, service and deployment models, and the shared security model (who is responsible for what). | p. 6 |
| Domain 5 topics: data handling (classification, labeling, masking, sanitization); encryption (symmetric, asymmetric, hashing, quantum resistant); logging and monitoring; event triage; threat actors and cyber threat intelligence; incident response plans and exercises (including tabletop); asset lifecycle, configuration and change management. | p. 7 |
| Domain 5.5, security testing: readiness testing (blue, purple, red team); application testing (vulnerability scanning, static analysis, dynamic analysis, threat modeling); physical penetration testing (phishing, tailgating, impersonation). | p. 7 |
| Supplementary references and exam policies are pointed to on other ISC2 pages. | p. 8 |

### Useful for the paper

- **Topic 1 and 3 (what the field covers):** the five domains are a clean official map of the basics: principles, governance, access, networks and cloud, operations and incident response.
- **Topic 2 (career relevance):** an entry-level, no-experience-required certification, which matches BLS's note that many employers prefer certified candidates. It is a possible first step for someone moving from AI development toward security work. It does not by itself say anyone will be hired.
- **Topic 4 (methods and tools):** Domain 5.5 (vulnerability scanning, static and dynamic analysis, threat modeling, red and blue team) and Domain 5.2 (logging, triage).
- **Topic 5 (risks):** threat actors, social engineering, phishing, end-of-life software.
- **Topic 7 (best practices):** least privilege, separation of duties, defense in depth, zero trust, deprovisioning access, data classification, incident response exercises.
- **Topic 8 (application to a proposed coordinator):** identity life cycle, least privilege and deprovisioning map to a product where several family members share access to one person's care information; data classification, masking and encryption map to health data. These are ideas to discuss, not evidence that the proposed product has any of these controls.

### Limits and cautions

- The outline lists **topics, not depth**. It does not tell how hard the exam is or what a candidate must be able to do on the job.
- It does not mention AI, machine learning or health data. Do not claim it covers them.
- This is the certifying body's own document. ISC2 sells the exam, so this is not an independent view of the profession.
- Effective date is September 1, 2026; if the paper is graded after a newer outline is posted, re-check.
- Passing CC would show entry-level knowledge only (ISC2's words, p. 2).
- Weights are "average" weights under adaptive testing, so a real exam may differ.

### Not read

- The supplementary references list, the exam policies page, the CAT explanation page, and the four other-language PDFs (Chinese, German, Japanese, Spanish). I saved only the English PDF. Fees and marketing pages were left out on purpose.
