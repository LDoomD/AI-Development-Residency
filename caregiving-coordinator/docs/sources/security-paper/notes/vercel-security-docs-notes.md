# Notes: Vercel documentation, security pages (21 pages)

- **Source:** Vercel Inc. (2026). *Vercel documentation: Security and compliance, access, firewall and environment variable pages* [Web pages]. Vercel. Retrieved November 18, 2026, from https://vercel.com/docs/security (each page's own URL and "Last updated" date are in the table below; APA-7 needs one reference per page you cite, so cite the page title and URL).
- **Label for the paper:** vendor documentation (tier: what the vendor says its own product does). It is **not independent proof**. Every "Vercel does X" below is a vendor claim. Nothing here shows that a product built on Vercel is secure or compliant.
- **Local copies:** folder `caregiving-coordinator/docs/sources/security-paper/vercel-security-docs/`. Each page has a `.html` (raw download) and a `.txt` (text copy, with the left sidebar menu cut off). File names use `_` instead of `/` in the URL path.
- **Retrieval:** 2026-11-18, plain `curl -L`, all returned HTTP 200. Two pages came from the Vercel blog and changelog, not /docs.
- **Read in full (2026-11-18):** I printed and read the whole `.txt` copy of all 21 pages with `cat` (not the Read tool; the text copies were short enough to read in full that way). One gap: the **Team Level Roles** page builds its permissions table with JavaScript, so the saved copy only says "Loading permissions...". I could not read the role-by-role table (see "Not read").

## Pages read (URL, date shown on the page)

| # | Page title | URL | Date on page |
|---|---|---|---|
| 1 | Vercel security overview | https://vercel.com/docs/security | Last updated Aug 11, 2026 |
| 2 | Shared Responsibility Model | https://vercel.com/docs/security/shared-responsibility | Aug 11, 2026 |
| 3 | Security & Compliance Measures | https://vercel.com/docs/security/compliance | Sep 8, 2026 |
| 4 | Security Dashboard | https://vercel.com/docs/security/security-dashboard | Aug 17, 2026 |
| 5 | Access Control | https://vercel.com/docs/security/access-control | Sep 15, 2026 |
| 6 | Deployment Protection on Vercel | https://vercel.com/docs/deployment-protection | Sep 15, 2026 |
| 7 | Vercel Firewall | https://vercel.com/docs/vercel-firewall | Sep 10, 2026 |
| 8 | Vercel WAF | https://vercel.com/docs/vercel-firewall/vercel-waf | Jul 29, 2026 |
| 9 | DDoS Mitigation | https://vercel.com/docs/vercel-firewall/ddos-mitigation | Aug 11, 2026 |
| 10 | Environment variables | https://vercel.com/docs/environment-variables | Sep 17, 2026 |
| 11 | Config and Secret environment variables | https://vercel.com/docs/environment-variables/sensitive-environment-variables | Aug 28, 2026 |
| 12 | Role-based access control (RBAC) | https://vercel.com/docs/rbac | Jun 16, 2026 |
| 13 | Team Level Roles | https://vercel.com/docs/rbac/access-roles/team-level-roles | May 6, 2026 |
| 14 | Two-factor Authentication | https://vercel.com/docs/two-factor-authentication | Aug 28, 2026 |
| 15 | Two-factor Enforcement | https://vercel.com/docs/two-factor-enforcement | Aug 28, 2026 |
| 16 | SAML Single Sign-On | https://vercel.com/docs/saml | Aug 28, 2026 |
| 17 | Audit Logs | https://vercel.com/docs/audit-log | Aug 26, 2026 |
| 18 | Encryption and TLS | https://vercel.com/docs/cdn-security/encryption | Sep 15, 2026 |
| 19 | Production checklist for launch | https://vercel.com/docs/production-checklist | Aug 11, 2026 |
| 20 | Next.js May 2026 security release (changelog) | https://vercel.com/changelog/next-js-may-2026-security-release | Published 2026-05-07 (from page metadata) |
| 21 | Postmortem on Next.js Middleware bypass (blog) | https://vercel.com/blog/postmortem-on-next-js-middleware-bypass | Published 2025-03-25 (from page metadata) |

