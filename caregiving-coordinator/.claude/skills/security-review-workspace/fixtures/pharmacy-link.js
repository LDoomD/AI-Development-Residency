// routes/pharmacy-link.js
// Lets a family member link a parent's pharmacy portal account so the whole
// family can see refill status without each person logging in separately.

const express = require('express');
const router = express.Router();
const db = require('../db');

router.post('/pharmacy-link', async (req, res) => {
  const { userId, pharmacyUsername, pharmacyPassword, careRecipientId } = req.body;

  await db.query(
    `INSERT INTO pharmacy_links (user_id, care_recipient_id, username, password)
     VALUES ('${userId}', '${careRecipientId}', '${pharmacyUsername}', '${pharmacyPassword}')`
  );

  console.log(`Linked pharmacy account for care recipient ${careRecipientId}: ${pharmacyUsername}/${pharmacyPassword}`);

  res.json({ success: true });
});

router.get('/pharmacy-link/:careRecipientId', async (req, res) => {
  const rows = await db.query(
    `SELECT * FROM pharmacy_links WHERE care_recipient_id = '${req.params.careRecipientId}'`
  );
  res.json(rows);
});

module.exports = router;
