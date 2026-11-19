# Notes: OWASP Top 10 Proactive Controls 2024

- **Source:** OWASP Foundation. (2024). *OWASP top 10 proactive controls 2024*. https://top10proactive.owasp.org/archive/2024/the-top-10/ . Each control is a page of its own, so it can be cited by control number, for example "C1: Implement Access Control".
- **Label for the paper:** official project guidance (tier 1 in the source list). The list is a set of techniques, not a standard.
- **Domain note:** the pages sit on `top10proactive.owasp.org`, which is a subdomain of `owasp.org` (an approved domain), and the OWASP project page `https://owasp.org/www-project-proactive-controls/` links to it. The source list names `owasp.org/www-project-proactive-controls/`. I treated the subdomain as official OWASP. If the owner disagrees, the notes stay and the citation changes.
- **Local copies:** `caregiving-coordinator/docs/sources/security-paper/owasp-proactive-controls/project-page.html` (the project page saved earlier) and `caregiving-coordinator/docs/sources/security-paper/owasp-proactive-controls/2024/` (12 pages saved 2026-11-18: the list's introduction, controls C1 to C10 and the Final Word).
- **There are no page numbers.** These notes cite the control number and heading. APA 7 allows this for web pages without page numbers.
- **Read in full (2026-11-18):** the introduction ("About this Project"), controls C1 to C10 and the Final Word. I did not read the 2018, 2016 or 2014 archive lists, which are older editions.
- **Currency check (2026-11-18):** the saved site menu lists "Top 10 2024" as the newest set, with the 2018, 2016 and 2014 lists as archives. I found no 2025 or 2026 edition on that page. The 2024 pages still link to the OWASP Top 10 2021, not the 2025 list, so use the 2025 list for any ranking claim.

## The ten controls (my words)

| Control | What it says | Heading |
|---|---|---|
| **C1: Implement Access Control** | Design access control thoroughly up front, because it is hard to change later, especially for multiple tenants and data-dependent access. Force every request through a check, keep the check in one place, deny by default (also when the check throws an error, and for new accounts and new features), give least privilege (and just-in-time access), and avoid hard-coded roles in favor of permission checks. | Implementation (items 1 to 7) |
| **C2: Use Cryptography to Protect Data** | Classify data by sensitivity. Never send data in plain text. Do not invent cryptography or write your own routines. Avoid storing sensitive data if possible. Store passwords as salted hashes, keep secrets out of code, config files and environment variables, use a secrets vault, rotate keys, use TLS 1.2 or 1.3, and make algorithm choices configurable ("cryptographic agility"). | Description; Implementation |
| **C3: Validate all Input & Handle Exceptions** | Check data is correct in form and in meaning, using allow lists. Validate on the server, because client checks are easy to bypass. Keep data and commands apart with prepared statements. Input validation alone does not make data safe. Block mass assignment (the attacker setting fields such as `privilege=admin`). Treat deserialization of untrusted data as dangerous. | Syntactic and Semantic Validity; Allowlisting vs Denylisting; Unexpected User Input (Mass Assignment); Limits of Input Validation |
| **C4: Address Security from the Start** | Secure architecture prevents flaws before they exist. The design principles are: keep it simple, make it easy to do the right thing, do not rely on obscurity, minimize the attack surface (exposed parts), and design defense-in-depth so a breach has a small blast radius. Use well-maintained third-party components and keep them up to date. Use known secure architecture patterns and threat modeling. | Description; Implementation |
| **C5: Secure By Default Configurations** | Software should start in its most secure state without extensive setup. Use least privilege, deny by default, private cloud storage, encrypted traffic, and infrastructure defined in code so it can be reviewed like source code. Turn off unneeded accounts, features and debugging in production. | Description; Implementation |
| **C6: Keep your Components Secure** | Pick libraries by source, popularity, activity, maturity, complexity and security. Keep an inventory (a software bill of materials, SBOM), check for known vulnerabilities continuously with software composition analysis tools, and update on a regular schedule. The page names OWASP Dependency-Check and Dependency-Track. | Implementation: Best Practices to Identify Trusted libraries; to Keep them Secure |
| **C7: Secure Digital Identities** | Use NIST SP 800-63B's three assurance levels: passwords alone for low-risk apps; multi-factor sign-in for apps that hold personal information; cryptographic sign-in (WebAuthn, passkeys) where harm could be serious. Prefer server-side sessions. Password rules: at least 8 characters with multi-factor sign-in (10 without), no composition rules, block breached passwords. Use secure, HttpOnly, SameSite cookies. Idle and absolute session timeouts should be shorter when the data is more valuable. | Authentication Assurance Levels; Implementation |
| **C8: Leverage Browser Security Features** | Browser protections are opportunistic, since the site cannot verify the browser obeys them, so treat them as extra hardening. Headers named include HSTS, Content Security Policy, Referrer-Policy, X-Frame-Options and a permissions policy. Set the cookie flags. Use SameSite and Fetch Metadata checks against cross-site request forgery. | Opportunistic Security and Browser-Support; Implementation |
| **C9: Implement Security Logging and Monitoring** | Log security events to detect and respond to incidents. Log out-of-range input, changes to fields that should not change, and requests that break access rules. Do not log passwords, session IDs, payment cards or social security numbers. Protect log integrity, escape input to stop log injection, and forward logs to a central, secure service. | Description; Secure Logging Design; Implementation |
| **C10: Stop Server Side Request Forgery** | SSRF tricks a server into making requests for the attacker, using the server's own identity. Check outgoing request targets against an allow list. | Description; Implementation |

| Other points | Where |
|---|---|
| Proactive controls are meant to prevent common flaws during development. The list says that following them reduces the chance of a vulnerability but gives no guarantee. | Introduction ("About this Project") |
| The authors say the list is a starting point, not a complete program. They suggest next steps: the OWASP Top Ten, a list of security requirements, threat modeling, ASVS, and the OWASP SAMM project. | Final Word |
| The list was built by the project leads with hundreds of changes from an open community process. | Introduction: How this List Was Created |

## Where this page disagrees with other sources I read (flag for the paper)
- **Password rotation.** C7 lists "Enforce password rotation." The OWASP Authentication Cheat Sheet and NIST SP 800-63B (as the cheat sheet quotes it) say not to force periodic password changes. For the paper, do not recommend rotation of user passwords. If the paper mentions it, cite the Authentication Cheat Sheet and the NIST guideline and say that the Proactive Controls page is older on this point.
- **Password length.** C7 says at least 8 characters with multi-factor sign-in and at least 10 without. The Authentication Cheat Sheet, quoting NIST SP 800-63B, says under 8 is weak with multi-factor and under 15 is weak without it. Do not quote a minimum length from C7.
- **Secrets in environment variables.** C2 says not to pass secrets through environment variables. The Secrets Management Cheat Sheet says environment variables are not recommended unless other methods are not possible. The two are close, but the paper must not say that the proposed coordinator "never" uses environment variables, since hosts such as Vercel use them. That is a matter for the Vercel documentation, still to be read.

## Possible use in the paper
- **Topic 4 (how it works when building products):** C4 and C5 are the plainest statement of "secure from the start" and "secure by default". C1 and C3 are the core developer controls.
- **Topic 5 (what it includes):** the ten controls are a ready list of what application security work contains.
- **Topic 7 (tools and skills):** C6 names dependency-checking tools. C9 and C2 connect to logging and secret scanning.
- **Topic 8:** C1 (deny by default, least privilege, multi-tenancy) matches the proposed care circles and roles in a general way. The paper may say these are controls the idea plans to follow and must not say they are built.

## Limits
- The list is guidance written by volunteers. It has no page numbers and no formal version control beyond the year.
- Some pages cite older material (the 2021 Top 10, NIST SP 800-63 Revision 3, and the 2023 CWE list). Use the newer sources I read for current ranking claims.
- It says nothing about health data, caregiving, or any specific hosting service.
