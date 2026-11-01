# Operational readiness: first real family

**Verdict: not-assessed, so I can't say "ready."** I only have your one-line description. Nothing below is `proven` or `observed`. Treat every item as a question until you show evidence. This app holds family health data, so the bar is higher.

**Stack (reported):** Node API, managed Postgres, nightly reminder job. I don't know the host. Which host runs the API and the job?

## Failure modes (five questions: detect, alert, diagnose, recover, communicate)

1. **Database lost or corrupted: Blocker until proven.** "Managed host" does not equal "restore tested." Backup schedule and age: not-assessed. Restore ever tried: not-assessed. Smallest fix: confirm automated backups (or point-in-time recovery) are on, restore one into a scratch database, and write down how long it took.
2. **Nightly reminder job fails silently: Blocker.** A missed reminder is something nobody would notice. Smallest fix: the job writes a success heartbeat, and a dead-man's-switch check (for example Healthchecks.io) alerts you if it doesn't arrive.
3. **API down: Should fix.** Needs a health check that also queries the database, plus an uptime monitor that texts or emails you. A family reporting it is the weakest detection.
4. **Errors and logs: Should fix.** Is error tracking in place and does a person look at it? Check that logs have timestamps and request IDs and contain no health details, names, tokens, or passwords. Not checked.
5. **Bad deploy: Should fix.** Is there a rollback step? See `release-deployment-safety`.
6. **Dependency down (the reminder channel, such as email or SMS): Should fix.** What happens to the reminder if it is down?
7. **Leaked credential: Should fix.** Can secrets be rotated without a code change?

## Before next week
- Name one incident owner and write a half-page runbook: status, restart, roll back, restore.
- Decide what you tell the family if something breaks.

**Not checked:** code, hosting config, actual logs, backups, alerts, `docs/architecture.md`.
