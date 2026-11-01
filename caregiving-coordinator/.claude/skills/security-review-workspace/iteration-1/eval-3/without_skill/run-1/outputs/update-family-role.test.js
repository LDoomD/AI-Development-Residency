// update-family-role.test.js
//
// Proves: a non-admin for a care recipient cannot change ANY family
// member's role for that care recipient, including their own (no
// self-promotion), and that a legitimate admin still can (so the fix
// doesn't just block everything).
//
// Run with: node --test update-family-role.test.js
// (uses Node's built-in test runner, no install needed)

const test = require('node:test');
const assert = require('node:assert/strict');

const { createMockDb } = require('./db.mock.js');
const createFamilyRoleRouter = require('./update-family-role.fixed.js');

// Pulls the raw PATCH handler off the router so it can be called directly
// with fake req/res objects, without spinning up an HTTP server.
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

test('non-admin cannot promote themselves to admin', async () => {
  const db = createMockDb([
    { care_recipient_id: 'care-1', user_id: 'viewer-1', role: 'viewer' },
    { care_recipient_id: 'care-1', user_id: 'admin-1', role: 'admin' },
  ]);
  const handler = getHandler(createFamilyRoleRouter(db));

  const req = {
    params: { careRecipientId: 'care-1', targetUserId: 'viewer-1' },
    body: { role: 'admin' },
    user: { id: 'viewer-1' }, // requester === target: self-promotion attempt
  };
  const res = mockRes();

  await handler(req, res);

  assert.equal(res.statusCode, 403, 'expected 403 Forbidden for self-promotion by a non-admin');
  const stored = db.rows.find((r) => r.user_id === 'viewer-1');
  assert.equal(stored.role, 'viewer', 'role must be unchanged after a rejected request');
});

test('non-admin cannot change a DIFFERENT member\'s role', async () => {
  const db = createMockDb([
    { care_recipient_id: 'care-1', user_id: 'viewer-1', role: 'viewer' },
    { care_recipient_id: 'care-1', user_id: 'editor-1', role: 'editor' },
    { care_recipient_id: 'care-1', user_id: 'admin-1', role: 'admin' },
  ]);
  const handler = getHandler(createFamilyRoleRouter(db));

  const req = {
    params: { careRecipientId: 'care-1', targetUserId: 'viewer-1' },
    body: { role: 'admin' },
    user: { id: 'editor-1' }, // editor trying to promote someone else to admin
  };
  const res = mockRes();

  await handler(req, res);

  assert.equal(res.statusCode, 403);
  const stored = db.rows.find((r) => r.user_id === 'viewer-1');
  assert.equal(stored.role, 'viewer');
});

test('user with no family_access row for this care recipient cannot change roles', async () => {
  const db = createMockDb([
    { care_recipient_id: 'care-1', user_id: 'viewer-1', role: 'viewer' },
  ]);
  const handler = getHandler(createFamilyRoleRouter(db));

  const req = {
    params: { careRecipientId: 'care-1', targetUserId: 'viewer-1' },
    body: { role: 'admin' },
    user: { id: 'stranger-1' }, // not in family_access for care-1 at all
  };
  const res = mockRes();

  await handler(req, res);

  assert.equal(res.statusCode, 403);
  const stored = db.rows.find((r) => r.user_id === 'viewer-1');
  assert.equal(stored.role, 'viewer');
});

test('admin for a different care recipient cannot act on this one', async () => {
  const db = createMockDb([
    { care_recipient_id: 'care-1', user_id: 'viewer-1', role: 'viewer' },
    { care_recipient_id: 'care-2', user_id: 'roaming-admin', role: 'admin' }, // admin, but elsewhere
  ]);
  const handler = getHandler(createFamilyRoleRouter(db));

  const req = {
    params: { careRecipientId: 'care-1', targetUserId: 'viewer-1' },
    body: { role: 'admin' },
    user: { id: 'roaming-admin' },
  };
  const res = mockRes();

  await handler(req, res);

  assert.equal(res.statusCode, 403);
  const stored = db.rows.find((r) => r.user_id === 'viewer-1');
  assert.equal(stored.role, 'viewer');
});

test('control: a real admin for this care recipient CAN change another member\'s role', async () => {
  const db = createMockDb([
    { care_recipient_id: 'care-1', user_id: 'viewer-1', role: 'viewer' },
    { care_recipient_id: 'care-1', user_id: 'admin-1', role: 'admin' },
  ]);
  const handler = getHandler(createFamilyRoleRouter(db));

  const req = {
    params: { careRecipientId: 'care-1', targetUserId: 'viewer-1' },
    body: { role: 'editor' },
    user: { id: 'admin-1' },
  };
  const res = mockRes();

  await handler(req, res);

  assert.equal(res.statusCode, 200);
  const stored = db.rows.find((r) => r.user_id === 'viewer-1');
  assert.equal(stored.role, 'editor');
});
