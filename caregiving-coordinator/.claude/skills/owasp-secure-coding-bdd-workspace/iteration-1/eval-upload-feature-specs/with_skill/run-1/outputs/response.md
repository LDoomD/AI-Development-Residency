Assumption (I can't ask live): the feature takes audio uploads, stores them, and may send them to an AI service. Drafted from `docs/risk-profile.md` (draft, unapproved). OWASP sources: not verified this session. Proposed file: `docs/security-specs/visit-recording-upload.md` (not written until you approve).

**Scenario: Family member uploads a recording**
  Given a signed-in member of the care circle
  When they upload a valid audio file under the size limit
  Then it is stored encrypted and visible only to that circle
Source: File Upload cheat sheet   Check: automatable   Gate rule: none

**Scenario: Disguised or oversized file**
  Given a signed-in member
  When they upload an .exe renamed to .mp3, or a file far over the limit
  Then it is rejected by content type and size (not the name), nothing is stored, and the message says only "unsupported file"
Source: File Upload cheat sheet   Check: automatable   Gate rule: none

**Scenario: Unsafe filename**
  When the filename is "../../x" or contains script text
  Then the server ignores it and stores the file under a generated ID
Source: File Upload cheat sheet   Check: automatable   Gate rule: none

**Scenario: Reading someone else's recording (IDOR)**
  Given a signed-in user outside the care circle
  When they change the recording ID in the URL
  Then they get "not found", and the attempt is logged
Source: Authorization/IDOR cheat sheets, Top 10 A01   Check: automatable   Gate rule: none

**Scenario: Removed family member**
  Given a member whose access was removed
  When they use an old session or link
  Then access is denied, with no shared password change needed
Source: Session Management cheat sheet   Check: automatable   Gate rule: none

**Scenario: AI transcription service fails**
  When the third-party service is down or returns bad data
  Then the upload is kept, the user sees "transcript pending", and no recording content or health detail appears in logs or errors
Source: Error Handling, Logging cheat sheets   Check: review   Gate rule: none

**Scenario: Sending to AI service**
  When a recording would be sent out
  Then it happens only after a disclosed, approved data-handling term
Source: Cryptographic Storage/TLS; risk profile   Check: review   Gate rule: none

Later: retention/deletion, upload rate limits, virus scanning.

Next: after approval, use `writing-security-tests` on the first automatable scenario once code exists. Skills not used: security-review (no code yet).
