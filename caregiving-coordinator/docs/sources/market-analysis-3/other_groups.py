"""Group the 67 'Other' posts by their new_theme text (Claude's grouping, 2026-11-04). Run: python3 -I other_groups.py"""
import json, collections
G = {
 "Hands-on personal care, equipment and supplies": ["incontinence", "bedbound", "personal care products", "Medical equipment broke", "Washing the hair", "wound care", "move a paralyzed", "incontinence supplies", "medical equipment, like oxygen", "urine smell", "stockpiling medical supplies", "pressure sore", "catheter", "chores like laundry done after surgery", "recover after surgery", "wheelchair"],
 "Technology the older person can't use or is misled by": ["everyday tools a frail", "technology simple", "cannot learn or remember how to use technology", "distrust new technology", "very poor eyesight", "social media, hacked", "misleading online videos", "use their phones", "robot vacuum"],
 "End-of-life decisions and conversations": ["resuscitation", "feeding tube", "funeral and burial", "burial wishes and end-of-life", "euthanasia", "end-of-life care", "dying parent"],
 "Paid caregivers asking about their own work": ["paid carer afraid", "Paid aide working unpaid", "Paid caregiver mistreated", "license is needed", "certification course", "unable to lift", "companionship visits"],
 "Sharing good moments and life stories": ["life stories", "funny moment", "calm and rewarding", "funny, positive", "abilities remain"],
}
r = json.load(open('reddit-sample-theme-counts.json'))
out = collections.defaultdict(list)
for t in r['other_new_themes']:
    g = next((k for k, keys in G.items() if any(s.lower() in t.lower() for s in keys)), 'Mixed one-offs')
    out[g].append(t)
json.dump(out, open('other-groups.json', 'w'), indent=1, ensure_ascii=False)
for k, v in out.items(): print(len(v), k)
print(sum(len(v) for v in out.values()))
