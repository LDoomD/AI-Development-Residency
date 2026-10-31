# Quality Check: POST /share, Redis, no tests, README unchanged

**Verdict: Not ready.**

## What was checked
Only your one-line description. I did not see the code, run tests, the linter, the build, or the architecture gate (`node .claude/skills/judge-arch/scripts/arch-gate.mjs`). So nothing here is verified. I can say nothing "works" or "passes".

## Blocking issues
1. **No tests for new behavior.** A new endpoint needs a test. This is a risk, not a nice-to-have. First test worth writing: POST /share with valid input returns success, and with a request from a user who does not own the data is rejected.
2. **Undocumented new dependency.** Redis adds a service people must install and run. The README is unchanged, so setup steps, the connection setting (env var name), and how to run locally are missing.
3. **Big decision with no record.** Choosing Redis changes structure and operations. Draft a short decision record in `docs/adr/` (what was decided, why Redis, alternatives, trade-offs) using `architectural-decision-records`.
4. **Architecture review needed.** The change adds code and a data store. Run `judge-arch` and the arch-gate. A gate failure means not ready.

## Needs a look (cannot judge from the description)
- **Security:** /share likely exposes caregiving or health data. Run `security-review` (authorization, input validation, expiry of shared links, what Redis stores and for how long). Also consider `data-lifecycle-compliance`.
- **Operations:** what happens if Redis is down? Use `operational-readiness` / `release-deployment-safety` before release.
- Redis version pin, credentials not committed, error handling in the endpoint.

## Not assessed
Code quality, naming, complexity, lint, build, the gate.

## Next step
Add one endpoint test, a README setup section for Redis, and an ADR. Then re-run the checks and send the diff for a full review.
