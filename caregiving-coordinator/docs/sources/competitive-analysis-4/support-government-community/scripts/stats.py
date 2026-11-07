import pickle,collections,json,re
rows=pickle.load(open('rows.pkl','rb'))
BL=[('eligibility / income / asset rules',r'eligib|income|assets|qualif|age rule|residency|immigration|share of cost|deductible'),
('waitlist / slow / no slots',r'waitlist|waiting|slow|wait|no emergency|no slots|2027|8 months|months'),
('paperwork / system problems',r'paperwork|payroll|app|phone|record|portal|wrong information|unclear benefits|late checks|rules|passed along|did not know|busy'),
('cost',r'cost|\$|pay too low|low pay|money'),
('too few hours / low pay',r'too few|hours|low pay|pay too low|pay goes|pay change'),
('parent / patient refused',r'refus|will not|does not want|parent refused|patient refused|turned'),
('group fit / tone',r'group fit|judg|toxic|negative|overwhelm|fit|moderator|harsh|not sick enough|hearing others|only dad|age mismatch|too many groups|ads and sketchy'),
('quality / safety / bad experience',r'quality|neglect|bad facility|aide|caretakers|boundaries|abusive|quit|care team|network|doctors rotate|facility|negative reviews|no hospice'),
('guilt / feels wrong to ask',r'guilt|begging|feels|asking|not allowed'),
('time / schedule / access to a group',r'schedule|meeting times|meets too|link|invite|no server|expired|no group|could not find|hard to get|timing|only 3'),
('family / friends did not follow through',r'friends|relative is in|family|siblings|sibling|aunt'),
('no pay after change / benefit ended',r'ended|stopped|ends when'),
]
def blk(s):
    out=[]
    for n,rx in BL:
        if re.search(rx,s,re.I): out.append(n)
    return out
by=collections.defaultdict(list)
for r in rows: by[r['name']].append(r)
AUD={'parent':'A1 parent','spouse or partner':'A2 spouse/partner','other relative':'other relative','child':'own child','client':'client','unclear':'unclear'}
out={}
for nm,rs in by.items():
    lab=collections.Counter(r['label_n'] for r in rs)
    cg=[r for r in rs if r['label_n'] in (1,2,3)]
    aud=collections.Counter(AUD.get(r['cared_for'],r['cared_for']) for r in cg)
    outc=collections.Counter(r['outcome'] for r in cg)
    u123={1:[r for r in cg if r['label_n']==1]}
    outc1=collections.Counter(r['outcome'] for r in u123[1])
    b=collections.Counter(x for r in cg for x in (blk(r['blockers']) if r['blockers'] else []))
    uses=collections.Counter(u.strip() for r in cg for u in r['used_for'].split(',') if u.strip())
    out[nm]=dict(n_read=len(rs),labels=dict(sorted(lab.items())),n_caregiver_reports=len(cg),aud=dict(aud),outcomes=dict(outc),outcomes_used=dict(outc1),blockers=dict(b.most_common(5)),uses=dict(uses.most_common(4)))
json.dump(out,open('stats.json','w'),indent=1)
for nm,s in sorted(out.items(),key=lambda x:-x[1]['n_caregiver_reports']):
    print(f"{nm}\n  read={s['n_read']} labels={s['labels']} cg={s['n_caregiver_reports']} aud={s['aud']}\n  outcomes_all={s['outcomes']} used_only={s['outcomes_used']}\n  blockers={s['blockers']} uses={s['uses']}")
