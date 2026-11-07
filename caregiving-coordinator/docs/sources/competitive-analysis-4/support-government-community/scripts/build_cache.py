"""Builds the caches the other scripts load. Run first, from the folder that holds these scripts.
Reads only saved files under docs/sources (no web)."""
import json, glob, pickle
from corp import load, S
from pats import C
U = load()
pickle.dump(U, open('U.pkl', 'wb'))
M = S + 'market-analysis-3/segments-11-12/'
codes = []
for f in glob.glob(M + 'codes/*.json'):
    codes += json.load(open(f))
packs = {}
for f in glob.glob(M + 'packs/pack-*.json'):
    for p in json.load(open(f)):
        packs[p['id']] = p
pickle.dump(packs, open('packs.pkl', 'wb'))
rel = [c['id'] for c in codes if c['relevant']]
sg = [c['id'] for c in codes if c['relevant'] and 'support group' in c['help']]
json.dump(rel, open('rel_ids.json', 'w'))
json.dump(sg, open('sg_ids.json', 'w'))
rawhits = {k: [i for i, v in U.items() if rx.search(v['text'])] for k, rx in C.items()}
json.dump(rawhits, open('rawhits.json', 'w'))
print(len(U), len(rel), len(sg))
