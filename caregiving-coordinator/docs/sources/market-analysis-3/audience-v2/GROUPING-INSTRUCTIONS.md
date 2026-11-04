# Grouping moments and wants (2026-11-04)

Discovery research. Never mention an app or a solution. Edit no file except your own output file.

Input: `moments-by-usecase.json` in this folder. Each key is "<audience>|<use case>". Each use case has:
- `moments`: a list of [item id, moment]
- `wants`: a list of [item id, want]

Do only the keys for your audience (A1 or A2).

For each use case:
1. **Group the moments** into 3 to 6 groups of moments that describe the same kind of situation. Give each group:
   - a plain label of 10 words or fewer, starting with "When", "After", "During" or "While"
   - the list of every item id in it
   Every moment goes into exactly one group, or into "other" if it fits none.
2. **Group the wants** the same way into 3 to 6 groups. Labels start with "We want them to" (for example: "We want them to get real breaks without guilt"). Each label has 14 words or fewer, written about the caregiver. Every want goes into exactly one group or "other".
3. Labels must be in general words (no names or ages), and must say only what the grouped items say.

Output JSON in `groups-<A1 or A2>.json`:
{"<audience>|<use case>": {"moments": [{"label": "...", "ids": ["..."]}, ..., {"label": "other", "ids": [...]}],
                           "wants": [{"label": "...", "ids": [...]}, ...]}}

When done, run a Python check against moments-by-usecase.json:
- Every id in each use case's moments appears exactly once across that use case's moment groups. Do the same for wants.
- No id appears that isn't in the input.

Fix any failures. Reply with a 3-line summary only.
