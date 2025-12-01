# Advent of Code

My solutions to [Advent of Code](https://adventofcode.com/) puzzles.

## Structure

```
2025/
  01/
    input.txt      # Puzzle input
    example.txt    # Example from puzzle description
    solution.py    # Python solution
    solution.rs    # Rust solution
    solution.lisp  # Common Lisp solution
    solution.clj   # Clojure solution
```

## Setup a New Day

```bash
python setup.py 2025 1 py
```

This creates `2025/01/` with empty input files and solution templates.

## Running Solutions

```bash
cd 2025/01

# Python
python solution.py

# Rust
rustc solution.rs -o solution && ./solution

# Common Lisp
sbcl --script solution.lisp

# Clojure (via Babashka)
bb solution.clj
```

## Prerequisites

- Python 3
- Rust: `brew install rust` or [rustup.rs](https://rustup.rs)
- Common Lisp: `brew install sbcl`
- Clojure: `brew install borkdude/brew/babashka`
