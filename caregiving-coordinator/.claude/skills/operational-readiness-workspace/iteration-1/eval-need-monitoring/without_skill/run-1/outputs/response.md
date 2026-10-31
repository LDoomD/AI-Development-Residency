Yes, but keep it minimal. With two users you don't need a full monitoring stack, but you do need to know when the app breaks before a user tells you. For a caregiving app that holds health information, a silent failure (missed reminder, lost update, a caregiver seeing stale data) matters more than the user count suggests.

What to set up now (about an hour, mostly free tiers):

1. Uptime check: a free external pinger (UptimeRobot, Better Stack) hitting a simple /health endpoint every 5 minutes, emailing or texting you on failure.
2. Error tracking: Sentry (free tier) or equivalent, so unhandled exceptions reach you with a stack trace instead of disappearing.
3. Basic logs: keep your host's logs, log errors and failed logins, and never log health details, tokens, or passwords.
4. Backups: monitoring tells you something broke; backups let you recover. Turn on automatic database backups and do one test restore.
5. Dependency failures: if you call email, SMS, or an AI service, make sure a failure is logged and visible, not swallowed.
6. A short note on who gets alerted and what the first three steps are when it breaks (check host status, check recent deploy, roll back).

What to skip for now: dashboards, metrics pipelines, paging rotations, performance tracing, and anything that costs money or takes days to maintain.

Revisit when you add real users beyond the pilot, handle reminders that must fire on time, or someone depends on the app for something urgent. At that point add alerts on error rate and a background-job heartbeat.

I have not looked at your code or hosting setup, so this is general advice, not a check of what is already in place.
