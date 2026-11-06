# Wrap-up skill vs GitHub best practices (audit, 2026-11-06)

What was checked: the `wrap-up` skill (`.claude/skills/wrap-up/SKILL.md` at the repo root, commit 419cd57), compared with GitHub's own documentation and the Pro Git book, plus the live settings of `LDoomD/AI-Development-Residency`. Findings only. Nothing was changed.

Sources (saved copies in `docs/sources/github-practices/`, downloaded 2026-11-06 from the GitHub Docs article API):
- [GH-FLOW] GitHub flow, https://docs.github.com/en/get-started/using-github/github-flow (`github-flow.md`)
- [GH-REVIEW] Helping others review your changes, https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/helping-others-review-your-changes (`helping-others-review.md`)
- [GH-REPO] Best practices for repositories, https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories (`repo-best-practices.md`)
- [GH-MERGE] About merge methods on GitHub (`merge-methods.md`)
- [GH-PROTECT] About protected branches (`protected-branches.md`)
- [GH-PLANS] GitHub's plans (`github-plans.md`)
- [GH-SECRET] About secret scanning (`secret-scanning.md`); [GH-PUSHPROT] Push protection (`push-protection.md`)
- [GH-CI] About continuous integration (`about-ci.md`)
- [PRO-GIT] Pro Git, 2nd ed., "Contributing to a Project", Commit Guidelines, https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project (`git-book-contributing.html`)

## What the repo looks like today (observed 2026-11-06 with `gh api`)

| Setting | Value | Command |
|---|---|---|
| Visibility / owner | Private, personal account | `gh api repos/LDoomD/AI-Development-Residency` |
| Branch protection on `main` | None ("Branch not protected", 404) | `gh api repos/.../branches/main/protection` |
| Rulesets | None (`[]`) | `gh api repos/.../rulesets` |
| GitHub Actions workflows (automatic checks) | 0 | `gh api repos/.../actions/workflows` |
| Dependabot alerts | Off (404) | `gh api repos/.../vulnerability-alerts` |
| Secret scanning / push protection | Not reported (`security_and_analysis: null`) | `gh api repos/...` |
| Delete branch after merge | On | same |
| Merge methods allowed | Merge commit, squash, rebase | same |
| Last 6 PRs | 5 to 591 files each; #23 = 407 files, +272,967 lines | `gh pr list --state all -L 6` |

## Findings

| # | Practice (source) | Wrap-up skill today | Verdict | Evidence state |
|---|---|---|---|---|
| 1 | Short, descriptive branch names [GH-FLOW l.20] | Says to name the branch after the session's work | ✅ Meets | documented + observed (skill text) |
| 2 | Never work directly on `main`; branch, push, PR [GH-FLOW l.20-45] | Says so ("never a direct commit to main") | ✅ Meets, but not enforced (see #8) | observed |
| 3 | Descriptive commit messages [GH-FLOW l.30] | Follows repo style from `git log` | ✅ Meets | observed |
| 4 | Each commit is one isolated, complete change [GH-FLOW l.32; PRO-GIT "Commit Guidelines"] | Not mentioned; one wrap-up tends to make one big commit | ⚠️ Gap | inferred from skill text |
| 5 | A separate branch for each set of unrelated changes; small PRs [GH-FLOW l.39; GH-REVIEW l.11-15] | Reuses the open PR across sessions | ❌ Gap. PRs here hold weeks of mixed work (407 files in #23) | observed (`gh pr list`) |
| 6 | PR description says what changed, why, and where to look [GH-FLOW l.45; GH-REVIEW "Provide context"] | Not mentioned | ⚠️ Gap | observed (skill text) |
| 7 | Self-review before merge: read the diff, check for accidental changes, make sure builds/tests ran; security review [GH-REVIEW l.23-29] | Step 4b covers the diff, deletions, secrets, junk, description. It does not require running the project's tests | ⚠️ Mostly meets; tests missing | observed |
| 8 | Protect `main` with protected branches or rulesets [GH-REPO l.31; GH-PROTECT] | Not mentioned; `main` is unprotected | ❌ Gap: anyone with access, including Claude, can push straight to `main` | observed (`gh api`) |
| 9 | Automatic checks (CI) run on every PR [GH-FLOW "Create a pull request"; GH-CI] | 4b reads checks, but the repo has none | ❌ Gap once code exists | observed (0 workflows) |
| 10 | At a minimum, turn on Dependabot alerts, secret scanning, push protection [GH-REPO l.13-17] | Not mentioned. Dependabot is free for private repos [GH-PLANS] but off. Secret scanning is not available for a personal private repo [GH-SECRET l.57-58]; push protection for users only covers public repos [GH-PUSHPROT l.70] | ❌ Gap: Dependabot off; secret safety rests only on local checks | documented + observed |
| 11 | Merge after approval [GH-FLOW l.61]; default merge = merge commit [GH-MERGE l.12] | Asks "Merge now?", merges with `--merge` only on yes | ✅ Meets | observed |
| 12 | Delete the branch after merging [GH-FLOW l.69] | GitHub does it automatically (setting on); the local branch is left behind | ✅ Remote meets; ⚠️ local cleanup not covered | observed (only `main` left on GitHub) |
| 13 | Branch up to date with `main` / conflicts resolved before merge [GH-FLOW "Merge your pull request"; GH-PROTECT "strict" checks] | Not mentioned | ⚠️ Gap | observed (skill text) |

## What to fix before app code is pushed (proposed, not done)

1. **One branch and one PR per task, not per week.** New branch from the latest `main` for each piece of work; merge it before starting the next. (#5)
2. **Protect `main`** with a ruleset: require a pull request before merging, block force pushes and deletion. Don't require an approving review: you can't approve your own PR, so it would block you. Protected branches for private repos need GitHub Pro [GH-PLANS l.47]. Students get Pro free through the GitHub Student Developer Pack (not checked here). The API answered "not protected" instead of "upgrade", which suggests the feature is available, but that's inferred. (#8)
3. **Add a GitHub Actions workflow** that runs the app's tests on every PR, then make it a required check. (#9)
4. **Turn on Dependabot alerts** (Settings → Code security). Keep the local secret check in wrap-up, since GitHub won't scan this private repo. (#10)
5. **Wrap-up additions:** write a PR description (what, why, where to look); run the project's tests and show the result in the 4b table; check the branch is up to date with `main`; after a merge, offer to switch to `main` and pull (ask first, other sessions may use the folder); split unrelated changes into separate commits. (#4, 6, 7, 12, 13)

## Update after the owner's answers (2026-11-06)

- **Plan: GitHub Free** (owner; student account, treat as Free). On Free, protected branches and rulesets are not available for private repos [GH-PLANS l.47 lists them under Pro], so fix 2 can't be done on GitHub. The alternatives are a local hook that blocks pushing to `main` (protects only Claude sessions on this computer) or making the repo public (gets protection, secret scanning and push protection free, but shows the work to everyone).
- **The instructor must be able to check the repo.** Observed: `gh api .../collaborators` lists only LDoomD (admin). `gh api .../invitations` shows a **pending invite for mdenner1234 with write access, sent 2026-10-22, not accepted**. Until it's accepted, he can't see this private repo through that invite.

## Not checked

- Whether the instructor sees the repo some other way (for example, a shared link or screen share).
- Whether GitHub's web settings show options the API hides.
- Wrap-up's new step 4b on a real PR: it was added after PR #23 merged, so it hasn't run yet.
- Code-specific practices (CODEOWNERS, release tags, semantic versioning): no app code exists yet.
