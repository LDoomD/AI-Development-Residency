# Do we need monitoring with two users?

**Yes, but the smallest version.** Two users means no big setup. It does not mean none: these two are caregivers sharing health-related information, so a silent failure matters. Not having monitoring is a Blocker for any product with real users (skill rule). Two real users counts.

Not assessed: I did not check hosting, database, or what is deployed. Please tell me where it runs; I won't guess.

## Smallest setup (about an hour, free tier)

1. **Health check** (`/health`) that tests the app and its database, not just that the process is up. [documented: checklist]
2. **Uptime pinger** (e.g. UptimeRobot free) hitting it every 5 minutes, emailing or texting you. This answers detect and alert. An alert nobody sees does not count, so send it somewhere you check.
3. **Error tracking** (e.g. Sentry free tier) so errors land where a person looks.
4. **Logs with no sensitive data:** timestamps and request IDs, but no passwords, tokens, or health details in logs, errors, or alerts. Not checked yet; I haven't read the code.
5. **Backup with a tested restore.** A backup never restored is `not-assessed`. Losing the data is the worst case. Try one restore.
6. **Five-line runbook** and a named owner (you): how to check status, restart, roll back, restore, and what to tell the other user.

## Verdict
Not ready until 1-3 exist (Blocker). Items 4-6 are should-fix-before-launch. Dashboards, on-call rotations, and paging tools are Later.

## Not checked
Hosting, existing logs, backups, third-party dependency failures (for example any AI service).
