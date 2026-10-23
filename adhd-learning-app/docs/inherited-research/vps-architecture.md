# VPS Architecture

**Status:** research complete, verified against primary docs where possible
**Date:** 2026-08-08
**Context:** Orlando now has an always-on Linux VPS, a Claude Max subscription, Google
One AI Pro (Gemini + NotebookLM), a Google account, and an iPhone. Already decided and
not re-litigated here: Obsidian (plain Markdown) for notes, Anki for the review queue,
Claude as the generator. Google Drive connector is tested and works from Claude Code.
NotebookLM has no public API.

**Adherence constraint carried through every answer below:** reminder/notification
nudges FAILED in an ADHD RCT (Nordby et al. 2022, N=109) — nothing here proposes a
notification-based fix. Commitment and social mechanisms are what showed effect
instead, and none of the tools below have a commitment-device analog built in.

**Grading key:** `High — rely on as-is` / `Moderate — directional` /
`Extrapolated — tune by feel` / `Not covered`.

---

## Q1 — n8n on the VPS

**Answer.** Self-hosted n8n is free for this use under the Sustainable Use License —
verified against `docs.n8n.io/privacy-and-security/sustainable-use-license`: the only
prohibitions are white-labeling n8n for resale or hosting it as a paid service for
others, neither of which applies to a personal single-user instance. What always-on
genuinely unlocks: a webhook that receives phone captures and writes them into the
Obsidian inbox as Markdown, a scheduled job that batches new inbox notes and calls
Claude to generate structured study content, a workflow that pushes generated card
pairs into Anki via AnkiConnect or direct `.apkg` write, and a nightly git-commit of
the vault. What it does **not** solve: it isn't the generator (Claude is), isn't the
scheduler (Anki is), and building any notification/nudge workflow in it would just
reproduce the mechanism that already failed in the ADHD RCT — n8n is pipeline plumbing,
not an adherence fix.

**Docker setup** (verified, `docs.n8n.io/deploy/host-n8n/install-options/install-with-docker`):

```
docker volume create n8n_data
docker run -it --rm --name n8n -p 5678:5678 \
  -e GENERIC_TIMEZONE="<TZ>" -e TZ="<TZ>" \
  -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
  -e N8N_RUNNERS_ENABLED=true \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
```

Default port 5678, default DB SQLite (Postgres optional), data + auto-generated
encryption key persisted under `/home/node/.n8n`. The encryption key protects stored
credentials — losing the volume without a backup makes any stored credentials
unrecoverable, so the whole volume (not just workflow JSON exports) is the backup unit.

| Claim | Grade |
|---|---|
| Free under Sustainable Use License for personal use | High |
| Docker run/volume/port/SQLite defaults | High |
| Encryption key auto-generated, must be backed up with the volume | High |
| Concrete workflow ideas (capture→Obsidian, Claude trigger, Anki push) | Moderate |
| RAM/CPU footprint (official n8n spec page 404s; third-party estimates ~1–2GB RAM/1–2 vCPU) | Extrapolated |
| Failure modes (image-upgrade breakage, SQLite lock under load, lost key, silent restart failure without `--restart unless-stopped`) | Moderate |
| No adherence value; notification workflows repeat the failed RCT mechanism | High |

**Backup:** tar/snapshot the `n8n_data` volume on the same cron as the vault backup.
**Cost:** $0 recurring.

---

## Q2 — Phone capture

**Answer.** Apple Shortcuts → webhook POST to n8n, triggered from the iPhone **Action
Button** (or Home Screen icon fallback) with Siri dictation filling the body, is a true
2-step path (press → speak) with no app switch — the only option under the "≤2-3 taps
or it doesn't get used" bar. Telegram bot → n8n webhook is the resilient second choice
(3-4 steps: unlock → open Telegram → speak/type → send) and should be built as backup,
not primary: if the Shortcut POST fails silently, a Telegram message still lands safely
on Telegram's servers until a recovery job picks it up. Email/IMAP-poll and a watched
Drive folder are both worse at the capture moment (poll lag, more UI) — keep them, if
at all, as desktop-capture channels, not lot-capture channels.

