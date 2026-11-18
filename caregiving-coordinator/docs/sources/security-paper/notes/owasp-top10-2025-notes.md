# Notes: OWASP Top 10:2025

- **Source:** OWASP Foundation. (2025). *OWASP Top 10:2025*. https://owasp.org/Top10/2025/ (accessed 2026-11-18)
- **Saved copy:** `caregiving-coordinator/docs/sources/security-paper/owasp-top10-2025/` (17 HTML pages and a text copy of each) and the project page in `caregiving-coordinator/docs/sources/security-paper/owasp-top10-2025-project-page/`.
- **These are web pages, so there are no page numbers.** Cite by page and section name, for example (OWASP, 2025, "A01:2025 Broken Access Control," "How to prevent").
- **Read in full (2026-11-18):** the index, Introduction, About OWASP, What are Application Security Risks?, Establishing a Modern Application Security Program (including "Using the OWASP Top 10 as a standard"), A01 to A10 (background, description, how to prevent, attack scenarios), and Next Steps X01 (Lack of Application Resilience) and X03 (Inappropriate Trust in AI Generated Code).
- **Not read line by line:** the long "List of Mapped CWEs" lists and the reference link lists on each risk page, and Next Steps X02 (Memory Management Failures, which is about memory-unsafe languages and does not apply to a JavaScript web app). The CWE counts per category come from each page's score table.

## Currency check, 2026-11-18
The project page (`https://owasp.org/www-project-top-ten/`) says: "The most current released version is the OWASP Top 10 2025," with 2021 and 2017 as earlier versions, and shows Latest Version 2025. So 2025 is the newest released edition.

## What the pages say (my words)

| Point | Page and section |
|---|---|
| This is the 8th installment of the Top Ten. It is an awareness document, not a complete list. | Introduction; Establishing a Modern Application Security Program |
| The 2025 list is: A01 Broken Access Control, A02 Security Misconfiguration, A03 Software Supply Chain Failures, A04 Cryptographic Failures, A05 Injection, A06 Insecure Design, A07 Authentication Failures, A08 Software or Data Integrity Failures, A09 Security Logging and Alerting Failures, A10 Mishandling of Exceptional Conditions. | Introduction |
| Two categories are new or widened (A03 widens the old "Vulnerable and Outdated Components"; A10 is new), and Server-Side Request Forgery was folded into A01. | Introduction, "What's changed" |
| Eight categories come from contributed data and two from a community survey, because test data looks backward. The data covers more than 2.8 million applications and 589 weakness types, and the ten categories hold 248 of them. | Introduction, "Methodology" and "Why we use a community survey" |
| OWASP did not use CVSS 4.0 for scoring because the algorithm changed. | What are Application Security Risks? |
| The same software can mean different risk: a CMS used for public information and the same CMS holding health records have different threat actors and business impact. | What are Application Security Risks? |
| A01 Broken Access Control: all tested applications had some form of it, and it has the highest number of occurrences. Failures include breaking "deny by default," changing an identifier to view someone else's account, and missing checks on POST, PUT and DELETE. | A01, "Background" and "Description" |
| Prevention for A01: access control works only in trusted server-side code, deny by default, implement it once and reuse it, enforce record ownership, log failures and alert, rate-limit, and test access control in unit and integration tests. A scenario shows a front-end-only admin check bypassed with a plain command. | A01, "How to prevent" and "Example attack scenarios" |
| A02 Security Misconfiguration: all tested applications had some. Prevention includes a repeatable hardening process, identical configurations across development, test and production with different credentials, security headers, and short-lived credentials instead of static keys in code. | A02 |
| A03 Software Supply Chain Failures: the survey's top concern (50% ranked it first). It covers build systems and distribution, not just known vulnerable packages. Prevention includes tracking every dependency including indirect ones, a software bill of materials, only trusted sources, staged rollouts, MFA and least privilege on the code repository and CI, and not checking in secrets. | A03 |
| The Shai-Hulud attack in 2025 was the first successful self-spreading npm worm. It reached over 500 package versions before npm stopped it, and it targeted developer machines and npm tokens. | A03, "Example attack scenarios," scenario 3 |
| A04 Cryptographic Failures: classify data, encrypt sensitive data at rest and in transit (TLS 1.2 or higher), do not store sensitive data you do not need, store passwords with Argon2, scrypt or PBKDF2, never check keys into source code, and prepare for post-quantum cryptography. | A04 |
| A05 Injection: keep data separate from commands, use parameterized queries, and validate input on the server. | A05 |
| A06 Insecure Design: a perfect implementation cannot fix a design that lacks needed controls. Use threat modeling for authentication, access control and key flows, add security language to user stories, and separate tenants by design in every tier. Security questions for password recovery are named as a design flaw. | A06 |
| A07 Authentication Failures: prevent credential stuffing and weak passwords, require multi-factor authentication where possible, check new passwords against breached lists, follow NIST 800-63b section 5.1.1, give the same message for all login failures, and use a trusted authentication system when possible. | A07 |
| A08 Software or Data Integrity Failures: verify the source and integrity of updates, packages and data, review code and configuration changes, and protect the build pipeline. | A08 |
| A09 Security Logging and Alerting Failures: log logins and failures, keep audit trails with integrity controls such as append-only database tables, always fail closed, alert on suspicious behavior, and do not log sensitive data such as PII or PHI. | A09 |
| A09 gives a breach example in which a children's health plan website had no logging, attackers may have had access for over seven years, and more than 3.5 million children's records were involved. | A09, "Example attack scenarios," scenario 1 |
| A10 Mishandling of Exceptional Conditions (new): handle errors where they happen, roll back whole transactions and fail closed, add rate limits, and do not show full error messages to users. | A10 |
| Next Steps: X01 Lack of Application Resilience (limits, quotas, failover) and X03 "Inappropriate Trust in AI Generated Code" (vibe coding). X03 says AI-generated code often has more vulnerabilities, a person should be able to read and understand every line they commit, and AI code should be reviewed with security tooling. | Next Steps |
| The Top 10 is the bare minimum as a coding or testing standard. OWASP recommends ASVS as the verifiable standard and discourages claiming full Top 10 coverage. | Establishing a Modern Application Security Program, "Using the OWASP Top 10 as a standard" |

## Possible use in the paper
- Topic 3 (background) and Topic 5 (what it includes): the ten categories as the field's main web risks.
- Topic 8: A01 (deny by default, server-side checks, record ownership), A07 (sign-in), A09 (an append-only access log), A10 (fail closed) and A03 (package safety) line up with the idea's planned tasks T4.1.3, T4.3.1 and T4.3.2 in `caregiving-coordinator/docs/clean-deliverables/non-functional-epics-features-tasks-2026-11-15.md`. This does not say the idea is secure or compliant.
- Topic 4 or 7: X03 on AI-generated code bears on how the owner builds with Claude Code.

## Limits
- It is an awareness list, not a standard (OWASP says so). The data is from contributing vendors and testers.
- The paper must not claim the proposed coordinator "covers" the Top 10. OWASP discourages such claims.
