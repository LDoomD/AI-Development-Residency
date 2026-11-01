// visit-notes.xss.test.js
//
// Proves (or disproves) that routes/visit-notes.js cannot be used to inject
// executable script into the rendered page via `note_text` (or `author_name`).
//
// Why this approach:
//   routes/visit-notes.js has no package.json / node_modules next to it (it's
//   a fixture file pulled out of the real app for a security review), and
//   this project has no test framework installed. Rather than adding a
//   dependency or reimplementing the route's logic in the test (which would
//   only prove the *reimplementation* is safe, not the real file), this test
//   stubs out the two things visit-notes.js requires at the top of the file
//   -- 'express' and '../db' -- and then loads and runs the ACTUAL route
//   handler from the real file. That way the assertions are exercising the
//   real vulnerable (or fixed) code path.
//
// Run with: node --test visit-notes.xss.test.js
// Uses only Node's built-in test runner (node:test) + assert -- no install
// needed (requires Node >= 18; this machine has v26).

const { test } = require('node:test');
const assert = require('node:assert/strict');
const Module = require('node:module');
const path = require('node:path');

const ROUTE_PATH = path.join(
  __dirname,
  '..', '..', '..', '..', '..', // up to security-review-workspace
  'fixtures',
  'visit-notes.js'
);

// --- Minimal fake 'express' + fake '../db', injected only for this file ---

function loadRouteHandler(fakeDbRows) {
  const originalLoad = Module._load;

  Module._load = function (request, parent, isMain) {
    if (request === 'express') {
      // Fake express module: just enough surface for `express.Router()`
      // and `router.get(path, handler)` to work.
      return {
        Router() {
          const handlers = {};
          return {
            get(routePath, handler) {
              handlers[routePath] = handler;
            },
            __handlers: handlers,
          };
        },
      };
    }
    if (request === '../db') {
      // Fake db module: query() resolves with attacker-controlled rows.
      return {
        query: async () => fakeDbRows,
      };
    }
    return originalLoad.apply(this, arguments);
  };

  // Force a fresh require so our stubs are actually used.
  delete require.cache[ROUTE_PATH];
  let router;
  try {
    router = require(ROUTE_PATH);
  } finally {
    Module._load = originalLoad; // always restore, even if require throws
  }

  const handler = router.__handlers['/visit-notes/:careRecipientId'];
  assert.ok(handler, 'expected GET /visit-notes/:careRecipientId handler to be registered');
  return handler;
}

// Fake Express req/res. We only need res.send() to capture the final HTML
// string the route would have sent to the browser.
function makeReqRes(careRecipientId) {
  const req = { params: { careRecipientId } };
  let sent = null;
  const res = {
    send(html) {
      sent = html;
    },
  };
  return { req, res, getSent: () => sent };
}

test('note_text containing a <script> payload is not sent to the browser unescaped', async () => {
  const payload = '<script>alert(document.cookie)</script>';
  const handler = loadRouteHandler([
    { author_name: 'Jane Caregiver', note_text: payload, created_at: '2026-10-29' },
  ]);

  const { req, res, getSent } = makeReqRes('recipient-123');
  await handler(req, res);
  const html = getSent();

  assert.ok(html, 'route should have called res.send() with HTML');
  assert.ok(
    !html.includes('<script>alert(document.cookie)</script>'),
    'raw <script> tag from note_text must not appear verbatim in the response HTML -- ' +
      'this means it would execute in the viewer\'s browser (stored XSS)'
  );
});

test('note_text containing an onerror-image payload is not sent to the browser unescaped', async () => {
  const payload = '<img src="x" onerror="alert(1)">';
  const handler = loadRouteHandler([
    { author_name: 'Jane Caregiver', note_text: payload, created_at: '2026-10-29' },
  ]);

  const { req, res, getSent } = makeReqRes('recipient-123');
  await handler(req, res);
  const html = getSent();

  assert.ok(
    !/<img[^>]*onerror=/i.test(html),
    'an onerror handler attribute from note_text must not survive into the response HTML'
  );
});

test('author_name containing a script payload is not sent to the browser unescaped', async () => {
  // Same bug, same line of code -- author_name is concatenated the same way
  // note_text is. Included because it's the identical vulnerability class in
  // the same file, not a separate issue.
  const payload = '<script>alert(1)</script>';
  const handler = loadRouteHandler([
    { author_name: payload, note_text: 'Patient is doing well.', created_at: '2026-10-29' },
  ]);

  const { req, res, getSent } = makeReqRes('recipient-123');
  await handler(req, res);
  const html = getSent();

  assert.ok(
    !html.includes('<script>alert(1)</script>'),
    'raw <script> tag from author_name must not appear verbatim in the response HTML'
  );
});

test('sanity check: a normal, benign note still renders its text content', async () => {
  const handler = loadRouteHandler([
    { author_name: 'Jane Caregiver', note_text: 'Blood pressure was normal today.', created_at: '2026-10-29' },
  ]);

  const { req, res, getSent } = makeReqRes('recipient-123');
  await handler(req, res);
  const html = getSent();

  assert.ok(
    html.includes('Blood pressure was normal today.'),
    'ordinary note text should still be visible in the rendered page (escaping must not corrupt legitimate content)'
  );
});
