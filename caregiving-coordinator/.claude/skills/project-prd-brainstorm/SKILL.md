---
name: project-prd-brainstorm
description: Interviews the user one question at a time to turn a rough project idea into a clear one-page product requirements document (PRD). Use when the user wants to brainstorm a new project, start a project from scratch, write a PRD, define requirements, or says things like "help me plan my app", "I have an idea", or "what should I build". Do not use for writing code, designing screens, or reviewing a PRD that already exists.
---

# Project PRD Brainstorm

Help the user go from a rough idea to a one-page PRD (product requirements
document). A PRD says what is being built, for whom, and why. It gives every
later session the context it needs, so nothing has to be guessed.

You are a thinking partner, not a form to fill in. People often have not
finished working out what they want. Good questions help them get there.

## Ground rules

- **Ask one question at a time.** Wait for the answer before asking the next.
  End each message with a single question and no list of example answers.
- **Use plain language.** If a technical term is needed, explain it in one
  short sentence.
- **Follow their energy.** Dig into whatever they sound excited or annoyed
  about before moving on.
- **Challenge vague words.** When you hear "good", "simple", "fast" or
  "users", ask what that means in a real situation.
- **A guess they can correct beats a question.** Say "I'm guessing this
  comes from X bugging you. Is that right?" Always mark guesses as guesses.
- **Never invent facts.** If the user has not said it, write it down as an
  open question.
- **Do not write code or pick technology yet.** This skill only defines the
  project. Building comes later.

## Before you start

1. Check whether a PRD already exists (look for `docs/PRD.md`). If one does,
   ask whether to update it or start a new one.
2. If the user shared background material (a profile, notes, past projects),
   read it first and skip questions it already answers.

## Workflow

### Phase 1: Explore the idea

Goal: turn a fuzzy idea into one clear sentence.

1. Your first message has two parts only. First, one line saying they can
   skip the questions and just tell you to start whenever they want. Second,
   one open question about a real moment, such as "What is the moment you
   find yourself wishing this existed?"
2. If they skip the questions, stop this skill, say in one line what you
   will assume, and continue with their request.
3. Use the Explore questions in `references/question-bank.md`. Ask them to
   walk you through using the idea, so it becomes concrete.
4. If they have no idea yet, offer two or three directions based on their
   skills and interests. Let them pick or mix.
5. End the phase by writing the idea as one sentence and confirming it.

### Phase 2: Define the project

Goal: fill in the sections of the PRD template.

Work through these topics in order, one question at a time, using the
matching questions in `references/question-bank.md`.

1. **Problem:** what pain or need does this solve?
2. **Users:** who has the problem? Make the description specific.
3. **Core value:** the one thing that must work. If everything else fails,
   this is what matters.
4. **Goals:** what does success look like? Push for something measurable.
   Also ask what would make it a failure even if it technically works.
5. **Features:** sort ideas into must have, nice to have, and later.
6. **Out of scope:** what this project will not do, and why.
7. **Constraints:** time, budget, skills, tools, deadlines. Ask which
   choices the user wants to make (such as tools) and which they want you
   to suggest. Record any choice you make as your suggestion.

After each topic, play it back in two or three lines and ask what is wrong
or missing. If an answer is vague, offer two or three concrete examples to
react to instead of repeating the question.

### Phase 3: Write the PRD

1. Fill in `assets/prd-template.md` using only what the user told you.
2. Keep it to one page. Cut anything that does not help someone decide what
   to build.
3. Put every unknown under "Open questions". Do not guess.
4. Show the draft and ask what is missing or wrong. Revise once or twice.
5. **Approval gate:** do not save the final version or start building until
   the user says the PRD is right.
6. Save the final version to `docs/PRD.md` in the project folder.
7. Close by suggesting one next step. Examples: answer the open questions,
   choose a technology, or sketch the main screens.

## Quality check before finishing

Confirm every item before saving:

- The problem is stated in one sentence.
- The users are named specifically, not just "everyone".
- The core value is one sentence.
- There is at least one measurable success goal.
- Features are split into must have, nice to have, and later.
- Out of scope is not empty, and each item has a reason.
- Nothing in the PRD was invented by Claude.
- **Cold read:** read it as a stranger who has never met the user. Could
  they start planning the first version without asking anything? If not, add
  the missing pieces to "Open questions".

## If something goes wrong

- **The user wants to jump straight to building.** Say a short PRD first
  saves time, offer to keep it to ten minutes, and continue.
- **The user is stuck on a question.** Offer two or three options, or skip
  it and add it to "Open questions".
- **The user changes the idea midway.** Go back to Phase 1, confirm the new
  one-sentence idea, and keep any answers that still apply.
- **You are tempted to fill in a gap yourself.** Do not. Say it out loud as
  a suggestion and let the user accept or reject it.

## Files in this skill

- `references/question-bank.md`: the questions for each phase.
- `assets/prd-template.md`: the format of the finished PRD.

## Credits

The interview approach borrows ideas, not text, from two MIT-licensed
projects: the brainstorming skill in Superpowers by Jesse Vincent
(github.com/obra/superpowers) and the project-start workflow in Get Shit Done
by Lex Christopherson (github.com/gsd-build/get-shit-done).
