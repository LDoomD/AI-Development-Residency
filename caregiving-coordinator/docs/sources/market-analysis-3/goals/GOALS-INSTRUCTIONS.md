# Coding motivations, situational goals and life goals (2026-11-04)

Discovery research. Do not judge anything by what a team might build. Edit no file except your own output file.

These Reddit posts are by caregivers of a parent (Audience 1) or a spouse or partner (Audience 2). The audience page codes forum threads with the lists below. Use the same lists so the numbers can be compared. Code only what the post states or clearly shows. Many posts show none, and that's fine.

MOTIVATIONS (what drives them to act):
M1 Keep them safe and comfortable, spare them suffering
M2 Do the right thing, avoid blame or guilt
M3 Keep them at home and in control of their own life
M4 Love, loyalty and promises
M-NEW: anything else that clearly drives them (describe in plain words, max 10 words)

SITUATIONAL GOALS (outcomes they want right now in the caregiving):
S1 Get help, relief or services
S2 Find, choose or pay for a place
S3 Manage money and legal affairs
S4 Understand what is happening and what to do
S5 Keep them safe and watch over them
S6 Medicines
S-NEW: any other clear outcome they want (plain words, max 10 words)

LIFE GOALS (outcomes they want for their own life):
L1 Time and breaks for themselves
L2 Keep their own life, job and money
L3 Their own health and sanity
L-NEW: any other clear life goal (plain words, max 10 words)

Read EVERY post in your file in full. For each post, output:
{"id": "...", "cared_for": "...", "motivations": ["M1", ...], "situational": ["S1", ...], "life": ["L2", ...],
 "new": {"M": "", "S": "", "L": ""},
 "quotes": {"M": "...", "S": "...", "L": "..."}}   // one exact word-for-word excerpt (max 30 words) per category that has a code; "" otherwise

Write a JSON list to `docs/sources/market-analysis-3/goals/codes-N.json` (N = your file number). Check by script that every quote is an exact substring of its post. Reply with a 3-line summary.
