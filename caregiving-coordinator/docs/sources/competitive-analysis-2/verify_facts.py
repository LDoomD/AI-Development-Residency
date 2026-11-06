"""Check every company-fact quote is in its saved file (spacing and HTML codes ignored). python3 -I verify_facts.py"""
import json, glob, re, html, os, sys
R = '../../..'
norm = lambda s: re.sub(r'\s+', ' ', html.unescape(s)).strip().lower().replace('’', "'").replace('“','"').replace('”','"')
bad = 0
for f in sorted(glob.glob('facts/*.json')):
    d = json.load(open(f)); n = e = 0
    for k, v in d.items():
        if not isinstance(v, dict) or 'evidence' not in v: continue
        for ev in v['evidence']:
            n += 1
            p = os.path.join(R, ev['file'])
            if not os.path.exists(p) or norm(ev['quote']) not in norm(open(p, errors='ignore').read()):
                e += 1; print('  MISSING', f, k, ev['file'], ev['quote'][:60])
    print(f, n, 'quotes', e, 'missing'); bad += e
sys.exit(1 if bad else 0)
