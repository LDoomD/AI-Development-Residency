# Notes: GitHub security docs and npm audit docs

Retrieval date for every page: 2026-11-18. All pages were fetched with plain `curl -L` (no blocks, all HTTP 200). I read the text of each saved HTML page after turning it into plain text (menus removed). GitHub Docs pages say "GitHub Inc. © 2026" and show no "last updated" date. The npm pages show their own "last edited" dates (below).

Why these sources: topic 4 (current methods and tools), topic 7 (best practices) and topic 8 (application to the proposed caregiving coordinator, which is a product idea and is not built). Stack in the idea: Next.js, Supabase, Vercel, code on GitHub, npm packages.

---

## Source A. GitHub secret scanning

- **Reference (APA 7):** GitHub. (2026). *Secret scanning*. GitHub Docs. Retrieved November 18, 2026, from https://docs.github.com/code-security/secret-scanning/about-secret-scanning (this URL redirects to https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning)
- **Page title seen:** "Secret scanning" (in the Docs list it is titled "About secret scanning").
- **Local copies:** `caregiving-coordinator/docs/sources/security-paper/github-security-docs/about-secret-scanning.html` (read, as text). Also `raw-secret-scanning.md`, the raw Markdown of the same page from github/docs on GitHub (7,137 bytes, fetched; I used the rendered HTML as the main read and the Markdown only to confirm the page source).
- **Read in full:** the whole page.

| What the page says (my words) | Page and heading |
|---|---|
| Secret scanning looks for hardcoded credentials such as API keys, passwords and tokens. It searches the whole Git history on every branch. | "How secret scanning protects your code" |
| GitHub rescans from time to time when new secret types are added. It also checks issue and pull request text, discussions, wikis and secret gists. | same |
| When it finds a leak, it raises an alert on the repository's Security and quality tab. GitHub says to rotate (replace) the leaked credential right away. Removing it from Git history is slow and often not needed once the credential is revoked. | "Secret scanning alerts and remediation" |
| For secrets from partner companies, GitHub tells the provider, who can revoke it. These are not shown in your own alerts. | "Partner integration" |
| You can add generic patterns (private keys, connection strings), custom patterns, validity checks (is the secret still active), AI-found secrets and AI-written patterns. | "Customizability" |
| Validity checks may contact the service that issued the secret to see if it was revoked. | "About validity checks" |
| Public repositories: runs automatically, free. Organization private and internal repositories: needs GitHub Secret Protection on GitHub Team or Enterprise Cloud. User-owned repositories: only on Enterprise Cloud with Enterprise Managed Users, or Enterprise Server with Secret Protection. | "How can I access this feature?" |

## Source B. GitHub security features overview

- **Reference (APA 7):** GitHub. (2026). *GitHub security features*. GitHub Docs. Retrieved November 18, 2026, from https://docs.github.com/en/code-security/getting-started/github-security-features
- **Local copy:** `caregiving-coordinator/docs/sources/security-paper/github-security-docs/github-security-features.html` (read, as text).
- **Read in full:** the whole page.

| What the page says (my words) | Page and heading |
|---|---|
| Some features are for all plans. More are for Team and Enterprise Cloud organizations that buy "GitHub Secret Protection" or "GitHub Code Security". Some of these paid features run free on public repositories. | "About GitHub's security features" |
| Free on all plans: security policy, dependency graph, SBOM export (SPDX), GitHub Advisory Database, Dependabot alerts and security updates, Dependabot version updates, security advisories, repository rulesets, secret scanning alerts for partners, and push protection for users. Dependabot malware alerts are also listed. | "Available for all GitHub plans" |
| Artifact attestations (proof of how software was built) on Free, Pro or Team plans work only for public repositories. Private repositories need Enterprise Cloud. | "Artifact attestations" note |
| Push protection for users is on by default and protects against accidentally committing secrets to public repositories. You can turn it off in account settings. | "Push protection for users" |
| Needs Secret Protection: secret scanning alerts for users, AI-detected secrets, push protection for repositories, delegated bypass, custom patterns, security overview. Secret scanning alerts and push protection are "available for public repositories by default." | "Available with GitHub Secret Protection" |
| Needs Code Security: code scanning, CodeQL CLI, Copilot Autofix, AI Scan, custom auto-triage rules for Dependabot, dependency review, security campaigns. Code scanning, CodeQL CLI, Copilot Autofix and dependency review are marked "available for public repositories by default." | "Available with GitHub Code Security" |

