// Minimal in-memory stand-in for the real db module (pg-like `query(sql, params)`
// interface), used only so the route under test can run without a live Postgres
// instance. Seeded per-test by the test file below.

function createDb(seedRows) {
  // seedRows: array of { care_recipient_id, user_id, role }
  const rows = seedRows.map((r) => ({ ...r }));

  async function query(sql, params) {
    const normalized = sql.replace(/\s+/g, ' ').trim();

    if (normalized.startsWith('SELECT role FROM family_access')) {
      const [careRecipientId, userId] = params;
      const match = rows.find(
        (r) => r.care_recipient_id === careRecipientId && r.user_id === userId
      );
      return { rows: match ? [{ role: match.role }] : [] };
    }

    if (normalized.startsWith('UPDATE family_access')) {
      const [newRole, careRecipientId, targetUserId] = params;
      const match = rows.find(
        (r) => r.care_recipient_id === careRecipientId && r.user_id === targetUserId
      );
      if (match) {
        match.role = newRole;
      }
      return { rows: [] };
    }

    throw new Error(`Unhandled query in test db mock: ${normalized}`);
  }

  return { query, _rows: rows };
}

module.exports = { createDb };
