"""Add the question columns (the template's three questions plus the niche ones) to the ten-row table. Company quotes come from extract-q-A/B.json (checked by verify_q.py);
review quotes come from caregiving-only reviews (review-evidence-q.json). Workaround rows are marked not applicable or not assessed. Nothing typed by hand except labels."""
import json, pathlib, re
HERE = pathlib.Path(__file__).parent
rows = json.load(open(HERE / "table-rows-10.json"))
ext = {r["company"]: r for f in ("extract-q-A.json", "extract-q-B.json") for r in json.load(open(HERE / f))}
rev = json.load(open(HERE / "review-evidence-q.json"))
man = json.load(open(HERE.parent / "competitive-analysis/manifest.json"))
vu = json.load(open(HERE / "urls.json")); url = {k: v["url"] for k, v in vu.items() if v.get("url")}
cut = lambda s, n=200: (lambda s: s if len(s) <= n else s[:n].rstrip() + "...")(re.sub(r"\s+", " ", s).strip())
NF = "Not found in the saved pages"
COLS = [  # (header, fields, review key)
 ("What is their business model? How do they make money?", ["business_model"], None),
 ("How do they retain customers?", ["retention"], "cost_cancel"),
 ("How do they approach their customer experience (company's own words)?", ["customer_experience"], None),
 ("Who uses it and who pays?", ["who_pays"], None),
 ("Can a second or third relative join without the account holder handing over a login?", ["second_person_access"], None),
 ("How does it treat health data and consent: who sees what, and how is a person removed?", ["health_data_consent"], None),
 ("What happens when it fails in an emergency, and how does support respond?", ["emergency_support"], "emergency"),
 ("What does setup take, who does it, and does it work on the phones the family already has?", ["setup"], "setup"),
]
DROPQ = [  # (company, field, quote prefix): weak or off-topic, dropped from the cells (logged in questions-drop-log.txt)
 ("Lively","health_data_consent","Consumer Health Data Privacy Statement"),
 ("Medical Guardian","health_data_consent","By leaving this box unchecked"),
 ("Medical Guardian","business_model","Partners Dealers Healthcare"),
 ("Everplans","retention","Let our smart planning system"),
 ("Everplans","emergency_support","If we discover a security incident"),
 ("Everplans","emergency_support","With your explicit permission, the Unlocker"),
]
dropped = []
for r_ in ext.values():
    for f_, qs_ in r_["fields"].items():
        keep_ = []
        for q_ in qs_:
            if any(r_["company"] == c_ and f_ == ff_ and q_["quote"].startswith(pp_) for c_, ff_, pp_ in DROPQ): dropped.append(f"{r_['company']} / {f_}: {q_['quote'][:90]}")
            else: keep_.append(q_)
        r_["fields"][f_] = keep_
(HERE / "questions-drop-log.txt").write_text("\n".join(dropped) + "\n")
WORK = {"Group texts", "Paper notebook and visit log"}
hdr = [c[0] for c in COLS] + ["Sources for the question columns (links and saved files)"]
out = []
for r in rows:
    co = r[0]; new = []; srcs = []
    for h, flds, rk in COLS:
        if co in WORK:
            new.append("Not applicable (not a company)" if rk is None or rk == "cost_cancel" else "Not assessed"); continue
        parts = []
        for f in flds:
            for q in ext[co]["fields"].get(f, [])[:2]:
                parts.append("• \"" + cut(q["quote"]) + "\"")
                u = url.get(q["file"], "page link not verified"); t = f"{u} [{q['file'].split('/',1)[1]}]"
                if t not in srcs: srcs.append(t)
        if rk:
            rv = sorted(rev.get(co, {}).get(rk, []), key=lambda x: -len(x["quote"]))[:2 if rk == "emergency" else 1]
            label = "Review signal (price or cancelling)" if rk == "cost_cancel" else "Reviews (problems, caregiving-only)"
            for x in rv: parts.append(f"• {label}: \"{cut(x['quote'],170)}\" (review {x['id']})")
        new.append("\n".join(parts) if parts else NF)
    new.append("; ".join(srcs[:5]) + (f"; +{len(srcs)-5} more in extract-q-A.json / extract-q-B.json" if len(srcs) > 5 else "") if srcs else "Not applicable" if co in WORK else NF)
    out.append(r + new)
json.dump({"headers": hdr, "rows": out}, open(HERE / "table-rows-10q.json", "w"), ensure_ascii=False)
print(len(out), "rows x", len(out[0]), "cols; longest new cell", max(len(c) for r in out for c in r[14:]))
for r in out[:1]+out[6:7]:
    print(r[0]); [print(" ", i, repr(c[:230])) for i, c in enumerate(r[14:])]
