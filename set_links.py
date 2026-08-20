#!/usr/bin/env python3
"""
Point every file in this repo at the real GitHub repository.

Run this ONCE after you create the repo, before you upload:

    python3 set_links.py your-github-username your-repo-name

It rewrites the placeholder YOUR-USERNAME / YOUR-REPO inside README.md and
inside both class notebooks (the notebooks load crimeSTATS.csv from the raw URL).
"""
import sys, pathlib

if len(sys.argv) != 3:
    sys.exit("usage: python3 set_links.py <github-username> <repo-name>")

user, repo = sys.argv[1], sys.argv[2]
root = pathlib.Path(__file__).parent
changed = 0

for path in list(root.rglob("*.ipynb")) + list(root.rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    new = text.replace("YOUR-USERNAME", user).replace("YOUR-REPO", repo)
    if new != text:
        path.write_text(new, encoding="utf-8")
        changed += 1
        print("updated", path.relative_to(root))

print(f"\n{changed} file(s) updated.")
print(f"Student page will be:  https://github.com/{user}/{repo}")
