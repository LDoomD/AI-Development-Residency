# BRIEF — VPS-hosted architecture for the ADHD Learning System

## Deliverable

Write your report to:
`/Users/landodoom/Desktop/VS Code_Projects/ADHD-Learning-System/specs/vps-architecture.md`

Read these first and stay consistent with them:
- `specs/build-plan.md` — stack decisions already made
- `specs/subjects.md` — the 20 subjects this must serve
- `specs/research/2026-08-08_knowledge-management-tools.md` — tool survey
- `specs/research/2026-08-08_spaced-repetition-tools-and-adherence.md` — what makes
  adherence work (competition works +11pp; reminders FAILED in an ADHD RCT, n=109)

## Context that changed

Orlando has a VPS (always-on Linux server). Every prior objection based on "his Mac is
closed most of the time" is void. He also has: Claude Max subscription, Google One AI Pro
(Gemini + NotebookLM), a Google account, and an iPhone.

Already decided and NOT up for re-litigation: Obsidian for notes (plain Markdown),
Anki for the review queue, Claude as the generator. Google Drive connector is tested
and works from Claude Code. NotebookLM has no public API.

## Questions to answer

1. **n8n on the VPS.** Now that always-on is real, what does it genuinely unlock for
   THIS system? Be concrete — name the actual workflows worth building, and be equally
   concrete about what it does NOT solve. Self-hosted n8n is free under the Sustainable
   Use License (verified). Cover Docker setup, resource footprint, backup, and how it
   breaks.
2. **Phone capture.** Orlando needs to capture a thought while standing on a dealership
   lot, one-handed. Compare the real options: Telegram bot → n8n webhook, email → IMAP
   poll, Apple Shortcuts → webhook, Drive folder. Which has the least friction at the
   moment of capture? Friction at capture is the whole game — an ADHD capture path that
   takes 4 taps is a capture path that doesn't get used.
3. **Anki sync server.** Anki ships a self-hosted sync server. Verify this, document how
   to run it on a VPS, and say whether it removes the need for AnkiWeb. This matters
   because it puts his review queue on his phone without a third party.
4. **Scheduled Claude agents on the VPS.** Can `claude -p` run headless on a Linux VPS
   under a Max subscription (OAuth), or does headless force an API key and therefore
   per-token billing? THIS IS THE CRITICAL QUESTION — verify it properly, do not guess.
   Check the Claude Code docs and the ruflo repo. If OAuth works headless, what is the
   auth flow on a box with no browser?
5. **Obsidian vault sync via the VPS.** Git remote on the VPS vs Syncthing vs Drive.
   Which gives him vault-on-iPhone without paying for Obsidian Sync? Note Obsidian's own
   warnings about cloud-sync conflicts.
6. **NotebookLM automation, reconsidered.** Earlier this was rejected because the
   community MCP servers use stealth browser automation with his primary Google account's
   cookies stored unencrypted. A VPS changes the blast radius: isolated box, dedicated
   throwaway Google account, no personal data on it. Reassess honestly — is that an
   acceptable risk profile or still not worth it? Give a clear recommendation with
   reasoning, and state what would be lost by simply not automating it.
7. **Security.** This box will hold his notes and possibly credentials. Baseline
   hardening: SSH keys only, firewall, fail2ban, unattended-upgrades, Docker rootless,
   secrets handling, backups. Keep it proportionate — this is a personal server, not a
   production fleet.
8. **What should NOT go on the VPS.** Argue the other side. Every service added is a
   thing that can rot. Name what genuinely belongs there and what is better left local
   or manual.

## Hard conditions

- **Verify before asserting.** Fetch the actual docs. Where you cannot verify, write
  UNVERIFIED explicitly. A previous pass in this project caught two fabricated citations.
- **Grade every claim:** `High — rely on as-is` / `Moderate — directional` /
  `Extrapolated — tune by feel` / `Not covered`.
- **Cost everything.** Orlando is not looking for a new monthly bill. Flag anything that
  adds one.
- **Respect the adherence evidence.** Do not propose reminder-based nudges as a solution;
  that specific intervention failed in an ADHD RCT. Commitment and social mechanisms are
  what showed effect.

## Style

Terse. Tables over prose. Lead with a one-paragraph answer. End with a concrete
recommended build order and an explicit "do not build this" list.
