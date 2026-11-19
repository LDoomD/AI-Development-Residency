# Notes: OWASP Application Security Verification Standard (ASVS) 5.0.0

- **Source:** OWASP Foundation. (2025). *Application security verification standard* (Version 5.0.0). https://github.com/OWASP/ASVS/releases/tag/v5.0.0_release (the standard's own pages are at https://owasp.org/www-project-application-security-verification-standard/). Licensed CC BY-SA 4.0 (printed p. 7).
- **Label for the paper:** official project standard (tier 1 in the source list). OWASP says it does not certify anyone, and any claim of "ASVS certification" is not endorsed by OWASP (printed p. 18).
- **Local copy:** `caregiving-coordinator/docs/sources/security-paper/owasp-asvs/OWASP_ASVS_5.0.0_en.pdf` (123 PDF pages, created May 29, 2025). Version check: this is the fixed v5.0.0 release dated 2025-05-30. GitHub's rolling "latest" build (2026-11-17) was not used.
- **Page numbers below are the printed page numbers.** Printed page = PDF page − 1.
- **Read status (2026-11-18):** the whole document was read in order. The status of each part is in the table. Chapters V10, V17 and Appendix C are noted more briefly because the proposed coordinator uses little or none of them (no OAuth provider of its own, no WebRTC, no custom cryptography).

| Part | Printed pages | Status |
|---|---|---|
| Frontispiece, Preface, What is the ASVS, How to use, Assessment, Changes from v4 | 7 to 22 | Read in full |
| V1 Encoding and Sanitization | 23 to 28 | Read in full |
| V2 Validation and Business Logic | 28 to 31 | Read in full |
| V3 Web Frontend Security | 32 to 37 | Read in full |
| V4 API and Web Service | 38 to 41 | Read in full |
| V5 File Handling | 41 to 43 | Read in full |
| V6 Authentication | 44 to 52 | Read in full |
| V7 Session Management | 52 to 56 | Read in full |
| V8 Authorization | 56 to 59 | Read in full |
| V9 Self-contained Tokens | 59 to 61 | Read in full |
| V10 OAuth and OIDC | 61 to 69 | Read in full |
| V11 Cryptography | 70 to 75 | Read in full |
| V12 Secure Communication | 75 to 77 | Read in full |
| V13 Configuration | 77 to 81 | Read in full |
| V14 Data Protection | 81 to 84 | Read in full |
| V15 Secure Coding and Architecture | 84 to 88 | Read in full |
| V16 Security Logging and Error Handling | 88 to 92 | Read in full |
| V17 WebRTC | 92 to 95 | Read in full |
| Appendices A to E (glossary, references, cryptography standards, recommendations, contributors) | 96 to 122 | Read in full (the contributor list only skimmed) |

## A. How the standard works (printed pp. 7 to 22)

| Point | Page |
|---|---|
| ASVS 5.0 has about 350 requirements in 17 chapters. A table in the document counts 345 total and 70 at Level 1 (20%). | pp. 9, 22 |
| It is a list of security requirements that architects, developers, testers and buyers can use to define, build, test and verify applications. | p. 7 |
| The requirements are written as goals, not as exact methods, so that each says why it exists. Every requirement must be verifiable as pass or fail. | pp. 8, 10 |
| "Documented security decisions": for rules that differ for each application (permissions, input rules, how sensitive data is protected), the standard asks the organization to write down its decision, and separately to implement it. Documentation requirements are always the first section of a chapter. | pp. 9, 11 to 12 |
| The standard has three levels: Level 1 is the first layer of defense and about 20% of requirements; Level 2 adds about 50% and is the level "most applications should be striving to achieve" (about 70% in all); Level 3 adds the last ~30%, mostly defense in depth and hard-to-implement controls. | pp. 12 to 14 |
| Which level to choose is the organization's decision from its risk and its users' expectations. The standard's own example: an early-stage startup that collects limited sensitive data may start with Level 1; a bank would find it hard to justify less than Level 3. | p. 14 |
| Chapters can be filtered. For example, a machine-to-machine API can skip the web frontend chapter, and an app with no OAuth or WebRTC can skip those chapters. | p. 14 |
| Requirements are referenced as `v5.0.0-<chapter>.<section>.<requirement>`, for example v5.0.0-1.2.5. The version must be included because numbers change between major versions. | pp. 15 to 16 |
| The ASVS does not cover things like backups run by an external process, or DNS. It says "there is no such thing as scope for attackers", so requirements should be read alongside guidance on build pipelines, hosting and operations. | p. 10 |
| Uses named: security architecture guidance, a secure coding reference, a guide for automated unit and integration tests, developer training, and buying software ("must be developed at ASVS level X"). | pp. 16 to 17 |
| To verify, running an automated scanner alone is not enough. The standard says testable using automation is not the same as running an off-the-shelf tool, and recommends documentation- or source-led penetration testing over "black box" testing. | pp. 19 to 20 |
| Changes from 4.x: of 286 requirements in 4.0.3, only 11 stay unchanged and 109 (38%) are no longer separate requirements. New or restructured chapters: OAuth and OIDC, WebRTC, Self-contained Tokens, Web Frontend Security, Secure Coding and Architecture. Direct mappings to CWE and NIST are no longer kept. | pp. 20 to 22 |

