I was told to read only the prompt file, so I have not seen the existing ADRs. This is the update I would make. I have not applied it.

**1. Keep ADR-0003 and change only its status.** Do not delete or rewrite it. It is the history of why we self-hosted.

```
# ADR-0003: Self-hosted Postgres
Status: Superseded by ADR-00NN (managed Postgres)
```

**2. Add a new ADR with the next free number (ADR-00NN, called "N" below).**

```
# ADR-00NN: Use managed Postgres
Status: Accepted
Date: 2026-10-31
Supersedes: ADR-0003

## Context
Why self-hosting no longer fits. For example, we do not want to run
backups, patching and failover ourselves. We hold health data, so
encryption and recovery matter. [Fill in the real reasons.]

## Decision
Use a managed Postgres service [provider/plan] for all environments.

## Consequences
+ The provider handles backups, patching and failover.
- Vendor lock-in and a monthly cost.
- We need a data processing agreement or BAA, a region choice,
  and a migration plan from the current database.
- Connection strings and credentials move to the provider's secret store.

## Alternatives considered
Staying self-hosted (ADR-0003); a different managed provider.
```

**3. Update the other records.**
- Add the new ADR to the index or README in docs/adr/, and mark ADR-0003 as superseded there.
- Search the docs for references to ADR-0003 or "self-hosted Postgres" (architecture doc, README, deploy notes). Point them to ADR-00NN.
- Add a "Superseded by" link at the top of ADR-0003.

**4. Open questions for you**
- What is the provider?
- What is the real reason for the change?
- What is the migration timing?

Send me those and I will fill in the ADRs.
