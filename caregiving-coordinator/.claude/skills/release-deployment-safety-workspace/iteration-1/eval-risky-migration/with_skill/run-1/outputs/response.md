# Release safety check: medications -> drugs migration

**Verdict: No-go as planned. Go after fixes.**

Nothing was run or deployed. Evidence tags follow skeptical-audit; I only have your one-line description, so most items are `not-assessed`.

## What changes
- Schema: rename `medications` to `drugs` (health data).
- Data: drop the old `notes` column (permanent data loss).
- Config: new env var `NOTIFY_KEY` (a secret; I name it, never its value).

## Findings
1. **Blocker: dropping `notes` is irreversible.** Rollback of the code cannot bring the notes back. No verified backup or recovery plan is mentioned (`not-assessed`).
2. **Blocker: the rename breaks old code.** During deploy, and on any rollback, old code still queries `medications` and fails. Use expand/contract: add `drugs` (or a view), ship code that works with both, migrate, and drop the old column in a later release.
3. **High: straight to production with no staging.** The migration has never run against a copy of real data (`not-assessed`).
4. **High: `NOTIFY_KEY` unconfirmed.** Is it set in production before deploy? Is it kept out of the repo? Can it be rotated? (`not-assessed`)
5. **High: no rollback plan.** Steps, owner, duration and whether tried are all unknown (`not-assessed`).
6. **Medium: merge gate** (tests, linter, build, arch-gate) has no output shown (`not-assessed`).
7. **Medium: no rollout step or after-release check named.**

## Needed before Go
- Take a backup, restore it somewhere, and confirm the notes are readable.
- Split the release: rename with compatibility first, drop `notes` later.
- Rehearse the migration on a copy of production data.
- Set `NOTIFY_KEY` in production first.
- Write the rollback steps.
- Deploy off-hours to a small share of users if possible.
- Watch the first 15 minutes: health check, loading and saving a medication, error rate.

## Not checked
Migration file, git diff, deploy method, table size and locking, CI results.
