---
name: operational-readiness
description: Checks whether a product is ready to run in production and be supported, covering monitoring, alerts, logging, backups and recovery, health checks, on-call and incident steps, and what happens when a dependency fails. Use before launch or before a first real user, when asked "are we ready to go live", "how do we know if it breaks", "what if the database is lost", or when a feature adds a new dependency or background job. Make sure to use this skill before calling a product launch-ready, even if the user never says "operations". Do not use for code review (use engineering-quality-check), for releasing a change safely (use release-deployment-safety), or for security review of code (use security-review).
---

# Operational Readiness

Code that works on a laptop is not the same as a service that can be run. This
skill asks: if this breaks at 2 a.m., how will we know, how will we recover, and
what will a person who did not build it do?

## Ground rules

- **Findings first.** Report gaps. Do not add monitoring or change
  infrastructure until the user asks.
- **Evidence for every "yes".** "We have backups" needs the schedule and proof a
  restore was tried. A backup never restored is `not-assessed`, not `proven`.
- **Use `skeptical-audit` tags** on each claim.
- **Size to the product.** A pre-launch solo product needs the basics done
  honestly, not a large operations team's process.
- **Sensitive data never goes into logs or alerts.** Check this explicitly.
- **Plain language.** Explain terms the first time.

## Before you start

1. Find what runs where: hosting, database, background jobs, third-party
   services. Ask one question if unclear.
2. Read `docs/architecture.md` and `docs/risk-profile.md` if they exist.
3. Read `references/readiness-checklist.md`.

## Workflow

1. **Name the failure modes:** app down, database down, a dependency down or
   slow, a bad deploy, data lost or corrupted, a credential leaked.
2. For each, check the five questions in the checklist: detect, alert,
   diagnose, recover, communicate.
3. **Check recovery for the worst case** (data loss): is there a backup, how
   old can it be, and has a restore actually been tried?
4. **Check what is logged** and confirm no credentials or sensitive personal
   data appear in logs, errors, or alerts.
5. **Check the first-hour plan:** who is told, where the steps are written, and
   how to roll back (see `release-deployment-safety`).
6. Write the report: ready, ready after fixes, or not ready, with each gap, its
   severity, and the smallest fix.

## Severity

- **Blocker:** a failure that loses or exposes data, or that nobody would notice.
- **Should fix before launch:** a failure that is noticed late or hard to recover.
- **Later:** an improvement that does not change the answer to the five questions.

## Quality check before finishing

- Each failure mode has a verdict on all five questions or a stated reason it
  does not apply.
- Backup and restore claims have proof or are marked `not-assessed`.
- The log check names what was looked at.
- The report lists what was not checked.

## If something goes wrong

- **Nothing is deployed yet.** Review the plan and mark every item
  `not-assessed` for evidence. Do not report a pass.
- **No monitoring exists.** That is a Blocker for any product with real users.
  Suggest the smallest option that fits the budget.
- **Hosting is unknown.** Ask. Do not guess.

## Files in this skill

- `references/readiness-checklist.md`: the five questions and the checks.

## Sources

Google, Site Reliability Engineering book, "Monitoring Distributed Systems",
https://sre.google/sre-book/monitoring-distributed-systems/
Google, SRE book, "Launch Coordination Checklist",
https://sre.google/sre-book/launch-checklist/
