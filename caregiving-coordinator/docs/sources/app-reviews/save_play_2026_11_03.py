"""Save Google Play reviews copied from the built-in browser on 2026-11-03 (feature analysis gap fill).
Usage: python3 save_play_2026_11_03.py <slug> <app name> <package> <note> < reviews.json
Writes google-play/google-play-reviews-<slug>.json in the same shape as the 2026-11-02 files. Reviewer names are not collected."""
import json, sys, pathlib
slug, app, pkg, note = sys.argv[1:5]
revs = json.load(sys.stdin)
out = {"app": app, "package": pkg, "store": "Google Play US (en_US)", "collected": "2026-11-03",
       "source_url": f"https://play.google.com/store/apps/details?id={pkg}&hl=en_US&gl=US",
       "note": note, "count": len(revs), "reviews": revs}
p = pathlib.Path(__file__).parent / "google-play" / f"google-play-reviews-{slug}.json"
p.write_text(json.dumps(out, ensure_ascii=False, indent=1)); print(p.name, len(revs))
