## Verification

I ran `npm test` locally and it reported 12 passing, 0 failing. I also read `src/auth.js` and confirmed that passwords are hashed with bcrypt at cost factor 12. The test run shows the existing 12 tests pass; it does not by itself show that the password hashing is covered by a test, and I did not check that. The bcrypt cost comes from reading the source, not from a runtime check, so I did not confirm that the value is applied on every code path that sets a password. I did not run a security review, a dependency audit, or testing against a deployed environment.
