# Phone-based engagement mechanisms — non-notification options

**Date:** 2026-10-24
**Why this exists:** push notifications are already locked-rejected in the
inherited research (`docs/inherited-research/DECISIONS.md` §4 — failed in an
ADHD RCT, Nordby et al. 2022, n=109). This project's queued but unresearched
idea was a "habit-stack trigger ... never a notification"
(`DECISIONS.md` §11, item 2). This doc researches what that could actually be,
constrained to what a **responsive web app on Vercel/Supabase** can build in
about a week — no native app is in the mandated stack.

---

## 1. Habit-stack / implementation-intention theory

The general mechanism is well evidenced — Gollwitzer & Sheeran (2006),
d ≈ 0.65. **For ADHD specifically, the supporting studies (Gawrilow &
Gollwitzer) are in children, not adults**, and no study tested delivery via
phone specifically. Applying it to adult ADHD learners is a reasoned
extrapolation from adjacent evidence, not a direct finding — label it that
way wherever it's cited.

## 2. What a PWA can actually do in this stack

| Capability | Feasible here? |
|---|---|
| Home-screen install ("Add to Home Screen") | Yes — trivial, do this |
| Badging API | Partial — iOS 16.4+ only, **not supported on Android Chrome**. Don't rely on it |
| Web Speech API (voice capture) | Yes — single-utterance mode, cross-platform |
| `.ics` calendar export / "Add to Calendar" link | Yes — trivial, zero risk |
| Geofencing / location triggers | **Not available to web apps at all** — do not propose |
| Background sync / periodic fetch | Not supported on Safari — skip |
| Offline cache persistence | iOS evicts cache after ~7 days unopened — real constraint on any offline plan |

## 3. Phone as a capture device, not a delivery channel

Voice-to-text note capture is cheap and safe to build (Web Speech API), but
the claim that "speaking lowers ADHD task-initiation friction" only turns up
in commercial-app marketing blogs — **no peer-reviewed source found.** Build
it as a UX bet, not as an evidence-backed adherence mechanism.

## 4. Rejected-mechanism trojan horses — watch for these

These sound new on mobile but are mechanisms this project has already killed,
wearing a different costume:

- **Badge counts** ("3 overdue") — loss-aversion/gamification in disguise.
- **App-pushed recurring calendar alerts** — a notification with a calendar
  costume.
- **Streak badges** — straight gamification, already rejected.
- **Location-based study triggers** — not buildable on web anyway, and still
  external control rather than self-regulation.

## 5. Four mechanisms that are buildable now and don't violate a locked decision

1. **Self-authored if-then plan widget** — "After I ___, I open a practice
   session." A static dashboard artifact the student writes themselves; the
   app never pushes it at them.
2. **One-tap voice capture for notes** — Web Speech API, single-utterance,
   cross-platform.
3. **"Add to Home Screen" prompt** — the icon itself is the environmental
   cue. No extra trigger logic needed.
4. **Student-generated `.ics` export of their own plan** — one-time,
   student-initiated, never app-pushed or recurring.

## Open question this doc does not resolve

None of this has been tested with the actual target population (no real
daily user exists during the residency window, per `STATUS.md`). These are
evidence-consistent and buildable, not validated for this specific product.
