"""Assemble the audience update content. Run: python3 -I assemble_audience.py"""
import json
A = json.load(open('audience-tables.json')); M = json.load(open('../ma3-filled.json')); S = json.load(open('../reddit-sample-by-audience.json'))
for a in A.values():
    for rows in a['tables'].values():
        for r in rows:
            if r[2].startswith('0 ('): r[3] = 'not seen on Reddit'
sp = S['Audience 2: spouse or partner']; n2 = sp['n']; th = sp['themes']
def p(t):
    m, an = th.get(t, [0, 0]); return f"{m} ({round(100*m/n2)}%) / {an} ({round(100*an/n2)}%)"
OWN = "The caregiver's own life"
a2uc = [["Use case on the board", "Forum threads (of 54 spouse threads, as on the board; % = count ÷ 54)", f"Reddit posts about a spouse ({n2}): main / anywhere", "What Reddit shows (small sample)"],
 ["Exhaustion, loneliness and own health", "22 of 54 (41%)", "Burnout " + p('Burnout, guilt, isolation, grief') + "; own life " + p(OWN), "Top in both."],
 ["Dementia behavior and hard conversations", "18 of 54 (33%)", p('Dementia behavior and communication'), "Much lower on Reddit. The forum spouses came mostly from a dementia community (ALZConnected)."],
 ["Personal care and medicines", "12 of 54 (22%)", "Medications " + p('Medications'), "Similar."],
 ["Safety when they are alone or out", "9 of 54 (17%)", p('Safety'), "Lower on Reddit."],
 ["Aides, hospice and trusting others", "8 of 54 (15%)", p('Paid caregivers and agencies'), "Similar or lower."],
 ["Placing them and care costs", "7 of 54 (13%)", p('Choosing, placing and paying for care'), "Similar or lower."],
 ["Money, scams and bills", "6 of 54 (11%)", p('Money, insurance, legal papers'), "Higher on Reddit."],
 ["Diagnosis and doctor delays", "4 of 54 (7%)", p('Doctors, appointments, records'), "Much higher on Reddit."],
 ["Relatives and others not helping or criticizing", "3 of 54 (6%)", p('Family coordination, siblings'), "Similar."]]
c1 = S['Audience 1: parent']['n']
out = {
 "title": "UPDATED 2026-11-04 — AUDIENCES, MOTIVATIONS, GOALS AND USE CASES, WITH THE NEW REDDIT RESEARCH",
 "intro": f"Everything on this page checked against the new Reddit research: a random sample of 500 Reddit posts (412 by caregivers). {c1} are about a parent (Audience 1) and {n2} are about a spouse or partner (Audience 2). Each post was coded with the same lists this page uses: the 14 problem themes, the motivations, situational goals and life goals, plus anything new. The boxes to the left are unchanged. Read the tables as forums versus Reddit. The Reddit readers marked more items per post than the forum readers, so compare the order (rank), not the exact percentages.",
 "changes": open('changes.txt').read().replace('{c1}', str(c1)).replace('{n2}', str(n2)),
 "a1_traits": f"AUDIENCE 1 LABEL AND TRAITS, added: on Reddit, {c1} of 412 caregiver posts (65%) are about a parent, compared with 55 of 117 forum threads. Everything else in the label box stands.",
 "a2_traits": f"AUDIENCE 2 LABEL AND TRAITS, added: on Reddit, {n2} of 412 caregiver posts (8%) are about a spouse or partner, compared with 54 of 117 forum threads. That's too few to change the label. The traits from AARP and the forums stand.",
 "mcols": ["Item", "Forum threads (count, % of the audience's threads)", "Reddit posts (count, % of the audience's posts)", "Rank: forums → Reddit"],
 "A": A, "a1uc": [M['aud_columns']] + M['aud_rows'], "a2uc": a2uc, "segments": M['aud_segments'],
 "limits": "LIMITS: one reader coded each post once, and no person double-checked. Posts only, no comments. The forum and Reddit readers differ, so compare order, not exact shares. Audience 2 has 35 Reddit posts. The 'NEW' groups are Claude's grouping of the readers' notes (docs/sources/market-analysis-3/goals/group_new.py). Data: docs/sources/market-analysis-3/goals/ (GOALS-INSTRUCTIONS.md, codes-1..3.json, count_goals.py, build_audience.py). Nothing on the page was chosen or removed; adding or moving anything is the owner's call."}
json.dump(out, open('audience-update.json', 'w'), ensure_ascii=False, indent=1)
print('ok', len(json.dumps(out)))
