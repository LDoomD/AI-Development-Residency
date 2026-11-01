# Structuring the Caregiving Coordinator

Start with a modular monolith. One deployable app, one database, clear internal modules. Microservices are overkill for a solo or small-team MVP.

## Layers
1. **UI**: screens and forms. No business rules.
2. **API/routes**: parse input, authenticate, call services, shape responses.
3. **Services (domain logic)**: scheduling, medication rules, permission checks.
4. **Data access**: queries and migrations only.

Dependencies point downward only. The UI never touches the database.

## Modules
- **Accounts**: users, care circles (one per care recipient), memberships.
- **Appointments**
- **Medications**: drugs, schedules, dose logs.
- **Notifications**: reminders, behind an interface so providers can be swapped.

## Permissions (the core design decision)
- Model a **CareCircle** with **Memberships**, each holding a role (owner, editor, viewer, or a limited role such as a paid aide).
- Enforce access in ONE place, a service-layer policy function such as `can(user, action, resource)`. Never rely on UI hiding.
- Every record carries a `care_circle_id`, and every query filters by it.
- Audit-log who changed what, especially medications.

## Data
- Postgres. Relational fits this well.
- Store times in UTC with the recipient's timezone.
- Treat medication and health data as sensitive: encrypt in transit and at rest, minimize collection, and support delete/export.
- Log dose changes as append-only history, not overwrites.

## Suggested order
1. Auth, circles, memberships, and the permission policy, with tests.
2. Appointments (simplest vertical slice).
3. Medications and dose logging.
4. Reminders.

## Write down
- A short architecture doc and ADRs for the big choices (stack, permission model, health-data handling).
- Permission tests: a viewer cannot edit, and a user cannot see another circle's data.

## Open questions
Who are the users (family only, or paid aides too)? Does it need to meet HIPAA? Web, mobile, or both?
