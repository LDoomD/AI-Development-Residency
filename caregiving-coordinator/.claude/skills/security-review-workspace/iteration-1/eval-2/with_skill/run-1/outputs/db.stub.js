// db.stub.js
// Minimal stand-in for ../db used by visit-notes.js in this isolated test
// harness. Real code queries Postgres; the security property under test
// (output escaping) has nothing to do with the query layer, so we swap in
// a fake that returns whatever rows the test configures.

let rowsToReturn = [];

module.exports = {
  // Matches the shape routes/visit-notes.js expects: db.query(sql, params)
  // resolving to an array of rows.
  query: async (_sql, _params) => rowsToReturn,

  // Test helper, not part of the real db module's API.
  __setRows(rows) {
    rowsToReturn = rows;
  },
};
