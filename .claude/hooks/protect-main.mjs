#!/usr/bin/env node
// PreToolUse hook (matcher: Bash). Blocks Claude sessions from committing on, or
// pushing straight to, the main branch. Work must go through a branch and a pull
// request. Merging a pull request (gh pr merge) is allowed.
//
// Why a local hook: on GitHub Free, private repos can't use branch protection or
// rulesets (docs/reports/wrap-up-github-audit-2026-11-06.md, finding 8).
// Limits: only covers Claude sessions on this computer, not git typed by hand,
// the GitHub website, or other people.
import { readFileSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { resolve } from "node:path";

const PROTECTED = new Set(["main", "master"]);

let input;
try {
  input = JSON.parse(readFileSync(0, "utf8"));
} catch {
  process.exit(0);
}
const command = input?.tool_input?.command || "";
if (!/\bgit\b/.test(command)) process.exit(0);

function currentBranch(dir) {
  try {
    return execFileSync("git", ["-C", dir, "rev-parse", "--abbrev-ref", "HEAD"], {
      encoding: "utf8",
      stdio: ["ignore", "pipe", "ignore"],
    }).trim();
  } catch {
    return null; // not a git folder
  }
}

// Split shell words, keeping quoted parts together.
function words(s) {
  return (s.match(/"[^"]*"|'[^']*'|\S+/g) || []).map((w) => w.replace(/^["']|["']$/g, ""));
}

function deny(reason) {
  process.stdout.write(
    JSON.stringify({
      hookSpecificOutput: {
        hookEventName: "PreToolUse",
        permissionDecision: "deny",
        permissionDecisionReason: reason,
      },
    }),
  );
  process.exit(0);
}

let dir = input.cwd || process.cwd();
const switched = new Map(); // branch changes earlier in the same command line
for (const segment of command.split(/&&|\|\||;|\|/)) {
  const w = words(segment.trim());
  if (w[0] === "cd" && w[1]) {
    dir = resolve(dir, w[1].replace(/^~(?=\/|$)/, process.env.HOME));
    continue;
  }
  if (w[0] !== "git") continue;

  // Handle "git -C <path> ..."
  let i = 1;
  let gitDir = dir;
  while (w[i] && w[i].startsWith("-")) {
    if (w[i] === "-C" && w[i + 1]) {
      gitDir = resolve(dir, w[i + 1]);
      i += 2;
    } else i += 1;
  }
  const sub = w[i];
  const args = w.slice(i + 1);
  const branch = switched.has(gitDir) ? switched.get(gitDir) : currentBranch(gitDir);
  if (branch === null) continue;

  // "git switch X" / "git checkout X" earlier in a chain changes the branch for later parts.
  if (sub === "switch" || sub === "checkout") {
    const flagIdx = args.findIndex((a) => ["-c", "-C", "-b", "-B"].includes(a));
    const target = flagIdx >= 0 ? args[flagIdx + 1] : args.filter((a) => !a.startsWith("-") && a !== "--")[0];
    if (target && !args.includes("--")) switched.set(gitDir, target);
    continue;
  }

  if (sub === "commit" && PROTECTED.has(branch)) {
    deny(
      `Blocked: you are on '${branch}'. Don't commit to ${branch} directly. ` +
        "Make a branch for this task (git switch -c <short-task-name>), commit there, push it, and open a pull request.",
    );
  }

  if (sub === "push") {
    if (args.includes("--all") || args.includes("--mirror")) {
      deny("Blocked: 'git push --all/--mirror' would also push main. Push only the task branch.");
    }
    const positional = args.filter((a) => !a.startsWith("-"));
    const refspecs = positional.slice(1); // first one is the remote
    const targetsMain = refspecs.some((r) => {
      const dest = r.replace(/^\+/, "").split(":").pop().replace(/^refs\/heads\//, "");
      return PROTECTED.has(dest);
    });
    const pushesCurrent = refspecs.length === 0 || refspecs.includes("HEAD");
    if (targetsMain || (pushesCurrent && PROTECTED.has(branch))) {
      deny(
        "Blocked: this would push straight to main. Push a task branch and open a pull request instead; " +
          "merge it with 'gh pr merge' after the owner says yes.",
      );
    }
  }
}
process.exit(0);
