# Who is the writer caring for? (audience split, 2026-11-04)

Edit no file except your own output file. Read EVERY item in your pack (`audience-packs/apack-N.json`) in full, paging with offset and limit.

For each item, write one JSON object:

{"id": "...",
 "cared_for": "parent" | "spouse or partner" | "other relative" | "child" | "client" | "unclear",
 "quote": "<one exact excerpt, max 25 words, that shows who the writer cares for; '' only if unclear>"}

- "parent" includes a parent-in-law and a step-parent, and an adult child helping a parent who cares for the other parent.
- "spouse or partner" includes a husband, wife, boyfriend or girlfriend the writer cares for.
- If the writer cares for more than one person, choose the person most of the post is about.
- "other relative": grandparent, sibling, aunt, uncle, cousin. "child": the writer's own child of any age. "client": paid care.
- Only label what the writer says. Don't guess. Quotes must be copied exactly from the item text.

Write a JSON list to `audience-codes/acodes-N.json`. Then run `python3 verify_audience.py N` and fix every failure until it prints "OK". Reply in 2 lines: items read, and how many of each label.
