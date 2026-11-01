**Verification**

I ran `npm test` and it printed `12 passing, 0 failing`. I did not save the full output, so the count is my report of that run, not an attached log. It shows that 12 tests passed at the time I ran them. It does not show what those tests cover, and I have not checked whether any of them exercises password hashing.

I read `src/auth.js` and it hashes passwords with bcrypt at cost 12. This is from reading the code only. I did not run it, and no test I know of asserts the cost factor. The code could be bypassed, or the value overridden by config, and I did not check either.

Not checked: whether any test covers `src/auth.js`; the cost factor at runtime (for example, by decoding a stored hash, which starts `$2b$12$`); other places passwords are handled; security of the login flow beyond hashing.

| Claim | State | Source | Limit |
|---|---|---|---|
| `npm test`: 12 passing, 0 failing | reported (by the author, who ran it) | `npm test`, run by the author on 2026-10-31 | Output not attached. Coverage of auth unknown. A single run. |
| `src/auth.js` uses bcrypt cost 12 | observed (by the author, by reading) | `src/auth.js`, line number not given | Reading code does not prove it runs or that the value is used at runtime. |

Note for you: I did not see either result myself, so I tagged both as your observations. To make the bcrypt claim `proven`, add a test that hashes a password and asserts the stored hash begins `$2b$12$`, then paste its passing output here.
