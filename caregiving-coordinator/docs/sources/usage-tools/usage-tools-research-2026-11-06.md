# Seeing Claude usage: sources read 2026-11-06

Question: how can the owner see plan usage and context without typing a command, on the Mac desktop app, and does it still work on an Enterprise plan?

## Official (Anthropic)
- Usage and length limits: https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work. Current session and weekly resets are shown in Settings > Usage (https://claude.ai/settings/usage).
- Usage limit best practices: https://support.claude.com/en/articles/9797557-usage-limit-best-practices. On Pro, Max, Ultra, Team or seat-based Enterprise, the usage page shows how much of the plan limit is used. On a usage-based Enterprise plan there are no specific usage limits; consumption is billed and can be tracked in Settings > Usage.
- What is the Enterprise plan: https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan. Usage-based Enterprise has no plan or seat-level usage limits. Seat-based Enterprise (Standard and Premium seats) has limits.
- Usage analytics for Team and Enterprise: https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans. On usage-based Enterprise, members can see their own usage in Settings > Usage when the admin turns on individual usage analytics.
- Claude Code status line docs: https://code.claude.com/docs/en/statusline (full copy: `claude-code-statusline-docs.md`). A status line script receives `context_window.used_percentage` and `rate_limits.five_hour` / `seven_day` as JSON. `rate_limits` "appears only for claude.ai Pro, Max, and Ultra subscribers, or behind a Claude apps gateway that sets a spend limit", and only after the first API response. The docs do not say whether the desktop app draws the status line.

## Open-source tools (GitHub metadata from `gh api`, 2026-11-06)
| Repo | Type | Stars | License | Last push | Open issues |
|---|---|---|---|---|---|
| hamed-elfayome/Claude-Usage-Tracker | Mac menu bar app | 3,751 | MIT | 2026-08-31 | 68 |
| danielmackay/claude-code-statusline | status line script | 111 | none listed | 2026-10-25 | 5 |
| pchalasani/claude-code-tools | status line + tools | 2,030 | MIT | 2026-11-06 | 18 |
| ccusage/ccusage | reads local logs | 19,345 | not stated | 2026-11-06 | 11 |

Menu bar app README (https://github.com/hamed-elfayome/Claude-Usage-Tracker): signs in with Claude Code's CLI credentials, a browser sign-in, or a `sessionKey` cookie pasted from claude.ai. Says credentials are kept in the macOS Keychain and that it sends a version-only anonymous heartbeat. Its code was NOT audited here.
