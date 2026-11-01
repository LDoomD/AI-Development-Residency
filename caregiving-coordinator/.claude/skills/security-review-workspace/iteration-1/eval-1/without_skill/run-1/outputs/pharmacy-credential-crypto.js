// lib/pharmacy-credential-crypto.js
//
// Small helper used to encrypt/decrypt the pharmacy portal password at rest.
// Pharmacy passwords must be *reversible* (the app needs the plaintext to log
// into the pharmacy portal on the family's behalf), so this uses symmetric
// encryption (AES-256-GCM) rather than a one-way hash like bcrypt.
//
// Assumption: PHARMACY_CREDENTIAL_KEY is a 32-byte key provided via env var,
// base64-encoded. In a real deploy this should come from a secrets manager
// (e.g. AWS KMS / Secrets Manager), not a raw env var, but env var + rotation
// plan is a reasonable starting point for an early-stage app.

const crypto = require('crypto');

const ALGORITHM = 'aes-256-gcm';

function getKey() {
  const b64Key = process.env.PHARMACY_CREDENTIAL_KEY;
  if (!b64Key) {
    throw new Error(
      'PHARMACY_CREDENTIAL_KEY is not set. Generate one with: ' +
      "node -e \"console.log(require('crypto').randomBytes(32).toString('base64'))\""
    );
  }
  const key = Buffer.from(b64Key, 'base64');
  if (key.length !== 32) {
    throw new Error('PHARMACY_CREDENTIAL_KEY must decode to exactly 32 bytes');
  }
  return key;
}

function encryptSecret(plaintext) {
  const key = getKey();
  const iv = crypto.randomBytes(12);
  const cipher = crypto.createCipheriv(ALGORITHM, key, iv);
  const ciphertext = Buffer.concat([cipher.update(plaintext, 'utf8'), cipher.final()]);
  const authTag = cipher.getAuthTag();

  return {
    ciphertext: ciphertext.toString('base64'),
    iv: iv.toString('base64'),
    authTag: authTag.toString('base64'),
  };
}

function decryptSecret({ ciphertext, iv, authTag }) {
  const key = getKey();
  const decipher = crypto.createDecipheriv(ALGORITHM, key, Buffer.from(iv, 'base64'));
  decipher.setAuthTag(Buffer.from(authTag, 'base64'));
  const plaintext = Buffer.concat([
    decipher.update(Buffer.from(ciphertext, 'base64')),
    decipher.final(),
  ]);
  return plaintext.toString('utf8');
}

module.exports = { encryptSecret, decryptSecret };
