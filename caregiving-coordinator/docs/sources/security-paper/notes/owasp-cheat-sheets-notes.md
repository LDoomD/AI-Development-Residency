# Notes: OWASP Cheat Sheet Series (8 selected sheets)

- **Source:** OWASP Foundation. (n.d.). *OWASP cheat sheet series*. https://cheatsheetseries.owasp.org/ . Each sheet is cited by its own title, for example: OWASP Foundation. (n.d.). *Input validation cheat sheet*. https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
- **Label for the paper:** official project guidance (tier 1 in the source list, approved domain `cheatsheetseries.owasp.org`).
- **Read status (2026-11-18):** all 8 sheets read in full.
- **Local copies:** `caregiving-coordinator/docs/sources/security-paper/owasp-cheat-sheets/` (8 HTML files, saved earlier on 2026-11-18). The saved pages show no date on the page. The pages are living documents, so cite the retrieval date, 2026-11-18, in the bibliography.
- **There are no page numbers.** The sheets are web pages, so these notes cite the section heading that holds each point. APA 7 allows a heading or section name when a page number does not exist.
- **Status of each sheet:**

| Sheet | Status | Notes below |
|---|---|---|
| Input Validation | Read in full (2026-11-18) | Section A |
| Forgot Password | Read in full (2026-11-18) | Section B |
| Cryptographic Storage | Read in full (2026-11-18) | Section C |
| Authentication | Read in full (2026-11-18) | Section D |
| Authorization | Read in full (2026-11-18) | Section E |
| Logging | Read in full (2026-11-18) | Section F |
| Secrets Management | Read in full (2026-11-18) | Section G |
| Session Management | Read in full (2026-11-18) | Section H |

