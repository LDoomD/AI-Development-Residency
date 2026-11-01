# Architecture

Status: Draft | Approved by <name> on <date>

## Open questions

- (anything not yet decided)

## Layers

| Layer | Job | Must not |
|---|---|---|
| e.g. Screens | Show data, collect input | Query the database, hold business rules |

## Dependency direction

Allowed: Screens -> Logic -> Data access -> Storage. Anything else is drift.

## Data ownership

| Data | Written by (one module) | Read through (one path) | Sensitivity |
|---|---|---|---|

## Error handling

- Caught at: 
- Logged: 
- Shown to the user: 
- Never logged: credentials, sensitive personal data

## Cross-cutting rules

| Concern | Rule | Layer that handles it | Enforced by |
|---|---|---|---|
| Authentication | | | gate / review |
| Authorization | | | |
| Audit trail | | | |
| Secrets and config | | | |
| Data retention and deletion | | | |

## What would force a redesign

- (a second user type, a second deployment, a regulated customer, ...)

## Decisions

Links to `docs/adr/` records.
