# How to Set Up GitHub and Vercel
- Source copy: https://app.notion.com/p/c239219a46918329916781bb84cafff4
- Copied from the live Tech Fleet page by the owner on 2026-11-13; read through the Notion connector on 2026-11-13
- Notion "last edited" of the copy: 2026-11-13T22:08:23.100Z
- Not saved: none

---

This guide shows you how to put your code on GitHub and how to put your app on the internet with Vercel. GitHub stores your code and runs automatic checks on it. Vercel builds your app and hosts it so people can visit it. Together they let you push your code and watch it go live. Follow the steps in order. Each step says what to do and why it matters.

## Part A: GitHub

1. **Create your GitHub account and a new repository.** A repository, or repo for short, is the online home for your code. It keeps a full history of every change, and it lets other people work on the code with you. Go to [github.com](http://github.com) and sign in. Click New to make a new repository. Give it a clear name, choose Public or Private, and create it.
2. **Connect your code to the repo.** Your code lives on your computer right now. You need to link your computer to the repo so you can send your work up to it. If your code is not yet in git, run these commands in your project folder:

```javascript
git init
git remote add origin https://github.com/your-name/your-repo.git
git add .
git commit -m "first commit"
git push -u origin main
```

Here is what each one does. The command git init starts tracking your folder. The command git remote add points your folder at the repo online. The commands git add and git commit save a snapshot of your work. The command git push sends that snapshot up to GitHub. If the repo already has code in it, you can copy it to your computer instead by running git clone with the repo address.

3. **Work in branches and pull requests.** You should not change the main code directly, because one mistake would break the version everyone shares. Instead you make a branch, which is a safe copy, do your work there, and then open a pull request, which is a request to merge your branch into main. This gives you or a teammate a chance to review the change before it goes in. Start a branch like this:

```javascript
git checkout -b my-change
```

Make your edits, commit them, then push the branch:

```javascript
git push -u origin my-change
```

Then open a Pull Request on GitHub.

4. **Add automatic checks with GitHub Actions.** You want the computer to test your code every time you push, so small mistakes are caught early instead of after they ship. GitHub Actions is GitHub's built in tool for this. You add a file at .github/workflows/ci.yml that lists the steps to run, such as installing your project, running your tests, and building it. Once that file is in your repo, these checks run on every pull request.
5. **Make the checks required. This step is recommended.** By default a failing check does not stop a merge, so someone could merge broken code even when the checks are red. Branch protection fixes this. It makes the checks block the merge until they pass. In your repo, go to Settings, then Branches, and add a rule for your main branch that requires your checks to pass before merging.

## Part B: Vercel

6. **Create a Vercel account and import your repo.** Vercel watches your GitHub repo and builds your app whenever you push new code. This is the service that puts your app on the internet. Go to [vercel.com](http://vercel.com) and sign in with your GitHub account. Click Add New, then Project, then import the repo you just made.
7. **Set the Framework Preset and the Root Directory.** Vercel needs to know what kind of app you built and where it lives inside your repo. If either setting is wrong, the build will fail. This is the most common setup mistake, so take your time here. For Framework Preset, choose your framework, such as Next.js. Vercel can usually detect it for you. For Root Directory, point it at the folder that holds your app. If your app sits at the top level of your repo, leave this set to ./ which means the root. Do not point it at a subfolder like src unless your app truly lives in that folder. A wrong Root Directory makes Vercel try to build an empty folder, and the build fails with a confusing error.
8. **Set your Node version and your environment variables.** Your app should build with the same version of Node that you test with, so the results match. Your server code also needs its secret keys, and Vercel keeps those keys on its own servers, safe from the browser. In Project Settings, set the Node version to the one you use, such as 20. Under Environment Variables, add your server secrets, such as your database URL and your service\_role key. Never set a secret in a way that sends it to the browser.
9. **Deploy your app and open it.** This is the payoff. Vercel builds your app and gives you a live web address. From then on, every push to your main branch deploys the app again, and every pull request gets its own preview link so you can test changes before they go live. Click Deploy. When it finishes, open the address and make sure your app works.
10. **If a build fails, read the log.** The build log tells you exactly what went wrong, line by line. Most early failures come from a wrong Root Directory, a wrong Framework Preset, or a missing environment variable. Read the log from the top, find the first error, and fix that one first.

## The big picture

Here is the whole loop in one sentence. You push your code to GitHub, GitHub runs its checks, and Vercel builds and deploys it. Once this is set up, you rarely touch the server by hand. You write code, you open a pull request, and you watch it go live.