| Method | Steps to capture | Reliability | Latency | Setup |
|---|---|---|---|---|
| **Shortcuts → webhook (Action Button)** | 2 (press, speak) | High if VPS/n8n up; fails silently without explicit retry handling in the shortcut | Sub-second–few sec | Low-moderate |
| **Telegram bot → n8n webhook** | 3-4 | High — Telegram's `setWebhook` pushes an HTTPS POST of the JSON Update on receipt, no polling | 1-3 sec | Low |
| **Email → IMAP poll** | 4-5 | Moderate — poll-interval bound, silent failure if the poll job dies | 1-5 min | Moderate |
| **Watched Drive folder** | 4-5 | Moderate — Drive sync reliable, but VPS-side watching is poll-based for consumer accounts | ~1 min+ | Moderate-high |

Verified: Telegram Bot API's `setWebhook` push mechanism (`core.telegram.org/bots/api`,
fetched directly) — **High**. Apple's own Shortcuts guide pages did not return
fetchable body content in three attempts (TOC only) — the HTTP-POST/JSON-body
capability of "Get Contents of URL" is well-documented across the ecosystem and has
shipped since iOS 13, but per this project's verification standard it is marked
**UNVERIFIED against primary source this pass** — confirm on-device before relying on
it. Action Button/Home Screen/Siri as trigger surfaces: confirmed present in Apple's
guide TOC, exact tap-count not confirmed — **Moderate**. IMAP/Drive poll latency:
**Extrapolated**, generic polling behavior, not fetched from n8n's own node docs.

**Recommendation:** build both — Shortcuts as the primary reflex action, Telegram as
the belt-and-suspenders channel. **Cost:** $0 recurring.

---

## Q3 — Anki sync server

**Answer.** Confirmed: Anki ships an official self-hostable sync server (source in the
main `ankitects/anki` repo, docs at `docs.ankiweb.net/sync-server.html`), and both
AnkiDroid and AnkiMobile (iOS) can point at it. It replaces **collection + media sync**
only — Shared Decks browsing/uploading stays a separate AnkiWeb website feature,
untouched by self-hosting. For Orlando's actual goal (review queue on phone, no
third party), the self-hosted server covers exactly what's needed.

| Item | Detail | Grade |
|---|---|---|
| Install | Bundled with packaged Anki 2.1.57+, `pip install anki`, `cargo install`, or Docker (no official prebuilt image — build from `docs/syncserver/` Dockerfile, or use community images) | High |
| Config | Env vars: `SYNC_USER1=user:pass` (required), `SYNC_BASE` (default `~/.syncserver`), `SYNC_HOST`/`SYNC_PORT`, `MAX_SYNC_PAYLOAD_MEGS` (100MB default) | High |
| Protocol | Unencrypted HTTP by design — docs explicitly warn against exposing directly to the internet; use a VPN (Tailscale suggested) or TLS reverse proxy | High |
| iOS caveat | AnkiMobile requires **TLS 1.2** specifically (TLS 1.3 breaks it — error `-9836`) if fronted by a reverse proxy | High |
| AnkiDroid support | Settings → Advanced → Custom Sync Server; pre-2.16 needed separate collection/media endpoint URLs, 2.16+ unified | High |
| AnkiMobile support | Settings → Synchronization → Custom Sync Server (since ~2.0.90); confirmed via the sync-server doc + maintainer forum posts, not the dedicated AnkiMobile manual page itself | Moderate |
| Does it replace all of AnkiWeb? | No — Shared Decks browsing/uploading and AnkiWeb's browser-based review UI are not replicated | High |
| Failure mode | Client/server protocol version mismatch is the primary one — server must be upgraded in lockstep with clients | High |
| Resource footprint | No official numbers published; architecture (flat-file storage, no DB server) implies it's light | Extrapolated |
| Behavior on brief VPS outage | Not explicitly documented; inferred as opportunistic sync (local collection keeps working, retries later) — same shape as AnkiWeb | Extrapolated |

