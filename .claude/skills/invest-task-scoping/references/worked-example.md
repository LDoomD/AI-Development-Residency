# Worked example

An illustrative example (not from the course). It shows the output shape from `SKILL.md` and passes `scripts/check_invest.py`.

Mode: backlog

## What is being scoped

"Build the caregiver dashboard so a parent's medication reminders show up for the whole family."

## Grade: the original task

| Letter | Result | Reason |
|---|---|---|
| Independent | Fail | Needs a family group, a medication record and reminders, and none exist yet |
| Negotiable | Fail | "Dashboard" is a screen. The outcome is that the family knows whether the parent took the pills |
| Valuable | Pass | Families stop calling each other to ask "did she take it?" |
| Estimable | Fail | Unknowns: who counts as family, and where reminders come from |
| Small | Fail | Several features, well over 2 weeks |
| Testable | Fail | "Whole family" has no clear check |

## Split into 4 pieces (build in this order)

1. Family circle: invite a sibling or spouse (~1 wk)
2. Add a medication reminder (~1 wk). Needs 1.
3. Family sees today's reminders (~1 wk). Needs 1 and 2.
4. Tell the family when a dose is missed (~1 wk, once "missed" is defined)

The "Independent" fails on pieces 2 to 4 are build-order dependencies, not defects.

## Story 1: Family circle

**User story:** As an adult child caring for a parent, I want to invite my siblings or my parent's spouse into one shared circle, so that everyone sees the same information without separate calls and texts.

| Letter | Result |
|---|---|
| Independent | Pass |
| Negotiable | Pass |
| Valuable | Pass |
| Estimable | Pass |
| Small | Pass: ~1 wk |
| Testable | Pass |

**Background:** Every later piece shows the parent's reminders to "the family". Without a circle there is nobody to show them to.

**Problem statement:** "I'm the only one who knows the schedule, and I answer the same questions every day."

**Definition of result:** I can invite people to my parent's circle. They join, and I can see who is in it.

**Scope / Definition of done:** In: invite, accept, list members, remove a member. Out: medications, reminders, and permission levels beyond owner and member. Done when two people can join one circle and both see the member list.

**Acceptance criteria:**
- An invited person can join with one action.
- The owner sees everyone who joined.
- The owner can remove a member.

**BDD scenarios:**
- *Given* I have created a circle for my parent, *When* I invite my sister and she accepts, *Then* we both see two members.
- *Given* I invited someone, *When* they don't accept, *Then* they show as "invited" and can't see anything.

**Technical acceptance:** Member names are personal data. Only members of the circle can see the list.

## Receipt

- **Audited:** the original task and Story 1, each on all 6 letters.
- **Split:** the task into 4 pieces.
- **Written:** Story 1, with acceptance criteria and 2 Given/When/Then scenarios.
- **Not checked:** whether the 1-week sizes match your real speed; stories 2 to 4 are named but not written.

Story 1 as written? If yes, I'll show Story 2.

---

# A story that gets rewritten

**Before (names a solution):** As a user, I want a dropdown menu in the sidebar with a red "Remind" button, so that I can click it.

- Fails **Negotiable**: dropdown, sidebar and button are solutions.
- Fails **Valuable**: "so that I can click it" is not a benefit.
- Fails **Testable**: nobody can check a benefit that isn't stated.

**After (names the outcome):** As an adult child caring for a parent, I want to set a reminder for my parent's evening pill, so that the dose isn't missed on days I can't call.
