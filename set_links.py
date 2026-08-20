#!/usr/bin/env python3
"""
Point every file in this repo at a GitHub repository.

    python3 set_links.py <github-username> <repo-name>

Rewrites the Colab badge links in README.md and the raw-CSV URL inside notebook 01.
Safe to run again after renaming or recreating the repo — it rewrites whatever
username/repo is currently written in, not just the original placeholders.
"""
import re, sys, pathlib

if len(sys.argv) != 3:
    sys.exit("usage: python3 set_links.py <github-username> <repo-name>")

user, repo = sys.argv[1], sys.argv[2]
root = pathlib.Path(__file__).parent
changed = 0

# Any owner/repo currently sitting after one of these hosts gets replaced.
HOSTS = [
    r"raw\.githubusercontent\.com",
    r"github\.com",
    r"colab\.research\.google\.com/github",
]
PATTERNS = [(re.compile(h + r"/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+"), h) for h in HOSTS]

for path in list(root.rglob("*.ipynb")) + list(root.rglob("*.md")):
    text = original = path.read_text(encoding="utf-8")
    text = text.replace("YOUR-USERNAME", user).replace("YOUR-REPO", repo)
    for pattern, host in PATTERNS:
        literal = host.replace("\\", "")
        text = pattern.sub(f"{literal}/{user}/{repo}", text)
    if text != original:
        path.write_text(text, encoding="utf-8")
        changed += 1
        print("updated", path.relative_to(root))

print(f"\n{changed} file(s) updated.")
print(f"Student page:  https://github.com/{user}/{repo}")
print(f"Data URL:      https://raw.githubusercontent.com/{user}/{repo}/main/data/crimeSTATS.csv")
