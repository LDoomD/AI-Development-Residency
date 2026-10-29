// db.mock.js
// Minimal in-memory stand-in for the real ../db module, just enough to
// support the two queries used by update-family-role.js (and its fixed
// version). Not a general-purpose SQL mock.

function createMockDb(seedRows) {
  const rows = seedRows.map((r) => ({ ...r }));

  return {
    rows, // exposed so tests can assert on final state directly

    async query(sql, params) {
      const normalized = sql.replace(/\s+/g, ' ').trim();

      if (normalized.startsWith('SELECT role FROM family_access')) {
        const [careRecipientId, userId] = params;
        const found = rows.filter(
          (r) => r.care_recipient_id === careRecipientId && r.user_id === userId
        );
        return { rows: found };
      }

      if (normalized.startsWith('UPDATE family_access SET role')) {
        const [role, careRecipientId, userId] = params;
        rows.forEach((r) => {
          if (r.care_recipient_id === careRecipientId && r.user_id === userId) {
            r.role = role;
          }
        });
        return { rows: [] };
      }

      throw new Error('Unexpected query in mock db: ' + sql);
    },
  };
}

module.exports = { createMockDb };
