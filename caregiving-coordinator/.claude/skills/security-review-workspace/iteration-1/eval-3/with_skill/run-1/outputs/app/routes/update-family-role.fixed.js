// routes/update-family-role.js (fixed)
// Lets the family admin change what another family member is allowed to
// see/do for a care recipient (e.g. promote someone to co-admin, or demote
// them to view-only).
//
// Fix: the original version had no check that the requester is an admin
// for this specific care recipient, so any authenticated caller could
// promote themselves (or anyone else) to admin via this endpoint. This
// version looks up the requester's own family_access row for the same
// care recipient and rejects the request with 403 unless that row's role
// is 'admin'.
//
// Test seam note: this fixture has no real auth middleware, so the test
// harness sets `req.user = { id }` directly (simulating whatever the
// project's real session/auth middleware would attach) rather than
// wiring a full login flow.

const express = require('express');

module.exports = function buildRouter(db) {
  const router = express.Router();
  router.patch('/family-role/:careRecipientId/:targetUserId', async (req, res) => {
    const { role } = req.body; // 'admin' | 'editor' | 'viewer'
    const { careRecipientId, targetUserId } = req.params;
    const requesterId = req.user && req.user.id;

    if (!requesterId) {
      return res.status(401).json({ error: 'Not authenticated' });
    }

    const { rows } = await db.query(
      'SELECT role FROM family_access WHERE care_recipient_id = $1 AND user_id = $2',
      [careRecipientId, requesterId]
    );
    const requesterRole = rows[0] && rows[0].role;

    if (requesterRole !== 'admin') {
      return res
        .status(403)
        .json({ error: 'Only an admin for this care recipient can change roles' });
    }

    await db.query(
      'UPDATE family_access SET role = $1 WHERE care_recipient_id = $2 AND user_id = $3',
      [role, careRecipientId, targetUserId]
    );

    res.json({ success: true, targetUserId, newRole: role });
  });

  return router;
};
