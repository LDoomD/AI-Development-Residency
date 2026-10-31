# Doctor visit recording upload: misuse behavior

Recordings are health data, so default to deny and fail closed.

**Who can upload or listen**
- Only signed-in members of that care circle can upload, list, or play recordings. Anyone else gets 404 (not 403), so IDs reveal nothing.
- Check membership on the server for every request, including playback URLs.
- Removed members lose access immediately. Playback links are short-lived and signed.

**Bad files**
- Allow-list audio types (mp3, m4a, wav) by checking the file's real content, not its name or declared type. Reject everything else with a clear message.
- Enforce a size and duration cap server-side. Reject oversized uploads early.
- Rename files on save, ignoring the user's filename (no path tricks). Store outside the web root, in private storage.
- Scan for malware if possible. Never execute or render uploaded content.

**Abuse and volume**
- Rate-limit uploads per user and cap total storage per care circle.
- Handle interrupted or duplicate uploads without leaving partial files.

**Privacy**
- Encrypt at rest and in transit (HTTPS only).
- Never put filenames, transcripts, or patient details in logs or error messages.
- Log who uploaded, played, or deleted each recording (audit trail).
- Errors stay generic; no stack traces or storage paths.

**Consent and lifecycle**
- Show a reminder to get consent from everyone recorded (some places require all-party consent).
- Let the uploader or circle admin delete a recording, and make deletion remove the stored file and any transcripts or backups on a defined schedule.
- If recordings are sent to an AI transcription service, tell users and check that vendor's retention terms.

**Write these as scenarios before coding**, for example:
- Given a user outside the circle, when they request a recording, then they get "not found".
- Given a .exe renamed to .mp3, when uploaded, then it is rejected.
- Given a 5 GB file, when uploaded, then it is refused before it fully transfers.
- Given a removed member with an old link, when they play it, then access is denied.

Not checked: nothing is built, so none of this is verified against code.