**Backup:** snapshot the `SYNC_BASE`/data directory directly (it's the authoritative
copy) — docs explicitly warn not to hand-edit it. **Cost:** $0 recurring (AnkiMobile's
~$25 one-time purchase is unrelated to sync-server choice, not verified this pass).

---

## Q4 — Scheduled Claude agents on the VPS (critical question)

**Answer.** Yes — `claude -p` (headless/print mode) can run under a Claude Max/Pro OAuth
subscription on a Linux VPS with no browser, and this is officially documented, not a
workaround. Default (non-`--bare`) `-p` uses whatever subscription credentials are
already in `~/.claude/.credentials.json`; Anthropic ships `claude setup-token`
specifically for headless auth — a one-year OAuth token meant for "CI pipelines,
scripts, or other environments where interactive browser login isn't available."
API-key billing only kicks in if `ANTHROPIC_API_KEY` is explicitly set, or if `--bare`
mode is used (which never reads OAuth credentials at all — avoid `--bare`).

**No-browser auth flow, confirmed from `docs.claude.com/en/docs/claude-code/authentication`:**
1. SSH into the VPS, run `claude setup-token`.
2. It prints a login URL — open it on any other device (your laptop; it needs no
   network path to the VPS).
3. Complete login on claude.ai there; since it can't reach the VPS's local callback
   server, the page shows a code.
4. Paste that code into the SSH terminal.
5. The long-lived token prints to terminal — `export CLAUDE_CODE_OAUTH_TOKEN=...` in
   the cron/service environment. Prefer this over relying on `/login`'s session, which
   is short-lived and subject to the refresh issue below.

**Known reliability caveats** (community/GitHub issues on `anthropics/claude-code`,
lower trust than the docs, resolution status not independently confirmed):
- Issue reports of OAuth **access-token refresh failing in scripted/looped invocations**
  after ~10-15 min — argues for `setup-token`'s long-lived token over relying on
  `/login` session refresh for cron jobs.
- Issue reports of `-p` with OAuth **billing against the API/Console dashboard instead
  of Max subscription quota** for some users — status unclear, treat as unresolved risk
  and watch the Max usage dashboard (not just the API console) after deployment.
- A secondary news source states Anthropic's ban on subscription-OAuth for third-party
  "Sign in with Claude" products explicitly **exempts Claude Code itself** — this
  wasn't verified against Anthropic's primary Usage Policy/Consumer Terms text; read
  those directly (`anthropic.com/legal/consumer-terms`, `anthropic.com/legal/aup`)
  before treating fully unattended automation as ToS-safe long-term.

| Claim | Grade |
|---|---|
| `-p` uses subscription OAuth by default (not API key) unless `ANTHROPIC_API_KEY` set or `--bare` used | High |
| `claude setup-token` no-browser flow, one-year token | High |
| OAuth refresh flakiness in long-running loops | Moderate (community-sourced) |
| Billing-routing bug (Max usage billed as API usage) | Moderate — unverified fix status |
| ToS-safe for automated/scripted use | Not covered — only a secondary source checked |

**Overall grade: Moderate — directional.** The mechanism is real and documented;
deploy it, but use `setup-token`, monitor the Max dashboard after go-live, and read the
primary ToS text before leaning on this for a fully unattended long-term setup.

---

## Q5 — Obsidian vault sync via the VPS

**Answer.** Run a bare git remote on the VPS as source of truth, with **Working Copy**
(native iOS git client) for pull/read and manual push from the phone. Do not use Google
Drive or Syncthing as the primary path. Obsidian's own docs state directly: **"Google
Drive is not officially supported for syncing Obsidian vaults on iOS"** and warn against
syncing the same vault across multiple services to avoid conflicts/corruption
(`obsidian.md/help`, fetched directly — **High**). Syncthing has **no official iOS
app** — only third-party BEP clients (e.g. Möbius Sync, paid), and sync only runs while
foregrounded, not truly in the background.

