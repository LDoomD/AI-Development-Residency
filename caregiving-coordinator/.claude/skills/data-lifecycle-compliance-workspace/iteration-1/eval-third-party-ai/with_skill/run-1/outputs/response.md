Yes. Two gaps, both about health-related data. I applied data-lifecycle-compliance. I did not read docs/risk-profile.md, docs/architecture.md, or any privacy text, so everything below is `reported` (from your one sentence) or `not-assessed`. This is not legal advice, and I can't say anything is compliant.

## Inventory (partial)

| Data | Purpose | Sent to | Kept | Deleted how |
|---|---|---|---|---|
| Visit transcripts (health and care details, names) | Summaries | Third-party AI service (`reported`) | Unknown | Unknown |
| Visit recordings (voices, health details) | Unknown | Unknown | Forever (`reported`) | None (`reported`) |
| Summaries | Show to caregivers | Unknown | Unknown | Unknown |

## Gaps

1. **Blocker: recordings kept forever.** Nothing limits keeping them to what is needed. Raw audio is the most sensitive copy, and it also makes any breach larger. Set a retention period and an automatic delete.
2. **Blocker until answered: the AI vendor.** Nothing documents whether the vendor stores the transcripts, trains on them, who at the vendor can read them, or where they are processed. Do not assume. Get the vendor's data terms in writing.
3. **Should fix before launch: user notice.** Are people told that their transcripts go to an AI service? Are the other people in the recording told? `not-assessed`.
4. **Should fix before launch: deletion and export.** Can a user delete a visit? Does it reach the recording, the transcript, the summary, backups, logs, and the vendor? `not-assessed`.
5. **Should fix before launch: access.** Who on the team can play recordings, and is access logged? `not-assessed`.
6. **Later: minimization.** Can names or identifiers be removed before the transcript is sent?

## Open questions for a qualified person

- Do health-data rules (for example HIPAA or the FTC Health Breach Notification Rule) apply to this product?
- Is consent needed to record visits where you live? Rules vary.
- Do you need a data processing agreement with the AI vendor?

## Not checked

Code, vendor terms, privacy text, backups, logs, and whether any deletion feature runs.
