"""Random Reddit sample for the market analysis update (2026-11-04). No keyword filter.
200 posts each from r/CaregiverSupport and r/AgingParents (2023-2026 download) and 100 from the
other 11 communities, seed 20261104. Skips removed/deleted posts and posts under 150 characters.
Run: python3 -I build_sample.py"""
import json, random
R = '../reddit/arctic-shift-2026-11-03'
def load(f):
    out = []
    for l in open(f'{R}/{f}'):
        p = json.loads(l); t = (p.get('text') or '').strip()
        if len(t) < 150 or '[removed]' in t[:200] or '[deleted]' in t[:200]: continue
        out.append(p)
    return out
main = load('posts.jsonl'); other = load('posts_targeted.jsonl')
seen = {p['key'] for p in main}; other = [p for p in other if p['key'] not in seen]
rng = random.Random(20261104)
pick = []
for sub in ('CaregiverSupport', 'AgingParents'):
    pool = [p for p in main if p['subreddit'] == sub]; pick += rng.sample(pool, 200)
pick += rng.sample(other, 100)
rng.shuffle(pick)
rows = [{'id': p['key'], 'url': p['url'], 'subreddit': p['subreddit'], 'date': p['created'], 'text': p['text'][:5000]} for p in pick]
for i in range(4):
    json.dump(rows[i*125:(i+1)*125], open(f'sample/part-{i+1}.json', 'w'), ensure_ascii=False, indent=1)
json.dump({'pool_main': len(main), 'pool_other': len(other), 'picked': len(rows)}, open('sample/summary.json', 'w'))
print(len(main), len(other), len(rows))
