"""Compare Figma cell hashes (passed as JSON list) with a grid in a payload file. python3 -I hashcheck.py file key 'H-json'"""
import json, sys
d = json.load(open(sys.argv[1])); g = d[sys.argv[2]]; F = json.loads(sys.argv[3])
def h(s):
    b = s.encode('utf-16-le'); u = [int.from_bytes(b[i:i+2], 'little') for i in range(0, len(b), 2)]
    return sum(c*((i%7)+1) for i, c in enumerate(u)) % 1000000007
P = [h(v) for row in g for v in row]
print(len(P), len(F), 'mismatch', [divmod(i, len(g[0])) for i, (a, b) in enumerate(zip(P, F)) if a != b])