| Option | iOS story | Setup | Reliability | Cost | Grade |
|---|---|---|---|---|---|
| **(a) Bare git remote on VPS** | Obsidian Git plugin's mobile support is officially called "very unstable, not recommended" by its own README; real path is Working Copy mirrored into the vault folder, manual/Shortcuts-triggered, manual conflict resolution | High effort once (SSH keys, Working Copy pairing) | Manual-trigger reliability — a "remember to sync" tax, no smart merge | Working Copy Pro: one-time $19.99–35.99 IAP | High |
| **(b) Syncthing** | No official iOS app; third-party clients only, foreground-only sync | Moderate on VPS+desktop, weak on iOS | Degraded specifically on the iOS leg | Third-party iOS client is paid, unverified exact price | Moderate |
| **(c) Google Drive** | Explicitly unsupported by Obsidian on iOS; free plugin path ("Google Drive Sync"/OGD Sync) is BRAT-only beta, not in the official directory; the maintained plugin (Remotely Save) put Google Drive behind a paid PRO tier in 2026 | Low-moderate but built on unofficial/beta software | Unsupported, highest conflict risk of the three | Remotely Save Drive tier is a recurring cost if used | Moderate (cost claim: High, fetched directly) |

**Recommendation:** (a), with (c)'s Drive-app-plus-manual-export as a low-effort
fallback if git friction proves too high in practice. **Cost:** $0 recurring for (a);
avoid the paid Drive-plugin tier in (c) if used as a fallback.

---

## Q6 — NotebookLM automation, reconsidered

**Answer.** Still not worth it, even with the VPS's better risk profile. Isolating the
automation on the VPS with a dedicated throwaway Google account genuinely eliminates the
original objection (leaking Orlando's primary account's Gmail/Calendar/Workspace
cookies) — that risk drops close to zero. But a different risk replaces it: this is
still unofficial automation of a Google consumer product with no public API
(`policies.google.com/terms`, fetched directly — prohibits automated/bot access without
permission and reserves the right to suspend/terminate accounts for repeated breach —
**High**), done via Patchright, a browser stack purpose-built to evade Google's bot
detection — which strengthens rather than weakens the ToS-violation read. Once
isolated, the downside is bounded to losing the throwaway account, which is real but
low-cost. The upside is thin: NotebookLM already works fine manually as a drag-and-drop
surface — the standing decision elsewhere in this project — so the automation buys a
few saved clicks in exchange for ongoing maintenance debt every time Google changes the
NotebookLM UI and breaks the scraper.

| Claim | Grade |
|---|---|
| No public NotebookLM consumer API (separate paid Enterprise API exists, not usable here) | High |
| Google ToS bars automated/bot access, allows account suspension for repeat breach | High |
| Stealth automation strengthens the ToS-violation read (built specifically to evade detection) | Moderate |
| VPS + throwaway account bounds blast radius to that one account | High |
| Manual alternative already exists and costs only a few extra clicks | High |

**Verdict: do not automate.** Revisit only if Google ships an official API.
**Cost:** $0 either way — this is a build/don't-build call, not a bill.

---

## Q7 — Security baseline

**Answer.** Proportionate for a single-user personal box, not enterprise hardening:
SSH key-only auth (disable password auth), ufw with default-deny-incoming plus explicit
allow rules, fail2ban on the SSH jail, unattended-upgrades for patching, Docker
rootless for any containers (n8n), secrets in a `chmod 600` env file rather than a
secrets manager, and automated encrypted off-box backups that are actually restore-tested
at least once. No SIEM, no IDS stack, no MFA-gated VPN layer — disproportionate for one
person's notes.

