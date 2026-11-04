# How each Reddit post in the random sample is coded (2026-11-04)

Discovery research. Do not judge anything by what a team might build. Edit no file except your own output file.

The goal is to compare Reddit with the forum research, which coded 117 caregiving forum threads with the 14 themes below (docs/community-voice-findings.md). Use the same themes so the numbers can be compared.

Read EVERY post in your part file in full (page with offset/limit if needed). For each post, write one JSON object:

{"id": "...",
 "caregiver": true/false,      // written by someone caring for another person (parent, spouse, partner, child, relative, client). false for patients writing about themselves, researchers, surveys, app makers, ads, rule posts.
 "cared_for": "parent" | "spouse or partner" | "other relative" | "child" | "client" | "unclear",
 "main": "<one theme>",        // the ONE theme the post is mainly about (only if caregiver is true)
 "anywhere": ["<theme>", ...], // every theme the post talks about, including main
 "new_theme": "",              // if the main problem fits none of the 14 well, describe it in plain words (max 12 words) and use "Other" as main
 "quote": "..."}               // one word-for-word excerpt, max 30 words, that shows the main theme ("" if caregiver is false)

The 14 themes (use these exact names):
1. Choosing, placing and paying for care: finding or paying for a nursing home, assisted living, memory care, home care, or deciding whether to place someone.
2. Burnout, guilt, isolation, grief: the caregiver's exhaustion, stress, resentment, guilt, loneliness, grief, no breaks.
3. Family coordination, siblings: dividing the work, siblings or family not helping or fighting, keeping family informed.
4. Long-distance caregiving: caring from far away.
5. Medications: giving, tracking, refusing, mixing up or changing medicines.
6. Money, insurance, legal papers: bills, the parent's money, Medicaid or Medicare, insurance, power of attorney, wills, getting into accounts, scams.
7. Care recipient refuses help: the person won't accept help, aides, moving, doctors, or giving up driving.
8. New diagnosis, crisis, "where do I start": a sudden event or new diagnosis and not knowing what to do.
9. Dementia behavior and communication: confusion, aggression, paranoia, repeating, wandering, sundowning, how to talk to the person.
10. Safety: falls, wandering danger, being alone, driving danger, emergency alerts, monitoring.
11. Paid caregivers and agencies: problems with or managing aides, agencies, facility staff.
12. Doctors, appointments, records: doctors, hospitals, appointments, discharge, medical records, portals, being left out by doctors.
13. The caregiver's own life: job, money, health, marriage, kids, own future affected by caregiving.
14. Other: none of the above (then fill new_theme).

Write your output as a JSON list to `docs/sources/market-analysis-3/codes/part-N.json` (N = your part number). Quotes must be copied exactly from the post text. When done, run a check that every quote is an exact substring of its post, and reply with a 3-line summary only.