**Plan limits in one place (from this page and the pages below):** public repository = most scanning features free. Private repository on Free or Pro = only the "all plans" list (for example Dependabot alerts, dependency graph) plus push protection for users on public repos. Private repository code scanning and secret scanning need a paid Team or Enterprise plan plus the add-on product.

## Source B1. Dependabot alerts (linked from Source B)

- **Reference (APA 7):** GitHub. (2026). *Dependabot alerts*. GitHub Docs. Retrieved November 18, 2026, from https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-alerts
- **Local copy:** `docs/sources/security-paper/github-security-docs/dependabot-alerts.html`. **Read in full.**

| What the page says (my words) | Page and heading |
|---|---|
| Dependabot alerts tell you when a package you use has a known weakness, so you can upgrade. Available for organization-owned and user-owned repositories. | Intro; "Who can use this feature?" |
| It scans the default branch. It sends an alert when a new weakness is added to the GitHub Advisory Database or when your dependency list changes. | "When Dependabot sends alerts" |
| Each alert shows the file, details, severity and a fixed version when there is one. Optional reachability analysis (public preview) checks if your code can reach the weak code; it covers JavaScript with npm, pnpm or Yarn, and TypeScript. | "Understanding alerts" |
| Repository admins and organization owners turn alerts on. Assigning alerts to people or AI agents needs a Code Security or Advanced Security license, even on public repositories. | "Who can enable alerts?"; "Alert ownership and assignments" |
| Limits: alerts cannot catch every issue; new weaknesses may take time to appear; only advisories reviewed by GitHub trigger alerts; archived repositories are not scanned. | "Limitations" |

## Source B2. Code scanning (linked from Source B)

- **Reference (APA 7):** GitHub. (2026). *Code scanning*. GitHub Docs. Retrieved November 18, 2026, from https://docs.github.com/en/code-security/concepts/code-scanning/code-scanning
- **Local copy:** `docs/sources/security-paper/github-security-docs/code-scanning.html`. **Read in full.**

| What the page says (my words) | Page and heading |
|---|---|
| Code scanning analyzes the code in a repository for security weaknesses and coding errors and shows alerts. It can run on a schedule or on events such as a push. | Intro |
| Available for public repositories on GitHub.com, and for organization-owned repositories on Team, Enterprise Cloud or Enterprise Server with GitHub Code Security enabled. Private repositories need a Code Security license. | "Who can use this feature?"; intro |
| It uses GitHub Actions, and each run uses Actions minutes. | Intro |
| The built-in engine is CodeQL. Other tools work if they output SARIF (an open standard format). | "About tools for code scanning" |
| Copilot Autofix suggests fixes for alerts. | Intro |

## Source B3. Push protection (linked from Source A and B)

- **Reference (APA 7):** GitHub. (2026). *Push protection*. GitHub Docs. Retrieved November 18, 2026, from https://docs.github.com/en/code-security/concepts/secret-security/push-protection
- **Local copy:** `docs/sources/security-paper/github-security-docs/push-protection.html`. **Read in full.** The table "Supported push surfaces" lost its check marks when I converted the page to text, so I did not use it for claims.

| What the page says (my words) | Page and heading |
|---|---|
| Push protection blocks a push that contains a secret before it reaches the repository. The developer must remove the secret and try again. | "What is push protection?"; "How push protection works" |
| It can block partner patterns, generic patterns (private keys, database connection strings), custom patterns, and AI-found secrets (public preview). | same, subheadings |
| For repositories: needs Secret Protection, is off by default, and an admin must turn it on. For users: on by default, only on GitHub.com, only for public repositories. | "Types of push protection" |
| By default anyone with write access can bypass a block by giving a reason. That creates an alert and an audit log entry. "I'll fix it later" creates an open alert. | "Push protection bypass and alerts" |

## Source C. npm audit

- **Reference (APA 7):** npm, Inc. (2023). *Auditing package dependencies for security vulnerabilities*. npm Docs. Retrieved November 18, 2026, from https://docs.npmjs.com/auditing-package-dependencies-for-security-vulnerabilities/ (page footer: last edited October 23, 2023, by a GitHub contributor; npm is part of GitHub)
- **Local copy:** `docs/sources/security-paper/npm-audit-docs/auditing.html`. **Read in full.**
- **Linked pages also read in full** (each saved in the same folder):
  - About audit reports, https://docs.npmjs.com/about-audit-reports/ (`about-audit-reports.html`; last edited April 17, 2024).
  - npm-audit command page, https://docs.npmjs.com/cli/audit, which redirects to https://docs.npmjs.com/cli/v12/commands/npm-audit/ (`cli-v12-audit.html`; shows "Version 12.2.3 (Latest)"; last edited March 18, 2026). `cli-npm-audit.html` is only the 77-byte redirect stub.
  - Verifying ECDSA registry signatures, https://docs.npmjs.com/verifying-registry-signatures (`verifying-registry-signatures.html`; last edited October 23, 2023). This page is in the left menu but is not linked from the audit page body. I read it because the task asked about `npm audit signatures`.
