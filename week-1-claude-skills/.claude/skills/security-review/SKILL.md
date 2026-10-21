---
name: security-review
description: Reviews code and project setup for common security weaknesses using the OWASP Top 10:2025 and reports each finding with its severity and a fix. Use when the user asks for a security review, to check for vulnerabilities, or to look at logins, permissions, user input, secrets, dependencies, or error handling, or says a project is ready to ship. Make sure to use this skill whenever code handles passwords, logins, payments, personal data, or API keys, even if the user never says "security". Do not use for accessibility, usability, performance tuning, or for testing systems the user does not own.
---

# Security Review

Look for weaknesses that attackers commonly use, and explain them so a
beginner can fix them. The guide is the OWASP Top 10:2025, a widely used list
of the most serious web application risks.

## Ground rules

- **Review only.** Read code and settings. Never try to break into anything,
  never run exploit code, and never test systems the user does not own.
- **Never print secrets.** If you find a password, token, or key, give the file
  and line and show only the first four characters followed by `...`. Tell the
  user to treat it as leaked and replace it.
- **Evidence, not fear.** Every finding names the file and line, what is
  wrong, and how it could be misused, in one or two plain sentences.
- **Never say "secure".** Say "no problems found in what was checked", and
  list what was not checked.
- **Review first, change later.** Do not edit files unless the user asks for
  fixes after seeing the report.
- **Explain jargon** the first time you use it.

## Before you start

1. Find out what to review. If unclear, ask one question: "Which folder or
   feature should I check?"
2. Identify the stack (language, framework, database, hosting, login method)
   and where user input comes in.
3. Read `references/owasp-top-10-2025-checklist.md`.

## Workflow

1. **Secrets and settings.** Search for keys, tokens, and passwords in code,
   config, and history-prone files. Check `.gitignore` covers `.env` files.
2. **Access control (A01).** For every route or action, ask who is allowed and
   where the code checks it. Look for users reaching other users' data.
3. **Configuration (A02).** Debug mode, default accounts, open CORS, missing
   security headers, verbose errors.
4. **Dependencies (A03).** Lock files present, versions pinned, known
   vulnerable packages, untrusted install scripts. Suggest a dependency audit
   (`npm audit` or the equivalent).
5. **Cryptography (A04).** Passwords hashed with a modern algorithm, HTTPS
   enforced, no home-made encryption.
6. **Injection (A05).** Database queries, shell commands, and HTML output built
   from user input without safe handling.
7. **Design and login (A06, A07).** Rate limits, session handling, password
   reset flow, multi-factor options.
8. **Integrity, logging, errors (A08, A09, A10).** Unsigned updates, missing
   audit logs, secrets in logs, and errors that fail open.
9. **Write the report** with `assets/security-report-template.md`.

## Severity

- **Critical:** exposed secrets, or anyone can read or change other people's
  data. Fix before anything else.
- **High:** a likely route to a breach, such as injection or missing login
  checks.
- **Medium:** weakens defenses or needs another flaw to be misused.
- **Low:** hardening and good practice.

## Quality check before finishing

- Every finding has a location, an OWASP category, a severity, and a fix.
- No secret value is printed in full anywhere in the report.
- The report lists what was checked and what was not.
- It does not claim the project is secure.
- If findings include exposed secrets, the first line of the summary says to
  replace them now.
- Suggest next steps: dependency audit, a secrets scanner, and a human
  security review before handling real customer data.

## If something goes wrong

- **The code is not a web app.** Use the same method, skip categories that do
  not apply, and say which were skipped.
- **Too many findings.** Group repeats, show counts, and list the top ten by
  severity.
- **You cannot tell whether something is a problem.** Put it under "needs a
  human decision" with the question to answer.

## Files in this skill

- `references/owasp-top-10-2025-checklist.md`: what to look for in each category.
- `assets/security-report-template.md`: the format of the report.

## Sources

OWASP Foundation, OWASP Top 10:2025 introduction:
https://top10.owasp.org/2025/0x00_2025-Introduction/
NIST, SP 800-218 Rev. 1 (SSDF v1.2) initial public draft, December 2025:
https://csrc.nist.gov/pubs/sp/800/218/r1/ipd
