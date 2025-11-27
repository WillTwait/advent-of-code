#!/usr/bin/env python3
import sys
import shutil
from pathlib import Path


def setup_day(year: int, day: int, language: str):
    root = Path(__file__).parent
    day_dir = root / str(year) / f"{day:02d}"
    template_file = root / "templates" / f"solution.{language}"
    solution_file = day_dir / f"solution.{language}"

    # Check if template exists
    if not template_file.exists():
        print(f"Template not found: {template_file}")
        print("Available languages: clj, lisp, py, rs")
        sys.exit(1)

    # Create day directory if it doesn't exist
    day_dir.mkdir(parents=True, exist_ok=True)

    # Check if solution file already exists
    if solution_file.exists():
        print(f"Solution file already exists: {solution_file}")
        return

    # Copy template
    shutil.copy(template_file, solution_file)  # pyright: ignore[reportUnusedCallResult]

    # Create input files if they don't exist
    (day_dir / "input.txt").touch()
    (day_dir / "example.txt").touch()

    print(f"Created: {solution_file}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python setup.py <year> <day> <language>")
        print("Example: python setup.py 2020 1 py")
        sys.exit(1)
    setup_day(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3])
