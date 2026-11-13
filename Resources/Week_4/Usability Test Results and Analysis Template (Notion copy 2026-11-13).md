# Usability Test Results and Analysis Template
- Source copy: https://app.notion.com/p/c1c9219a4691829bacb301607bbc4bae
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:26.333Z
- Not saved: none (the page's own title in Notion is "Rapid Prototype Test Analysis Template")

---

> 📍 This is your research report. Fill it out after all of your tests. Then turn the problems into user requirements and technical requirements, and give them to Claude to build the next version.

# 1. Summary

Write this part last. In 3 to 5 sentences, say what you tested, who tested it, and the most important problems you found.

# 2. What we tested

- App link and version:
- Dates of the tests:
- Goals of the test (copy from your plan):

# 3. Who tested it

Use P1, P2. Do not use real names.

| Participant | How they match our audience | Format (in person or video) |
| --- | --- | --- |
| P1 |  |  |
| P2 |  |  |

# 4. Task results

Write Yes, Partly, or No in each box.

| Task | P1 | P2 | Notes |
| --- | --- | --- | --- |
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |

# 5. How to analyze your notes

This is called affinity diagramming. You can do it on sticky notes in FigJam.

1. **Write one note for each thing you saw.** Use your notes from every person. Put one problem or one quote on each sticky note.
2. **Group the notes.** Put notes that are about the same thing together. Give each group a short name, like "People could not find where to add money."
3. **Rank the groups.** Decide which problems are the most important to fix. Use the severity scale below.

# 6. How bad is each problem?

Rate each problem with this scale from Jakob Nielsen.

| Score | What it means |
| --- | --- |
| 0 | Not a usability problem. |
| 1 | Cosmetic. Fix it only if there is extra time. |
| 2 | Minor. Fix it, but it is low priority. |
| 3 | Major. Important to fix. High priority. |
| 4 | Catastrophe. You must fix it before people use the app. |

To pick a score, ask three questions:

- **How often?** Did one person hit it, or everyone?
- **How much did it hurt?** Could they get past it, or were they stuck?
- **Does it keep happening?** Do people learn to avoid it, or do they hit it every time?

# 7. Findings

List each problem. Start with the most severe.

| # | The problem | What we saw (actions and exact quotes) | How many people (out of 2) | Severity (0 to 4) |
| --- | --- | --- | --- | --- |
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

# 8. What worked well

Write down what people liked or did easily, so you do not break it in the next version.

- 

# 9. Requirements for the next version

Turn each problem you will fix into requirements. Use the same format as your Week 2 requirements.

| Finding # | User requirement (what the person needs) | Technical requirement (what the app must do) | Priority |
| --- | --- | --- | --- |
| 1 | Example: As a person with ADHD, I need to see how much money I have left on the first screen, so I do not have to search for it. | Example: The home screen shows the amount left for each budget, read from the database each time the page loads. | High |
| 2 |  |  |  |

# 10. Next steps

- [ ] Add a ticket for each requirement to the Backlog Kanban Board.
- [ ] Give this report and the requirements to Claude. Build the new version one ticket at a time.
- [ ] If a fix changes a big decision, write a new ADR.
- [ ] Launch the new version on GitHub, Vercel, and Supabase.
- [ ] Test the fixed parts again, if you can.

# 11. Limits of this test

Be honest about what this test cannot tell you.

- We tested with only a few people. Nielsen Norman Group recommends 5 people per group, so we likely missed some problems.
- Write down anything else that could have changed the results, like testing with friends or testing on only one kind of device.

# Sources

- [Affinity Diagramming](https://www.nngroup.com/articles/affinity-diagram/), Nielsen Norman Group
- [Severity Ratings for Usability Problems](https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/), Jakob Nielsen, Nielsen Norman Group
- [Usability Testing 101](https://www.nngroup.com/articles/usability-testing-101/), Nielsen Norman Group
