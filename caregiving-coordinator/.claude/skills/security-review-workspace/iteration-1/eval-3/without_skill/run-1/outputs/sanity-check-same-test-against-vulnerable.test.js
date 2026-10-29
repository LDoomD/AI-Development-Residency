// sanity-check-same-test-against-vulnerable.test.js
//
// Not part of either deliverable suite. Re-runs the exact same assertions
// as update-family-role.test.js but wired to the UNPATCHED handler, to
// prove the test suite actually discriminates between vulnerable and
// fixed code (red before the fix, green after). Expected result: these
// all FAIL, because the vulnerable handler has no authorization check.
//
// Run with: node --test sanity-check-same-test-against-vulnerable.test.js

const test = require('node:test');
const assert = require('node:assert/strict');

const { createMockDb } = require('./db.mock.js');
const createVulnerableRouter = require('./update-family-role.vulnerable.js');

function getHandler(router) {
  return router.stack[0].route.stack[0].handle;
}

function mockRes() {
  return {
    statusCode: 200,
    body: null,
    status(code) {
      this.statusCode = code;
      return this;
    },
    json(payload) {
      this.body = payload;
      return this;
    },
  };
}

test('[expected to FAIL on vulnerable code] non-admin cannot promote themselves to admin', async () => {
  const db = createMockDb([
    { care_recipient_id: 'care-1', user_id: 'viewer-1', role: 'viewer' },
  ]);
  const handler = getHandler(createVulnerableRouter(db));

  const req = {
    params: { careRecipientId: 'care-1', targetUserId: 'viewer-1' },
    body: { role: 'admin' },
    user: { id: 'viewer-1' },
  };
  const res = mockRes();

  await handler(req, res);

  assert.equal(res.statusCode, 403);
  const stored = db.rows.find((r) => r.user_id === 'viewer-1');
  assert.equal(stored.role, 'viewer');
});

test('[expected to FAIL on vulnerable code] non-admin cannot change a different member\'s role', async () => {
  const db = createMockDb([
    { care_recipient_id: 'care-1', user_id: 'viewer-1', role: 'viewer' },
    { care_recipient_id: 'care-1', user_id: 'editor-1', role: 'editor' },
  ]);
  const handler = getHandler(createVulnerableRouter(db));

  const req = {
    params: { careRecipientId: 'care-1', targetUserId: 'viewer-1' },
    body: { role: 'admin' },
    user: { id: 'editor-1' },
  };
  const res = mockRes();

  await handler(req, res);

  assert.equal(res.statusCode, 403);
  const stored = db.rows.find((r) => r.user_id === 'viewer-1');
  assert.equal(stored.role, 'viewer');
});
