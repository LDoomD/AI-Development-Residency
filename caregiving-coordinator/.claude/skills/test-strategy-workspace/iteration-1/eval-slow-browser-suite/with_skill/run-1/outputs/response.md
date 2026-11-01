**Skill applied:** test-strategy. Not applied: security-review, writing-security-tests, performance load testing (not relevant here).

**Diagnosis:** 90% browser tests is an upside-down pyramid. 12 minutes means slow feedback, and browser tests are the likeliest to be flaky. I have not seen your suite, test tool, or `package.json`, so the numbers below are targets, not measurements.

**Target shape (roughly):** about 70% unit, 20-25% integration, 5% or less end-to-end.

**Steps**
1. **Inventory.** List every browser test and the behavior it checks. Run the suite with a timing report (your existing tool's reporter) to find the slowest ones. Do not add a new framework.
2. **Re-level each test, using the lowest level that can catch the failure.**
   - Rules, validation, calculations, permissions logic: move to unit tests.
   - Forms saving, API plus database behavior: move to integration tests against a real test database.
   - Keep as end-to-end only the 3-5 journeys that must never break (for example sign in, add a care task, a caregiver sees the shared update).
3. **Delete duplicates.** If a unit or integration test now covers a behavior, remove the browser version.
4. **Risk decides depth.** Health data, shared credentials, and deletion/permissions get edge cases (empty, duplicate, two users at once, service down) at unit or integration level, not in the browser.
5. **Flaky tests are bugs.** Fix the cause (timing, shared state, network) before keeping them. Quarantine, don't ignore.
6. **Merge gate (commands must exist in the project):** unit plus integration tests, linter, build, arch-gate, secret scan. Run the small end-to-end set on merge or nightly if it is still slow.
7. **Test data is fake.** No real personal or health data in fixtures.
8. **Write it down** in `docs/test-plan.md` using `assets/test-plan-template.md`, including a "Not tested" list.

**Success check (evidence required):** the suite time before and after, with the command and its output. Target: fast layers finish in about a minute; the browser set in a few minutes.

**One question:** which feature or area should the first plan cover?
