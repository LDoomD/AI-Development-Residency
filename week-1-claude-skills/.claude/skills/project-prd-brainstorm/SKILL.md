---
name: project-prd-brainstorm
description: Interviews the user one question at a time to turn a rough project idea into a clear one-page product requirements document (PRD). Use when the user wants to brainstorm a new project, start a project from scratch, write a PRD, define requirements, or says things like "help me plan my app", "I have an idea", or "what should I build". Do not use for writing code, designing screens, or reviewing a PRD that already exists.
---

# Project PRD Brainstorm

Help the user go from a rough idea to a one-page PRD (product requirements
document). A PRD says what is being built, for whom, and why. It gives every
later session the context it needs, so nothing has to be guessed.

## Ground rules

- **Ask one question at a time.** Wait for the answer before asking the next.
- **Use plain language.** If a technical term is needed, explain it in one
  short sentence.
- **Never invent facts.** If the user has not said it, write it down as an
  open question instead of filling it in.
- **Do not write code or pick technology yet.** This skill only defines the
  project. Building comes later.
- **Summarize often.** After about four answers, say back what you have
  heard in two or three lines and ask if it is right.

## Before you start

1. Check whether a PRD already exists (look for `docs/PRD.md` in the
   project folder).
2. If one exists, ask whether to update it or start a new one.
3. If the user has shared background material (a profile, past projects,
   notes), read it first so you can skip questions it already answers.

## Workflow

### Phase 1: Explore the idea

Goal: turn a fuzzy idea into one clear sentence.

1. Ask the user to describe the idea in their own words, however rough.
2. Use the Explore questions in `references/question-bank.md`.
3. If the user has no idea yet, offer two or three directions based on what
   they have said about their skills and interests. Let them pick or mix.
4. End the phase by writing the idea as one sentence and confirming it.

### Phase 2: Define the project

Goal: fill in the sections of the PRD template.

Work through these topics in order, one question at a time. Use the matching
questions in `references/question-bank.md`.

1. **Problem:** what pain or need does this solve?
2. **Users:** who has the problem? Make the description specific.
3. **Goals:** what does success look like? Push for something measurable.
4. **Features:** sort ideas into must have, nice to have, and later.
5. **Out of scope:** what will this project deliberately not do?
6. **Constraints:** time, budget, skills, tools, deadlines.

If an answer is vague, offer two or three concrete examples to react to
instead of repeating the question.

### Phase 3: Write the PRD

1. Fill in `assets/prd-template.md` using only what the user told you.
2. Keep it to one page. Cut anything that does not help someone decide what
   to build.
3. Put every unknown under "Open questions". Do not guess.
4. Show the draft and ask what is missing or wrong. Revise once or twice.
5. Save the final version to `docs/PRD.md` in the project folder.
6. Close by suggesting one next step. Examples: answer the open questions,
   choose a technology, or sketch the main screens.

## Quality check before finishing

Confirm every item before saving:

- The problem is stated in one sentence.
- The users are named specifically, not just "everyone".
- There is at least one measurable success goal.
- Features are split into must have, nice to have, and later.
- Out of scope is not empty.
- Nothing in the PRD was invented by Claude.

## If something goes wrong

- **The user wants to jump straight to building.** Say a short PRD first
  saves time, offer to keep it to ten minutes, and continue.
- **The user is stuck on a question.** Offer two or three options, or skip
  it and add it to "Open questions".
- **The user changes the idea midway.** Go back to Phase 1, confirm the new
  one-sentence idea, and keep any answers that still apply.

## Files in this skill

- `references/question-bank.md`: the questions for each phase.
- `assets/prd-template.md`: the format of the finished PRD.