## B. V1 Encoding and Sanitization (printed pp. 23 to 28)

| Point | Where |
|---|---|
| The chapter's goal: stop untrusted data from being treated as commands. Use safer interfaces (parameterized queries, auto-escaping, templating frameworks); otherwise encode, escape or sanitize. | p. 23, Control Objective |
| 1.1.1, 1.1.2 (Level 2): decode input once into a canonical form before validation; encode output as the last step before the interpreter. | p. 24 |
| 1.2.1 to 1.2.5 (Level 1): encode output for the context (HTML, URL, JavaScript), use parameterized queries or ORMs against injection, and protect against OS command injection. Note: table and column names cannot be escaped. | pp. 24 to 25 |
| 1.3.1 (L1): sanitize HTML from editors with a well-known library. 1.3.2 (L1): avoid `eval()` and similar dynamic code execution. | p. 26 |
| 1.3.6 (L2): protect against server-side request forgery with an allowlist of protocols, domains, paths and ports. 1.3.7 (L2): no templates built from untrusted input. | p. 26 |
| 1.5.1 (L1): configure XML parsers restrictively. 1.5.2 (L2): safe handling of deserialization. | pp. 27 to 28 |
| The Level 3 items include CSV and formula injection in exports (1.2.10) and regular expression backtracking (1.3.12). | pp. 25, 27 |

## C. V2 Validation and Business Logic (printed pp. 28 to 31)

| Point | Where |
|---|---|
| The goals: input matches business expectations, the business flow is processed in order and cannot be bypassed, limits stop automated abuse, and high-value flows consider abuse cases. | pp. 28 to 29 |
| 2.1.1 (L1), 2.1.2 and 2.1.3 (L2): the documentation must define validation rules, how related data is checked together, and business limits per user and across the application. | p. 29 |
| 2.2.1 (L1): validate input against an allow list or expected structure. For Level 1, this can focus on input used to make business or security decisions; at Level 2 and up it applies to all input. 2.2.2 (L1): enforce validation at a trusted service layer; client-side validation is only for usability. | p. 30 |
| 2.3.1 (L1): process a user's flow in the expected order without skipping steps. 2.3.3 (L2): use transactions so an operation completes fully or rolls back. 2.3.5 (L3): high-value flows need approval from more than one person. | pp. 30 to 31 |
| 2.4.1 (L2): anti-automation controls against excessive calls, data exfiltration, garbage data, quota exhaustion and denial of service. | p. 31 |

## D. V3 Web Frontend Security (printed pp. 32 to 37)

