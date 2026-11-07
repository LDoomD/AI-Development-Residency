"""Check 3b: search ALL saved items for caregiver-help names the helper may have missed. Prints hit counts and writes contexts to a scratch file.
Run: python3 -I a_missed.py"""
import json,re,pickle,collections
D="/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator/docs/sources/competitive-analysis-4/support-government-community/"
SC="/private/tmp/claude-501/-Users-landodoom-Desktop-AI-Developer-Residency--caregiving-coordinator/88c39ed8-fc0d-46c0-b385-032bd23092de/scratchpad/"
U,packs,codes=pickle.load(open(SC+'corpus.pkl','rb'))
rows=[json.loads(l) for l in open(D+'MENTIONS-READ.jsonl')]
readids=collections.defaultdict(set)
for r in rows: readids[r['id']].add(r['name'])
rel={c['id'] for c in codes if c['relevant']}
I=re.I
T={
 'VA caregiver (PCAFC/Aid&Attendance/VD-HCBS/Structured Family Caregiving)':r"\bPCAFC\b|program of comprehensive assistance|aid (and|&) attendance|veteran[- ]directed|structured family caregiv|VA caregiver (support )?program|VA respite",
 'respite voucher/grant/Lifespan Respite/NFCSP/ARCH':r"respite (voucher|grant|fund|program|benefit)|lifespan respite|NFCSP|national family caregiver support|ARCH national respite",
 'caregiver stipend / paid family caregiver':r"caregiver stipend|stipend|paid family caregiver|get paid to (care|take care)|paid by (medicaid|the state)|medicaid.{0,40}pay(s|ing)? (me|family)|pay me as (a )?caregiver",
 'PCA / personal care attendant / PCS / self-directed / cash and counseling':r"\bPCA\b|personal care (attendant|assistant|services)|\bPCS\b|self[- ]directed|cash (and|&) counseling|participant[- ]directed|consumer[- ]directed|community first choice|\bCFC\b|\bCDPAP\b|\bCDPAS\b|\bIRIS\b",
 'Medicare Advantage in-home / supplemental benefit':r"(medicare )?advantage.{0,80}(in[- ]home|home care|aide|caregiver|respite|adult day)|supplemental benefit",
 'church / faith / community group':r"\bchurch\b|\bsynagogue\b|\bparish\b|\bmosque\b|faith[- ]based|\bpastor\b|\bchurch group",
 'senior center':r"senior cent(er|re)s?",
 'caregiver coach/coaching/training class':r"caregiver coach|care coach|caregiver training|caregiver class|caregiver education class|powerful tools for caregivers|savvy caregiver|care ?navigator",
 'hospital caregiver program':r"hospital.{0,40}caregiver (program|support)|caregiver (program|support) .{0,30}hospital|palliative care (team|program)|hospital social work",
 'AgingCare forum / agingcare.com':r"agingcare|aging care (forum|dot com)",
 'Well Spouse Association':r"well ?spouse",
 'Caregiver Action Network / National Alliance for Caregiving':r"caregiver action network|caregiveraction|national alliance for caregiving|caregiving\.org",
 'Area Agency on Aging / council on aging':r"area agency on aging|\bAAA\b|council on aging|dept\.? of aging|department of aging|aging and disability resource|\bADRC\b",
 'Adult day program':r"adult day (program|center|care|health)",
 'Meals on Wheels':r"meals on wheels",
 'CaringBridge':r"caring ?bridge",
 'Discord':r"\bdiscord\b",
 'WhatsApp':r"whats ?app",
 'Facebook (any)':r"facebook|\bfb\b",
 'Respite (any)':r"\brespite\b",
}
out=open(SC+'missed_contexts.txt','w')
summary=[]
for name,rx in T.items():
    R=re.compile(rx,I)
    hits=[i for i,v in U.items() if R.search(v['text'])]
    inrel=[i for i in hits if i in rel]
    unread=[i for i in hits if i not in readids]
    summary.append((name,len(hits),len(inrel),len(unread)))
    out.write(f"\n=========== {name}: all {len(hits)}, in 831 relief set {len(inrel)}, not in helper's read file {len(unread)}\n")
    for i in hits:
        v=U[i]; m=R.search(v['text'])
        out.write(f"[{i}] {v['date']} read_as={sorted(readids.get(i,[]))[:2]} | {v['text'][max(0,m.start()-160):m.end()+160]!r}\n")
for s in summary: print(f"{s[0][:75]:75s} all={s[1]:5d}  in831={s[2]:4d}  not-in-helper-file={s[3]:5d}")
print('items by source:',collections.Counter(v['src'] for v in U.values()))
