# Testing plan for a Node app with zero tests

## Approach: test pyramid, risk first
Many fast unit tests, some integration tests, very few end-to-end tests. Start where a bug hurts most: medication data and invite access.

## Setup
- Use Node's built-in `node:test` or Vitest/Jest, plus Supertest for HTTP routes.
- Add `npm test` and run it in CI and in a pre-commit or pre-merge check.
- Use a throwaway test database (in-memory SQLite or a test schema) reset between tests.

## 1. Unit tests (the bulk)
Pure logic, no network or DB:
- Appointments: date/time validation, timezone handling, overlap detection, recurring-date generation, past-date rejection.
- Medications: dosage and frequency validation, duplicate entries, schedule calculation, refill-due logic.
- Invites: token generation (unguessable, unique), expiry checks, role/permission rules.

## 2. Integration tests (the middle)
Routes + real test DB:
- Create/read/update/delete for appointments and medications.
- Invite flow: create invite, accept valid one, reject expired, reused, or tampered token.
- Auth and access control: a user cannot read or change another family's appointments or medications (test this explicitly; it is the highest-risk area for health data).
- Bad input returns 4xx, not a crash or a stack trace.

## 3. End-to-end (very few)
One or two happy paths only, e.g. sign up, invite a sibling, sibling accepts and sees the shared medication list. Use Playwright if there is a UI.

## 4. Checks that run as scripts before merge
- Test suite, linter, `npm audit`, secret scan.

## Order of work
1. Set up the runner and one passing test.
2. Access-control and invite-token tests.
3. Medication logic unit tests.
4. Appointment logic unit tests.
5. Add a regression test for every bug found from now on.

## Enough?
Not a coverage percentage. Enough means every rule above has a test that fails when you break the rule.
