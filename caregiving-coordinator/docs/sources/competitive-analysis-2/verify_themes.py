"""Check every theme file against its pack: ids exist and were kept, count == len(ids),
quotes are exact substrings of the quoted item. Run: python3 -I verify_themes.py"""
import json, glob, os, sys
bad = 0
for tf in sorted(glob.glob('themes/*.json')):
    slug = os.path.basename(tf)[:-5]
    pack = {i['id']: i for i in json.load(open(f'packs/{slug}.json'))}
    t = json.load(open(tf))
    kept = set(t['kept_ids'])
    errs = []
    if t['items_in_pack'] != len(pack): errs.append(f"items_in_pack {t['items_in_pack']} != {len(pack)}")
    if t['items_kept'] != len(kept): errs.append(f"items_kept {t['items_kept']} != {len(kept)}")
    if not kept <= set(pack): errs.append(f"kept ids not in pack: {sorted(kept-set(pack))[:5]}")
    groups = [('works_well', t['works_well']), ('does_not_work_well', t['does_not_work_well'])] + \
             [(f'q:{k}', v) for k, v in t['questions'].items()]
    nthemes = nquotes = 0
    for gname, themes in groups:
        for th in themes:
            nthemes += 1
            if th['count'] != len(set(th['ids'])): errs.append(f"{gname} '{th['theme']}' count {th['count']} != {len(set(th['ids']))} ids")
            if not set(th['ids']) <= kept: errs.append(f"{gname} '{th['theme']}' uses ids not kept: {sorted(set(th['ids'])-kept)[:3]}")
            for q in th.get('quotes', []):
                nquotes += 1
                txt = (pack.get(q['id']) or {}).get('text') or ''
                if q['quote'] not in txt: errs.append(f"{gname} quote not exact in {q['id']}: {q['quote'][:60]}")
    print(f"{slug}: kept {len(kept)}/{len(pack)}, {nthemes} themes, {nquotes} quotes, {len(errs)} errors")
    for e in errs: print('   ', e)
    bad += len(errs)
sys.exit(1 if bad else 0)