| Point | Where |
|---|---|
| The chapter applies to browser-facing applications, not to machine-to-machine solutions. | p. 32 |
| 3.2.1 (L1): stop browsers from rendering content in the wrong context (for example a user-uploaded file requested directly). 3.2.2 (L1): show text with safe functions such as `textContent`. | pp. 32 |
| 3.3.1 (L1): cookies must have the `Secure` attribute and use the `__Host-` or `__Secure-` name prefix. 3.3.2 and 3.3.3 (L2): set `SameSite` by purpose; use `__Host-` unless shared across hosts. 3.3.4 (L2): session cookies that scripts do not need must be `HttpOnly`. | p. 33 |
| 3.4.1 (L1): send an HSTS header on all responses, with a maximum age of at least 1 year (and all subdomains from Level 2). 3.4.2 (L1): the CORS allowed-origin value must be fixed or checked against an allowlist. | p. 34 |
| 3.4.3 (L2): send a Content-Security-Policy that at least includes `object-src 'none'` and `base-uri 'none'`, using an allowlist or nonces or hashes. 3.4.4 (L2): `X-Content-Type-Options: nosniff`. 3.4.5 (L2): set a referrer policy. 3.4.6 (L2): use `frame-ancestors` so the page cannot be embedded by default; the standard calls `X-Frame-Options` obsolete. | p. 34 |
| 3.5.1 to 3.5.3 (L1): defend against cross-site request forgery with anti-forgery tokens or extra headers, require cross-origin protection for sensitive functions, and use POST, PUT, PATCH or DELETE (not GET) for sensitive actions. | pp. 35 to 36 |
| 3.5.4 (L2): host separate applications on different hostnames. | p. 36 |
| 3.6.1 (L3): external scripts and styles must be static and versioned and use Subresource Integrity, or have a documented security decision. | p. 37 |
| 3.7.1 (L2): use only client-side technologies that are still supported (not Flash or ActiveX). 3.7.2 (L2): only redirect to other sites from an allowlist. | p. 37 |

## E. V4 API and Web Service (printed pp. 38 to 41)

| Point | Where |
|---|---|
| The chapter covers applications that expose APIs (JSON, XML, GraphQL). Authentication, sessions and validation rules from other chapters also apply to APIs. | p. 38 |
| 4.1.1 (L1): every response with a body has a correct `Content-Type` with a charset. 4.1.2 (L2): only user-facing endpoints redirect from HTTP to HTTPS automatically. 4.1.3 (L2): headers set by a proxy or load balancer (such as `X-Forwarded-*` or `X-User-ID`) cannot be overridden by the end user. | p. 38 |
| 4.2 covers HTTP message structure (request smuggling and header injection), all Level 2 or 3. 4.3 covers GraphQL (depth limits, introspection off in production). 4.4 covers WebSocket (4.4.1, L1: use WSS, the secure version, for every connection). | pp. 39 to 41 |

## F. V5 File Handling (printed pp. 41 to 43)

| Point | Where |
|---|---|
| The risks are denial of service, unauthorized access and storage exhaustion. 5.1.1 (L2): document the permitted file types, extensions and maximum size for each upload feature. | p. 41 |
| 5.2.1 (L1): only accept files of a size the application can process. 5.2.2 (L1): check that the extension matches the content (such as magic bytes), at Level 1 for files used in business or security decisions, at Level 2 and up for all files. | p. 42 |
| 5.3.1 (L1): files uploaded into a public folder are not run as server-side code. 5.3.2 (L1): do not build file paths from user-submitted filenames (path traversal). | p. 43 |
| 5.4.3 (L2): scan files from untrusted sources with antivirus. | p. 43 |

## G. V6 Authentication (printed pp. 44 to 52)

