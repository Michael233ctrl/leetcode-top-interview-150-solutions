import os
import re
import json
from pathlib import Path

ROOT = Path(__file__).parent
README = ROOT / "README.md"

# Matches filenames like: 383-ransom_note.py or 049-anagram-groups.py
FILENAME_RE = re.compile(r"(\d+)[\-_\s](.*)\.py$", re.IGNORECASE)

CATEGORIES = {
    "array_string": 27,
    "two_pointers": 11,
    "sliding_window": 7,
    "matrix": 10,
    "hashmap": 8,
    "intervals": 6,
    "stack": 13,
    "linked_list": 11,
    "tree": 16,
    "bst": 8,
    "backtracking": 7,
    "divide_and_conquer": 4,
    "graph": 10,
    "dynamic_programming": 14,
    "greedy": 8,
    "bit_manipulation": 4,
    "math": 6,
}

def scan_solutions():
    """Scan category folders, extract solved problems, return dict."""
    solved = {}

    for category, total in CATEGORIES.items():
        folder = ROOT / category
        solved[category] = []

        if not folder.exists():
            continue

        for file in folder.iterdir():
            match = FILENAME_RE.match(file.name)
            if not match:
                continue

            num = int(match.group(1))
            title = match.group(2).replace("_", " ").replace("-", " ").title()

            solved[category].append((num, title, file))

        # Sort problems inside category by number
        solved[category].sort(key=lambda x: x[0])

    return solved


def build_progress_table(solved):
    """Generate markdown table of solved problems."""
    rows = ["| # | Title | Category | File |", "|---|--------|----------|------|"]

    for category, problems in solved.items():
        for num, title, file in problems:
            link = str(file).replace("\\", "/")
            rows.append(f"| {num} | {title} | {category} | [{file.name}]({link}) |")

    return "\n".join(rows)


def update_readme(solved):
    """Update README.md progress section and solved table."""
    content = README.read_text()

    total_solved = sum(len(v) for v in solved.values())
    total_problems = sum(CATEGORIES.values())

    # Update the progress badge
    content = re.sub(
        r"Progress-\d+%20/%20150",
        f"Progress-{total_solved}%20/%20150",
        content
    )

    # Update category table
    for category, total in CATEGORIES.items():
        solved_count = len(solved[category])
        pattern = rf"(\|\s*{category.replace('_', ' ').title()}\s*\|\s*)\d+"
        repl = rf"\1{solved_count}"
        content = re.sub(pattern, repl, content, flags=re.IGNORECASE)

    # Replace solved table section
    solved_table = build_progress_table(solved)

    content = re.sub(
        r"<!-- START_SOLVED_TABLE -->(.*?)<!-- END_SOLVED_TABLE -->",
        f"<!-- START_SOLVED_TABLE -->\n{solved_table}\n<!-- END_SOLVED_TABLE -->",
        content,
        flags=re.DOTALL
    )

    README.write_text(content)


def main():
    solved = scan_solutions()
    update_readme(solved)
    print("README updated successfully.")


if __name__ == "__main__":
    main()
