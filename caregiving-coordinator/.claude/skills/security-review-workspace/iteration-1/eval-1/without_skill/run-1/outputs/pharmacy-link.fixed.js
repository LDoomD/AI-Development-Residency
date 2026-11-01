// routes/pharmacy-link.js (FIXED)
//
// Lets a family member link a parent's pharmacy portal account so the whole
// family can see refill status without each person logging in separately.
//
// Security fixes applied, relative to the original file:
//   1. SQL injection -> parameterized queries (no string interpolation into SQL).
//   2. Credential leakage -> password is never logged, in full or in part.
//   3. Plaintext credential storage -> password is encrypted at rest (AES-256-GCM)
//      before it ever reaches a db.query call.
//   4. Missing authorization (IDOR) -> both routes now require an authenticated
//      req.user and verify that user is actually allowed to manage/view the
//      given careRecipientId before touching the database.
//   5. Missing input validation -> required fields are checked and type/shape
//      validated before use.
//   6. Response leakage -> the GET route never returns the stored credential
//      material (encrypted or not) back to the client.
//
// Assumptions made (no existing app scaffolding was present to confirm these):
//   - `db.query(sql, params)` is a parameterized query helper (e.g. node-pg,
//     mysql2, or a thin wrapper around one of them) that accepts `$1, $2, ...`
//     or `?` placeholders plus a params array, and never concatenates values
//     into the SQL string itself.
//   - Some auth middleware upstream of this router sets `req.user = { id, ... }`
//     after verifying a session/JWT. If that middleware doesn't exist yet, the
//     `requireAuth` check here is a placeholder that should be replaced with
//     whatever the app's real auth stack produces.
//   - `care_recipient_links` is a table that records which userIds are allowed
//     to manage a given careRecipientId (family members linked to a recipient).
//     If the real schema differs, `assertAuthorizedForCareRecipient` is the only
//     place that needs to change.

const express = require('express');
const router = express.Router();
const db = require('../db');
const { encryptSecret, decryptSecret } = require('../lib/pharmacy-credential-crypto');

function requireAuth(req, res, next) {
  if (!req.user || !req.user.id) {
    return res.status(401).json({ error: 'Authentication required' });
  }
  next();
}

async function assertAuthorizedForCareRecipient(userId, careRecipientId) {
  const rows = await db.query(
    'SELECT 1 FROM care_recipient_links WHERE user_id = $1 AND care_recipient_id = $2',
    [userId, careRecipientId]
  );
  return rows.length > 0;
}

function isNonEmptyString(value) {
  return typeof value === 'string' && value.trim().length > 0;
}

router.post('/pharmacy-link', requireAuth, async (req, res) => {
  const { pharmacyUsername, pharmacyPassword, careRecipientId } = req.body;
  const userId = req.user.id; // trust the authenticated session, not the request body

  if (
    !isNonEmptyString(pharmacyUsername) ||
    !isNonEmptyString(pharmacyPassword) ||
    !isNonEmptyString(careRecipientId)
  ) {
    return res.status(400).json({ error: 'pharmacyUsername, pharmacyPassword, and careRecipientId are required' });
  }

  const authorized = await assertAuthorizedForCareRecipient(userId, careRecipientId);
  if (!authorized) {
    return res.status(403).json({ error: 'Not authorized to link a pharmacy account for this care recipient' });
  }

  const { ciphertext, iv, authTag } = encryptSecret(pharmacyPassword);

  await db.query(
    `INSERT INTO pharmacy_links (user_id, care_recipient_id, username, password_ciphertext, password_iv, password_auth_tag)
     VALUES ($1, $2, $3, $4, $5, $6)`,
    [userId, careRecipientId, pharmacyUsername, ciphertext, iv, authTag]
  );

  // Never log the raw username/password pair. Log identifiers only.
  console.log(`Linked pharmacy account for care recipient ${careRecipientId} by user ${userId}`);

  res.json({ success: true });
});

router.get('/pharmacy-link/:careRecipientId', requireAuth, async (req, res) => {
  const { careRecipientId } = req.params;
  const userId = req.user.id;

  if (!isNonEmptyString(careRecipientId)) {
    return res.status(400).json({ error: 'careRecipientId is required' });
  }

  const authorized = await assertAuthorizedForCareRecipient(userId, careRecipientId);
  if (!authorized) {
    return res.status(403).json({ error: 'Not authorized to view pharmacy links for this care recipient' });
  }

  const rows = await db.query(
    `SELECT id, user_id, care_recipient_id, username, created_at
     FROM pharmacy_links
     WHERE care_recipient_id = $1`,
    [careRecipientId]
  );

  // Deliberately omit password_ciphertext/password_iv/password_auth_tag from
  // the response. The decrypted password should only ever be used server-side
  // (e.g. by a job that logs into the pharmacy portal), never returned to a client.
  res.json(rows);
});

module.exports = router;
module.exports._decryptSecret = decryptSecret; // exposed for internal server-side use only, not via HTTP
