"""Build one evidence pack per competitor from ALL research data (2026-11-04).
Run from this folder: python3 -I build_packs.py
Sources: caregiving-filtered app reviews, extra Google Play tags, MyChart/Everplans
Apple reviews (unfiltered, reader filters), Reddit posts (both downloads), forum app mentions."""
import json, re, collections, os
S = '..'
rel = json.load(open(f'{S}/app-reviews/analysis/relevance-final.json'))
care = {k for k, v in rel.items() if v['relevance'] == 'caregiving'}
APPS = {
 'caring-village': (['Caring Village','caring-village'], r'caring ?village'),
 'caringbridge': (['CaringBridge','caringbridge'], r'caring ?bridge'),
 'lotsa': (['lotsa-helping-hands'], r'\blotsa\b'),
 'medisafe': (['Medisafe','medisafe'], r'medisafe'),
 'everplans': (['everplans'], r'everplans?'),
 'mychart': (['epic-mychart'], r'\bmy ?chart\b'),
 'lively': (['lively-link'], r'jitterbug|greatcall|lively (?:link|mobile|wearable|app|smart|flip|device|button|pendant|plan)|lively\.com'),
 'medical-guardian': (['MyMedicalGuardian','mymedicalguardian'], r'medical guardian'),
 'group-texts': ([], r'group (?:chat|text|thread|message)s?|whats ?app|family chat'),
 'paper-notebook': ([], r'notebook|binder|whiteboard|white board|paper calendar|visit log|log ?book|wall calendar'),
}
UNFILTERED = {'epic-mychart', 'everplans'}  # all-reviews3 never went through the caregiving filter
packs = collections.defaultdict(list)
for f in ['all-reviews.jsonl', 'all-reviews2.jsonl', 'all-reviews3.jsonl']:
    for l in open(f'{S}/app-reviews/{f}'):
        r = json.loads(l)
        for slug, (names, _) in APPS.items():
            if r['app'] in names and (r['id'] in care or r['app'] in UNFILTERED):
                packs[slug].append({'id': r['id'], 'type': 'app review', 'store': r['store'], 'stars': r.get('stars'),
                    'date': r.get('date'), 'prefiltered_caregiving': r['id'] in care,
                    'text': (r.get('title') or '') + ' — ' + r['text']})
extra = json.load(open(f'{S}/app-reviews/analysis/extra-tags-2026-11-03.json'))['sources']
GP = {'Epic MyChart': 'mychart', 'CaringBridge': 'caringbridge', 'Lively': 'lively'}
for path, v in extra.items():
    if v.get('app') in GP and path.startswith('google-play'):
        data = json.load(open(f'{S}/app-reviews/{path}'))
        revs = data.get('reviews') or data.get('items') or [x for x in data.values() if isinstance(x, list)][0]
        for i in v['tags']:
            r = revs[int(i)]
            packs[GP[v['app']]].append({'id': f'gp-{GP[v["app"]]}-{i}', 'type': 'app review', 'store': 'google',
                'stars': r.get('score') or r.get('stars'), 'date': str(r.get('at') or r.get('date'))[:10],
                'prefiltered_caregiving': True, 'text': r.get('content') or r.get('text')})
seen = set()
for f in ['posts.jsonl', 'posts_targeted.jsonl']:
    for l in open(f'{S}/reddit/arctic-shift-2026-11-03/{f}'):
        p = json.loads(l)
        if p['key'] in seen: continue
        seen.add(p['key'])
        t = p.get('text') or ''
        for slug, (_, rx) in APPS.items():
            if re.search(rx, t, re.I):
                packs[slug].append({'id': 'reddit-' + p['key'], 'type': 'reddit post', 'url': p['url'],
                    'subreddit': p['subreddit'], 'date': p['created'], 'prefiltered_caregiving': False, 'text': t[:4000]})
for f in ['agingcare', 'alzconnected']:
    d = json.load(open(f'{S}/forums/app-mentions-2026-11-03/{f}.json'))
    for j, th in enumerate(d['threads']):
        txt = ' '.join(h if isinstance(h, str) else h.get('text', '') for h in th.get('hits', []))
        for slug, (_, rx) in APPS.items():
            if re.search(rx, txt + ' ' + th.get('title', ''), re.I):
                packs[slug].append({'id': f'{f}-{j}', 'type': 'forum thread', 'url': th['url'],
                    'prefiltered_caregiving': False, 'text': th.get('title', '') + ' — ' + txt[:4000]})
summary = {}
for slug, items in packs.items():
    json.dump(items, open(f'packs/{slug}.json', 'w'), indent=1, ensure_ascii=False)
    summary[slug] = dict(collections.Counter(i['type'] for i in items), chars=sum(len(i['text'] or '') for i in items))
json.dump(summary, open('packs/summary.json', 'w'), indent=1)
print(json.dumps(summary, indent=1))
