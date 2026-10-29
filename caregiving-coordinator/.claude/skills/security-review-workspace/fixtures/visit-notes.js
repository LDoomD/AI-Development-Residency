// routes/visit-notes.js
// Shows AI-generated and caregiver-written notes from a doctor visit to
// everyone in the family who has access to this care recipient.

const express = require('express');
const router = express.Router();
const db = require('../db');

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
