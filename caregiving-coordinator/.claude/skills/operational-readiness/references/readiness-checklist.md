# Readiness checklist

For each failure mode, answer five questions:

1. **Detect.** How would we know it broke? (health check, error tracking, a user
   report is the weakest answer)
2. **Alert.** Who is told, how fast, and through what? An alert nobody sees does
   not count.
3. **Diagnose.** What do logs and metrics show to find the cause? Do they
   contain what is needed and nothing sensitive?
4. **Recover.** What are the steps to restore service or data, and have they been
   tried?
5. **Communicate.** Who tells users or the owner, and what do they say?

## Basics for any product with real users

- A health check that tests the app and its database, not only that the process
  is running.
- Errors are captured somewhere a person looks.
- Logs have timestamps and request identifiers, and contain no credentials or
  sensitive personal data.
- Backups run on a schedule, are stored separately from the data, and a restore
  has been tested.
- Secrets and configuration live outside the code and can be rotated.
- A short written runbook: how to check status, restart, roll back, and restore.
- A known answer to "what happens if each third-party service is down?"
- A named owner for incidents, even if it is one person.
