# OWASP Top 10:2025 checklist for code review

Source: OWASP Foundation, OWASP Top 10:2025 introduction,
https://top10.owasp.org/2025/0x00_2025-Introduction/
The category names below match the OWASP 2025 introduction page. Read the
category's own page there for exact definitions before quoting it.

Contents: A01 to A10, Always check, What code reading cannot prove

## A01 Broken Access Control

Users can act outside their permissions. In the 2025 list this also covers
SSRF (server-side request forgery, where the server is tricked into fetching
internal addresses).

- Every route and action checks who the user is and what they may do.
- Data lookups use the logged-in user, not only an ID from the request.
- Admin features are guarded on the server, not just hidden in the UI.
- Server code that fetches a URL from user input limits where it can go.

## A02 Security Misconfiguration

- Debug mode, sample accounts, and default passwords are off.
- Error pages do not show stack traces to users.
- CORS (which sites may call your API) is not set to allow everyone.
- Security headers are set; cloud storage is not public by accident.

## A03 Software Supply Chain Failures

Risks from the code you depend on and the way you build it.

- Lock files are committed; versions are pinned.
- Dependencies are checked with `npm audit`, `pip-audit`, or similar.
- Packages come from trusted sources; names are not look-alikes.
- Build and install scripts are reviewed; CI secrets are protected.
- Consider an SBOM (software bill of materials, a list of what is inside).

## A04 Cryptographic Failures

- Passwords are hashed with bcrypt, scrypt, or Argon2, never stored in plain
  text or fast hashes like MD5.
- Data in transit uses HTTPS; sensitive data at rest is encrypted.
- No home-made encryption; keys are not in the code.

## A05 Injection

Untrusted input is run as a command or query.

- Database queries use parameters, not string joining.
- Shell commands avoid user input; if needed, pass arguments as a list.
- Output to HTML is escaped to prevent XSS (cross-site scripting).
- Input is validated on the server, not only in the browser.

## A06 Insecure Design

Missing protection in the plan itself.

- Rate limits on login, signup, password reset, and costly actions.
- Sensitive actions need confirmation or re-login.
- Limits exist for upload size, request size, and counts.

## A07 Authentication Failures

- Sessions expire and are renewed after login; cookies are `Secure`,
  `HttpOnly`, and `SameSite`.
- Passwords reset through a safe, expiring link.
- Multi-factor authentication is available for important accounts.
- No default or shared credentials; failed logins are limited.

## A08 Software or Data Integrity Failures

- Updates, plugins, and packages are verified before use.
- CI/CD pipelines cannot be changed by untrusted users.
- Data from outside is not trusted when loaded back into objects.

## A09 Security Logging and Alerting Failures

- Logins, access failures, and admin actions are logged.
- Logs never contain passwords, tokens, or full card numbers.
- Someone is alerted to repeated failures.

## A10 Mishandling of Exceptional Conditions

New in 2025.

- Errors fail closed: when a check breaks, access is denied, not allowed.
- Every error path is handled; no empty catch blocks that hide failures.
- Error messages do not reveal internal details.
- Half-finished operations are rolled back.

## Always check

- Secrets: search for `password`, `secret`, `token`, `api_key`, private key
  headers, and `.env` files committed to the repo.
- `.gitignore` covers environment files and credentials.
- Personal data: collect only what is needed, and know where it is stored
  (rules such as GDPR and CCPA may apply, so recommend a legal check).

## What code reading cannot prove

Report these as "not verified":

- whether a vulnerable package is actually reachable
- live server, cloud, and network settings
- behavior under real attack
- anything that needs a professional penetration test or compliance audit
  (for example SOC 2 or ISO 27001)
