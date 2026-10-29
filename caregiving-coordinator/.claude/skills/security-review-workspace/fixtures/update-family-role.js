// routes/update-family-role.js
// Lets the family admin change what another family member is allowed to
// see/do for a care recipient (e.g. promote someone to co-admin, or demote
// them to view-only).

const express = require('express');
const router = express.Router();
const db = require('../db');

router.patch('/family-role/:careRecipientId/:targetUserId', async (req, res) => {
  const { role } = req.body; // 'admin' | 'editor' | 'viewer'
  const { careRecipientId, targetUserId } = req.params;

  await db.query(
    'UPDATE family_access SET role = $1 WHERE care_recipient_id = $2 AND user_id = $3',
    [role, careRecipientId, targetUserId]
  );

  res.json({ success: true, targetUserId, newRole: role });
});

module.exports = router;