Local file names: 1 `security`, 2 `security_shared-responsibility`, 3 `security_compliance`, 4 `security_security-dashboard`, 5 `security_access-control`, 6 `deployment-protection`, 7 `vercel-firewall`, 8 `vercel-firewall_vercel-waf`, 9 `vercel-firewall_ddos-mitigation`, 10 `environment-variables`, 11 `environment-variables_sensitive-environment-variables`, 12 `rbac`, 13 `rbac_access-roles_team-level-roles`, 14 `two-factor-authentication`, 15 `two-factor-enforcement`, 16 `saml`, 17 `audit-log`, 18 `cdn-security_encryption`, 19 `production-checklist`, 20 `changelog_nextjs-may-2026-security-release`, 21 `blog_postmortem-nextjs-middleware-bypass` (each with `.html` and `.txt`).

## What the pages say (my words)

| Point | Page and heading |
|---|---|
| Vercel says the customer handles their data, their application and user access. Vercel says it manages the infrastructure: compute, storage and networking. | #2, intro |
| Customer duties listed: decide if the platform's security is enough for the app; pay for and handle malicious traffic; encrypt server-side data (file system or database); secure source code; choose access control settings; pick compute regions; follow the production checklist; turn on Spend Management; meet any compliance rules for a regulated industry. | #2, Customer responsibilities |
| For apps in regulated industries, the customer must make sure the app is set up to meet the rules that apply. Vercel does not take this on. | #2, "Customer Compliance Obligations" |
| Shared items: the customer owns and controls their data. The customer manages app code and "the exposure of environment variables". The customer handles the app's own login (the page names NextAuth.js as an example). Vercel handles login to the Vercel platform itself. | #2, Shared responsibilities |
| Log handling is split: Vercel keeps only short-term runtime logs. The customer must set up log drains for long-term logs and auditing. | #2, "Log Management" |
| Incident response is split: Vercel handles incidents on its own infrastructure. The customer watches and responds to incidents in their code, settings and integrations. | #2, "Incident Response" |
| Vercel says it encrypts data at rest and in transit for services it controls. Customers must make sure their own third-party tools (proxies, CMSs, integrations) are secured. | #2, "Encryption & Data Integrity" |
| Vercel claims a SOC 2 Type 2 attestation (Security, Confidentiality, Availability) and ISO 27001:2022 certification. It says it "supports" GDPR and PCI DSS and is certified under the EU-U.S. Data Privacy Framework. These are Vercel's claims about Vercel. | #3, Compliance |
| Vercel says it "supports HIPAA compliance as a business associate" and signs a Business Associate Agreement (BAA) with eligible Pro and Enterprise customers. A Pro team buys a "HIPAA BAA add-on" in billing. Enterprise teams can add Secure Compute (private, isolated cloud, fixed outgoing IPs). The page does not say a customer's app becomes HIPAA compliant by using Vercel. | #3, HIPAA |
| Data location: the customer picks the region for functions. The default is the U.S. The page also says Vercel may transfer data to the U.S. and "anywhere else in the world" where it or its providers process data. | #3, "Where does my data live?" |
| Vercel says data at rest uses AES-256 and data in transit uses HTTPS/TLS 1.3. The encryption page says TLS 1.2 and 1.3 are supported, HTTP is always redirected to HTTPS, and this cannot be turned off. | #3, Data encryption; #18 |
| Vercel says it backs up its own data every two hours, keeps each backup 30 days, and that "These backups are not available to customers." So these are not a backup of the customer's app data. | #3, Data backup |
| Vercel says it uses third-party penetration testers, daily code reviews and static analysis. No test report is in the page. | #3, last section |
| Enterprise teams get separate build infrastructure from Hobby and Pro accounts. | #3, "Do Enterprise accounts run on a different infrastructure?" |
| Deployment Protection lets you control who can open preview and production URLs. It is set per project. It also requires login for requests that go through Routing Middleware. | #6, intro |
| Methods: Vercel Authentication; Passport (Enterprise); Password Protection (Pro: $20 per month per protected project, included in Enterprise, not on Hobby); Trusted IPs (Enterprise). | #6, protection methods |
| Scope: "Standard Protection" protects everything except production domains and is on all plans. "All Deployments" also protects production domains and is on all plans. Protecting only production needs Trusted IPs (Enterprise). | #6, protection scope |
| Standard Protection is called "the recommended option for most projects." Under it, a project's production generated URL becomes restricted, so code that fetches `VERCEL_URL` may break. | #6, Standard Protection |
| Vercel Authentication lets a person with a Vercel account on the team open the protected deployment. It is free on all plans. | #5, #6 |
| Protected Source Maps puts `.map` files behind Vercel Authentication so source code is not exposed. | #6, "Restrict access to source maps" |
| The Vercel Firewall has a platform-wide layer (with DDoS mitigation, free, no setup, all plans) and a customizable WAF (all plans). Rules run in this order: DDoS rules, WAF IP blocking, WAF custom rules, WAF managed rulesets. | #7 |
| Vercel says WAF changes apply globally within 300 ms and can be rolled back. Limits depend on plan: Hobby up to 3 custom rules, Pro up to 40, Enterprise up to 250. The OWASP core ruleset is listed as Enterprise only. | #8, Limits |
| Vercel says it blocks L3, L4 and L7 DDoS attacks on every plan and does not charge for blocked traffic. It does charge for requests served before the attack was spotted, and for bot or crawler traffic it does not call an attack. | #9, "DDoS and billing" |
| Environment variables are "encrypted at rest." Each one is "Config" (readable later by members with access) or "Secret" (write-only after saving). Use Secret for passwords, API keys and tokens. | #10, intro; #11 |
| Changes to environment variables apply only to new deployments, not to ones already running. | #10, intro |
| Next.js puts `NEXT_PUBLIC_` variables into the browser code at build time. (The page says this only to explain why a variable can show as undefined.) Dynamic lookups like `process.env[name]` are not inlined. | #10, Troubleshooting table |
| The Security Dashboard flags "Environment variables exposed via a web application framework" as a medium risk and says to "keep secrets server-only." It also flags variables not marked Secret, and credential-named variables older than 90 days. | #4, project checks |
| Build logs: if a Secret value is 32 characters or longer and appears in a build log, Vercel replaces it with [REDACTED]. | #11, "Build log redaction" |
| An optional team policy, "Separate Production Secret Values", makes each Secret use a different value in Production than in Preview and Development. Only the team owner role can turn it on. | #11, Environment variables policy |
| Security Dashboard high-risk checks: team members without multi-factor sign-in; too many owners; personal access tokens that never expire; long-lived credentials where short-lived (OIDC) tokens would work; projects where forked pull requests can deploy and read environment variables; preview deployments anyone with a URL can open. | #4, checks tables |
| The `vercel security` command runs the same checks. A failing check still exits 0, so a CI step must read the report, not the exit code. | #4, "Run checks from the CLI" |
| 2FA: all Vercel users must set up an authenticator app by January 20, 2027. Passkeys are supported as an added, phishing-resistant method. Team owners can require 2FA for all members. | #14, #15 |
| When team 2FA is enforced, personal access tokens use their owner's 2FA status, so CLI and CI deployments can fail if the owner has no 2FA. Integration tokens are exempt. | #15, "What happens when enforcement is enabled" |
| SAML single sign-on lets a team log in through an identity provider such as Okta. Pro needs a paid add-on. Owner role only. Default session is 24 hours (can be 1 hour to 30 days). Automatic user provisioning (Directory Sync) is Enterprise. | #16 |
| Team roles (RBAC) are on Enterprise and Pro. Pro does not have the Security and Contributor roles. | #12, #13 |
| Audit logs are Enterprise only, readable by owner and security roles. CSV export covers the last 90 days. They record things like env variable created/updated/deleted, member added/removed, role changed, project deleted. | #17 |
| Vercel's production checklist lists security steps: CSP and security headers, Deployment Protection, WAF, log drains, commit lockfiles, rate limiting, access roles, SAML SSO, SCIM, audit logs, and a bot-blocking rule. It says to define an incident response plan. | #19, Security and Operational excellence |
| Changelog (2026-05-07): 13 Next.js advisories patched in a coordinated release, including four "High" middleware/proxy bypass issues. It affects apps that rely on `middleware.js` or `proxy.js` for authorization. Fixed in Next.js 15.5.18 and 16.2.6. | #20, Impact; Fixed in |
| In that changelog Vercel says: "Patching is the only complete mitigation." It says it deployed no new WAF rules because these cannot be reliably blocked at the WAF layer. | #20, Resolution |
| Postmortem (March 2025, CVE-2025-29927): Vercel says it does "not recommend Middleware to be the sole method of protecting routes." It says Vercel-hosted apps were not affected because of how Vercel runs routing, while self-hosted Next.js apps were. | #21, Technical analysis; timeline |

