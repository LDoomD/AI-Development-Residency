// update-family-role.vulnerable.js
//
// Behavioral copy of the original fixture
// (.claude/skills/security-review-workspace/fixtures/update-family-role.js)
// used only so the vulnerability can be exercised against the same test
// harness as the fixed version. Logic is unchanged from the original; the
// only difference is that `db` is injected instead of required directly,
// and it's wrapped in a factory so the route handler can be grabbed and
// called without standing up a real Express server.
//
// THIS FILE INTENTIONALLY CONTAINS THE BUG: no check that the requester is
// an admin for the care recipient before changing someone's role.

const express = require('express');

function createFamilyRoleRouter(db) {
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
}

module.exports = createFamilyRoleRouter;
