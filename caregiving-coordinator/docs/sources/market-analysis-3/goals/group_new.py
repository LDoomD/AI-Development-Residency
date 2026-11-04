"""Group the readers' NEW motivations and goals (Claude's grouping, by exact text). Run: python3 -I group_new.py
Every new item must land in exactly one group; leftovers go to 'Other one-offs'."""
import json
C = json.load(open('goal-counts.json'))
G = {
 ('Audience 1: parent','M'): {
   "Honor their wishes and make the time left count": ["Honor her end-of-life wishes", "Respect his end-of-life wishes", "make the most of every remaining day", "give parents joy and ease their depression"],
   "Relieve the other parent who is the main caregiver": ["Protect mom's health from the strain of dad's care", "Support the stepmom who is the main caregiver", "lighten the load on mother who cares daily", "relieve burnt-out mother who is main caregiver"],
   "I'm the only one, they need me": ["Being the family's designated caregiver", "She needs me and I am the only one there"],
   "Preserve their life stories": ["Preserve his life stories and family history", "preserve parents' stories for grandchildren"]},
 ('Audience 1: parent','S'): {
   "Get the parent to accept care and look after their own health": ["Get dad to accept going to the hospital", "Get dad to downsize and let go of stuff", "Get dad to manage his own health and diet", "Get dad to see a doctor", "Get her to trust a new doctor", "Get him to do his part to regain strength", "Get mom to keep clean without upsetting her", "Get mom to use her new hearing aids", "Help dad build healthier habits", "Help mom accept hospice and feel safe", "Improve wellbeing of a parent who refuses care", "Mom starts taking care of her own health", "get dad to finish rehab before going home", "get mom to eat and see a doctor", "get mom to take care of her own health", "Get mom through dentist visits despite dementia"],
   "Handle the parent's behavior and emotions": ["Help dad calm his anger outbursts", "Stop dad harassing waitstaff in public", "Get mom to stay out of private rooms", "calm mother's anxiety and constant phone calls", "Set limits on father's over-texting", "Support mom emotionally through depression and anxiety", "Handle parent's toilet hygiene tactfully"],
   "Technology and simple devices for the parent": ["Find an easy radio so mom sleeps with music", "Find an easy-to-use flashlight for mom", "Find trustworthy human-made YouTube channels for mom", "Help parents learn to use their phones", "Teach mom to handle tech on her own", "Shield dad from spam that triggers his anxiety", "filter unwanted content on dad's social media"],
   "End-of-life plans and wishes": ["Decide his resuscitation level of care", "Know parents' burial and end-of-life wishes", "learn mom's burial and end-of-life wishes", "get mom's final wishes settled", "Plan her father's funeral"],
   "Equipment, hygiene and hands-on care": ["Find equipment to turn and clean bedbound dad", "Get oxygen equipment that gives her more mobility", "get urine smell out of laundry quickly and cheaply", "heal mother's wound", "Manage shopping trips with a wheelchair user"],
   "Hold a facility to account and stay in touch with them": ["Hold nursing home accountable for mom's care", "Stop her clothes going missing in rehab", "Reach mom by phone at memory care", "Keep a say in where she lives"],
   "Family roles and costs": ["Plan future care and family roles together", "siblings share parents' costs in a steady system", "Stop relatives adding calls, visits and demands", "get dad's partner to follow the care plan"]},
 ('Audience 1: parent','L'): {
   "Protect their own marriage, children and family": ["Keep intimacy and her marriage healthy", "Keep private time with husband and protect marriage", "Protect new marriage and the plan to move out", "Protect own marriage and the family she created", "Start a family of her own", "be a present mother to own kids", "keep own marriage and care for own young kids", "shield own husband and kids from caregiving burden", "Peaceful home for son and start dating again"],
   "Not be alone, and be seen": ["Feel less alone and get support", "Not be left alone without support", "company and not feeling alone", "recognition for own caregiving work", "Leave home and be seen by family"],
   "A life and a home after caregiving": ["Figure out life after caregiving ends", "Never be an unpaid caregiver again", "afford a place of my own", "keep a place to live after mom dies"]},
 ('Audience 2: spouse or partner','L'): {
   "Companionship, intimacy and someone who understands": ["A partner who can also support him", "Be seen and understood by partner", "Find a friend in a similar situation to talk", "Find peers their own age who get it", "Get affection back and save the marriage", "Have a future and progress as a couple", "companionship, dating and sex", "get own needs for intimacy and affection met", "not feel alone in the marriage", "someone to talk to about it", "someone who understands to talk to"]},
}
out = {}
for aud, v in C.items():
    for k, items in v['new'].items():
        groups = G.get((aud, k), {}); res = {g: 0 for g in groups}; left = []
        for it in items:
            g = [name for name, keys in groups.items() if it in keys]
            if len(g) == 1: res[g[0]] += 1
            else: left.append(it)
        res['Other one-offs'] = len(left)
        out[f'{aud}|{k}'] = {'groups': res, 'one_offs': left, 'total': len(items)}
        print(aud, k, res)
json.dump(out, open('new-groups.json', 'w'), indent=1, ensure_ascii=False)