| Point | Where |
|---|---|
| The chapter is based on NIST SP 800-63B but focuses on common threats. It says that where full NIST SP 800-63 compliance is needed, readers should use NIST SP 800-63 itself. It also says the adaptive (risk-based) sign-in feature is covered in the Authorization chapter. | p. 44 |
| 6.1.1 (L1): documentation must say how rate limiting and anti-automation defend against credential stuffing and brute force, and how malicious account lockout is prevented. 6.1.3 (L2): document every authentication pathway. | pp. 44 to 45 |
| **Passwords.** 6.2.1 (L1): at least 8 characters, though at least 15 is strongly recommended. 6.2.2 (L1): users can change their password. 6.2.3 (L1): changing it needs the current and new password. 6.2.4 (L1): check new passwords against at least the top 3,000 common passwords. 6.2.5 (L1): no composition rules. 6.2.7 (L1): paste, browser helpers and password managers are allowed. 6.2.8 (L1): the password is checked exactly as received, without truncation or case change. | pp. 45 to 46 |
| 6.2.9 (L2): passwords of at least 64 characters are allowed. **6.2.10 (L2): a password stays valid until it is found compromised or the user changes it; the application must not require periodic rotation.** 6.2.12 (L2): check passwords against a set of breached passwords. | p. 46 |
| General: Level 2 applications must force multi-factor authentication. Level 3 must use hardware-based authentication. The chapter admits this is "a relatively aggressive stance" and says any relaxation needs a clear plan to mitigate the risk. It also notes that, at release, NIST SP 800-63 considers email not acceptable as an authentication mechanism. | p. 46 |
| 6.3.1 (L1): defend against credential stuffing and brute force as documented. 6.3.2 (L1): no default accounts such as root or admin. 6.3.3 (L2): require multi-factor, or a combination of single-factor methods, to access the application. 6.3.6 (L3): email is not used as a single-factor or multi-factor method. 6.3.8 (L3): valid users cannot be deduced from failed sign-ins (error text, response codes, timing), including in registration and forgot password. | pp. 46 to 47 |
| 6.4.1 (L1): system-generated initial passwords or activation codes are random and expire soon, and cannot become the long-term password. 6.4.2 (L1): no password hints or "secret questions". 6.4.3 (L2): a forgotten-password reset must not bypass multi-factor sign-in. | p. 48 |
| 6.5: one-time codes and recovery codes can be used once, are generated by a secure random generator, and out-of-band requests last at most 10 minutes (TOTP codes 30 seconds). | p. 49 |
| 6.6: email and VoIP are not permitted as out-of-band methods. SMS and phone are "restricted" by NIST; if offered, the number must be validated, stronger options offered, and risks explained. For Level 3, not available. The chapter warns about "push bombing". | pp. 49 to 50 |
| 6.8: when using an outside identity provider, identify the user by the provider's ID plus the user's ID at that provider, validate signatures on assertions, and check the strength of sign-in the provider reports. | pp. 51 to 52 |

## H. V7 Session Management (printed pp. 52 to 56)

| Point | Where |
|---|---|
| Sessions must be unique per person, hard to guess, and invalidated when no longer needed or after inactivity. Cookie rules are in V3 and token rules in V9. | pp. 52 to 53 |
| 7.1: the timeouts, the number of parallel sessions and any shared sign-on setup must be documented, with a risk analysis. | p. 53 |
| 7.2.1 (L1): verify session tokens in a trusted backend service. 7.2.2 (L1): use dynamically generated tokens, not static API secrets and keys. 7.2.3 (L1): reference tokens need at least 128 bits of randomness from a secure generator. 7.2.4 (L1): issue a new session token on every authentication, including re-authentication. | p. 54 |
| 7.3.1 and 7.3.2 (L2): an inactivity timeout and an absolute maximum session lifetime, set from risk analysis and the documented decisions. The 5.0 text does not give fixed times. | p. 54 |
| 7.4.1 (L1): when logout or expiry happens, the session cannot be used again. For self-contained tokens this needs a list of ended tokens, a cutoff time per user, or key rotation. 7.4.2 (L1): end all sessions when an account is disabled or deleted. 7.4.3 (L2): offer to end other sessions after a password or MFA change. | p. 55 |
| 7.5.1 (L2): require full re-authentication before changing email, phone, MFA settings or recovery details. 7.5.2 (L2): users can see and end their active sessions. | pp. 55 to 56 |

## I. V8 Authorization (printed pp. 56 to 59)

| Point | Where |
|---|---|
| The goals: written authorization rules, and least privilege for every consumer (users, servers, other clients). | p. 56 |
| 8.1.1 (L1): documentation must define rules for function-level and data-specific access based on permissions and resource attributes. 8.1.2 (L2): also field-level rules for read and write. | p. 57 |
| 8.2.1 (L1): function-level access only for consumers with explicit permission. **8.2.2 (L1): data-specific access is limited to consumers with explicit permission to specific data items, to stop insecure direct object reference (IDOR) and broken object level authorization (BOLA).** 8.2.3 (L2): the same for individual fields (BOPLA). | pp. 57 to 58 |
| 8.3.1 (L1): enforce authorization at a trusted service layer, not in browser code. 8.3.3 (L3): decisions use the permissions of the original user, not of an intermediary service. | p. 58 |
| 8.4.1 (L2): multi-tenant applications must have controls so one tenant's operations never affect tenants they have no permission to interact with. | p. 59 |

