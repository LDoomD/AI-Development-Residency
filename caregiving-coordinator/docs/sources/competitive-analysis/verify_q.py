"""Check every quote in extract-q-*.json is an exact substring (whitespace collapsed) of its saved file and at most 300 characters."""
import json, re, sys, pathlib
SRC = pathlib.Path(__file__).parent.parent
ws = lambda s: re.sub(r"\s+", " ", s).strip()
bad = 0; n = 0
for f in sys.argv[1:]:
    for r in json.load(open(f)):
        for fld, qs in r["fields"].items():
            for q in qs:
                n += 1; p = SRC / q["file"]
                ok = p.exists() and ws(q["quote"]) in ws(p.read_text(errors="ignore")) and len(q["quote"]) <= 300
                if not ok: bad += 1; print("FAIL", r["company"], fld, q["file"], q["quote"][:70])
print(n, "quotes checked,", bad, "failures")
