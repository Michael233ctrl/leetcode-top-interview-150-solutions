import os
import re

ROOT = "."
README = "README.md"
TOTAL = 150

def count_solved():
    solved = 0
    for root, dirs, files in os.walk(ROOT):
        for f in files:
            if re.match(r"\d+_.*\.(py|cpp|js|ts|java)$", f):
                solved += 1
    return solved

def update_readme(solved):
    with open(README, "r") as f:
        content = f.read()

    new_block = f"![progress](https://img.shields.io/badge/Progress-{solved}%20/%20{TOTAL}-brightgreen?style=for-the-badge)"

    # Replace existing progress badge
    updated = re.sub(r"!\[progress\].*?badge.*?style=for-the-badge\)", new_block, content)

    with open(README, "w") as f:
        f.write(updated)

if __name__ == "__main__":
    solved = count_solved()
    update_readme(solved)
    print(f"Updated README: {solved}/{TOTAL}")
