# Release checklist

- [ ] Merge gate passed, with output: tests, linter, build, `arch-gate`.
- [ ] Changes listed: code, schema/data, configuration, secrets, third-party
      settings.
- [ ] Each migration: reversible? backup taken? old code safe against the new
      schema while rolling out?
- [ ] New configuration exists in the target environment. No secret is in the
      repo.
- [ ] Rollout can start small (flag, staged, or a test user group).
- [ ] Rollback steps written, owner named, time estimated, and tried at least
      once.
- [ ] After-release check defined: health check, one key user journey, error
      rate, for the first 15 minutes.
- [ ] Someone is available to act after the release, not only before it.
- [ ] Users or the owner know if something visible changes.
