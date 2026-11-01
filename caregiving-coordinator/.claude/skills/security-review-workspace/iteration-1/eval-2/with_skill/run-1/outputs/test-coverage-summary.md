# Security Test Coverage: routes/visit-notes.js

## Proven (test written and passing)

| Finding | Attack tested | Structural control | Test file | Command run |
| --- | --- | --- | --- | --- |
| Stored XSS: `note_text` concatenated unescaped into the HTML response | GET `/visit-notes/:careRecipientId` returns a note with `note_text = '<script>alert(document.cookie)</script>'` | HTML-escaping (`escapeHtml`) applied to `author_name`, `created_at`, and `note_text` before string concatenation | `visit-notes.xss.test.js` | `npx jest --colors=false` — "FIXED route" test: **1 passed** |

Red/green evidence, both runs in this session:
- Against `visit-notes.vulnerable.js` (verbatim copy of the real finding, only the `db` require path changed to a local stub): the test **fails** — `res.text` contains the raw `<script>alert(document.cookie)</script>`. This proves the test actually detects the bug.
- Against `visit-notes.fixed.js` (same route, same query, escaping added): the test **passes** — the payload appears only as the inert `&lt;script&gt;alert(document.cookie)&lt;/script&gt;`.

## Still open (no passing test yet)

None for this finding — `author_name` and `created_at` are escaped the same way in the fix and covered by the same request/response round trip, though no dedicated assertion isolates each field individually.

## Not attempted

- The real `routes/visit-notes.js` was not modified in place — the repo copy under `.claude/skills/security-review-workspace/fixtures/` was left untouched as the reference "before" state. The actual fix should be applied there (escape `note.author_name`, `note.created_at`, `note.note_text` the same way `visit-notes.fixed.js` does) and this test re-pointed at it once that change lands.
- No test framework existed in this fixtures folder, so Jest + Supertest + Express were installed as devDependencies scoped to this `outputs/` directory only (`package.json` here) — not added to any real project manifest.
