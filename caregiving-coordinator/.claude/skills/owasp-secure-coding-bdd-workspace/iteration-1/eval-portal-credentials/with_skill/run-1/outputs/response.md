**Assumed answer to the skill's first question:** the feature takes a portal username and password, stores it, and logs into a third-party site. `docs/risk-profile.md` rates plaintext storage Critical. OWASP sources not opened this session.

**Design first:** ask whether the first version needs stored logins at all (open question in the risk profile). Storing someone else's password is the riskiest choice here. A safer path is to have the user type in claim status, or use an official insurer API with token-based consent, if one exists.

Scenarios (would be saved to `docs/security-specs/portal-credentials.md` after approval):

```
Scenario: Valid save
  Given a signed-in family member
  When they submit a portal login
  Then it is stored encrypted, and is never shown again in full
Source: OWASP Secrets Mgmt, Crypto Storage   Check: automatable   Gate rule: none

Scenario: Plaintext leak
  Given a saved login
  When the database, a log, an error page, or an API response is read
  Then the password never appears in readable form
Source: OWASP Secrets Mgmt, Logging   Check: automatable   Gate rule: none

Scenario: Another family's login (IDOR)
  Given user A is signed in
  When they change an ID to request user B's saved login
  Then access is refused and the attempt is logged
Source: OWASP Authorization, Top 10 A01   Check: automatable   Gate rule: none

Scenario: Removed member
  Given a member's access is revoked
  When they try to use the login
  Then it fails
Source: OWASP Authorization   Check: automatable   Gate rule: none

Scenario: Portal call fails
  Given the insurer site is down or returns bad data
  When the app checks status
  Then the user sees a generic message, nothing sensitive is logged
Source: OWASP Error Handling   Check: review   Gate rule: none
```

**Later:** audit trail; encryption key kept outside the database.

Next: approve these, then use `writing-security-tests` on the first automatable one.