- **npm versions:** the audit page says the command exists "in npm@6". The command page shows CLI 12.2.3 (latest). On this machine, `npm --version` printed 11.17.0 (observed 2026-11-18). So the machine's npm is older than the docs' latest. The signatures page says it needs npm 8.15.0 or later.

| What the pages say (my words) | Page and heading |
|---|---|
| A security audit checks your package's dependencies for known weaknesses. `npm audit` sends a description of your dependencies to your registry and gets back a report. | "About security audits"; npm-audit "Description" |
| It checks direct, dev, bundled and optional dependencies but not peer dependencies. It needs `package.json` and `package-lock.json`. It runs automatically on `npm install`. | "Running a security audit with npm audit"; "Resolving EAUDITNOPJSON..." |
| Reports show severity, description, package, patched-in versions, dependency path and a "More info" link. Critical = address immediately; High = as quickly as possible; Moderate = as time allows; Low = your discretion. | About audit reports, "Severity" |
| `npm audit fix` installs compatible updates. A "SEMVER WARNING" means the fix may break your code. If no fix exists, check mitigating factors, update a parent package, fix it yourself, or open an issue. | "Security vulnerabilities found..." sections |
| "No vulnerabilities found" only means no known ones. The advisory database changes, so run it often or add it to CI (continuous integration). | "No security vulnerabilities found" |
| By default `npm audit` exits with a failing code if it finds any weakness. `--audit-level` sets the lowest level that fails the run (useful in CI). It does not filter the report. | npm-audit "Description"; "audit-level" |
| Without a lock file results may differ each run. | npm-audit "Package lock" |
| `npm audit signatures` checks that downloaded packages carry valid registry signatures and also checks provenance attestations (where a package says how it was built). Update npm often because the format may change. If signatures are missing while the registry offers keys, "an attacker might be trying to circumvent" it. | npm-audit "Audit Signatures"; Verifying registry signatures, "Some packages are missing..." |
| Since npm 7, npm sends package names and versions to the registry's bulk advisory endpoint. Privacy point: your dependency list is sent to the registry. | npm-audit "Bulk Advisory Endpoint" |

## Useful for the paper

- **Topic 4 (tools):** three layers exist for a GitHub plus npm project: GitHub secret scanning and push protection (leaked keys), Dependabot alerts and `npm audit` (known weak packages), and code scanning with CodeQL (weaknesses in your own code). `npm audit signatures` adds a check on package origin.
- **Topic 7 (best practices):** rotate a leaked key first; run audits often and in CI; keep lock files; treat "no findings" as "no known findings".
- **Topic 8 (application to the proposed coordinator):** if the product's code lives in a public repository, secret scanning, push protection, code scanning and dependency review are free. If it lives in a private repository on a free plan, the paid features would not be available; Dependabot alerts, the dependency graph and `npm audit` would still apply. The paper can state this as a plan-choice point, not as a decision already made.

## Limits and cautions

- These are vendor docs. They describe what GitHub and npm say their own products do. They do not test how well the tools work (no detection rates, no false-positive rates).
- Features and plan limits change often. Several items are labeled "public preview" (AI-detected secrets, reachability analysis). Check again before the paper is final.
- Dependabot and `npm audit` only find known, published weaknesses. Secret scanning finds secrets by pattern. None of this proves any code is secure. The product is only an idea; nothing here shows it is secure or compliant.
- The npm audit page (2023) is older than the npm CLI page (2026). The npm CLI is at version 12 in the docs, but the machine I checked has 11.17.0.
- Plan wording ("GitHub Secret Protection", "GitHub Code Security") is GitHub's current product naming. I did not check prices.

## Not read

- The pages these docs link to for setup steps (configuring Dependabot alerts, configuring code scanning, enabling push protection, supported secret patterns list, validity checks, partner program, CodeQL pages, SARIF support, dependency review, SBOM, artifact attestations).
- npm's "Generating provenance statements" and "About registry signatures" pages (not linked from the audit page body).
- I did not test any of the tools. I did not check GitHub's pricing page.
