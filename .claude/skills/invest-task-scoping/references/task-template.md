# Task template

The course's task-level template, as the owner's NotebookLM listed it (verify against the Notion template "Week 2 Coding Challenge - Product Specs Template"). Fill every section for each piece. Keep each section short.

**Story formula:** As a [audience], I want [goal], so that [the problem solved, or the value gained]. Describe the problem or value, never the solution.

## Ticket fields (when the work goes into a board)

Title (summarizes the scope) · Team function · Type of work · Sprint forecast · Epic · Feature · Status (for example Writing requirements, To do, In progress, Ready, Demoed, Done).

## Task body

| Section | What goes in it |
|---|---|
| **User story** | One sentence in the formula above |
| **Background** | Why this matters now, in 1-2 lines |
| **Problem statement** | The problem the audience has, in their words |
| **Definition of result** | What is different for the audience when it's done |
| **Scope / Definition of done** | What's in, what's out, and when it counts as finished |
| **Acceptance criteria** | A short checklist anyone can verify |
| **Use case scenarios** | The main way it's used, and one way it goes wrong |
| **BDD scenarios** | Given / When / Then, for the happy path and one problem path |
| **Technical acceptance** | Needs from the system (speed, security, data) |
| **Prototypes** | Links to sketches or screens, if any |

## Example (illustrative, not from the course)

**User story:** As an adult child caring for a parent, I want to ask a sibling to cover one evening, so that I can take a break without calling everyone.

**BDD**
- *Given* I have added my sibling to the family circle, *When* I pick an evening and send the request, *Then* my sibling gets the request and sees the date.
- *Given* my sibling hasn't answered, *When* a day passes, *Then* I'm reminded and can ask someone else.

**Size check:** Small, about 1 week: one request and one reminder. Not included: a full shared calendar (a separate story).

## Course vocabulary

- **Epic:** a huge category of work.
- **Feature:** a smaller chunk of an epic.
- **Task:** a tiny increment, small enough to build and check in 1-2 weeks.
