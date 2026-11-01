// visit-notes.fixed.js
// Same route, same query, same template shape as the finding — the only
// change is the control: every value interpolated into the HTML string
// (author_name, created_at, note_text) is passed through escapeHtml()
// before concatenation, so a stored payload like
// `<script>alert(1)</script>` renders as inert text, not executable markup.

const express = require('express');
const router = express.Router();
const db = require('./db.stub');

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

router.get('/visit-notes/:careRecipientId', async (req, res) => {
  const notes = await db.query(
    'SELECT author_name, note_text, created_at FROM visit_notes WHERE care_recipient_id = $1',
    [req.params.careRecipientId]
  );

  let html = '<html><body><h1>Visit Notes</h1>';
  for (const note of notes) {
    html += `<div class="note">
      <strong>${escapeHtml(note.author_name)}</strong> — ${escapeHtml(note.created_at)}
      <p>${escapeHtml(note.note_text)}</p>
    </div>`;
  }
  html += '</body></html>';

  res.send(html);
});

module.exports = router;
