---
name: data-lifecycle-compliance
description: Reviews how a product collects, uses, shares, keeps, and deletes personal and sensitive data, producing a data inventory and flagging gaps (collect only what is needed, tell users, keep it only as long as needed, let users delete or export, control who sees it). Use when a feature stores personal or health information, sends data to a third party or an AI service, or adds user accounts, and before launch. Also use for casual asks like "what user data do we store", "how long do we keep it", "what happens to someone's data when they delete their account or leave", "can I send user text to an AI API", "are we GDPR compliant", even if the user never says "privacy". Do not use for code vulnerability review (use security-review), legal advice or declaring a product compliant, or deciding the architecture.
---

# Data Lifecycle and Compliance

Follow each kind of personal data from the moment it is collected to the moment
it is deleted. This skill produces an inventory and finds gaps. It does not give
legal advice and it never says a product is "compliant".

## Ground rules

- **Never say "compliant".** Say "no gaps found in what was checked" and list
  what was not checked. Which laws apply depends on the product, the users, and
  where they live. Recommend a qualified person confirm this before launch.
- **Findings first.** Report gaps. Do not change code or settings unless asked.
- **Product-specific data comes from `docs/risk-profile.md`.** Read it. If it
  does not exist, ask what data the product holds and offer to draft it.
- **Never print sensitive values.** Name the field, not the contents.
- **Use `skeptical-audit` tags.** A deletion feature that was never run is
  `not-assessed`.
- **Plain language.** Explain terms the first time.

## Before you start

1. Ask one question if unclear: "What personal or sensitive data does this
   feature touch?"
2. Read `docs/risk-profile.md`, `docs/architecture.md`, and any privacy text
   shown to users.
3. Read `references/lifecycle-questions.md`.

## Workflow

1. **Build the data inventory.** One row per kind of data: what it is, why it is
   collected, where it is stored, who can see it, who it is sent to, how long it
   is kept, and how it is deleted. Use `assets/data-inventory-template.md`.
2. **Walk each stage** with the questions in the reference: collect, use, share,
   keep, delete. Mark each answer `proven`, `observed`, `documented`, `reported`,
   or `not-assessed`.
3. **Check third parties.** For every service that receives personal data
   (including AI services), name what it receives, whether users are told, and
   whether it keeps or trains on the data. If this is not documented, say so.
4. **Check user control:** can a user see, correct, export, and delete their
   data, and does deletion also reach backups, logs, and third parties?
5. **Check access:** who inside the product and the team can read each kind of
   data, and is access logged?
6. **Rank each gap:** Blocker (sensitive data kept or shared with no basis or
   no protection), Should fix before launch, or Later.
7. **List open legal questions** for a qualified person, without answering
   them.

## Quality check before finishing

- Every kind of data has a row with all columns filled or marked unknown.
- Every third party that receives personal data is listed.
- Deletion and export have an answer with evidence or `not-assessed`.
- The report never uses the word "compliant" as a conclusion.
- Open legal questions are listed for a human.

## If something goes wrong

- **Nobody knows what the third party does with the data.** Mark it a gap and
  ask for the vendor's data terms. Do not assume.
- **Data is mixed with other data.** Treat the whole store as sensitive until it
  is separated.
- **The product is not built.** Review the plan. Everything is `not-assessed`
  for evidence. Say so.

## Files in this skill

- `references/lifecycle-questions.md`: the questions for each stage.
- `assets/data-inventory-template.md`: the inventory table.

## Sources

GDPR, Article 5, principles relating to processing of personal data,
https://gdpr-info.eu/art-5-gdpr/
NIST Privacy Framework, https://www.nist.gov/privacy-framework
U.S. Federal Trade Commission, Health Breach Notification Rule, for health
apps outside HIPAA (search ftc.gov; the direct link I tried returned 404).
Pointers only: these were not re-read in the session that wrote this skill.
Check them before relying on any detail.
