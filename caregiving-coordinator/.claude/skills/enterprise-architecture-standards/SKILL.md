---
name: enterprise-architecture-standards
description: Helps choose and write down a product's architecture, covering layers, who owns which data, dependency direction, error handling, and how the design will cope with growth, and saves it as docs/architecture.md for later reviews to judge against. Use when starting a product or a major feature, when the structure is unclear, when someone asks "how should this be organized", or before judge-arch has nothing to judge against. Make sure to use this skill before building anything with more than one layer or more than one kind of stored data. Do not use for reviewing a finished change (use judge-arch), for recording one decision (use architectural-decision-records), or for visual or interaction design.
---

# Enterprise Architecture Standards

Decide the shape of the product before the code decides it for you. The output
is a short `docs/architecture.md` that reviews can check changes against.

## Ground rules

- **Ask, do not assume.** The user owns the architecture. Offer two or three
  options with trade-offs and a recommendation. Do not fill the file with
  guesses.
- **Design for what is known.** Add structure for needs you can name today,
  including known later needs such as audit logs, access control, and data
  deletion. Do not add layers for imagined scale.
- **Product-specific risks come from `docs/risk-profile.md`.** If it does not
  exist, ask the user to describe what data the product holds and who can
  see it, then offer to draft it.
- **Every rule must be checkable or marked as judgment.** A rule that can be
  searched for goes into `arch-gate.config.json`. One that cannot is labeled
  "reviewed by judge-arch".
- **Plain language.** Explain terms the first time.

## Before you start

1. Read the PRD (`docs/PRD.md`) if it exists, and `docs/risk-profile.md`.
2. Read `docs/architecture.md` and `docs/adr/` if they exist. Extend, do not
   overwrite.
3. Ask one question at a time about anything the answer depends on: who the
   users are, what data is stored, what must never be shown to whom, and what
   hosting and budget limits apply.

## Workflow

1. **Name the layers.** For example: screens, application logic, data access,
   storage. State what each layer may and may not do.
2. **State dependency direction.** Which layers may call which. Usually screens
   call logic, logic calls data access, and never the reverse.
3. **Assign data ownership.** For each kind of data, name the one module that
   writes it and the one path that reads it.
4. **Set error handling.** Where errors are caught, what is logged, what the
   user sees, and what is never logged (credentials, sensitive personal data).
5. **Set the cross-cutting rules.** Authentication, authorization, audit
   trail, configuration and secrets, and data retention. Link
   `docs/risk-profile.md` items to the layer that handles them.
6. **List what would force a redesign** (a second user type, a second
   deployment, a regulated customer) so the cost of deferring is visible.
7. **Write `docs/architecture.md`** from `assets/architecture-template.md`.
   Create one decision record per big choice with `architectural-decision-records`.
8. **Turn the searchable rules into gate rules** in `arch-gate.config.json`,
   and show the user what each rule blocks.

## Quality check before finishing

- Every layer has a stated job and a stated forbidden job.
- Every kind of stored data has one owner.
- Every rule is tagged `gate` (script-enforced) or `review` (judgment).
- Cross-cutting risks from the risk profile are each assigned to a layer.
- The user approved the file before it was saved.

## If something goes wrong

- **The user does not know yet.** Save only the parts decided and list open
  questions at the top. `judge-arch` will then stop and ask, which is correct.
- **The code already exists.** Describe what is there, mark each part as
  "intended" or "accidental", and ask the user which to keep.
- **Rules conflict.** Do not pick one. Ask.

## Files in this skill

- `assets/architecture-template.md`: the layout of `docs/architecture.md`.

## Sources

Robert C. Martin, "The Clean Architecture" (2012),
https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html
Michael Nygard, "Documenting Architecture Decisions" (2011).
