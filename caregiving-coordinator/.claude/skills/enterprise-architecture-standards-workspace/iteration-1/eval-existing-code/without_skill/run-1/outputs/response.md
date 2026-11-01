# Architecture (as described, not yet verified against code)

I have not inspected the code. This documents only what you stated; items marked "to confirm" need a check.

## Overview
Two tiers: a React single-page app in the browser, and Supabase (hosted Postgres, Auth, optional Storage and Realtime). Components call Supabase directly through the client SDK. There is no custom backend.

```
Browser (React components) --supabase-js--> Supabase (Auth, Postgres + RLS, Storage)
```

## Layers
- UI and data access are mixed: components query and mutate data themselves.
- No service, repository, or API layer (to confirm).
- Business rules live in components, or in the database through constraints, RLS policies, and functions (to confirm).

## Data ownership
- Supabase Postgres is the system of record.
- Authorization depends entirely on Row Level Security, because the browser is untrusted. Any table without RLS is readable and writable by anyone holding the public anon key (to confirm per table).

## Dependency direction
Components depend on supabase-js and on the database schema. A schema change can break many components, since queries are scattered.

## Error handling
Per-component and probably inconsistent (to confirm).

## Risks
1. RLS gaps expose data. This matters because the app handles health and caregiving data.
2. Logic is duplicated across components, which makes it hard to test.
3. Secrets: only the anon key may be in the client. The service-role key must never be there (to confirm).
4. Multi-step operations are not atomic unless done in database functions.

## Recommended next steps
- Audit RLS on every table.
- Move queries into one data-access module (hooks or functions) so components stop calling Supabase directly.
- Put sensitive or multi-step logic in Postgres functions or Edge Functions.
- Record this as an ADR and save it as docs/architecture.md after you confirm it.
