# Prompt for AI - Paste This

**How to use it**
1. Copy the prompt below. Don't upload this file; paste its text.
2. Attach the other 7 files in this folder: the `00` index and the 6 CSV tables.
3. Replace the last line with what you want the AI to do.

**If your AI tool takes only one file at a time**
- Send the prompt with the `00` index file first.
- Then send each table in the order below, with one line each time: "Here is file 2 of 6: Audience Motivations and Goals.csv. Read it, then wait for the next file."
- After file 6, send your task.

## The prompt

```text
These 7 files are one deliverable: the audience segmentation for a product that helps family caregivers. Read 00 Audience Segmentation - Read First.md before anything else.

HOW EACH CSV IS BUILT
- Line 1 = table title. Line 2 = what the table shows and what each column means. Line 3 = column headers. Data starts on line 4.
- One row = one fact, goal, problem or note.

THE TWO AUDIENCES
- Audience 1 = adult child caring for a parent.
- Audience 2 = spouse or partner caring for a husband, wife or partner.

READ IN THIS ORDER
1. Audience Segmentation Definition.csv (Section 1): national facts about all US family caregivers. Not split by audience.
2. Audience Motivations and Goals.csv (Section 2, table 2a): why each audience acts and what they want. Rank 1 = most common.
3. Audience Use Cases.csv (Section 2, table 2b): each audience's problems, when they happen, what should change, and scenarios to support. "Seen in" = number of posts and threads.
4. Audience Sources and Limits.csv (Section 2, table 2c): how 2a and 2b were made, and their limits.
5. Top Problems.csv (Section 3, table 3a): top problems across all sources, both audiences together.
6. Top Problems Sources and Limits.csv (Section 3, table 3b): who the posts are about, and the limits of 3a.

HOW THEY CONNECT
- 2a and 2b are linked by the Audience column. Compare the two audiences row by row.
- 2c explains 2a and 2b. 3b explains 3a. Apply their limits before drawing conclusions.
- 3a and 2b overlap in topic but were counted differently. 3a is both audiences across all sources; 2b is per audience. Do not add or match their numbers one to one.
- Section 1 is national context only. Do not treat its numbers as Audience 1 or Audience 2.

RULES FOR YOUR ANSWER
- For every claim, name the file and the row (for example: "Audience Use Cases.csv, Audience 2, rank 1").
- Keep Audience 1 and Audience 2 separate unless I ask you to combine them.
- If a cell is empty, say the data does not cover it. Do not guess.
- Audience 2 has fewer posts (35 Reddit posts), so treat its ranking as less certain.
- Section 3 counts 117 forum threads; the market analysis counts 141. Do not mix those numbers.
- Use plain words, short sentences, and small tables.

MY TASK: [write what you want here]
```
