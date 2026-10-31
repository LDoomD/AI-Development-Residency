---
name: architectural-decision-records
description: Writes and maintains short architecture decision records (ADRs) in docs/adr/, one per significant decision, saying what was decided, why, and what the trade-offs are. Use when a change picks a technology, sets a structural rule, or changes how data is stored or secured. Also use for casual asks like "why did we pick X", "where do we write decisions down", "I want a record of why we chose Y", "how do I note that we changed our mind", or "someone asked why we chose this stack", even if nobody says "ADR". Make sure to use this skill whenever a decision other people or later work must follow is made. Do not use for reviewing code (use judge-arch or engineering-quality-check), for designing the architecture itself (use enterprise-architecture-standards), or for trivial choices nobody will look up.
---

# Architectural Decision Records

A decision record is a short note: what was decided, why, and what it costs.
Without it, the reason for a choice is lost, and the next person either repeats
the debate or breaks the rule without knowing.

## Ground rules

- **One decision per record.** If a record needs "and", split it.
- **Record the why and the cost.** A record with no downside listed is
  probably incomplete.
- **Never edit an accepted record's decision.** Write a new record that
  supersedes it, and mark the old one `Superseded by ADR-NNNN`.
- **Only the user decides.** Draft the record and show it. Do not mark it
  `Accepted` until the user agrees.
- **Trivial changes need none.** A rename or a bug fix does not need a record.
  A choice someone will later ask "why" about does.
- **Plain language.** Explain terms the first time.

## When a record is needed

Write one when a change does any of these:

- Picks or replaces a language, framework, database, host, or third-party
  service.
- Sets a rule other code must follow (layer boundaries, naming, how errors are
  reported).
- Decides how sensitive data is stored, shared, kept, or deleted.
- Accepts a known risk or a known shortcut on purpose.

## Workflow

1. Check `docs/adr/` for an existing record on this topic. Update status or
   supersede instead of duplicating. If the folder does not exist, create it
   with `0001-record-architecture-decisions.md`.
2. Number the new record: the next free four-digit number, then a short
   kebab-case title, for example `0007-store-visit-notes-encrypted.md`.
3. Fill the template in `assets/adr-template.md`. Keep it to one page.
4. List at least two options considered and why each was rejected.
5. If the decision can be enforced by search, add a rule to
   `arch-gate.config.json` and name the rule in the record.
6. Show the draft to the user. Set the status after they decide.

## Quality check before finishing

- The record has context, decision, options considered, and consequences,
  including at least one downside.
- The status is `Proposed` until the user accepts it.
- Superseded records are linked both ways.
- A greppable rule was added to the gate, or the record says why it cannot be.

## If something goes wrong

- **The decision is already made and shipped.** Write the record now and note
  the date it was actually decided if known.
- **The user is unsure.** Record it as `Proposed` with the open questions.
- **Two records conflict.** Do not pick one. Ask the user which stands and
  supersede the other.

## Files in this skill

- `assets/adr-template.md`: the template.

## Sources

Michael Nygard, "Documenting Architecture Decisions" (2011).
Martin Fowler, Architecture Decision Record,
https://martinfowler.com/bliki/ArchitectureDecisionRecord.html
