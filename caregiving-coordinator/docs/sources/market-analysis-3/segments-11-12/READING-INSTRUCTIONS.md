# Reading pass: how caregivers get relief, and what stops them (segments 11 and 12, 2026-11-04)

Discovery research. Never suggest an app, a product or a solution. Edit no file except your own output file.

Your pack (`packs/pack-N.json`) holds Reddit posts (full text) and forum thread excerpts (text around each mention). Read EVERY item in full. Page through the file with offset and limit; don't skip any.

For each item, write one JSON object:

{"id": "...",
 "relevant": true/false,   // true only if the writer is a family caregiver (caring for a parent, spouse, relative or friend) AND the text says something about getting relief, a break, respite, adult day, a therapist or counselor FOR THE CAREGIVER, a support group, or a named program. false for ads, researchers, app makers, professionals, people writing only about their own therapy unrelated to caregiving, or a therapist for the person being cared for.
 "help": ["..."],          // each kind of help the caregiver used, tried or considered. Use these labels: "in-home respite", "short-stay respite (facility)", "adult day program", "hospice respite", "therapist or counselor for the caregiver", "support group", "paid aide or companion", "family or friend stepping in", "named program: <name>", "app or online tool: <name>". [] if none.
 "status": "used" | "tried and stopped" | "looking or considering" | "wanted but couldn't get" | "recommends to others" | "mentioned only",
 "helped": ["<plain words, max 10 words>"],      // only what the writer says helped
 "barriers": ["..."],      // what stopped or limited them. Use any of: "cost", "waitlist or no openings", "hard application or eligibility rules", "inflexible program (hours, minimum stay, days)", "no trained or reliable providers", "doesn't trust strangers with the parent", "guilt or shame about handing off care", "worry about quality or safety", "the parent refuses", "transport or logistics", "didn't know it existed", "other: <max 8 words>". [] if none.
 "wanted_break_no_help": true/false,   // true if the writer says they need or want a break or relief and has no help in place
 "provider": "<the organization, program or company named, '' if none>",
 "payer_cost": "<who pays and the price, as written, '' if not said>",
 "quote": "<one exact excerpt, max 30 words, that shows the main point; '' if relevant is false>"}

Rules:
- Only record what the writer says. Don't guess.
- Quotes must be copied exactly from the item text, character for character.
- Use general words in "helped" ("got a full night of sleep", "time to see friends", "mom liked the activities") so similar points can be grouped.

Write a JSON list to `codes/codes-N.json` (N = your pack number). Then run:

    python3 verify_codes.py N

It checks that every item is coded once and every quote is an exact substring. Fix every failure and run it again until it prints "OK". Reply with a 3-line summary: items read, items relevant, the most common barriers.
