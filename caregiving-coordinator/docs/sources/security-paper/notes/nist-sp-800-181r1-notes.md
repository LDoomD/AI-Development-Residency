# Notes: NIST SP 800-181 Rev. 1, Workforce Framework for Cybersecurity (NICE Framework)

- **Source:** Petersen, R., Santos, D., Smith, M. C., Wetzel, K. A., & Witte, G. (2020). *Workforce framework for cybersecurity (NICE Framework)* (NIST Special Publication 800-181 Rev. 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-181r1 (PDF cover gives November 2020, 27 pages.)
- **Label for the paper:** official government guidance (tier 1). It is the **2020 edition**, and its own text says the lists of tasks, knowledge, skills and work roles were taken out of the document and are kept elsewhere (see "Limits").
- **Local copy:** `caregiving-coordinator/docs/sources/security-paper/nist-sp-800-181r1/NIST.SP.800-181r1.pdf` (27 PDF pages), `text.txt` (pdftotext -layout), and `status.html` (NIST status page saved 2026-11-18).
- **Page numbers below are printed page numbers.** Front matter uses Roman numerals (ii to vii), the body uses 1 to 18. Offset: PDF page = printed page + 9 (printed 18 is PDF page 27; printed vii is PDF page 9). Cover, title and copyright pages are unnumbered.
- **NIST status page says (checked 2026-11-18):** Date Published November 2020; Supersedes SP 800-181 (08/07/2017); document history shows the draft on 07/15/20 and the final on 11/16/20. It shows **no "superseded by" and no Rev. 2**. It carries a Planning Note dated 06/26/2025 saying the NICE Framework Components (the data elements: Task, Knowledge and Skill statements, Work Roles and Work Role Categories, and Competency Areas) are on the "Current Versions" page of the NICE Framework Resource Center, and to use that page for up-to-date information. So the components are kept as a separate, updated data set, and this PDF is not the current list.
- **Read in full (2026-11-18):** all 27 PDF pages as text: cover, title and copyright pages, abstract (ii), patent and conventions (iii), acknowledgments (iv), Note to Readers (v), Executive Summary (vi), table of contents (vii), Sections 1 to 4 (1 to 15), References (16), Acronyms (17), Glossary (18), and Tables 1 to 4. There are no appendices listing tasks, knowledge, skills or roles in this edition, so there were no large tables to count.

## What the pages say (my words)

| Point | Page |
|---|---|
| The NICE Framework is a common language for describing cybersecurity work and the people who do it. It is meant for hiring, training, development and keeping staff. | p. vi |
| The paper calls people who do cybersecurity work "Learners" (students, job seekers, employees). It says "cybersecurity workforce" does not mean only people fully inside the security field. | pp. iii, vi |
| The 2020 edition simplified the old structure. The older Categories (such as "securely provision") and Specialty Areas were deprecated. Organizations that like them may keep using them. | p. v |
| The "building blocks" are Task, Knowledge and Skill (TKS) statements. The old Ability statements were folded into Skill statements. | p. v |
| The lists of tasks, knowledge, skills and work roles from the 2017 edition were removed from this document. They are to be kept as separate items with version control. Until updated, the old lists stay in the NICE Framework Resource Center. | p. v |
| The framework describes two things: "the work" (what an organization must do to manage cybersecurity risk) and "the learner" (the person with knowledge and skills). Tasks describe the work; Knowledge and Skills describe the learner. | pp. 1-2 |
| Four attributes: agility, flexibility, interoperability, modularity. Modularity means the same blocks can describe other workforces, and the text names privacy, risk management and software engineering/development. | pp. 2-3 |
| The framework helps organizations manage cybersecurity risk by giving them a way to talk about the work and the people. These risks feed enterprise risk decisions (it cites NIST IR 8286). | p. 3 |
| Intended readers: public agencies, private and not-for-profit organizations, schools and trainers, credential providers, HR staff, hiring managers, recruiters and learners. | p. 3 |
| A Task is an activity aimed at reaching an organization's goals. A Task statement starts with the action and leaves out the goal. Example given: "Troubleshoot system hardware and software." | p. 4 |
| Knowledge is "a retrievable set of concepts within memory." It can be basic or specific. One task may need several knowledge statements, and one statement can serve many tasks. | p. 5 |
| A Skill is the ability to do something you can observe. It can be simple (recognize alerts from an intrusion detection system) or complex. Skill and Task wording should stay separate so skills can be assessed. | p. 5 |
| Organizations can tailor the blocks to their own setting and are warned not to rewrite existing statements, because that breaks matching with outside sources. They should write a new statement instead. | pp. 6-7 |
| Example uses of TKS: tracking employee skills for promotion, listing required knowledge for a course, making a weekly task list. | p. 6 |
| A Competency is "a mechanism for organizations to assess learners." It has a name, a description, an assessment method and a group of TKS statements. Assessment can be an interview, a test, a lab demonstration, or work observation. | pp. 7-8 |
| Two worked Data Analysis competency examples (Tables 1 and 2) use 2017 task, knowledge and skill IDs. | pp. 9-10 |
| A Work Role is a grouping of work someone is responsible for, built from Tasks. A role name is not the same as a job title or an occupation. One role (for example Software Developer) can fit many job titles, and one job can combine several roles. | pp. 11-12 |
| The framework does not set skill levels (basic, advanced). It leaves those to other models. | p. 12 |
| Teams can be built "top down" from Work Roles or "bottom up" from Competencies. A red-team example lists competencies: engagement planning, rules of engagement, pen testing, data collection, vulnerability exploitation. | pp. 12-13 |
| Table 3 is an example secure software development team, organized by life-cycle phase, using 2017 role IDs (see next section). The text points to NIST's Secure Software Development Framework. | pp. 12-13 |
| Table 4 maps a team to the five Cybersecurity Framework functions (Identify, Protect, Detect, Respond, Recover) and adds two new, made-up roles. | p. 13 |
| The conclusion repeats that the framework gives employers, trainers and learners one way to describe cybersecurity work. | p. 15 |

### Work roles actually named in the source (Table 3, p. 12, 2017 IDs)

| Life-cycle phase | Work role |
|---|---|
| Design | SP-ARC-002 Security Architect |
| Build | SP-DEV-001 Software Developer |
| Deploy | OM-NET-001 Network Operations Specialist |
| Operate | OM-STS-001 Technical Support Specialist |
| Maintain | OM-DTA-001 Database Administrator |
| Decommission | OV-LGA-001 Cyber Legal Advisor |

Table 4 (p. 13) also names Security Control Assessor (SP-RSK-002), Cyber Defense Analyst (PR-CDA-001) and Cyber Defense Incident Responder (PR-CIR-001). The paper names Software Developer as a role that covers titles such as software engineer, coder and application developer (p. 11).

## Useful for the paper

- **Topic 2 (career relevance):** Shows that NIST treats a Software Developer as part of a secure software development team next to a Security Architect, and that one role can match many job titles (pp. 11-12). It also says the framework is not only for people fully inside security (p. vi). It does not report job counts or pay.
- **Topic 3 (what the field covers):** Gives the structure of how the field describes itself (tasks, knowledge, skills, competencies, work roles) and example roles by life-cycle phase (p. 12). For the actual current list of roles and skills, cite the NICE Framework Resource Center, not this PDF.
- **Skills language:** Skill statements are written as observable actions (p. 5). This is useful when the paper describes what a security-aware web developer can show.
- **Not covered:** This document does not discuss web application vulnerabilities, health data, or any specific product. Do not use it for those topics.
- **Product wording:** Use only as background for the proposed caregiving coordinator (a product idea, not built). It says nothing about any product being secure or compliant.

## Limits and cautions

- This is the November 2020 edition. NIST's own page (Planning Note, 06/26/2025) says the components now live on the NICE Framework Resource Center "Current Versions" page. The work role IDs in Table 3 and Table 4 are the 2017 IDs, and roles may have been renamed, split or changed since. The paper should say so and not present them as the current list.
- The framework describes work and learning. It is not a rule that employers must follow, and it does not set skill levels (p. 12).
- Role examples in Tables 3 and 4 are labeled informative examples, "does not cover all the Work Roles" (p. 13).

## Not read

- The figures (Figures 1 to 4) are pictures. I read only their captions and the text around them, not the images themselves.
- I did not open the NICE Framework Resource Center "Current Versions" page, so I have not checked today's work role list. The words "capability indicators" and "Competency Areas" do not appear in this PDF; "Competency Areas" appears only on NIST's status page.
- The text in the saved `status.html` is NIST's page as fetched; I did not check any linked pages.
