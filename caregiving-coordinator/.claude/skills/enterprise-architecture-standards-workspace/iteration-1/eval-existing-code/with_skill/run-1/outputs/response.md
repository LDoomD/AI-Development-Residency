I can document this, but I will not save `docs/architecture.md` yet. The skill says to describe what exists, mark each part "intended" or "accidental", and let you decide. I have not read your code; the as-is comes from your sentence only.

## What is there (as-is)

- **Screens (React components)**: render the UI and also call Supabase directly.
- **Data access**: none. It is mixed into the components.
- **Storage (Supabase)**: reached straight from the browser.
- **Dependency direction**: screens -> storage, with no logic layer between.

## Intended or accidental? (you decide)

| Part | Tag | Why it matters |
|---|---|---|
| Components call Supabase directly | probably accidental | No single owner for each kind of data. Rules cannot be enforced in one place. |
| Browser talks to Supabase | possibly intended | This is safe only if Row Level Security (database rules that decide who can read which rows) is on for every table. Care data is health data with shared access. |
| No error-handling or logging rule | accidental | Nothing says what is logged or what the user sees. |

## Open questions (one at a time)

1. Is Row Level Security enabled, and does it carry all access control today?
2. Do you want to keep "front end calls Supabase directly", or add a thin data-access layer?

## Options

- **A. Keep direct calls, add RLS rules.** Cheapest, weak boundaries.
- **B. Add a data-access module** (e.g. `src/data/`) that is the only place importing Supabase. Components call it. **Recommended.** It is checkable in `arch-gate.config.json` (rule: no Supabase imports in `components/`).
- **C. Add a backend API.** Most control, most cost. Not justified today.

## Next

After you answer, I will fill the template, tag each rule `gate` or `review`, and ask for approval before saving.
