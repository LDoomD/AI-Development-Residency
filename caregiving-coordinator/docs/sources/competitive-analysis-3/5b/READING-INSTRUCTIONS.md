# Step 5b: reading every mention of a competitor (2026-11-04)

Discovery research. Never suggest an app or a solution. Edit no file except your own output file.

Each item in your pack is a Reddit post (full text) or part of a forum thread (the text around each mention) that names one competitor (`competitor`). Read EVERY item in full. Page through with offset/limit.

For each item, write one JSON object:

{"id": "...", "competitor": "...",
 "relevant": true/false,          // true only if the text really refers to this competitor (not another meaning of the word) AND the writer is a family caregiver (caring for a parent, spouse, relative). false for ads, app makers, researchers, page boilerplate, people writing only about themselves.
 "used": "used" | "tried and stopped" | "considering" | "recommends to others" | "mentioned only",
 "worked": ["<plain words, max 10 words, what worked or helped>", ...],      // only what the writer says
 "problems": ["<plain words, max 10 words, what went wrong or fell short>", ...],
 "instead": "<what they used or did instead, max 10 words, '' if not said>",
 "quote": "<one exact excerpt, max 30 words, that shows the main point; '' if relevant is false>"}

- Use general words in worked and problems ("advisor kept calling", "too expensive", "found a place fast", "no openings"), so similar points from different items can be grouped.
- "recommends to others" means the writer tells someone else to use it, without saying they used it themselves.
- Quotes must be copied exactly from the item text.

Write a JSON list to `docs/sources/competitive-analysis-3/5b/codes-N.json` (N = your pack number). When done, run a Python check that every quote is an exact substring of its item's text and that every item in the pack is coded once. Fix any failures. Reply with a 3-line summary.
