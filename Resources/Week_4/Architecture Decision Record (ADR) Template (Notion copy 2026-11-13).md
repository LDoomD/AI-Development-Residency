# Architecture Decision Record (ADR) Template
- Source copy: https://app.notion.com/p/78e9219a46918245a06e01228acef443
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:24.323Z
- Not saved: none

---

> 📍 This template becomes a file in your GitHub repository. Do not keep the only copy in Notion.

# What is an ADR?

- ADR stands for Architecture Decision Record.
- An ADR is a short document that writes down one important choice about how your app is built, and why you made it.
- Each ADR covers only one decision.
- Important choices are the ones that are hard to change later, like which database to use, which framework to use, or where to host your app.

# Where does it go?

1. Make a folder in your repository called `docs/adr`.
2. Save each decision as its own numbered file, like `docs/adr/0001-use-nextjs-with-material-ui.md`. The numbers show the order you made the decisions.
3. Commit and push it along with the code it affects.
4. Add this line to your project's `CLAUDE.md` file: "Read every ADR in docs/adr before making changes, and write a new ADR for every big decision."

# When a decision changes

- Do not erase an old ADR.
- Write a new ADR that replaces it. Change the old ADR's status to "Replaced by ADR-0004" (use the new number).
- Some teams add a dated note to the old ADR instead. Either way, keep what was decided before.

# The template

Copy everything in the box below into a new file in `docs/adr`. Fill in each part.

```markdown
# ADR-0000: [The decision, in a few words]

## Date and status
[Date]. [Proposed, Accepted, or Replaced by ADR-0000]

## Context
What is happening? What problem pushed you to make a choice?

## Options
What choices did you look at? Write the good and bad parts of each one.

- Option 1:
  - Good:
  - Bad:
- Option 2:
  - Good:
  - Bad:

## Decision
What did you choose, and why?

## Consequences
What happens because of this choice? What gets easier? What gets harder?
What do you need to do next?
```

# Example

```markdown
# ADR-0001: Use Next.js with Material UI

## Date and status
October 31, 2026. Accepted.

## Context
We need screens and server code for a three-tier app that runs on Vercel.

## Options
- Plain React:
  - Good: It is simple to start.
  - Bad: It needs a separate place for server code.
- Next.js:
  - Good: It holds the screens and the server code in one project.
  - Bad: We have to learn which code runs in the browser and which runs on the server.

## Decision
Use Next.js with Material UI, because it covers two of our three tiers in one project.

## Consequences
We learn where code runs, in the browser or on the server.
Material UI's theme file needs a "use client" line at the top.
```

# Tips for a good ADR

- Write down why you chose it, not only what you chose.
- Write down the other options you looked at, and the good and bad parts of each.
- Put a date on anything that may change, like costs or limits.
- Ask Claude to write the first draft. Then read it and fix anything that is wrong. You own the decision.

# Source

This template is based on the Michael Nygard template (Title, Status, Context, Decision, Consequences) and the guidance in the [Architecture Decision Record repository](https://github.com/architecture-decision-record/architecture-decision-record). We added an Options section so you write down the choices you did not pick.
