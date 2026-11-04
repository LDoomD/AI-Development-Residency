# Coding when each use-case problem happens, and what the caregiver wants changed (2026-11-04)

Discovery research. Do not judge anything by what a team might build, and never mention an app or a solution. Edit no file except your own output file.

Each item in your pack is a Reddit post or a forum thread (the thread's first post plus replies) by or about a family caregiver. `cared_for` says the audience:
- "parent" = Audience 1 (adult child caring for a parent)
- "spouse or partner" = Audience 2

Read EVERY item in full (use offset/limit to page through the file). For forum threads, code only the person who started the thread (the first post), plus replies only when they describe that same caregiver's situation.

## The use cases (use these exact names)

Audience 1 (parent):
1. Exhaustion, guilt and no life of their own
2. Dementia behavior and hard conversations
3. Money, legal papers and facility bills
4. Relatives don't help, or block each other
5. Medicines, eating and personal care
6. Choosing and arranging a place for them
7. Staying safe at home
8. Getting answers from doctors and hospitals
9. Being far away and not knowing what is happening
10. The parent refuses help
11. Getting into the parent's accounts (bank, insurance, phone, portals, passwords)

Audience 2 (spouse or partner):
1. Exhaustion, loneliness and own health
2. Dementia behavior and hard conversations
3. Personal care and medicines
4. Safety when they are alone or out
5. Aides, hospice and trusting others
6. Placing them and care costs
7. Money, scams and bills
8. Diagnosis and doctor delays
9. Relatives and others not helping or criticizing
10. The partner refuses help

Use only the list for the item's audience. Code a use case only when the item describes the writer actually facing that problem.

## Output: one JSON object per item

{"id": "...",
 "codes": [
   {"use_case": "<exact name>",
    "moment": "<WHEN or in what situation the problem shows up for them, plain words, max 12 words, starting with 'When', 'After', 'During', 'Every', 'At' or 'While'>",
    "want": "<what the writer says or clearly shows they want to be different, plain words, max 12 words; '' if not stated>",
    "quote": "<one word-for-word excerpt, max 30 words, that shows the moment>"}
 ]}

- Give one code per use case per item (pick the clearest moment). `codes` can be empty.
- A moment is a situation in time ("When the parent is discharged from the hospital", "At night when he tries to leave the house", "After a sibling refuses to pitch in"), not a feeling.
- Write moments and wants in general words (no names, no ages, no places), so similar moments from different items can be grouped.
- Quotes must be copied exactly from the item text.

Write a JSON list to `docs/sources/market-analysis-3/audience-v2/codes-N.json` (N = your pack number). When done, run a Python check that every quote is an exact substring of its item's text and that every use_case name is from the right audience's list; fix any failures. Reply with a 3-line summary only.
