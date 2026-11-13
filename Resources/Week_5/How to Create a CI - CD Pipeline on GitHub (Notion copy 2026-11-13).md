# How to Create a CI / CD Pipeline on GitHub
- Source copy: https://app.notion.com/p/dba9219a46918271accb01a7fd3fd4c3
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:14.888Z
- Not saved: none (page icon is the emoji gear)

---

This guide shows you how to build a CI/CD pipeline on GitHub by co-creating with Claude Code, not by copying commands.

CI stands for Continuous Integration, which means the computer builds your app and runs your tests every time you push code. CD stands for Continuous Delivery, which means your app is always kept ready to go live, so a passing change can ship to users.

Together they catch problems early and keep your live app working as you keep changing it. Your job is to tell Claude the outcome you want and the problems to solve, and then to shape the solution together and check that it works. Follow the parts in order.

## Part A: Name the outcome you want

Claude builds well when you give it a clear outcome, not a vague task or solutions. So before anything, say in plain words what goal you are trying to achieve. Tell Claude what "done" looks like.

For this work, the outcome sounds like this: "Every time I push code changes, I want to ensure that we can avoid new bugs or regressions. I want to ensure we can always produce code that follows UX or coding standards"

Write your own version of that outcome in a sentence or two.

## Part B: Give Claude the problems to solve and the context

Claude must be dogfed. Hand it what it needs to solve the problem with you:

1. **Your app and where it lives.** Point Claude at the GitHub repository you built in Week 4, and tell it the tools your app uses.
2. **What matters to test.** Give Claude your MVP requirements from Week 2, with your use cases and BDD scenarios. A use case is a path a person takes through your app, and a BDD scenario says what should happen on that path. These tell Claude what your checks should prove.
3. **Your limits and rules.** Tell Claude the problems it has to work within. For example: the checks should run on every push, a failing check should stop a change from going live, and you are on the free plan, so you do not need branch protection.
4. **The kinds of checks you want.** Part C lists the types of QA tests. Decide with Claude which ones fit your app.

Then ask Claude to explain its approach in plain words before it writes anything, so you understand what it is about to do.

## Part C: The types of QA tests to run as checks

Part of co-creating the pipeline is deciding which checks to run. Not every kind of test belongs in CI, and you do not need all of them at once. The testing pyramid from the lecture is your guide: have many small fast tests at the bottom, and only a few big slow tests at the top. Here are the types, from the ones you want the most to the ones you want the least. Talk them over with Claude and choose the ones that fit your app.

1. **Unit tests.** These check one small piece of code on its own, like one function that adds up a total. They are fast and cheap, so you want the most of them. Great for CI.
2. **Integration tests.** These check that two parts work together, like your code saving to the database. You want fewer of these. Good for CI.
3. **Browser, or end to end, tests.** These drive the whole app through the screen the way a user would. They give the most trust but are slow and break easily, so keep only a few. Run your most important ones in CI.
4. **Smoke test.** A quick, light check right after a build to see if the app even starts and the main paths work. It is a fast early gate in CI.
5. **Regression tests.** These check that a change did not break something that used to work. You run them on every push, so they are a perfect fit for CI.
6. **Security checks.** These look for weak spots, like a dependency with a known problem that an attacker could use.
7. **CI gate checks.** These are threshold checks that fail the build when a number crosses a line you set, like test coverage dropping too low. Add one once you have a set of tests.
8. **Your BDD scenarios.** Turn each Given, When, Then into a test. This ties your checks straight back to your requirements.
9. **Gate-check your Claude Skills.** Make sure the Claude Skills you made in Week 1 are checked on every push, so a change that breaks them does not pass.

The rule to remember from the lecture: automated tests still only catch what someone told them to look for, so they do not replace a human. That is why you also test by hand after you ship.

## Part D: Co-create the solution with Claude

Now build it together. You bring the outcome and the problems. Claude brings the building. You shape it and decide, like a head chef working with a cook.

1. **Ask Claude to propose the pipeline.** Based on your outcome, your requirements, and the checks you chose, ask Claude how it would set this up, and ask it to explain each part in plain words.
2. **Read it and ask questions.** If you do not understand a part, ask Claude what it does and why. Do not accept anything you cannot explain back.
3. **Decide together what to keep, change, or cut.** Start small, with your most important checks, and add more over time. You make the calls.
4. **Have Claude build it and write the tests.** Ask it to create the pipeline and to write the tests from the use cases and BDD scenarios you picked.
5. **Record the big decisions.** Have Claude write an ADR for the choices you made, so you remember why you built it this way.

## Part E: Red means stop, green ships

This is the behavior you and Claude are building toward. When all the checks pass, the change is safe to merge, and once it is merged into the main branch, Vercel builds it and puts the new version live. That is the CD part: passing code flows to your users on its own. When a check is red, do not merge, because merging broken code can cause real failures for your users. On a paid plan you can turn on branch protection to block the merge until the checks are green. On the free plan you may not have that, and that is fine for this class. The rule is simple: if the checks are red, fix them before you merge. After a change is live, run your two test case scenarios by hand, because autotests cannot catch everything.

## Part F: Prove it works, together

A check you cannot trust is worse than no check, so test the pipeline before you rely on it.

1. **Watch it pass.** Push a small change and open the Actions tab on GitHub. You should see your checks run and turn green.
2. **Break it on purpose.** Make a small change that should fail a test, push it, and confirm the pipeline turns red and stops the merge. Then undo it. Now you know your checks really work.
3. **When something fails that you do not understand,** give Claude the run log and ask it to explain the problem before it fixes it.

## The big picture

Here is the whole idea in one sentence. You bring the outcome you want and the problems to solve, Claude brings the building, and together you shape it and prove it works. Once this is set up, quality is built into every push instead of being saved for the end, and you can spend your own testing time on the things a script can never catch.
