# Handoff hook misses

When you ask for a dog feeding / handoff report and the skill doesn't load, tell Claude "it didn't trigger". Claude adds a row here, adds the phrase to `dogfood-handoff-trigger.mjs`, adds it to `dogfood-handoff-trigger.test.mjs`, and runs `node --test .claude/hooks/dogfood-handoff-trigger.test.mjs`.

| Date | What you said (exact words) | Fired? | Fix |
|---|---|---|---|
| 2026-11-06 | "dock fitting report", "dog fitting report", "dark feeding report" (speech-to-text) | Fixed | Added to the hook |
| 2026-11-06 | "doc premium report", "dog cream report" (speech-to-text) | No | Too far from "dog feeding" to match safely. Add only if it keeps happening. |
