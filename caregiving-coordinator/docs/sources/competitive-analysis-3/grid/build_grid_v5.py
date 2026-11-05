"""Competitive Analysis 3 grid VERSION 5 and business table VERSION 4 (2026-11-05, owner-approved).
Version 4 with four VA cells fixed. Three claims rested on one caregiver's post each, and the
"doesn't do well" cell had two weak parts (about 3 posts, and 5 posts that may not be about the VA).
Every claim left is backed by the VA's own pages or by a theme across many posts. Reasons:
docs/sources/competitive-analysis-3/va-check/va-cells-change-2026-11-05.md.
Older files are not rewritten: file writes are switched off while versions 2, 3 and 4 run.
Writes grid-v5.json and business-v4.json only."""
import json, pathlib, io, contextlib, builtins
H = pathlib.Path(__file__).parent
_open = builtins.open
def _read_only_open(f, mode="r", *a, **k):  # older versions' writes go nowhere, so their files stay unchanged
    return io.StringIO() if any(m in mode for m in "wax+") else _open(f, mode, *a, **k)
v4 = {"__file__": str(H / "build_grid_v4.py"), "open": _read_only_open}
builtins.open = _read_only_open
try:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(_open(H / "build_grid_v4.py").read(), v4)
finally:
    builtins.open = _open
_dump = json.dump
G, BG, VAP = v4["G"], v4["BG"], v4["VAP"]
verify, COLS, BCOLS = v4["v3"]["verify"], v4["v3"]["COLS"], v4["v3"]["BCOLS"]
V = "VA caregiver programs"
# What it doesn't do well: keep only the strong theme (14 of 45 VA posts), with facts from the VA's page
G[V][6] = ("Strict rules to qualify: the veteran needs a 70% or higher disability rating, and the veteran and caregiver must apply together.",
           [("rc", "va", "hard application or eligibility rules"),
            ("q", VAP, "The Veteran has a VA disability rating (individual or combined) of 70% or higher"),
            ("q", VAP, "You and the Veteran will need to apply together")])
# Help with money and papers: one-post claim removed; "stipend" said in plain words
G[V][10] = ("Partly: free legal and financial planning and a monthly payment.",
            [("q", VAP, "Free legal and financial planning assistance"), ("q", VAP, "A monthly stipend (payment).")])
# Customer experience: one-post claim removed
BG[V][3] = ("Local caregiver support teams and a weekday phone line.",
            [("q", VAP, "Monday through Friday, 8:00 a.m. to 8:00 p.m. ET"),
             ("q", VAP, "Discuss your options with a caregiver support team at your nearest VA facility")])
# Getting started: one-post claim removed
BG[V][4] = ("The veteran and caregiver apply together online, by mail or in person.",
            [("q", VAP, "You can apply online, by mail, or in person."), ("q", VAP, "You and the Veteran will need to apply together")])
verify(G, COLS, "grid v5"); verify(BG, BCOLS, "business")
_dump({"columns": COLS, "rows": {k: [c[0] for c in v] for k, v in G.items()}, "sources": {k: [c[1] for c in v] for k, v in G.items()}}, open(H / "grid-v5.json", "w"), indent=1, ensure_ascii=False)
_dump({"columns": BCOLS, "rows": {k: [c[0] for c in v] for k, v in BG.items()}, "sources": {k: [c[1] for c in v] for k, v in BG.items()}}, open(H / "business-v4.json", "w"), indent=1, ensure_ascii=False)
