// routes/pharmacy-link.js (fixed)
//
// Lets a family member link a parent's pharmacy portal account so the whole
// family can see refill status without each person logging in separately.
//
// This file is the proposed secure rewrite of
// .claude/skills/security-review-workspace/fixtures/pharmacy-link.js,
// produced per the owasp-secure-coding-bdd skill. It assumes two things this
// early-stage project does not have real modules for yet, documented so the
// next integration step is explicit rather than silently assumed away:
//
//   1. `req.user` is populated by auth middleware upstream (NOT trusted from
//      req.body). There is no auth middleware in this project yet -- this
//      file is written against the contract it needs, not a real import.
//   2. `../lib/carePermissions` exposes `canAccessCareRecipient(userId,
//      careRecipientId)`, backed by a parameterized lookup against whatever
//      table records caregiver <-> care-recipient relationships. No such
//      table/module exists yet either; this is the authorization seam this
//      route needs once one does.
//
// Everything else below (parameterized queries, envelope encryption, safe
// logging) is runnable today against a real `db` module that supports
// placeholder binding (e.g. `pg`, `mysql2`, `better-sqlite3`).

const express = require('express');
const crypto = require('crypto');
const router = express.Router();
const db = require('../db');
// const { canAccessCareRecipient } = require('../lib/carePermissions'); // see note 2 above

// ---------------------------------------------------------------------------
// Cryptographic_Storage control: the pharmacy portal password is NOT a login
// password the app itself authenticates -- it's a third-party credential the
// app must later replay to the pharmacy's own portal. Hashing it (the
// Password_Storage control) would make it unusable, since a hash cannot be
// reversed to log in on the family's behalf. The correct OWASP control here
// is reversible, authenticated encryption at rest (AES-256-GCM), with the
// key held outside the database the ciphertext lives in.
//
// PHARMACY_CREDENTIAL_KEY must be a 32-byte key sourced from a secrets
// manager (AWS KMS / Vault / etc.) in production, never committed or read
// from a plain .env file long-term. It is read from env here only as the
// minimum bar this early-stage project can meet today; see
// Secrets_Management.md and Key_Management.md for the hardened end state.
function getEncryptionKey() {
  const keyHex = process.env.PHARMACY_CREDENTIAL_KEY;
  if (!keyHex || Buffer.from(keyHex, 'hex').length !== 32) {
    throw new Error(
      'PHARMACY_CREDENTIAL_KEY must be set to a 32-byte (64 hex char) key before this route can run'
    );
  }
  return Buffer.from(keyHex, 'hex');
}

function encryptCredential(plaintext) {
  const key = getEncryptionKey();
  const iv = crypto.randomBytes(12); // CSPRNG, never Math.random()
  const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
  const ciphertext = Buffer.concat([cipher.update(plaintext, 'utf8'), cipher.final()]);
  const authTag = cipher.getAuthTag();
  // Store iv + authTag alongside the ciphertext; none of this is secret on
  // its own without the key, which lives outside this table.
  return Buffer.concat([iv, authTag, ciphertext]).toString('base64');
}

function decryptCredential(encoded) {
  const key = getEncryptionKey();
  const raw = Buffer.from(encoded, 'base64');
  const iv = raw.subarray(0, 12);
  const authTag = raw.subarray(12, 28);
  const ciphertext = raw.subarray(28);
  const decipher = crypto.createDecipheriv('aes-256-gcm', key, iv);
  decipher.setAuthTag(authTag);
  return Buffer.concat([decipher.update(ciphertext), decipher.final()]).toString('utf8');
}

// ---------------------------------------------------------------------------
// Logging control: never log the credential pair. Log only the event shape
// the Logging cheat sheet asks for (who, what, when), with no secret value.
function logPharmacyLinkEvent(event, { actingUserId, careRecipientId }) {
  // A real implementation should route through one shared, sanitizing log
  // handler (OWASP Logging control #10); this inline version at least drops
  // the two fields that must never appear: pharmacyUsername, pharmacyPassword.
  console.log(
    JSON.stringify({
      timestamp: new Date().toISOString(),
      event,
      actingUserId,
      careRecipientId,
    })
  );
}