## Useful for the paper

**Topic 7 (best practices)**
- The shared-responsibility page (#2) is the base for a "who does what" statement. Only claim what this page says. It gives the customer: data, app code, user access, server-side encryption, app login, secrets handling, log retention, response to app-level incidents, and compliance duties.
- Vercel's own checklist (#19) and Security Dashboard checks (#4) are a vendor-written list of settings. Good examples to name: 2FA for all members, secrets stored as Secret and rotated, short-lived credentials, protect preview deployments, block forked pull requests from reading environment variables.
- The two Next.js pages (#20, #21) support a point that matches other sources in the folder: do not rely on middleware alone to protect routes (Vercel's own wording). The Next.js middleware advisories are covered in `notes/nextjs-middleware-advisories-notes.md`. This is an overlap, not new work: #20 is Vercel's changelog summary of the same May 2026 advisories, and #21 is Vercel's postmortem on the 2025 CVE.

**Topic 8 (application to the proposed coordinator)**
Per the shared-responsibility page only, the proposed coordinator would still have to handle itself: its own sign-in and permissions (not Vercel's), encryption and protection of its database data, which variables are exposed to the browser, secret storage and rotation, long-term logs, watching for incidents, and any rules for health data. Vercel says it handles the platform side: infrastructure, compute isolation, and encryption it controls. Hosting on Vercel would not remove the app's own duties.
- Health data: the compliance page (#3) says Vercel signs BAAs and offers a HIPAA BAA add-on on Pro. The paper can report that vendor claim. It must not say the proposed product would be HIPAA compliant. Whether the product would count as a covered entity or business associate is a legal question these pages do not answer.
- Preview deployments: Deployment Protection (#6) and the Security Dashboard (#4) show preview URLs can be public unless protected. The proposed product would have to turn protection on.
- `NEXT_PUBLIC_` variables (#10) end up in browser code, so a database service key or other secret must never use that prefix. (The page says the prefix inlines the value into the client bundle; the "never put secrets there" step is my reading, supported by the dashboard check in #4.)

## Limits and cautions

- **All vendor claims.** Certifications and "supports X compliance" statements are what Vercel says. The pages link to audit reports and a Trust Center (security.vercel.com), which I did not open. Do not turn these into a claim about the proposed product.
- **Plan-dependent features (as stated on the pages):** Password Protection ($20 per month per project on Pro; not Hobby); Passport and Trusted IPs (Enterprise); SAML SSO (Pro add-on or Enterprise); Directory Sync/SCIM (Enterprise); Audit Logs and audit log drains (Enterprise); team roles Security and Contributor (Enterprise only); HIPAA BAA (Pro add-on or Enterprise; "eligible" customers); Secure Compute (Enterprise); OWASP core ruleset (Enterprise); account-level IP blocking (Enterprise). Free on all plans: DDoS mitigation, WAF (with plan-based limits), Vercel Authentication, Standard Protection, All Deployments protection.
- **Docs change often.** Pages carry 2026 "Last updated" dates. Prices and plan limits can change. The 2FA page says a new requirement starts January 20, 2027, so it will change soon.
- **Dates on pages are in 2026 and later than my training data;** I report only what the saved pages say.
- The postmortem (#21) is Vercel's account of its own response. It is a vendor view, written in 2025.
- Vercel says it does not deploy WAF rules for the May 2026 advisories. So the WAF is not a fix for those; upgrading is. This is Vercel's statement.
- I did not test any setting. Nothing here shows a feature works as described.

## Not read / pages skipped and why

- **Team Level Roles permission table (#13):** the page loads the table with JavaScript ("Loading permissions..."). Only the intro and plan note were read. I did not use a browser to get it. The Project Level Roles and Access Groups pages were not fetched.
- **Next.js on Vercel page** (`/docs/frameworks/full-stack/nextjs`): fetched, then deleted. It is a general framework guide (1.6 MB of HTML), not security guidance. Its only security text was a short Draft Mode note.
- **Not fetched (linked from these pages):** Attestations and Compliance Report, PCI DSS iframe, Bypass Deployment Protection, Security Headers, Security settings (Git fork protection), Directory Sync, Enterprise Managed Users, Activity Log, OIDC, Secure Compute, Key Management, Security Review (agent), Migrating from SIEM, Vercel Trust Center (security.vercel.com), the Responsibility Matrix, and the Data Processing Addendum. Reason: kept to about 20 core pages; they are good next picks if the paper needs more on these topics.
- `/docs/two-factor` returned 404; the right URLs are #14 and #15. No other fetch was blocked.
- Vercel's own earlier March 2025 changelog about CVE-2025-29927 was not found at a URL I could confirm; the postmortem (#21) describes it.
