# Fixing a 90% browser, 12-minute test suite

Your suite is shaped like an ice-cream cone: many slow end-to-end tests, few fast ones. Invert it into a pyramid.

## 1. Audit
Tag each browser test with what it really checks:
- Business logic or validation (e.g. permissions, date rules, formatting): move down to unit tests.
- Server behavior (API, database, auth): move to integration tests that call the API or handler directly, with no browser.
- Real user journeys through the UI: keep as E2E.

## 2. Target shape
- About 70% unit tests (milliseconds each).
- About 20-25% integration tests (API and database, seconds).
- About 5-10% E2E: only critical journeys (sign in, create a care task, share with a family member, delete data). Aim for 5-15 tests.

## 3. Speed up the E2E tests that remain
- Log in through the API or a saved session state, not the login form, in every test.
- Seed data through the API or database, not by clicking.
- Replace fixed sleeps with auto-waiting on conditions.
- Run in parallel, isolate data per test, and use headless mode.
- Stub third-party services and the AI service.

## 4. Gate in CI
- On every commit: unit and integration (target under 1-2 minutes).
- On pull request or merge: the small E2E smoke set (target under 3 minutes).
- Nightly: any broader browser or cross-browser runs.
- Quarantine flaky tests and fix or delete them. Do not rerun them blindly.

## 5. Process rules
- Write each new test at the lowest level that can catch the bug.
- When a bug is found in E2E, add a unit or integration test that reproduces it, then drop the E2E test if redundant.
- Track suite time and test counts per level, and fail the build if the E2E share grows.

## Expected result
Roughly 12 minutes becomes under 2 minutes for the pre-merge loop, with the same or better coverage of logic. Nothing was run or measured here; the numbers are targets, not results.
