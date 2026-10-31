# Security review: pasted snippet (login route)

**Replace the exposed secret now.** The key starting `sk-l...` is leaked once it is in code you share or commit. Revoke it and issue a new one. Do not commit this.

| Severity | Count |
|---|---|
| Critical | 1 |
| High | 2 |
| Medium | 1 |

## Findings

1. **Hardcoded API key (Critical)** - line 1, `apiKey = 'sk-l...'`. A01/A02-style secrets exposure. Anyone with the repo (or its history) can use the key. Fix: revoke it, load from an environment variable, add `.env` to `.gitignore`, run a secrets scanner. Removing it later does not erase git history.
2. **SQL injection (High)** - `/login` query, A05 Injection. Email and password are concatenated into the SQL string, so an input like `' OR '1'='1` can log in as anyone or read the database. Fix: parameterized queries (`db.query("... WHERE email = ?", [email])`).
3. **Plaintext password comparison (High)** - `pw='...'` in the query, A04 Cryptography. Passwords appear to be stored unhashed, so a database leak exposes every password. Fix: hash with bcrypt or argon2, fetch by email, compare hashes in code.
4. **No rate limiting or lockout visible (Medium)** - A07 Login. Unlimited guesses are possible. Fix: add rate limiting.

## What was checked
Only the pasted lines: secrets, injection, password handling, login design.

## Not verified
The code is truncated (`...`). Not seen: session handling, error output, HTTPS, dependencies, access control elsewhere, `.gitignore`. No other categories were checked. Nothing here shows the project is secure.
`docs/risk-profile.md` (health data, shared credentials) is a draft and no code shown touches it. If this app stores family portal logins, this plaintext pattern would be Critical.

## Next steps
1. Revoke the key. 2. Fix the query and hashing. 3. Run `npm audit` and a secrets scanner. 4. Human security review before real health data.
