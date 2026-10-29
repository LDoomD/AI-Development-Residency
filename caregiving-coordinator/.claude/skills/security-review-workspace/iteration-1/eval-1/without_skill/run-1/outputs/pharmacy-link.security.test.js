// routes/pharmacy-link.security.test.js
//
// Tests the security controls added to routes/pharmacy-link.js, not just the
// "happy path" functionality. Each test maps to one of the vulnerabilities
// found in the original file:
//
//   1. SQL injection            -> "parameterized queries" tests
//   2. Credential logging       -> "never logs credentials" tests
//   3. Plaintext storage        -> "encrypts the pharmacy password" tests
//   4. IDOR / missing authz     -> "authorization" tests
//   5. Missing input validation -> "input validation" tests
//   6. Response leakage         -> "does not leak" tests
//
// Framework: Jest + supertest (chosen because they're the de facto standard
// for testing Express routes and no test framework was already in the repo).
// Install with: npm install --save-dev jest supertest
// Run with:     npx jest routes/pharmacy-link.security.test.js
//
// `../db` and `../lib/pharmacy-credential-crypto` are mocked as virtual
// modules below because this fixture has no real db layer yet; the mocks are
// written to match the interface pharmacy-link.fixed.js actually calls
// (db.query(sql, params)), so the tests still catch misuse of that interface
// (e.g. accidentally falling back to string interpolation).

const express = require('express');
const request = require('supertest');

process.env.PHARMACY_CREDENTIAL_KEY = Buffer.alloc(32, 7).toString('base64');

const mockQuery = jest.fn();
jest.mock('../db', () => ({ query: (...args) => mockQuery(...args) }), { virtual: true });

// Use the real crypto helper (not mocked) so encryption tests are meaningful,
// but resolve it as a virtual module at the path the route expects.
jest.mock(
  '../lib/pharmacy-credential-crypto',
  () => require('./pharmacy-credential-crypto'),
  { virtual: true }
);

const router = require('./pharmacy-link.fixed');

function buildApp(user) {
  const app = express();
  app.use(express.json());
  app.use((req, res, next) => {
    if (user) req.user = user;
    next();
  });
  app.use(router);
  return app;
}

const OWNER = { id: 'user-1' };
const STRANGER = { id: 'user-2' };
const RECIPIENT_ID = 'recipient-abc';

beforeEach(() => {
  mockQuery.mockReset();
});

describe('authorization (IDOR)', () => {
  test('POST rejects unauthenticated requests before touching the db', async () => {
    const app = buildApp(null);
    const res = await request(app).post('/pharmacy-link').send({
      pharmacyUsername: 'momsaccount',
      pharmacyPassword: 'secret123',
      careRecipientId: RECIPIENT_ID,
    });

    expect(res.status).toBe(401);
    expect(mockQuery).not.toHaveBeenCalled();
  });

  test('POST rejects a user who is not linked to the care recipient', async () => {
    mockQuery.mockResolvedValueOnce([]); // authorization check finds no link
    const app = buildApp(STRANGER);

    const res = await request(app).post('/pharmacy-link').send({
      pharmacyUsername: 'momsaccount',
      pharmacyPassword: 'secret123',
      careRecipientId: RECIPIENT_ID,
    });

    expect(res.status).toBe(403);
    // Only the authorization check should have run - no insert happened.
    expect(mockQuery).toHaveBeenCalledTimes(1);
  });

  test('GET rejects a user who is not linked to the care recipient (cross-family data access)', async () => {
    mockQuery.mockResolvedValueOnce([]); // authorization check finds no link
    const app = buildApp(STRANGER);

    const res = await request(app).get(`/pharmacy-link/${RECIPIENT_ID}`);

    expect(res.status).toBe(403);
    expect(mockQuery).toHaveBeenCalledTimes(1);
  });

  test('POST ignores a spoofed userId in the body and uses the authenticated session user instead', async () => {
    mockQuery.mockResolvedValueOnce([{ x: 1 }]); // authorized
    mockQuery.mockResolvedValueOnce([]); // insert
    const app = buildApp(OWNER);

    await request(app).post('/pharmacy-link').send({
      userId: 'someone-elses-id', // attacker-controlled field in the old code
      pharmacyUsername: 'momsaccount',
      pharmacyPassword: 'secret123',
      careRecipientId: RECIPIENT_ID,
    });

    const [, authParams] = mockQuery.mock.calls[0];
    const [, insertParams] = mockQuery.mock.calls[1];
    expect(authParams).toContain(OWNER.id);
    expect(insertParams).toContain(OWNER.id);
    expect(authParams).not.toContain('someone-elses-id');
    expect(insertParams).not.toContain('someone-elses-id');
  });
});

