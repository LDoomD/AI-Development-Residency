// update-family-role.fixed.js
//
// Proposed fix for routes/update-family-role.js: adds the missing
// authorization check so that only a user who is already an admin for
// this specific care recipient can change anyone's role (their own or
// someone else's).
//
// Refactored into a factory (createFamilyRoleRouter(db)) that takes the db
// dependency as a parameter instead of requiring '../db' at module load
// time. That's the only structural change from the original file; it
// exists so the route handler can be unit tested with a mock db instead of
// a real database / full Express server. In the real app this would be
// wired up as:
//
//   const db = require('../db');
//   module.exports = createFamilyRoleRouter(db);
//
// Assumes an upstream auth middleware has already set req.user.id (the
// authenticated caller). If that assumption is wrong for this codebase,
// swap `req.user && req.user.id` for whatever the real auth middleware
// attaches.

const express = require('express');

function createFamilyRoleRouter(db) {
  const router = express.Router();

  router.patch('/family-role/:careRecipientId/:targetUserId', async (req, res) => {
    const { role } = req.body; // 'admin' | 'editor' | 'viewer'
    const { careRecipientId, targetUserId } = req.params;
    const requesterId = req.user && req.user.id;

    if (!requesterId) {
      return res.status(401).json({ error: 'Unauthorized' });
    }

    const requesterAccess = await db.query(
      'SELECT role FROM family_access WHERE care_recipient_id = $1 AND user_id = $2',
      [careRecipientId, requesterId]
    );
    const requesterRole = requesterAccess.rows[0] && requesterAccess.rows[0].role;

    // Requester must be an admin FOR THIS CARE RECIPIENT, not just an admin
    // somewhere else in the system. This also implicitly blocks a non-admin
    // from "promoting themselves" since the self case is just
    // targetUserId === requesterId checked against the same rule.
    if (requesterRole !== 'admin') {
      return res.status(403).json({ error: 'Forbidden: admin access required for this care recipient' });
    }

    await db.query(
      'UPDATE family_access SET role = $1 WHERE care_recipient_id = $2 AND user_id = $3',
      [role, careRecipientId, targetUserId]
    );

    res.json({ success: true, targetUserId, newRole: role });
  });

  return router;
}

module.exports = createFamilyRoleRouter;
