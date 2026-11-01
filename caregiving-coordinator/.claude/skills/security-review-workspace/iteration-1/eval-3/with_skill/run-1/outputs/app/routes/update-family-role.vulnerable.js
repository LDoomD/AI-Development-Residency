// Exact copy of the fixture flagged by security review — no authorization
// check. Used only to show the test failing (red) before the fix exists.
// Source: .claude/skills/security-review-workspace/fixtures/update-family-role.js

const express = require('express');

module.exports = function buildRouter(db) {
  const router = express.Router();
  router.patch('/family-role/:careRecipientId/:targetUserId', async (req, res) => {
    const { role } = req.body; // 'admin' | 'editor' | 'viewer'
    const { careRecipientId, targetUserId } = req.params;

    await db.query(
      'UPDATE family_access SET role = $1 WHERE care_recipient_id = $2 AND user_id = $3',
      [role, careRecipientId, targetUserId]
    );

    res.json({ success: true, targetUserId, newRole: role });
  });

  return router;
};