// ---------------------------------------------------------------------------
// POST /pharmacy-link
//
// Fixes applied, each paired with the @security scenario in
// pharmacy-link.feature that tests it:
//   - SQL Injection Prevention / Query Parameterization: bound parameters,
//     never string interpolation into SQL.
//   - Authorization: the acting user comes from the authenticated session
//     (req.user), not an unauthenticated req.body.userId, and must have an
//     existing care relationship with careRecipientId before a link can be
//     created for them.
//   - Cryptographic Storage: the pharmacy password is encrypted, never
//     stored or logged in plain text.
router.post('/pharmacy-link', async (req, res) => {
  const { pharmacyUsername, pharmacyPassword, careRecipientId } = req.body;
  const actingUserId = req.user && req.user.id; // trust the session, not the body

  if (!actingUserId) {
    return res.status(401).json({ error: 'authentication required' });
  }
  if (!careRecipientId || !pharmacyUsername || !pharmacyPassword) {
    return res.status(400).json({ error: 'careRecipientId, pharmacyUsername, and pharmacyPassword are required' });
  }

  // Authorization seam (see module header note 2): deny by default until a
  // real carePermissions check exists. Replace this block with
  // `if (!(await canAccessCareRecipient(actingUserId, careRecipientId))) { ... }`
  // once that module lands; keep the fail-closed behavior.
  const [relationship] = await db.query(
    'SELECT 1 FROM care_relationships WHERE caregiver_user_id = $1 AND care_recipient_id = $2',
    [actingUserId, careRecipientId]
  );
  if (!relationship) {
    return res.status(403).json({ error: 'not authorized for this care recipient' });
  }

  const encryptedPassword = encryptCredential(pharmacyPassword);

  await db.query(
    `INSERT INTO pharmacy_links (user_id, care_recipient_id, username, password)
     VALUES ($1, $2, $3, $4)`,
    [actingUserId, careRecipientId, pharmacyUsername, encryptedPassword]
  );

  logPharmacyLinkEvent('pharmacy_link_created', { actingUserId, careRecipientId });

  res.json({ success: true });
});

// ---------------------------------------------------------------------------
// GET /pharmacy-link/:careRecipientId
//
// Fixes applied:
//   - SQL Injection Prevention: bound parameter instead of interpolating
//     req.params.careRecipientId into the query string.
//   - IDOR / Authorization: the original route returned pharmacy credentials
//     for ANY careRecipientId to ANY caller with no ownership check -- a
//     textbook IDOR. It now requires an authenticated caller who has a care
//     relationship with that recipient, and a missing link or an
//     unauthorized caller both return 404 so the caller cannot distinguish
//     "doesn't exist" from "not yours" (IDOR control #5).
//   - Least data exposure: the decrypted password is never serialized back
//     to the client; only non-secret fields are returned.
router.get('/pharmacy-link/:careRecipientId', async (req, res) => {
  const actingUserId = req.user && req.user.id;
  const { careRecipientId } = req.params;

  if (!actingUserId) {
    return res.status(401).json({ error: 'authentication required' });
  }

  const rows = await db.query(
    `SELECT pl.user_id, pl.care_recipient_id, pl.username
     FROM pharmacy_links pl
     JOIN care_relationships cr
       ON cr.care_recipient_id = pl.care_recipient_id
      AND cr.caregiver_user_id = $1
     WHERE pl.care_recipient_id = $2`,
    [actingUserId, careRecipientId]
  );

  if (rows.length === 0) {
    // Same response whether the link doesn't exist or the caller isn't
    // authorized for it -- do not let the response shape leak which.
    return res.status(404).json({ error: 'not found' });
  }

  res.json(rows);
});

module.exports = router;