| Component | Verified detail | Grade |
|---|---|---|
| SSH keys | Ubuntu docs confirm ed25519 key-based auth setup replacing passwords | High |
| Disable password auth | Standard `PasswordAuthentication no` in `sshd_config` — not confirmed on the specific fetched Ubuntu page | Moderate |
| ufw | `ufw enable`, `ufw allow ssh`, default-deny incoming/allow outgoing (Ubuntu Community doc, fetched) | High |
| unattended-upgrades | `apt-get install unattended-upgrades`, `dpkg-reconfigure --priority=low unattended-upgrades`; auto-reboot requires explicit opt-in | High |
| Docker rootless | Runs daemon/containers in a user namespace, no root — Docker's own docs confirm purpose and install command | High |
| Docker rootless limitations (e.g. ports <1024) | Not retrievable from the fetched page this pass | Not covered |
| fail2ban SSH jail | Consistent config pattern across third-party tutorials; official wiki content didn't load this pass | Moderate |
| Secrets in `chmod 600` env file, no secrets manager needed | Standard practice, not a doc citation | Extrapolated |
| Backup strategy (tar + off-box + encrypt + restore-test) | Reasoning, not a doc citation | Extrapolated |

**Cost:** $0 for all tooling above; the only possible recurring cost is off-box backup
storage if cloud object storage is chosen over a second physical machine.

---

## Q8 — What should NOT go on the VPS

**Answer.** Put only what genuinely needs to be reachable from outside Orlando's own
devices, at any hour, on the VPS: the capture webhook receiver (n8n), the Obsidian git
remote, and the Anki sync server. Everything else is a judgment call against one test:
**does this need to answer at 2am from a car lot, or does it only need to run when
Orlando is already at a keyboard?** If the latter, it stays local/manual.

| Candidate | Verdict | Why |
|---|---|---|
| n8n (capture receiver) | **VPS** | Structurally needs always-on reachability — that's the entire point of Q2's capture path |
| Obsidian git remote | **VPS** | Needs to be reachable for phone sync; costs nothing extra to host alongside the above |
| Anki sync server | **VPS** | Same reachability argument; verified in Q3 to be low-footprint and low-maintenance |
| Scheduled Claude agent runs | **VPS, conditionally** | Only if Q4's OAuth-headless path is deployed with `setup-token` and the Max-usage dashboard is monitored — a broken unattended cron job nobody watches is worse than no automation |
| NotebookLM browser automation | **Do NOT put on VPS — do not build at all** | Highest blast radius (ToS violation, account risk) and highest rot rate (breaks on every Google UI change) of any candidate; doesn't need always-on since it's already a manual surface by standing decision |

---

## Build order

1. **VPS hardening first** (Q7) — SSH keys, ufw, fail2ban, unattended-upgrades, Docker
   rootless. Nothing else goes on an unhardened box.
2. **Anki sync server** (Q3) — smallest footprint, clearest win (review queue on phone,
   no AnkiWeb), lowest risk.
3. **Obsidian git remote + Working Copy** (Q5) — vault on phone, no paid Sync tier.
4. **n8n + phone capture webhook** (Q1, Q2) — Shortcuts→webhook primary, Telegram
   fallback. This is the piece that actually changes daily behavior.
5. **Scheduled Claude agents** (Q4) — only after `setup-token` auth is confirmed working
   reliably in a short-lived test loop and the Max usage dashboard is being watched.

## Do not build

- **NotebookLM browser automation** — stealth ToS-violating scraper for marginal
  convenience over an already-working manual surface. Revisit only if Google ships an
  official API.
- **Any notification/reminder-based adherence feature**, on or off the VPS — the
  specific intervention already failed in an ADHD RCT (N=109). If a social/commitment
  mechanism is wanted later, it has to be designed from scratch; none of the tools here
  (n8n, Obsidian, Anki) have one built in.
- **Syncthing for the vault** — no official iOS client exists; not worth the VPS+desktop
  leg's quality when the phone leg is structurally weak.
- **Google Drive as the primary vault sync path** — Obsidian's own docs say iOS support
  is unsupported; the free plugin path is beta-only, the maintained one is now paywalled.
