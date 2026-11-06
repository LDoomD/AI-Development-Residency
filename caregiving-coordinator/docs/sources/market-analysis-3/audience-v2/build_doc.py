"""Write docs/audience-teacher-format-2026-11-04.md from the same data used in Figma section 2623:76."""
import json, pathlib
H = pathlib.Path(__file__).parent; D = json.load(open(H / "figma-teacher-format.json"))
names = {"A1": "Audience 1: adult child caring for a parent", "A2": "Audience 2: spouse or partner caring for a husband, wife or partner"}
o = ["# Audience goals and use cases, teacher format (2026-11-04)", "",
     "Figma: section 2623:76 on the audience page (2378:7107). Built from 412 caregiver posts and threads: 303 Reddit posts (268 parent, 35 spouse) and 109 forum threads (55 parent, 54 spouse). Every list is most common first. Data and check scripts: `docs/sources/market-analysis-3/audience-v2/`.", ""]
for a in ("A1", "A2"):
    o += [f"## {names[a]}", ""]
    for k, v in D[a]["boxes"].items():
        o += [f"### {k.capitalize()}", ""] + [f"{i}. {s}" for i, s in enumerate(v, 1)] + [""]
    o += ["### Use cases that we should support", "", "| The problem | When it happens | What we want to change | Scenarios to support |", "|---|---|---|---|"]
    for i, r in enumerate(D[a]["rows"], 1):
        o.append(f"| **{i}. {r[0]}** Seen in {r[1]} posts and threads | " + " | ".join("<br>".join("• " + s for s in col) for col in r[2:]) + " |")
    o.append("")
o += ["## Limits", "", "- One reader marked each post, and no person double-checked it. People who post online tend to have harder problems.",
      "- Audience 2 has only 35 Reddit posts. 3 forum threads were filed under the wrong audience.",
      "- The scenarios are our own wording of what caregivers want: open problems, not features or decisions.",
      "- The box counts come from the earlier goals coding (269 Reddit parent posts, which includes one post that appears twice)."]
pathlib.Path(H.parents[2] / "audience-teacher-format-2026-11-04.md").write_text("\n".join(o) + "\n")
print("written")
