// visit-notes.vulnerable.js
// Verbatim copy of the finding under test
// (.claude/skills/security-review-workspace/fixtures/visit-notes.js),
// with only the require path for `db` changed to point at the local test
// stub instead of the real ../db module. Logic is unchanged: note_text is
// concatenated straight into the HTML string with no escaping.

const express = require('express');
const router = express.Router();
const db = require('./db.stub');

router.get('/visit-notes/:careRecipientId', async (req, res) => {
  const notes = await db.query(
    'SELECT author_name, note_text, created_at FROM visit_notes WHERE care_recipient_id = $1',
    [req.params.careRecipientId]
  );

  let html = '<html><body><h1>Visit Notes</h1>';
  for (const note of notes) {
    html += `<div class="note">
      <strong>${note.author_name}</strong> — ${note.created_at}
      <p>${note.note_text}</p>
    </div>`;
  }
  html += '</body></html>';

  res.send(html);
});

module.exports = router;
