Skill applied: enterprise-architecture-standards. Judged not relevant yet: judge-arch (nothing built), architectural-decision-records (no decision made yet). I did not read docs/PRD.md or docs/risk-profile.md in this run, so nothing below is saved. The user owns these choices.

**What is known:** appointments, medications, family accounts with different permissions. Medications and appointments are health data, and permissions are a known need now, so access control and an audit trail belong in the design from day one.

**Proposed layers (plain language)**
1. Screens: show data, collect input. Never decide who may see what.
2. Application logic: the rules (can this family member edit a medication?). Every permission check lives here.
3. Data access: the only code that talks to the database.
4. Storage: the database.

Dependency direction: screens call logic, logic calls data access. Never the reverse.

**Data ownership (one writer, one read path each):** accounts and roles, appointments, medications, audit log.

**Three structure options**
- A. Single app, layered folders (recommended): simplest, cheap to host, enough for a family-scale product. Layers are enforced by folder rules and a gate script.
- B. Separate frontend and API service: cleaner boundary, but two deployments for no named need.
- C. Backend-as-a-service with rules in the database: fast start, but permission logic is harder to review and test.

**Would force a redesign later:** a second kind of user (paid agency caregivers), a regulated customer, or a second deployment.

**Open question (one at a time):** who are the users and roles? For example, is there one "owner" per care recipient with family members as view-only or edit, or are roles more granular?

Once you answer, I will ask about hosting and budget, draft docs/architecture.md with each rule tagged gate or review, and ask your approval before saving.
