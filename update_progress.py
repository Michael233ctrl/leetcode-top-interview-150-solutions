import os
import re
from pathlib import Path

ROOT = Path(__file__).parent
README = ROOT / "README.md"

# Matches filenames like: 383-ransom_note.py or 49-group-anagrams.py
FILENAME_RE = re.compile(r"(\d+)[\-_ ](.*)\.py$", re.IGNORECASE)

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
    """Scan category folders and return {category: [(num, title, file_path), ...]}."""
    solved = {}

    for category, total in CATEGORIES.items():
        folder = ROOT / category
        solved[category] = []

        if not folder.exists():
            continue

        for file in folder.iterdir():
            if not file.is_file():
                continue

            match = FILENAME_RE.match(file.name)
            if not match:
                continue

            num = int(match.group(1))
            title = (
                match.group(2)
                .replace("_", " ")
                .replace("-", " ")
                .title()
            )

            solved[category].append((num, title, file))

        # Sort by problem number
        solved[category].sort(key=lambda x: x[0])

    return solved


def build_category_progress_table(solved):
    rows = [
        "| Category | Completed | Total |",
        "|----------|-----------|-------|"
    ]

    for category, total in CATEGORIES.items():
        completed = len(solved[category])
        name = category.replace("_", " ").title()
        rows.append(f"| {name} | {completed} | {total} |")

    return "\n".join(rows)



def update_readme(solved):
    """Update README.md with new progress numbers & solved table."""

    content = README.read_text(encoding="utf-8")

    total_solved = sum(len(v) for v in solved.values())
    total_problems = sum(CATEGORIES.values())

    # --- Update progress badge ---
    badge_pattern = r"Progress-\d+%20/%20150"
    badge_repl = f"Progress-{total_solved}%20/%20150"

    content = re.sub(badge_pattern, lambda m: badge_repl, content)

    category_table = build_category_progress_table(solved)

    content = re.sub(
        r"(## 🚀 \*\*Progress\*\*.*?\n)(\|.*?\|.*?\n)+",
        lambda m: m.group(1) + category_table + "\n",
        content,
        flags=re.DOTALL
    )

    README.write_text(content, encoding="utf-8")


def main():
    solved = scan_solutions()
    update_readme(solved)
    print(f"README updated successfully. Solved {sum(len(v) for v in solved.values())} problems.")


if __name__ == "__main__":
    main()
