"""Check 3b part 2: stricter searches for programs the helper's Medicaid/IHSS filters did not include; counts not already in helper's read file. Run: python3 -I a_missed2.py"""
import re,pickle,json,collections
SC="/private/tmp/claude-501/-Users-landodoom-Desktop-AI-Developer-Residency--caregiving-coordinator/88c39ed8-fc0d-46c0-b385-032bd23092de/scratchpad/"
D="/Users/landodoom/Desktop/AI Developer Residency /caregiving-coordinator/docs/sources/competitive-analysis-4/support-government-community/"
U,packs,codes=pickle.load(open(SC+'corpus.pkl','rb'))
rd={json.loads(l)['id'] for l in open(D+'MENTIONS-READ.jsonl')}
S={
'PCA/CDPAS/self-directed/cash&counseling (strict)':r"personal care (attendant|assistant)s?\b|\bPCA (program|hours|services|waiver)|\bCDPAS\b|self[- ]directed (care|program|services|waiver)|participant[- ]directed|cash (and|&) counseling|\bPCS (hours|program)",
'paid family caregiver programs (strict)':r"paid (by|through) (medicaid|the state|the va|ihss|cdpap)|(medicaid|the state|the va) (pays|paid) (me|family|for me)|get paid (by|through)|paid family caregiver|family caregiver (stipend|pay program)|caregiver stipend|pay(s|ing)? family members? to (care|take care)",
'VA caregiver programs (strict)':r"\bPCAFC\b|program of comprehensive assistance|veteran[- ]directed|VA caregiver (support|program|stipend|pay)|caregiver support program",
'Structured Family Caregiving':r"structured family caregiv",
'Medicare Advantage + in-home/respite benefit (strict)':r"(medicare )?advantage plan.{0,100}(in[- ]home|home care|aide|respite|adult day|caregiver)|(in[- ]home|home care|aide|respite|adult day|caregiver).{0,100}advantage plan",
'Church or faith group HELPED/NOT (strict)':r"(church|synagogue|parish|pastor|faith community).{0,80}(help|support|respite|volunteer|sit with|visit|bring|meal|group)",
'Senior center (any)':r"senior cent(er|re)s?",
'Hospital caregiver program/support group (strict)':r"hospital.{0,40}(caregiver (program|support|class|group)|support group)|(caregiver (program|support|class|group)).{0,40}hospital",
'Caregiver coaching / care navigator service (strict)':r"caregiver coach|care coach\b|care navigator|care concierge|geriatric care manager|aging life care",
'Hospice respite loose (hospice AND respite anywhere in item)':None,
'Adult day center (strict)':r"adult day (program|center|care|health)",
'Lifespan Respite/respite voucher (strict)':r"lifespan respite|respite voucher|respite (grant|fund)\b|caregiver respite voucher|NFCSP|ARCH national|archrespite",
}
C=re.compile
out=open(SC+'missed2_contexts.txt','w')
for k,rx in S.items():
    if rx is None:
        R1=re.compile('hospice',re.I);R2=re.compile('respite',re.I)
        hits=[i for i,v in U.items() if R1.search(v['text']) and R2.search(v['text'])]
        R=R2
    else:
        R=re.compile(rx,re.I); hits=[i for i,v in U.items() if R.search(v['text'])]
    unread=[i for i in hits if i not in rd]
    print(f"{k[:62]:62s} items={len(hits):4d} already-read-by-helper={len(hits)-len(unread):3d} NOT-read={len(unread):4d}")
    out.write(f"\n===== {k}: {len(hits)}\n")
    for i in unread:
        t=U[i]['text'];m=R.search(t)
        out.write(f"[{i}] {U[i]['date']} | {t[max(0,m.start()-130):m.end()+170]!r}\n")
