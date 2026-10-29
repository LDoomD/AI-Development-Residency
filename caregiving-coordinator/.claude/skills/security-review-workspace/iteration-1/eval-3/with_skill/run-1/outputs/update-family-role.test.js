// Security finding: routes/update-family-role.js changes a family member's
// role for a care recipient with no check that the requester is an admin
// for that care recipient. Any authenticated caller could promote
// themselves or anyone else to admin.
//
// Seam under test: PATCH /family-role/:careRecipientId/:targetUserId
// Attack: a non-admin ('viewer1') sends this request, targeting either
// another member (self-escalation's sibling case) or themselves
// (self-promotion).
// Control under test: the authorization check that requires the
// requester's own family_access role for this care recipient to be
// 'admin' before the UPDATE runs.
//
// ROUTE_VERSION env var selects which implementation is mounted:
//   'vulnerable' -> the original flagged fixture (expected to FAIL these tests)
//   'fixed'      -> the version with the authorization check (expected to PASS)

const express = require('express');
const request = require('supertest');
const { createDb } = require('./app/db');

const ROUTE_VERSION = process.env.ROUTE_VERSION === 'fixed' ? 'fixed' : 'vulnerable';
const buildRouter =
  ROUTE_VERSION === 'fixed'
    ? require('./app/routes/update-family-role.fixed')
    : require('./app/routes/update-family-role.vulnerable');

function buildApp(db, requesterId) {
  const app = express();
  app.use(express.json());
  // Stand-in for real session/auth middleware: attaches the authenticated
  // requester's id to req.user, same as the real app would after login.
  app.use((req, res, next) => {
    req.user = requesterId ? { id: requesterId } : undefined;
    next();
  });
  app.use(buildRouter(db));
  return app;
}

describe(`PATCH /family-role (${ROUTE_VERSION})`, () => {
  function seedDb() {
    return createDb([
      { care_recipient_id: 'cr1', user_id: 'admin1', role: 'admin' },
      { care_recipient_id: 'cr1', user_id: 'viewer1', role: 'viewer' },
      { care_recipient_id: 'cr1', user_id: 'viewer2', role: 'viewer' },
    ]);
  }

  test('a non-admin cannot promote another member to admin', async () => {
    const db = seedDb();
    const app = buildApp(db, 'viewer1'); // viewer1 is not admin for cr1

    const res = await request(app)
      .patch('/family-role/cr1/viewer2')
      .send({ role: 'admin' });

    expect(res.status).toBe(403);
    const viewer2Row = db._rows.find((r) => r.user_id === 'viewer2');
    expect(viewer2Row.role).toBe('viewer'); // unchanged
  });

  test('a non-admin cannot promote themselves to admin (self-escalation)', async () => {
    const db = seedDb();
    const app = buildApp(db, 'viewer1'); // viewer1 is not admin for cr1

    const res = await request(app)
      .patch('/family-role/cr1/viewer1')
      .send({ role: 'admin' });

    expect(res.status).toBe(403);
    const selfRow = db._rows.find((r) => r.user_id === 'viewer1');
    expect(selfRow.role).toBe('viewer'); // unchanged, no self-promotion
  });

  test('an actual admin for the care recipient can still change roles (control case)', async () => {
    const db = seedDb();
    const app = buildApp(db, 'admin1'); // admin1 IS admin for cr1

    const res = await request(app)
      .patch('/family-role/cr1/viewer2')
      .send({ role: 'editor' });

    expect(res.status).toBe(200);
    const viewer2Row = db._rows.find((r) => r.user_id === 'viewer2');
    expect(viewer2Row.role).toBe('editor');
  });
});
