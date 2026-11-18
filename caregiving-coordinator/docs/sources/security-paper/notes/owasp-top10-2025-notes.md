# Notes: OWASP Top 10:2025 (PARTLY READ, finish in the next chat)

- **Source:** OWASP Foundation. (2025). *OWASP Top 10:2025*. https://owasp.org/Top10/2025/ (accessed 2026-11-18)
- **Saved copy:** `caregiving-coordinator/docs/sources/security-paper/owasp-top10-2025/` (17 HTML pages and a text copy of each) and the project page in `owasp-top10-2025-project-page/`
- **These are web pages, so there are no page numbers.** Cite by page name: Introduction, About OWASP, What are Application Security Risks?, Establishing a Modern Application Security Program, and A01 to A10.
- **Read so far (2026-11-18):** the index page, Introduction, About OWASP, What are Application Security Risks?, and Establishing a Modern Application Security Program up to the "Operations and Change Management" part.
- **Still to read:** the end of the Establishing page, the ten pages A01 to A10, and Next Steps (X01).

## Currency check, 2026-11-18
The project page (`https://owasp.org/www-project-top-ten/`) says: "The most current released version is the OWASP Top 10 2025," with 2021 and 2017 as previous versions, and shows Latest Version 2025. So 2025 is the newest released edition.

## What the pages say (my words)

| Point | Where |
|---|---|
| This is the 8th installment of the Top Ten. It is an awareness document for developers, not a complete list. | Introduction; Establishing a Modern Application Security Program |
| The 2025 list is: A01 Broken Access Control, A02 Security Misconfiguration, A03 Software Supply Chain Failures, A04 Cryptographic Failures, A05 Injection, A06 Insecure Design, A07 Authentication Failures, A08 Software or Data Integrity Failures, A09 Security Logging and Alerting Failures, A10 Mishandling of Exceptional Conditions. | Introduction |
| Two categories are new (A03 widens the old "Vulnerable and Outdated Components"; A10 is new), and Server-Side Request Forgery was folded into A01. | Introduction, "What's changed" |
| Broken Access Control stays at #1. On average 3.73% of tested applications had at least one of its 40 weakness types. | Introduction |
| Security Misconfiguration moved from #5 to #2. | Introduction |
| Supply chain failures had the fewest occurrences in the data but the highest average exploit and impact scores. OWASP thinks testing for it is behind. | Introduction |
| Eight categories come from the data and two from a community survey, because test data looks backward. | Introduction, "Why we use a community survey" |
| The data covers more than 2.8 million applications. 589 weakness types were analyzed. The ten categories hold 248 of them. | Introduction |
| Rankings use incidence rate, coverage, exploit and impact scores. Risk differs by organization: the same software can mean different risk for a public information site and a health system. | What are Application Security Risks? |
| OWASP did not use CVSS 4.0 for the scores because its algorithm changed. | What are Application Security Risks? |
| The program advice: rank applications by risk, set a baseline of policies, build security into existing steps, train developers, and show management metrics. It names threat modeling, secure design, code review, penetration testing and a secure-by-default "paved road". | Establishing a Modern Application Security Program |
| It recommends ASVS for requirements, the Cheat Sheets and Proactive Controls for design, SAMM to assess a program, and secret-management and scanning tools for developers. | Establishing a Modern Application Security Program |
