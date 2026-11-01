# Scenario topics

Pick the topics that match what the feature touches. Each line is a prompt for
a misuse scenario, not a complete standard. Open the OWASP source before
quoting it.

| Feature touches | Misuse to write a scenario for | OWASP pointer |
|---|---|---|
| User input | Input containing code or query syntax is treated as data, never run | Injection Prevention, Input Validation cheat sheets |
| Logins | Wrong password, repeated attempts, reused or weak passwords | Authentication, Password Storage cheat sheets |
| Sessions | A stolen or old session cannot be reused after logout or timeout | Session Management cheat sheet |
| Permissions | A signed-in user asks for another user's record by changing an ID | Authorization, IDOR cheat sheets (Top 10 A01) |
| Files | An uploaded file has a dangerous type, name, or size | File Upload cheat sheet |
| Secrets | A key or password appears in code, logs, errors, or a response | Secrets Management, Logging cheat sheets |
| Other services | A call to another service fails, is slow, or returns bad data | SSRF, Error Handling cheat sheets |
| Errors | An error message exposes internals or personal data | Error Handling cheat sheet |
| Logging | Sensitive data is written to a log, or an important event is not | Logging cheat sheet |
| Sensitive data | Data is readable in storage, in transit, or by the wrong role | Cryptographic Storage, Transport Layer Security cheat sheets |
| Dependencies | A library has a known flaw or an untrusted source | Dependency, Software Supply Chain guidance (Top 10 A03) |

Always add the items from `docs/risk-profile.md` that apply to the feature.
