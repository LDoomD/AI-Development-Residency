# How each Reddit post is tagged (2026-11-03)

Discovery research only. Do not judge posts by what any team might build.

For every post in the chunk file, output one JSON line:

{"key": ..., "url": ..., "created": ..., "subreddit": ...,
 "caregiver": true/false,          # written by someone caring for another person (parent, spouse, child, relative, client). false for patients writing about themselves, researchers, ads, app makers, surveys.
 "relevant": true/false,           # says something about how caregivers organize care, share info with family, handle documents/accounts, get support, or names a tool/app
 "tools": ["..."],                 # every tool or method named: app names, "group text", "spreadsheet", "paper notebook", "whiteboard", "Google Calendar", etc.
 "columns": {"1": "W"|"P"|"N", ...},  # only the columns the post actually talks about (omit the others)
 "problem": "...",                 # if any column is P or N: the concrete problem in plain words, max 12 words (e.g. "brother never reads the group text")
 "wish": "...",                    # if the person says what they want or wish existed, in plain words, max 15 words; else ""
 "quote": "..."}                   # one word-for-word excerpt, max 30 words, that best shows the point; "" if not relevant

Columns (the feature comparison table):
1 Shared calendar and task sign-up (who does what, when; dividing tasks among family)
2 One update reaches everyone (keeping family informed)
3 Relatives join with their own access (logins, proxy access, sharing passwords/accounts)
4 Medication reminders family can see (tracking meds, pill schedules shared with others)
5 Store and share important documents (POA, insurance cards, directives, paperwork, binders)
6 See medical records and test results (portals, getting records, talking to doctors' offices)
7 Emergency help button and fall alerts
8 Support for the caregiver (burnout, respite, support groups, someone to talk to)

Values: W = the post says something that works for them for this need (any tool or method).
P = the post describes a problem with a tool or method they use for this need.
N = the post describes the need with no tool working / nothing available / doing it all alone.

Keep tagging honest: if a post doesn't speak to a column, leave it out. Quotes must be copied exactly from the text. No usernames.
