// visit-notes.xss.test.js
//
// Finding: routes/visit-notes.js concatenates note_text (and author_name,
// created_at) straight into an HTML string with no escaping. A stored
// payload in a note (e.g. a malicious caregiver or a compromised AI-note
// generator writing `<script>...</script>` into note_text) would execute
// in the browser of every family member who later views that care
// recipient's notes — classic stored XSS.
//
// Attack: GET /visit-notes/:careRecipientId where one of the returned
// notes has note_text = '<script>alert(document.cookie)</script>'.
//
// Control under test: HTML-escaping of every interpolated field before it
// goes into the response body, so the payload comes back as inert text
// (&lt;script&gt;...) instead of a live <script> tag.
//
// This file is run twice against two route modules that share the same
// query and template shape:
//   - visit-notes.vulnerable.js: unescaped copy of the real finding (RED)
//   - visit-notes.fixed.js: same route with escapeHtml() applied (GREEN)
// This proves the test would actually have caught the original bug, and
// that the fix closes it.

const express = require('express');
const request = require('supertest');

const XSS_PAYLOAD = '<script>alert(document.cookie)</script>';

function buildApp(routerPath) {
  // Fresh require each time so the two route modules don't share module
  // cache / db.stub state.
  jest.resetModules();
  const dbStub = require('./db.stub');
  dbStub.__setRows([
    {
      author_name: 'Jane Caregiver',
      note_text: XSS_PAYLOAD,
      created_at: '2026-10-29',
    },
  ]);

  const router = require(routerPath);
  const app = express();
  app.use('/', router);
  return app;
}

describe('visit-notes stored XSS (note_text output escaping)', () => {
  test('VULNERABLE route: raw <script> payload survives into the HTML response (expected to fail if the control is in place)', async () => {
    const app = buildApp('./visit-notes.vulnerable.js');

    const res = await request(app).get('/visit-notes/42');

    expect(res.status).toBe(200);
    // This assertion is the control: it should be IMPOSSIBLE for the raw,
    // executable <script> tag to appear in the response body.
    expect(res.text).not.toContain('<script>alert(document.cookie)</script>');
  });

  test('FIXED route: note_text is HTML-escaped, so the <script> payload is rendered inert', async () => {
    const app = buildApp('./visit-notes.fixed.js');

    const res = await request(app).get('/visit-notes/42');

    expect(res.status).toBe(200);
    // The control: no raw, executable <script> tag in the response.
    expect(res.text).not.toContain('<script>alert(document.cookie)</script>');
    // And positive proof the content is still present, just neutralized.
    expect(res.text).toContain('&lt;script&gt;alert(document.cookie)&lt;/script&gt;');
  });
});
