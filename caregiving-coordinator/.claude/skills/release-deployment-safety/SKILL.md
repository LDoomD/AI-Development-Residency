---
name: release-deployment-safety
description: Checks that a change can be released and undone safely, covering the release steps, rollback, database or data migrations, configuration and secrets changes, staged rollout or feature flags, and a post-release check. Use before deploying or releasing, when a change touches the database schema, configuration, or something users depend on, when asked "is it safe to ship", "how do we roll back", or "can we deploy this". Make sure to use this skill before any release or deploy, even if the user only says "ship it". Do not use for code quality review (use engineering-quality-check), for production monitoring and recovery (use operational-readiness), or for deciding what to build.
---

# Release and Deployment Safety

A release is safe when it can be undone quickly and its effect is checked
afterward. This skill asks: what changes, what could go wrong, how do we go back,
and how will we know it worked?

## Ground rules

- **Findings first.** Report gaps. Do not deploy, run migrations, or change
  configuration. The user does the release.
- **Rollback is part of the release.** A release plan with no tested way back
  is not ready.
- **Data changes are the hard part.** Code can be reverted. A migration that
  deletes or rewrites data may not be reversible.
- **Never print secrets.** If configuration holds credentials, name the setting
  and not the value.
- **Use `skeptical-audit` tags.** A rollback never tried is `not-assessed`.
- **Short and ordered.** Lead with the verdict, then list only the gaps and
  the next step. A small release gets a short answer; a long checklist
  recital hides the one blocker.
- **Plain language.** Explain terms the first time.

## Before you start

1. Find what is being released: `git log` and `git diff` since the last
   release. Ask which environment it goes to if unclear.
2. Find how deploys work now (scripts, CI, host dashboard). If unknown, ask.
3. Read `references/release-checklist.md`.

## Workflow

1. **List what changes:** code, database schema or data, configuration,
   secrets, third-party settings.
2. **Check the merge gate passed** (tests, linter, build, `arch-gate`) with
   command output, not memory.
3. **Check the data change.** For each migration: is it reversible, does it
   lock or rewrite large data, does old code still work against the new schema
   during rollout, and is there a backup taken first?
4. **Check configuration and secrets:** new settings exist in the target
   environment, nothing sensitive is in the repo, and rotation is possible.
5. **Check rollout:** can it go to a few users first (feature flag or staged
   rollout), or all at once?
6. **Check rollback:** the exact steps, who runs them, how long they take, and
   whether they have been tried.
7. **Check the after-release test:** what is looked at in the first 15 minutes
   to confirm it works (health check, key user journey, error rate).
8. Give a verdict: **Go**, **Go after fixes**, **No-go**, or **Cannot tell**,
   with the reason.

## Quality check before finishing

- The merge gate result is shown with output.
- Every data change has a reversibility answer.
- Rollback steps are written and marked tried or not tried.
- The after-release check names what to watch.
- The report lists what was not checked.

## If something goes wrong

- **No staging environment.** Say the release goes straight to production and
  recommend the smallest rollout step available.
- **A migration cannot be reversed.** Treat it as a Blocker unless a verified
  backup and a written recovery plan exist.
- **Deploys are manual.** Ask for the steps and check them for gaps. Do not run
  them.

## Files in this skill

- `references/release-checklist.md`: the checks in a compact list.

## Sources

Martin Fowler, "Feature Toggles", https://martinfowler.com/articles/feature-toggles.html
Jez Humble and David Farley, Continuous Delivery (2010), chapters on
deployment pipelines and release strategies.
Google, SRE book, "Release Engineering",
https://sre.google/sre-book/release-engineering/
