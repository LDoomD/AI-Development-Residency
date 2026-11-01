"""Read-only collector for public Reddit posts and comments about family caregiving.

- Uses PRAW in read-only mode: needs a client id and secret, never a Reddit password.
- Usernames are never stored. Each author becomes a code like U-3fa91c.
- Text is scrubbed of u/names, emails and phone numbers.
- Output: data/posts.jsonl (git-ignored). Re-running skips posts already saved.
"""
import hashlib
import hmac
import json
import os
import re
import secrets
import sys
from pathlib import Path

import praw

HERE = Path(__file__).parent
DATA = HERE / "data"
SALT_FILE = DATA / ".salt"
OUT = DATA / "posts.jsonl"

USER_RE = re.compile(r"(?<![\w/])/?u/[A-Za-z0-9_-]{3,20}")
EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE_RE = re.compile(r"\+?\d?[\s.-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}")


def load_env():
    env = HERE / ".env"
    if not env.exists():
        sys.exit("Missing .env. Copy .env.example to .env and fill it in.")
    for line in env.read_text().splitlines():
        if line.strip() and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())


def get_salt():
    DATA.mkdir(exist_ok=True)
    if not SALT_FILE.exists():
        SALT_FILE.write_text(secrets.token_hex(16))
    return SALT_FILE.read_text().encode()


def code_for(author, salt):
    if author is None:
        return "U-deleted"
    return "U-" + hmac.new(salt, str(author).lower().encode(), hashlib.sha256).hexdigest()[:6]


def scrub(text):
    text = USER_RE.sub("[user]", text or "")
    text = EMAIL_RE.sub("[email]", text)
    return PHONE_RE.sub("[phone]", text)


def main():
    load_env()
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 25
    salt = get_salt()
    reddit = praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_CLIENT_SECRET"],
        user_agent=os.environ["REDDIT_USER_AGENT"],
        check_for_updates=False,
    )
    reddit.read_only = True

    cfg = json.loads((HERE / "queries.json").read_text())
    seen = {}
    if OUT.exists():
        for line in OUT.read_text().splitlines():
            rec = json.loads(line)
            seen[rec["id"]] = rec

    new = 0
    for sub in cfg["subreddits"]:
        for item in cfg["queries"]:
            try:
                results = reddit.subreddit(sub).search(item["q"], sort="relevance", time_filter="all", limit=limit)
                for s in results:
                    tag = {"stage": item["stage"], "query": item["q"]}
                    if s.id in seen:
                        if tag not in seen[s.id]["matched"]:
                            seen[s.id]["matched"].append(tag)
                        continue
                    body = s.selftext or ""
                    if body in ("[removed]", "[deleted]"):
                        continue
                    s.comments.replace_more(limit=4)
                    comments = [
                        {
                            "author": code_for(c.author.name if c.author else None, salt),
                            "score": c.score,
                            "parent": c.parent_id,
                            "id": c.id,
                            "text": scrub(c.body),
                        }
                        for c in s.comments.list()
                        if c.body not in ("[removed]", "[deleted]")
                    ]
                    seen[s.id] = {
                        "id": s.id,
                        "subreddit": sub,
                        "created_utc": int(s.created_utc),
                        "author": code_for(s.author.name if s.author else None, salt),
                        "title": scrub(s.title),
                        "text": scrub(body),
                        "score": s.score,
                        "num_comments": s.num_comments,
                        "flair": s.link_flair_text,
                        "permalink": "https://www.reddit.com" + s.permalink,
                        "matched": [tag],
                        "comments": comments,
                    }
                    new += 1
                print(f"r/{sub} | {item['stage']} | total saved {len(seen)} (+{new} new)", flush=True)
            except Exception as exc:  # keep going; one bad subreddit should not stop the run
                print(f"r/{sub} | {item['q'][:40]}... skipped: {type(exc).__name__}", flush=True)

    OUT.write_text("\n".join(json.dumps(r) for r in seen.values()) + "\n")
    print(f"Done. {len(seen)} posts in {OUT}")


if __name__ == "__main__":
    main()