## J. V9 Self-contained Tokens (printed pp. 59 to 61)

| Point | Where |
|---|---|
| A self-contained token (such as a JWT) holds the data a receiving service relies on to make decisions, so the service must check its integrity and that it is meant for it. | p. 59 |
| 9.1.1 (L1): check the signature or MAC before trusting the token. 9.1.2 (L1): only allowed algorithms, and never "None". 9.1.3 (L1): get the verification keys only from trusted, pre-set sources. | p. 60 |
| 9.2.1 (L1): accept the token only inside its validity period (`nbf`, `exp`). 9.2.2 and 9.2.3 (L2): check the token type and that it is for this service (`aud`). | pp. 60 to 61 |

## K. V10 OAuth and OIDC (printed pp. 61 to 69)

| Point | Where |
|---|---|
| OAuth is a framework for delegated authorization (letting one application act for a user on another). OpenID Connect (OIDC) adds a user-identity layer on top. The chapter says it is "vitally important" to use a well-known industry-standard authorization server and its recommended settings. | pp. 61 to 62 |
| 10.1.1 (L2): tokens go only to components that strictly need them (for a browser app, access and refresh tokens stay on the backend). 10.4.1 (L1): the server checks redirect addresses against a pre-registered list with exact string matching. 10.4.2 and 10.4.3 (L1): an authorization code can be used once and is short-lived (at most 10 minutes for Levels 1 and 2). 10.4.4 (L1): the implicit and password grants must no longer be used. 10.4.6 (L2): require PKCE. 10.7 (L2): the user's consent is required for each authorization request and can be reviewed and revoked. | pp. 63 to 69 |
| Most of the rest of the chapter (sender-constrained tokens, pushed authorization requests, back-channel logout) is Level 2 or 3 and applies to people who run an authorization server. | pp. 64 to 68 |

## L. V11 Cryptography (printed pp. 70 to 75)

| Point | Where |
|---|---|
| The chapter wants cryptography that fails safely, can be changed, is inventoried and is ready for quantum computers. It says "encrypting everything is wasteful; not encrypting anything is legally negligent." | pp. 70 |
| 11.1.1 and 11.1.2 (L2): a written key-management policy (following NIST SP 800-57) and an inventory of all keys, algorithms and certificates. 11.1.4 (L3): a plan to move to post-quantum cryptography. | p. 71 |
| 11.2.1 (L2): use validated cryptographic libraries. 11.2.2 (L2): "crypto agility", meaning algorithms and keys can be swapped. 11.2.3 (L2): at least 128 bits of security. | pp. 71 to 72 |
| 11.3.1 and 11.3.2 (L1): no insecure block modes such as ECB; use approved ciphers and modes such as AES-GCM. 11.4.1 (L1): approved hash functions only; MD5 must not be used for any cryptographic purpose. 11.4.2 (L2): store passwords with an approved, computationally intensive password hashing function. | pp. 72 to 73 |
| 11.5.1 (L2): values that must not be guessable come from a secure random generator with at least 128 bits of entropy. The text adds: UUIDs do not meet this. | p. 74 |
| Appendix C lists approved, legacy and disallowed algorithms. For password hashing it approves argon2id, scrypt, bcrypt and PBKDF2 with minimum settings (for example PBKDF2-HMAC-SHA-256 with at least 600,000 iterations). It lists MD5, DES, RC4 and ECB as disallowed. It points to NIST FIPS 203, 204 and 205 for post-quantum methods. | Appendix C, pp. 103 to 116 |

## M. V12 Secure Communication (printed pp. 75 to 77)

| Point | Where |
|---|---|
| 12.1.1 (L1): only recent TLS versions (1.2 and 1.3), with the newest preferred. 12.2.1 and 12.2.2 (L1): TLS for all client connections to external services, with publicly trusted certificates and no fallback to unencrypted traffic. | pp. 76 |
| 12.3.1 (L2): use an encrypted protocol such as TLS for all inbound and outbound connections, including databases and external APIs, with no fallback to unencrypted. 12.3.2 (L2): clients must check the server certificate. | p. 77 |

## N. V13 Configuration (printed pp. 77 to 81)