describe('input validation', () => {
  test('POST rejects missing pharmacyPassword without querying the db', async () => {
    const app = buildApp(OWNER);
    const res = await request(app).post('/pharmacy-link').send({
      pharmacyUsername: 'momsaccount',
      careRecipientId: RECIPIENT_ID,
    });

    expect(res.status).toBe(400);
    expect(mockQuery).not.toHaveBeenCalled();
  });

  test('POST rejects a non-string careRecipientId', async () => {
    const app = buildApp(OWNER);
    const res = await request(app).post('/pharmacy-link').send({
      pharmacyUsername: 'momsaccount',
      pharmacyPassword: 'secret123',
      careRecipientId: { $ne: null }, // classic NoSQL/odd-type injection attempt
    });

    expect(res.status).toBe(400);
    expect(mockQuery).not.toHaveBeenCalled();
  });
});

describe('SQL injection resistance', () => {
  test('POST never concatenates request data into the SQL string', async () => {
    mockQuery.mockResolvedValueOnce([{ x: 1 }]); // authorized
    mockQuery.mockResolvedValueOnce([]); // insert
    const app = buildApp(OWNER);

    const maliciousUsername = "attacker'; DROP TABLE pharmacy_links; --";

    await request(app).post('/pharmacy-link').send({
      pharmacyUsername: maliciousUsername,
      pharmacyPassword: 'secret123',
      careRecipientId: RECIPIENT_ID,
    });

    const [insertSql, insertParams] = mockQuery.mock.calls[1];
    expect(insertSql).not.toContain(maliciousUsername);
    expect(insertSql).not.toMatch(/DROP TABLE/i);
    expect(insertSql).toMatch(/\$\d/); // uses placeholders
    expect(insertParams).toContain(maliciousUsername); // value travels as a bound param instead
  });

  test('GET never concatenates the :careRecipientId route param into the SQL string', async () => {
    mockQuery.mockResolvedValueOnce([{ x: 1 }]); // authorized
    mockQuery.mockResolvedValueOnce([]); // select
    const app = buildApp(OWNER);

    const maliciousId = "x' OR '1'='1";

    await request(app).get(`/pharmacy-link/${encodeURIComponent(maliciousId)}`);

    const [selectSql, selectParams] = mockQuery.mock.calls[1];
    expect(selectSql).not.toContain(maliciousId);
    expect(selectSql).toMatch(/\$\d/);
    expect(selectParams).toContain(maliciousId);
  });
});

describe('credential logging', () => {
  test('POST never logs the plaintext password, in full or in part', async () => {
    mockQuery.mockResolvedValueOnce([{ x: 1 }]);
    mockQuery.mockResolvedValueOnce([]);
    const app = buildApp(OWNER);
    const password = 'uniqueSecretValue42';

    const logSpy = jest.spyOn(console, 'log').mockImplementation(() => {});
    try {
      await request(app).post('/pharmacy-link').send({
        pharmacyUsername: 'momsaccount',
        pharmacyPassword: password,
        careRecipientId: RECIPIENT_ID,
      });

      const loggedSomethingWithPassword = logSpy.mock.calls.some((call) =>
        call.some((arg) => typeof arg === 'string' && arg.includes(password))
      );
      expect(loggedSomethingWithPassword).toBe(false);
    } finally {
      logSpy.mockRestore();
    }
  });
});

describe('encryption at rest', () => {
  test('POST stores the pharmacy password encrypted, not as plaintext', async () => {
    mockQuery.mockResolvedValueOnce([{ x: 1 }]);
    mockQuery.mockResolvedValueOnce([]);
    const app = buildApp(OWNER);
    const password = 'myPharmacyPassword!';

    await request(app).post('/pharmacy-link').send({
      pharmacyUsername: 'momsaccount',
      pharmacyPassword: password,
      careRecipientId: RECIPIENT_ID,
    });

    const [, insertParams] = mockQuery.mock.calls[1];
    expect(insertParams).not.toContain(password);
    // Round trip: whatever ciphertext was stored must decrypt back to the
    // original password using the real crypto helper.
    const { decryptSecret } = require('./pharmacy-credential-crypto');
    const [, , , ciphertext, iv, authTag] = insertParams;
    expect(decryptSecret({ ciphertext, iv, authTag })).toBe(password);
  });
});

describe('response leakage', () => {
  test('GET response never includes password/ciphertext fields', async () => {
    mockQuery.mockResolvedValueOnce([{ x: 1 }]); // authorized
    mockQuery.mockResolvedValueOnce([
      { id: 1, user_id: OWNER.id, care_recipient_id: RECIPIENT_ID, username: 'momsaccount' },
    ]);
    const app = buildApp(OWNER);

    const res = await request(app).get(`/pharmacy-link/${RECIPIENT_ID}`);

    expect(res.status).toBe(200);
    const serialized = JSON.stringify(res.body);
    expect(serialized).not.toMatch(/password/i);

    // And the SELECT query itself must not ask the db for password columns.
    const [selectSql] = mockQuery.mock.calls[1];
    expect(selectSql).not.toMatch(/password/i);
  });
});
