import re
NAMES={
 'Care.com': r'\bcare\.com\b|\bcare dot com\b',
 'Home Instead': r'\bhome instead\b',
 'Visiting Angels': r'\bvisiting angels?\b',
 'Senior Helpers': r'\bsenior helpers?\b',
 'Right at Home': r'\bright at home\b',
 'Comfort Keepers': r'\bcomfort keepers?\b',
 'Papa': r'\bjoinpapa\b|\bpapa pals?\b|\bpapa (app|inc|health|care|companion|caregiver)\b|\bpapa\.com\b|\bPapa\b(?=[^\n]{0,60}\b(companion|pal|app|company|service|medicare|helps? with)\b)',
 'BetterHelp': r'\bbetter ?help\b',
 'Talkspace': r'\btalk ?space\b',
 'Headway': r'\bheadway\b',
 'Psychology Today': r'\bpsychology today\b|\bpsychologytoday\b',
 'SonderMind': r'\bsonder ?mind\b',
 'Zencare': r'\bzencare\b',
 'Open Path': r'\bopen ?path\b',
}
C={k:re.compile(v,re.I if k!='Papa' else 0) for k,v in NAMES.items()}
# Papa: case-insensitive for explicit forms, capital-P for loose form handled by flags below
