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


def build_progress_table(solved):
    """Generate markdown table of solved problems."""
    rows = [
        "| # | Title | Category | File |",
        "|---|--------|----------|------|"
    ]

    for category, problems in solved.items():
        for num, title, file in problems:
            # Normalize link path for GitHub
            link = str(file).replace("\\", "/")
            rows.append(
                f"| {num} | {title} | {category} | [{file.name}]({link}) |"
            )

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

    # --- Update category progress numbers ---
    for category, total in CATEGORIES.items():
        solved_count = len(solved[category])

        # Category name in README is title case with spaces
        readme_category_name = category.replace("_", " ").title()

        # Matches the "| Category Name | X |" cell
        pattern = (
            rf"(\|\s*{re.escape(readme_category_name)}\s*\|\s*)"
            r"\d+(\s*\|)"
        )
        repl = rf"\1{solved_count}\2"

        # Use lambda to avoid backreference confusion
        content = re.sub(pattern, lambda m: repl, content)

    # --- Replace solved problems table ---
    solved_table = build_progress_table(solved)

    table_pattern = (
        r"<!-- START_SOLVED_TABLE -->.*?<!-- END_SOLVED_TABLE -->"
    )
    table_repl = (
        f"<!-- START_SOLVED_TABLE -->\n"
        f"{solved_table}\n"
        f"<!-- END_SOLVED_TABLE -->"
    )

    content = re.sub(
        table_pattern,
        lambda m: table_repl,
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