| Point | Where |
|---|---|
| "The application's default configuration must be secure for use on the Internet." | p. 77 |
| 13.1: documentation of all outside services the app relies on (13.1.1, L2) and a list of critical secrets with a rotation schedule (13.1.4, L3). | p. 78 |
| 13.2.1 (L2): connections between backend parts that do not use the user's session must be authenticated with individual service accounts, short-term tokens or certificates, and not with unchanging credentials such as passwords, API keys or shared privileged accounts. 13.2.2 (L2): those connections use the least privilege. 13.2.4 (L2): an allowlist of outside systems the app may connect to. | p. 79 |
| 13.3.1 (L2): a secrets management solution such as a key vault creates, stores, controls access to and destroys backend secrets. Secrets must not be in source code or build artifacts. 13.3.2 (L2): least privilege for secret access. | p. 80 |
| 13.4.1 (L1): deploy without source control folders such as .git, or make them unreachable. 13.4.2 (L2): debug modes off in production. 13.4.3 and 13.4.5 (L2): no directory listings, and no exposed internal documentation or monitoring endpoints. | pp. 80 to 81 |

## O. V14 Data Protection (printed pp. 81 to 84)

| Point | Where |
|---|---|
| The chapter is about defining what data needs protection and limiting unauthorized access on client devices. It says it no longer tries to duplicate privacy laws and advises asking a qualified privacy specialist or lawyer. | pp. 81 to 82 |
| 14.1.1 (L2): identify and classify all sensitive data into protection levels, including data that is only encoded (such as Base64 or a JWT payload). 14.1.2 (L2): write down protection requirements for each level: encryption, integrity, retention, logging, access controls, privacy techniques. | p. 82 |
| 14.2.1 (L1): sensitive data goes in the message body or headers, never in the URL or query string. 14.2.3 (L2): defined sensitive data is not sent to untrusted parties such as user trackers. 14.2.4 (L2): implement the controls as documented for each protection level. | pp. 82 to 83 |
| 14.2.6 (L3): return only the minimum sensitive data needed and mask it in the interface unless the user views it. 14.2.7 (L3): sensitive information has a retention classification, so old data is deleted on a schedule or when needed. | p. 83 |
| 14.3.1 (L1): clear authenticated data from client storage after the session ends. 14.3.2 (L2): anti-cache headers such as `Cache-Control: no-store`. 14.3.3 (L2): no sensitive data in browser storage except session tokens. | pp. 83 to 84 |

## P. V15 Secure Coding and Architecture (printed pp. 84 to 88)

| Point | Where |
|---|---|
| The chapter gathers general practices, including how to handle "dangerous functionality" (such as deserializing untrusted data or running dynamic code) and "risky components" (poorly maintained, unsupported or with a history of serious flaws). | pp. 84 to 85 |
| 15.1.1 (L1): the documentation sets risk-based time limits for fixing vulnerable third-party components and for updating libraries. 15.2.1 (L1): the application contains no component that has breached those time limits. 15.1.2 (L2): keep an inventory, such as a software bill of materials (SBOM), of all third-party libraries, and check that components come from trusted repositories. | pp. 85 to 86 |
| 15.2.3 (L2): production contains only the needed functionality (no test code or sample snippets). 15.2.4 (L3): components and their transitive dependencies come from the expected repository (to prevent dependency confusion). | p. 86 |
| 15.3.1 (L1): return only the required fields of a data object. 15.3.3 (L2): protect against mass assignment by limiting allowed fields per action. 15.3.6 (L2): write JavaScript so it prevents prototype pollution. | p. 87 |
| 15.4 (L3): safe concurrency, including avoiding time-of-check to time-of-use races. | pp. 87 to 88 |

## Q. V16 Security Logging and Error Handling (printed pp. 88 to 92)