- **Side finding (from the site's menu on the saved pages):** the series also has sheets named "Nextjs Security", "NPM Security", "Multi Tenant Security", "Software Supply Chain Security", "Vulnerable Dependency Management" and "Zero Trust Architecture". They are not on the approved list. Read them only if the owner approves adding them.

## A. Input Validation Cheat Sheet (read in full)

| Point | Section |
|---|---|
| Input validation checks that data meets the application's rules before the application uses it. It reduces malformed data, invalid business operations and resource exhaustion. | Introduction |
| Validation is not enough on its own. Use parameterized queries for SQL and output encoding for cross-site scripting. Check authorization separately: a valid account identifier does not mean the caller may use that account. | Introduction |
| Check both syntax (type and format) and meaning (for example, a booking's end date must be after its start date). | Input Validation Strategies |
| Define rules for each kind of field: fixed choices, numbers and dates, strings, objects, arrays. | Input Validation Strategies (table) |
| Define what is allowed and reject the rest. Do not try to list every bad string. Blocking apostrophes rejects real names without making a database query safe. | Allowlist vs Denylist |
| Limit request size before parsing, use a maintained parser, and reject invalid requests with a clear error instead of going on with half-checked data. | Implementing Input Validation: Parse Safely, Then Validate; Validate Structured Data |
| Treat file name and content type as untrusted. An allowed file extension alone does not prove the content is safe. | File Upload Validation |
| Do not build links (such as password reset links) from the request's Host header. Build them from configuration, and accept only hostnames the application serves. | Host and Forwarded Headers |
| Validate on the server even when the browser checks too. Validate data from internal sources when it crosses a trust boundary. Do not log rejected input verbatim. | Common Pitfalls |

## B. Forgot Password Cheat Sheet (read in full)

| Point | Section |
|---|---|
| Password reset is a common source of flaws, such as user enumeration (telling an attacker which accounts exist). Return the same message and take the same time whether or not the account exists. | Introduction; Forgot Password Request |
| Add limits on automated reset requests, for example a per-account rate limit. | Forgot Password Request |
| After the user proves identity with an emailed token, they set a new password, are told by email that it changed (never sent the password), and log in the usual way. The site should not log them in automatically. | User Resets Password |
| A password reset alone may not restore a hacked account. The attacker may keep a live session or may have changed recovery details. After recovery, end existing sessions and invalidate outstanding reset links. | Account Recovery After Suspected Compromise |
| Reset tokens must be random from a cryptographically secure source, long enough to resist guessing, tied to one user, single use and stored securely. | General Security Practices |
| For emailed links use HTTPS, do not trust the Host header, add a no-referrer policy on the reset page and rate-limit guessing. | URL Tokens |
| Do not use security questions as the only way to reset a password. Do not lock an account in response to forgotten-password attempts, since that lets an attacker lock out a known user. | Security Questions; Account Lockout |
| The sheet's references are NIST SP 800-63B-4 (account recovery) and ASVS V6.4. | References |

## C. Cryptographic Storage Cheat Sheet (read in full)

| Point | Section |
|---|---|
| Start from a threat model (who you are protecting the data from). Encryption can be done at the application, database, filesystem or hardware level, and the right layer depends on the threat. Hardware encryption protects against theft of a server but not against a remote attacker. | Architectural Design; Where to Perform Encryption |
| "The best way to protect sensitive information is to not store it in the first place." | Minimize the Storage of Sensitive Information |
| For symmetric encryption use AES with a key of at least 128 bits (ideally 256) and an authenticated mode (GCM or CCM first). Do not write a custom algorithm. | Algorithms; Custom Algorithms; Cipher Modes |
| RSA and elliptic-curve methods are not safe against a future quantum computer. The sheet points to NIST's ML-KEM (FIPS 203) for migration, and says it does not replace AES for stored data. | Post-Quantum Consideration |
| Use cryptographically secure random generators for keys, session IDs and reset tokens. Ordinary random functions are not safe for this. The sheet lists the safe function for each language (for example `crypto.randomBytes` in Node.js). | Secure Random Number Generation |
| Design so the application stays secure even if encryption fails. Do not rely on encrypted URL parameters. Enforce access control. | Defense in Depth |
| Use the key storage the platform or cloud provider offers where available. Where none is available, do not hard-code keys, do not commit keys to version control, protect key files with restrictive permissions and avoid keeping keys in environment variables (they can leak through some functions or files). | Key Management: Key Storage |
| Store keys apart from the data. Protect a data key with a separate key-encrypting key (envelope encryption). Rotate keys when compromised, after a set period, or when the algorithm weakens. | Key Management: Separation of Keys and Data; Encrypting Stored Keys; Key Lifetimes and Rotation |

## D. Authentication Cheat Sheet (read in full)

| Point | Section |
|---|---|
| Make user IDs random so they cannot be guessed or counted. Allow an email address as the username only if it was verified at sign-up. | Authentication General Guidelines: User IDs; Usernames |
| Passwords: set a minimum length, allow at least 64 characters, allow all characters including spaces, and do not force upper-case, number or symbol rules. The sheet quotes NIST SP 800-63B: under 8 characters is weak with multi-factor sign-in, and under 15 is weak without it. Do not force regular password changes. Change a password when a leak is found. | Implement Proper Password Strength Controls |
| Block common and breached passwords. The sheet names the Pwned Passwords service and says attackers use password lists and credentials from other breaches. | Implement Proper Password Strength Controls: Block common and previously breached passwords |
| Ask for the current password before a user changes their password or email, and again before sensitive actions. | Change Password Feature; Require Re-authentication for Sensitive Features |
| Send passwords only over TLS (the secure connection). The login page and all pages after login must use it. | Transmit Passwords Only Over TLS |
| Show the same error for a wrong user, wrong password, locked or missing account. Different messages, or different response times, let an attacker find which accounts exist. | Authentication and Error Messages; Authentication Responses |
| The sheet gives example wording: "If that email address is in our database, we will send you an email to reset your password." | Incorrect and correct response examples (Password recovery) |
| Automated attacks are brute force (many passwords, one account), credential stuffing (pairs stolen from another site) and password spraying (one weak password, many accounts). | Protect Against Automated Attacks |
| Multi-factor authentication is the best defense against most password attacks. The sheet cites a Microsoft analysis that suggests it would have stopped 99.9% of account compromises. | Multi-Factor Authentication |
| Use login throttling and lockouts tied to the account, not only the address, but take care that lockout cannot be used to lock out other people. A CAPTCHA is a defense-in-depth step, not a fix. | Login Throttling; Account Lockout; CAPTCHA |
| Do not use security questions for sign-in. Log and review authentication failures and lockouts. | Security Questions and Memorable Words; Logging and Monitoring |
| For sign-in with another identity provider use OpenID Connect and check the token's issuer, audience, signature and expiry. Link accounts by issuer plus subject, never only by matching email. | OpenID Connect; Secure Federated Account Linking |
| Passkeys and FIDO2 use public-key sign-in, which resists phishing. Do not assume the keys are hardware-backed unless verified. | FIDO; Hardware-backed Key Storage |
| When a user changes their email, confirm through their current session, ask for multi-factor or password, and email both the old and new addresses. | Changing A User's Registered Email Address |
| Adaptive (risk-based) sign-in may use signals such as device or location to ask for more proof. These are risk signals, not replacements for authentication. | Adaptive or Risk Based Authentication |

## E. Authorization Cheat Sheet (read in full)

| Point | Section |
|---|---|
| Authentication proves who you are. Authorization decides what you may do. A logged-in user is often not allowed to use everything. | Introduction |
| The sheet says a common weakness is "horizontal privilege escalation", meaning one signed-in user reaching another user's data. Without good logs, such violations can go unnoticed. | Introduction |
| Least privilege: give each person only the access needed, across and up the hierarchy. Map each user type to each resource and operation during design, write tests for it, and review permissions later for "privilege creep". | Enforce Least Privileges |
| Deny by default: the application must always decide, and when no rule matches the answer is no. Prefer your own explicit setting over a framework's default, because defaults can change. | Deny by Default |
| Check permission on every request, from every source, using one central mechanism. One missed check can expose a resource. | Validate the Permissions on Every Request |
| Assume any third-party component could have an authorization flaw. Keep a process to find and respond to vulnerable components, use dependency checking tools, and use more than one layer of defense. Do not rely on default configuration, and test it. | Thoroughly Review the Authorization Logic of Chosen Tools and Technologies |
| The sheet recommends attribute-based (ABAC) and relationship-based (ReBAC) access control over simple role-based (RBAC) control. It says RBAC does a poor job on per-object decisions, can suffer "role explosion", and is hard to use when separate organizations share the same resources. It gives a ReBAC example: only the user who created a post may edit it. | Prefer Attribute and Relationship Based Access Control over RBAC |
| Do not let a user reach another record just by changing an ID in a link. Hiding or randomizing IDs is not enough. Check access for the specific object on every request. | Ensure Lookup IDs are Not Accessible Even When Guessed |
| Protect static files and cloud storage with the same access rules. | Enforce Authorization Checks on Static Resources |
| Never rely on checks in the browser. Do the checks on the server, at the gateway, or in serverless functions. | Verify that Authorization Checks are Performed in the Right Location |
| Handle failed checks safely, centrally and without exposing debug information. | Exit Safely when Authorization Checks Fail |
| Log access decisions in a consistent format. Both too little and too much logging are weaknesses. Keep clocks in sync. | Implement Appropriate Logging |
| Write unit and integration tests for the authorization rules. The sheet says tests catch easy flaws, not sophisticated attacks. | Create Unit and Integration Test Cases for Authorization Logic |

## F. Logging Cheat Sheet (read in full)

| Point | Section |
|---|---|
| Application logs give much more insight than server logs alone, because the application knows who the user is and what they did. | Introduction; Design, implementation, and testing: Event data sources |
| Logs serve operational uses (debugging, performance) and security uses (spotting incidents, audit trails of data added, changed, deleted or exported, compliance). Audit trails and security logs often have different purposes and may be kept separate. | Purpose |
| Treat data from other systems as untrusted. Record logs in a protected place, with restricted permissions, and do not expose them on web-accessible pages. | Event data sources; Where to record event data |
| Decide what to log in the requirements and design stage, in proportion to risk. A blind checklist can cause "alarm fog" that hides real problems. | Which events to log |
| Where possible always log: input validation failures, authentication successes and failures, authorization (access control) failures, session failures, application errors, use of higher-risk functions such as user administration changes and access to sensitive data, data imports and exports, and legal opt-ins such as consent to personal data use. | Which events to log |
| Each entry should say when, where, who and what: time, the application and page, the user and source address, the type and severity of event. The sheet also lists optional details such as the action, the object, the result and the reason. | Event attributes |
| Do not write some data into logs directly, or remove, mask, hash or encrypt it first. The list includes session IDs, access tokens, passwords, database connection strings, encryption keys, payment card data, and "sensitive personal data ... e.g. health, government identifiers, vulnerable people". | Data to exclude |
| Never log data unless it is legally allowed. Do not log data a user has not consented to. Consider de-identification (deleting or pseudonymizing identifiers) where identity is not needed. | Data to exclude |
| Strip line breaks and delimiters from logged input to prevent log injection (an attacker faking log entries). Use a structured format such as JSON, and limit the size of logged input. | Event collection; Attacks on Logs: Log Injection |
| A failure in the logging system must not stop the application or leak information. | Event collection |
| Test the logging: that it works as specified, that logs cannot be used to fill up disk space, that access to logs is controlled, and that log data cannot be used to cause denial of service to other users. | Verification |
| Protect logs from tampering and from unauthorized reading. Build tamper detection, restrict and review who can read logs, record all access to them, and send them over a secure protocol. | Protection |
| Logs must be kept for the required retention period and not beyond it. Legal and contract duties may set the period. | Disposal of logs |
| Alerts should signal the responsible teams about serious events right away. | Monitoring of events |
| The sheet lists attacks on logs by confidentiality, integrity, availability and accountability (for example, flooding logs, or causing the wrong identity to be logged). | Attacks on Logs |
| The sheet's references are NIST SP 800-92 (log management) and the syslog protocol (RFC 5424). | References |

## G. Secrets Management Cheat Sheet (read in full)

| Point | Section |
|---|---|
| Secrets are API keys, database passwords, access permissions, SSH keys and certificates. Many organizations leave them hard-coded in source code and settings files. Services that share one secret make it hard to find the source of a leak. | 1 Introduction |
| Apply least privilege to the secrets themselves: engineers should not be able to read every secret. | 2.3 Access Control |
| Reduce human handling. Use automated creation and rotation, and short-lived "dynamic" credentials where possible. | 2.4 Automate Secrets Management |
| Audit who asked for a secret, when it was used and expired, and any failed attempts. Keep correct time stamps. | 2.6 Auditing |
| A secret has a life cycle: creation, rotation, revocation and expiration. User passwords are not rotated on a schedule, only when compromise is suspected (the sheet cites NIST). | 2.7 Secret Lifecycle (2.7.1 to 2.7.4) |
| Never send secrets in plain text. Use TLS everywhere. | 2.8 Transport Layer Security (TLS) Everywhere |
| Back up secrets safely, test restores, and keep a tested emergency ("break-glass") way to recover access. | 2.9 Downtime, Break-glass, Backup and Restore |
| Secrets stored in the build tool (for example GitHub secrets) are visible to jobs and maintainers. Limit their scope, review who can see them, check that forks do not copy them and rotate them. The sheet's preferred option is that the build pipeline does not handle runtime secrets at all. | 3.2 Where should a secret be? |
| Prefer a dedicated secrets service from the cloud provider over a general settings store. Look for fine-grained access, rotation support, encryption, audit logging and versioning. | 4.1 Choosing a Secret Management Service |
| Do not build secrets into container images. Environment variables are not recommended unless other methods are not possible, because they can be seen by all processes and can show up in logs and dumps. | 5.1 Injection of Secrets |
| Monitor who accesses a secret, from where and how. If a secret is used from an unexpected address, alert and assume it is compromised. | 6.4 Security Event Monitoring is Key |
| Use authenticated encryption such as AES-256 with GCM. Do not store keys next to the secrets they protect unless the keys are encrypted. | 7.1 Encryption Types to Use; 7.3 Where to store the Encryption Keys? |
| Detection: scan for secrets before they are committed (for example with a pre-commit check), use more than one tool, and make secrets part of threat modeling. | 8.1 General detection approaches |
| When a secret leaks, respond fast: revoke it, rotate it, delete the exposed copy, and review the logs. Removing a secret from code history rewrites git history and can break links, so plan for that. | 9.2 Remediation |
| Secrets in logs must be removed in a way that keeps the log trustworthy. Secrets should never be logged. | 8.3 Detection lifecycle; 9.2 Remediation |

## H. Session Management Cheat Sheet (read in full)

| Point | Section |
|---|---|
| After sign-in, the session ID is temporarily as powerful as the user's password. If someone steals or guesses it, they can pretend to be that user (session hijacking). | Introduction |
| A session ID must have at least 64 bits of randomness, from a cryptographically secure generator, and carry no personal data. Keep the meaning on the server. Use the session ID your framework creates. | Session ID Properties: Entropy; Length; Content (or Value) |
| Use cookies for the session ID, not the URL. Do not accept a session ID by another route, which stops session fixation (an attacker setting the ID). | Session Management Implementation; Used vs. Accepted Session ID Exchange Mechanisms |
| Use HTTPS for the whole session and set the `Secure`, `HttpOnly` and `SameSite` cookie attributes. The sheet recommends the `__Host-` cookie name prefix for session IDs. | Transport Layer Security; Cookies |
| Do not put authentication tokens or session IDs in `localStorage` or `sessionStorage`. Any script on the page can read them, so one cross-site scripting flaw exposes every token. Use an HttpOnly, Secure, SameSite cookie. | HTML5 Web Storage API (the warning box under "The localStorage API") |
| Create a new session ID after any privilege change, such as sign-in, password change or role change, and destroy the old one. | Renew the Session ID After Any Privilege Level Change |
| Ask the user to sign in again after risk events: password or email changes, sign-in from a new device, or account recovery. | Reauthentication After Risk Events |
| Every session needs an idle timeout and an absolute timeout, enforced on the server. The sheet gives common idle ranges: 2 to 5 minutes for high-value applications and 15 to 30 minutes for low-risk ones. | Session Expiration; Automatic Session Expiration |
| Provide a visible logout button. Logout must invalidate the session on the server, not just clear the cookie. Revoke every ID of that session together. | Manual Session Expiration: Logout Button |
| Set `Cache-Control: no-store` on sensitive pages, and use the `Clear-Site-Data` header at logout. | Web Content Caching and Clear-Site-Data |
| Detect session guessing and unusual session changes. Binding a session to IP address or browser details helps detection but a skilled attacker can get around it. | Session Attacks Detection |
| Log the life cycle of sessions (creation, renewal, destruction, timeouts), but never log raw session IDs. Log a salted hash so entries can be matched. Protect any admin tool that can view or impersonate sessions. | Logging Sessions Life Cycle |
| Let users see their active sessions and end them remotely. | Simultaneous Session Logons |
| The sheet's references are NIST SP 800-63B-4 (session management) and MDN. | References |

## Possible use and limits (sheets A to H)
- **Topic 5 (what it includes):** the Session Management sheet supports the point that a sign-in session is a target in itself, and that timeouts, secure cookies and re-sign-in after risk events limit damage. The proposed coordinator uses a managed sign-in service (Supabase Auth), so which of these controls the service provides is a question for its own documentation, not for this sheet.
- **Topic 7 (tools and skills):** the Secrets Management sheet supports secret scanning in a code repository (GitHub secret scanning), keeping keys out of source code, and a plan to revoke and rotate a leaked key. The sheet does not name Vercel or Supabase, so the paper must not say it describes them.
- **Topic 8:** the Logging sheet says health information and data about vulnerable people should not be written into logs directly, and that access to sensitive data, exports and consent changes are events to log. This matches the proposed coordinator's access log and consent records in a general way. The paper may describe this as a plan, never as built or compliant.
- **Topic 8:** the Authorization sheet's points on least privilege, deny by default, checking every request, and relationship-based control describe the kind of rules a care circle with roles would need. The sheet does not mention health or caregiving. The paper may say these are controls the idea plans to use, never that they are built.
- **Currency note:** the Authorization sheet refers to the OWASP Top 10 2021 and to an older version of ASVS (4.0.3). It has not been updated to the 2025 list, so cite the 2025 list for ranking claims.
- **Topic 5 (what it includes):** Authentication sheet supports identity and sign-in controls such as multi-factor authentication, generic error messages, lockout and re-authentication for sensitive changes.
- **Topic 4 and 7:** input validation as a developer skill; secure password reset; the idea of not storing sensitive data you do not need; key and secret handling.
- **Topic 8:** the proposed coordinator will send invite emails and may have a password reset flow. These sheets describe controls it would need to plan. The paper must not say they are done.
- **Limits:** cheat sheets are guidance written by volunteers and updated over time, not a standard. They have no page numbers. The Input Validation page links to ASVS and NIST SP 800-63B-4, so those are better sources for any claim that needs a requirement number.
