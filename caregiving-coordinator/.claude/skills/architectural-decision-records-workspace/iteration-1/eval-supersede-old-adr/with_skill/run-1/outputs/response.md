Applying architectural-decision-records. Rule: an accepted ADR's decision is never edited. It gets superseded by a new record, linked both ways.

I did not inspect `docs/adr/` (this task limited me to two files), so the next number is assumed. Step 1 in practice is to list the folder, confirm ADR-0003 exists and is Accepted, and use the next free number.

## Plan

1. **Create a new record** (assuming 0009 is next free): `docs/adr/0009-use-managed-postgres.md`
2. **Edit ADR-0003 only in its status line**: `Status: Superseded by ADR-0009`. Its decision text stays unchanged.
3. **Link back from the new record**: `Supersedes ADR-0003`.
4. **Check the gate**: if ADR-0003 named a rule in `arch-gate.config.json` (e.g. self-hosting config), update or remove it and name the new rule in ADR-0009.

## Draft ADR-0009 (Status: Proposed)

**Context:** ADR-0003 chose self-hosted Postgres. We now want a managed Postgres service (the host runs backups, patching, and failover).

**Decision:** Use managed Postgres for all application data.

**Options considered:**
- Keep self-hosted Postgres: rejected, we carry patching, backups, and recovery ourselves.
- A different managed database type (e.g. document store): rejected, the data is relational and the code already assumes SQL.

**Consequences:**
- Good: less operational work, built-in backups.
- Downside: monthly cost, vendor lock-in risk, and the health data now sits with a third party, so encryption, access control, and the provider's data-handling terms need checking.
- Migration of existing data is needed.

## Questions for you
- Which provider, and what is the real reason for the change? I need it for the "why".
- Do you accept the draft? ADR-0009 stays `Proposed` until you say yes, and I will not mark ADR-0003 superseded as final until then.
