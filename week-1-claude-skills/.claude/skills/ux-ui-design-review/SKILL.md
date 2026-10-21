---
name: ux-ui-design-review
description: Reviews screens, user flows, or UI code for usability using Nielsen's 10 usability heuristics and guidance for complex enterprise applications, and reports findings with severity and fixes. Use when the user asks to review UX or UI, usability, a dashboard, a form, a data table, onboarding, navigation, or a workflow. Make sure to use this skill when the user asks if a screen is confusing or easy to use, even if they never say "UX". Do not use for accessibility compliance checks, security review, creating a new design from scratch, or visual branding choices.
---

# UX and UI Design Review

Find places where real people would get confused, slowed down, or make
mistakes. Enterprise products are used for hours by people with complex jobs,
so clear workflows, fast paths for experts, and error prevention matter most.

## Ground rules

- **Anchor every finding to a heuristic.** A heuristic is a rule of thumb for
  good usability. Name it, point to the exact screen or code, and say what a
  user would experience.
- **Say who is affected.** Name the user type and the task. If you do not know
  the users, ask one question first.
- **Separate facts from taste.** If a finding is a matter of preference, label
  it "suggestion", not "problem".
- **Reviewing code is not user testing.** Say that real testing with real users
  would confirm or change the findings.
- **Review first, change later.** Do not edit files unless asked.
- **Plain language.** Explain each term the first time.

## Before you start

1. Find out what to review (a screen, a flow, a folder). If unclear, ask one
   question: "Which screen or task should I look at?"
2. Ask who uses it and what they are trying to do, unless a PRD such as
   `docs/PRD.md` already says.
3. Read `references/heuristics-and-enterprise-checks.md`.

## Workflow

1. **Walk the main task** step by step as the user would, and note every
   moment of doubt: What do I do next? Did that work? Can I go back?
2. **Check the 10 heuristics** against that walk.
3. **Check the enterprise points:** complex workflows, expert shortcuts,
   data tables, role-based views, in-context help.
4. **Check consistency:** same words, same buttons, same places everywhere.
   Note whether a design system (a shared set of components and rules) exists.
5. **Check errors and empty states:** what happens when something fails, has
   no data, or is loading.
6. **Write the report** with `assets/ux-review-template.md`.

## Severity

- **Blocker:** users cannot finish the task or may lose data.
- **Major:** users finish the task slowly or with mistakes.
- **Minor:** small friction or inconsistency.
- **Suggestion:** an idea based on preference or best practice.

## Quality check before finishing

- Every finding names a heuristic or enterprise check, a location, who is
  affected, a severity, and a fix.
- Findings describe user experience, not just code style.
- The report says what was not covered, such as real user testing.
- It starts with what already works well, in one or two lines.
- It suggests one next step, such as testing the main task with three users.

## If something goes wrong

- **Only code, no screenshots.** Review from the markup and say the visual
  look was not seen.
- **User and task unknown.** Ask once. If there is no answer, state the
  assumption in the report.
- **A request to redesign.** Say this skill reviews, and offer to turn the
  findings into a list of changes.

## Files in this skill

- `references/heuristics-and-enterprise-checks.md`: the checks and questions.
- `assets/ux-review-template.md`: the format of the report.

## Sources

Jakob Nielsen, 10 Usability Heuristics for User Interface Design, Nielsen
Norman Group: https://www.nngroup.com/articles/ten-usability-heuristics/
The enterprise checks come from these NN/g articles:
- 8 Design Guidelines for Complex Applications (Kaplan, 2020):
  https://www.nngroup.com/articles/complex-application-design/
- 10 Usability Heuristics Applied to Complex Applications (Kaplan, 2021):
  https://www.nngroup.com/articles/usability-heuristics-complex-applications/
- Data Tables: Four Major User Tasks (Laubheimer, 2022):
  https://www.nngroup.com/articles/data-tables/