| Point | Where |
|---|---|
| Security logs record authentication decisions, access decisions and attempts to bypass controls. The chapter says logs "should not include sensitive personal data unless legally required" and must be protected as a high-value asset. It says alerting and correlation are out of scope. | pp. 88 to 89 |
| 16.1.1 (L2): an inventory of logging at each layer: what is logged, formats, storage, access and retention. 16.2.1 (L2): each entry includes when, where, who and what. 16.2.2 (L2): synchronized time, with UTC or an explicit time-zone offset. 16.2.5 (L2): logging of sensitive data follows its protection level (credentials not logged; session tokens only hashed or masked). | pp. 89 to 90 |
| 16.3.1 (L2): log all authentication successes and failures. 16.3.2 (L2): log failed authorization attempts. For Level 3, log all authorization decisions, including when sensitive data is accessed, without logging the sensitive data itself. | p. 90 |
| 16.4.1 (L2): encode log data to prevent log injection. 16.4.2 (L2): logs are protected from access and cannot be modified. 16.4.3 (L2): send logs to a logically separate system so a breach of the application does not compromise them. | p. 91 |
| 16.5.1 (L2): return a generic message when something unexpected fails (no stack traces, queries, keys or tokens). 16.5.3 (L2): fail securely and avoid "fail-open" conditions. | p. 91 |

## R. V17 WebRTC and appendices (printed pp. 92 to 122)

| Point | Where |
|---|---|
| V17 WebRTC covers real-time voice and video servers (TURN, media and signaling servers). It says it does not apply to developers who only use a provider's SDK. The proposed coordinator has no real-time calls, so the paper does not use it. | pp. 92 to 95 |
| Appendix A is a glossary. The terms "Reference Token", "Self-Contained Token", "Trusted Service Layer" and "SBOM" are defined there. | pp. 96 to 101 |
| Appendix B lists related OWASP projects (Top 10, WSTG, Proactive Controls, SAMM, cheat sheets) and says a mapping from cheat sheets to ASVS exists. | pp. 102 to 103 |
| Appendix D lists items that were not made requirements: a password strength meter, a public `security.txt` file, client-side validation in addition to server checks, keeping sensitive pages out of search engines. It also lists practices moved out of the standard: use a secure development lifecycle, threat modeling for every design change, functional security constraints in every user story, a secure coding checklist, and detecting configuration drift. | pp. 116 to 118 |
| Appendix E lists contributors. | pp. 118 to 122 |

## Resolved: where ASVS settles earlier disagreements
- **Password rotation.** ASVS 6.2.10 says a password stays valid until it is found compromised or the user changes it, and that the application "must not require periodic credential rotation". This matches the Authentication cheat sheet and disagrees with Proactive Controls C7 (older). The paper should say periodic rotation is not required and cite ASVS 6.2.10.
- **Password length.** ASVS 6.2.1 sets at least 8 characters (at least 15 strongly recommended), 6.2.9 allows at least 64, and 6.2.5 forbids composition rules. The paper may quote these. Do not use Proactive Controls C7's numbers.
- **Environment variables.** ASVS 13.3.1 says secrets must not be in source code or build artifacts and calls for a secrets management solution at Level 2. It does not mention environment variables. How Vercel stores secrets is a question for the Vercel documentation.

## Possible use in the paper
- **Topic 4 (how it works when building products):** the idea of verification levels and documented security decisions (pp. 11 to 14); the standard's own startup example for Level 1 (p. 14).
- **Topic 5 (what it includes):** the chapter list (V1 to V17) is the clearest overview of what application security covers.
- **Topic 8:** relevant requirements for the proposed coordinator's plan: deny by default and object-level access (8.2.2, 8.3.1), multi-factor sign-in for Level 2 (6.3.3), no secret questions (6.4.2), session ending and re-authentication (7.4, 7.5), classification of sensitive data and no trackers (14.1.1, 14.2.3), retention (14.2.7), logging of access without logging the data itself (16.3.2), a bill of materials (15.1.2) and time limits for fixing vulnerable components (15.1.1). The paper may say the idea would use Level 1 as a starting target and plan toward Level 2. It must not say the coordinator meets any level. OWASP says no one can claim official ASVS certification (p. 18).

## Limits
- ASVS 5.0.0 is a May 2025 standard. A newer minor or patch release may exist, and GitHub's "latest" is a rolling build. The paper must cite "version 5.0.0".
- The standard says it is not a substitute for guides: the Cheat Sheet Series covers how to implement and the Web Security Testing Guide covers how to test (p. 11).
- Levels are priority-based and the document says they are not a measure of risk (pp. 12 to 14, 22 to 23).
- The PDF text has no figures to read. The only figure is the license badge.
