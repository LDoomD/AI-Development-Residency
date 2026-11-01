# Risk profile: caregiving coordinator

Product-specific risks that the general-purpose skills (`security-review`,
`owasp-secure-coding-bdd`, `data-lifecycle-compliance`, `operational-readiness`,
`enterprise-architecture-standards`) read. The skills stay reusable across
products. This file is where this product's specifics live.

Status: draft, moved from the "Extra categories for this project" section of
`security-review` on 2026-10-31. The user has not yet reviewed or approved it,
and the product idea itself is still being researched (see
`docs/market-research-template-run.md`), so the data listed here is what the
earlier design discussions assumed, not a final scope.

## Data this product may hold

| Data | Why it is sensitive |
|---|---|
| Doctor-visit recordings and transcripts | Sensitive personal health information |
| AI-generated visit notes | Derived from health information |
| Medication lists and refill status | Sensitive personal health information |
| Stored logins for insurance and pharmacy portals, so several family members can use them | Works like a password manager. A leak gives access to other people's accounts |
| Family member accounts and permissions | Controls who can see what |

## Risks to check on every relevant change

- **Health data at rest and in transit.** Check encryption at rest, who can
  query it, whether it is sent to a third-party AI service without a clear
  data-handling disclosure, and the retention and deletion policy. Earlier
  discussion assumed the product is not a HIPAA covered entity. That is an
  assumption to confirm with a qualified person, not a conclusion.
- **Shared credential storage.** Needs encryption, no plaintext storage or
  logging, and an audit trail of who accessed what and when. A plan to store
  these credentials in a plain database column is **Critical**.
- **Multi-user access control.** One family member must not be able to see or
  change another's permissions silently. Removing one person's access must not
  require everyone to change a shared password.

## Open questions

- Which laws and rules apply (depends on where users live and how the product
  is offered)? A qualified person should answer this before launch.
- Whether stored portal logins are in scope at all for the first version.
- Which third-party AI service, if any, would receive visit recordings, and
  under what terms.
