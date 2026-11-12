# Risk profile: caregiving coordinator

These are this product's own risks. The general-purpose skills read this file: `security-review`, `owasp-secure-coding-bdd`, `data-lifecycle-compliance`, `operational-readiness` and `enterprise-architecture-standards`. The skills stay reusable across products, and this file holds what is specific to this one.

**Status: Approved by the owner on 2026-11-12.** The earlier draft (2026-10-31) was never approved. It was rebuilt from the approved deliverables and from the laws research:
- the findings: `docs/sources/laws-consent-research-2026-11-12/verified-findings-2026-11-12.md`
- the sources: files 01 to 73, logged in `docs/sources/INDEX.md`

None of this is legal advice. Nothing here says the product is "compliant."

## Product facts these risks rest on
- A US web app that family caregivers sign up for themselves. It is direct to consumer, not through a doctor, hospital, health plan or employer. Source: `docs/clean-deliverables/vision-and-scope-boards-2026-11-10.md`.
- Audience 1 is an adult child caring for a parent. Audience 2 is a spouse or partner. Either one types in details about **another adult** who often never signs up.
- The stack is Vercel, a Supabase (Postgres) database, and user accounts with secured data. Source: coding challenge, requirement 6.

## Data this product holds in MVP #1

| Data | Why it is sensitive | Source |
|---|---|---|
| Health and behavior notes caregivers type in about a parent or partner | This is consumer health data under the Washington, Nevada and Connecticut laws. It is about someone who didn't sign up. | Epic 3 and 4 tasks; findings, section 2, row 1 |
| Money, benefits and coverage details | Financial and insurance details about a parent or partner | Epic 5 and 6 tasks |
| Family member accounts and permissions | They control who sees health and money data | Epic 2; coding challenge, requirement 6 |
| Who can see what about the parent or partner (consent records) | Proof of consent, required separately for collecting and for sharing | Board barrier, line 59; findings, rows 1 and 1b |

### Out of MVP #1, and why
| Data | Why it's out |
|---|---|
| Doctor-visit recordings and transcripts | No one asked for it (market master report, row 8). An outside AI service would also hold the health data. That second reason is general knowledge, not from our research. |
| AI-generated visit notes | Same as recordings |
| Stored logins for insurance and pharmacy portals | Out of scope (vision and scope, line 95). It would work like a password manager. |
| Medication lists and refills | Medications aren't one of the 5 needs (competitive master report, line 122) |

If any of these come back in a later release, add them here first and re-check the risks below.

## Risks to check on every relevant change

- **Consent comes from the person the data is about.** The Washington, Nevada and Connecticut laws give the consent right to the person the health data is about, not the caregiver who types it (RCW 19.373.030; NRS 603A.500; CT PA 25-113 §9).
  - Washington and Nevada have no clause letting anyone else consent for them. Connecticut allows only a guardian or conservator.
  - Any feature that collects or shares a parent's or partner's health data must show how that consent is handled. Until a lawyer answers open question 1, treat this as unresolved.
- **Two separate consents.** Consent to collect is one step. Consent to share, for example with invited relatives, is a separate step (RCW 19.373.030; NRS 603A.500(2)(a)).
- **No ad or analytics trackers on pages with health data.** Every Washington lawsuit found (2025 to 2026) and every FTC health-app case (GoodRx, Premom, BetterHelp, Flo) is about sending health data to ad or analytics companies without permission. Connecticut's AG found one telehealth company's consent step "insufficient."
- **Under the FTC rule, unauthorized sharing counts as a breach.** It needs notice within 60 days (16 CFR 318).
  - The rule covers "personal health record" apps. Typed-in data alone doesn't make an app one.
  - Any feature that pulls data in (an API, a calendar connection, a device) can make it one, even if no one uses the feature (89 FR 47035 to 47038).
  - **Adding any data-pulling feature is a High finding** until this question is re-checked.
- **Row-level security on every table with health, money or consent data.** Supabase says customers are responsible for table access and recommends always turning on row-level security (Supabase shared responsibility page).
- **Multi-user access control.**
  - One family member must not be able to see or change another's permissions silently.
  - Removing one person's access takes effect at once and doesn't affect anyone else.
- **Data region.** The Supabase project is created in a US region. Supabase says the data stays in the chosen region, and the region can't be changed later without a new project. Vercel functions run in Washington, D.C. (iad1) by default.
- **Backups.** The Supabase Free plan has no automatic backups. Pro keeps 7 days. Check the plan before real user data is stored.
- **Deletion.** The person the data is about has deletion rights under the Washington and Nevada laws. A caregiver's account deletion must also handle the data they entered about that person.

## Open questions (need a lawyer before launch)
1. **How can a caregiver lawfully enter and share a parent's or partner's health data, when Washington and Nevada let no one else consent?** A health care power of attorney gives rights to medical records and health care decisions. No power of attorney law mentions apps or privacy consent. Nevada's "consumer" is someone "who has requested a product or service," which a parent who never signs up may not be.
2. **Does California's medical privacy law (CMIA, Civil Code 56.06) apply?** An app "designed to maintain medical information" can be "deemed to be a provider of health care." Whether caregiver-typed notes count as "medical information" is unclear.
3. **HIPAA:** probably not covered. HHS says an app that serves consumers directly is "not likely" covered, but it depends on the facts. It changes if we ever work for a doctor, hospital or health plan.

## Recheck triggers
- A data-pulling feature is added (FTC rule).
- Revenue nears $26.6 million, or data on 100,000 people (California CCPA).
- Any partnership with a doctor, hospital, health plan or employer (HIPAA).
- Every 6 months: the state laws are new, and rules and cases are changing.
