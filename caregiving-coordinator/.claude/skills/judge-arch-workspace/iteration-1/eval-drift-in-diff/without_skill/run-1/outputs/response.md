# Architecture drift review

Scope: only the diff as described in the prompt. I did not read the code or run any checks. Judge-arch skill not used, per instructions.

Verdict: do not open the PR yet. All three changes break the stated rules.

## 1. routes/appointments.js: boundary violation (high)
- Copay calculation (`visits.reduce(...)`) is business logic in a route. Routes may only call services. Move it to a service, for example `billingService.copayOwed(visits)`.
- `db.query('UPDATE appointments SET status=...')` in a route breaks "only the repository layer touches the database". Add `appointmentRepository.updateStatus(id, status)`, call it from an `appointmentService`, and have the route call that service.

## 2. models/visit.js: duplicated data ownership (high)
- `refill_status` already lives in `medications.refill_status`. Adding it to visits and updating both places gives the fact two owners. They will drift apart.
- Fix: drop the new column. Read refill status from medications, through the repository, by join or lookup. If visits need a snapshot, name it differently, such as `refill_status_at_visit`, and document it as an immutable historical record.

## 3. services/notify.js: swallowed error (medium-high)
- `catch (e) {}` silently drops send failures. In a caregiving app, a missed refill or appointment notice would fail with no trace.
- Fix: log the error with context (never the message body, which may contain health data), then either rethrow, return a failure result, or queue a retry. Callers should be able to tell the notification failed.

## Before the PR
- Re-run the arch-gate script after fixing. I have not run it.
- Consider a short ADR if you keep any exception to the ownership rule.
