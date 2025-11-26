#!/usr/bin/env python3
import sys
import shutil
from pathlib import Path


def setup_day(year: int, day: int):
    root = Path(__file__).parent
    day_dir = root / str(year) / f"{day:02d}"

    if day_dir.exists():
        print(f"Day already exists: {day_dir}")
        return

    day_dir.mkdir(parents=True)

    # Copy templates
    templates = root / "templates"
    for template in templates.glob("solution.*"):
        shutil.copy(template, day_dir / template.name)

    # Create input files
    (day_dir / "input.txt").touch()
    (day_dir / "example.txt").touch()

    print(f"Created: {day_dir}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python setup.py <year> <day>")
        sys.exit(1)
    setup_day(int(sys.argv[1]), int(sys.argv[2]))
