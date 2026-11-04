# How each competitor's evidence is read and themed (2026-11-04)

Discovery research. Do not judge anything by what a team might build. Do not edit any file except your own output file(s).

Input: `packs/<slug>.json` (a list of items: app reviews, Reddit posts, forum threads). Read EVERY item in full (use offset/limit to page through big files; do not skim or sample).

Step 1. Keep only items where the writer is caring for or helping another person (parent, spouse, child, relative, client) AND says something about this product (for workarounds: about using group chats/texts, or notebooks/binders/paper/whiteboards, to coordinate care). Items with `prefiltered_caregiving: true` already passed a caregiving check, but still drop them if they say nothing about the product. Reddit posts often mention the name only in passing: keep only if they say how it worked, failed, cost, or was used. Record dropped counts by reason.

Step 2. Find themes from what people actually write (do not start from a list). One item can count in several themes. A theme needs 2 or more items; one-offs go in `single_mentions`.

Step 3. Write `themes/<slug>.json`:
{
 "competitor": "...",
 "items_in_pack": N, "items_kept": N, "dropped": {"not caregiving": n, "says nothing about the product": n, "app maker / ad": n},
 "kept_ids": [...],
 "works_well": [ {"theme": "plain words, max 12 words", "what_it_means": "1 sentence", "count": n, "ids": [...],
                  "quotes": [{"id": "...", "quote": "copied EXACTLY from the item text, max 30 words"}, ... 2 quotes]} ],
 "does_not_work_well": [ same shape ],
 "questions": {   // same theme shape, empty list if no evidence; these answer the competitive table questions
   "who_uses_and_who_pays": [], "relatives_joining_and_sharing": [], "cost_price_cancelling": [],
   "emergencies_and_support_response": [], "setup_and_ease_of_use": [], "privacy_data_trust": [],
   "why_people_stop_or_stay": [], "what_people_use_instead_or_alongside": []
 },
 "single_mentions": [ {"id": "...", "point": "plain words"} ],
 "reader_notes": "anything that limits the evidence (e.g. most reviews about one old bug, one year, one store)"
}
Rules: `count` must equal the number of `ids`. Quotes must be exact substrings of the item text (same spelling, punctuation, emoji). Sort themes by count, biggest first. Plain words, no jargon. When done, reply with a 5-line summary only.
