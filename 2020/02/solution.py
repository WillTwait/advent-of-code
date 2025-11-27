from collections import Counter
from dataclasses import dataclass


@dataclass
class PasswordPolicy:
    min_count: int
    max_count: int
    letter: str
    password: str


def get_rule_parts(line: str) -> PasswordPolicy:
    parts = line.split()

    rule = parts[0].split("-")
    min_count = int(rule[0])
    max_count = int(rule[1])

    letter = parts[1].strip(":")

    password = parts[2]

    return PasswordPolicy(
        min_count=min_count, letter=letter, max_count=max_count, password=password
    )


def is_pt1_valid(line: str) -> bool:
    policy = get_rule_parts(line)

    count_map = Counter(policy.password)

    count = count_map.get(policy.letter)

    if not count:
        return False

    return policy.min_count <= count <= policy.max_count


def is_pt2_valid(line: str) -> bool:
    # exactly ONE position must contain the letter
    # One Indexed policy parts
    policy = get_rule_parts(line)
    password = policy.password
    letter = policy.letter

    return (password[policy.min_count - 1] == letter) ^ (
        password[policy.max_count - 1] == letter
    )


def part1(data: str) -> int:
    valid: int = 0
    lines = data.strip().split("\n")

    for line in lines:
        if is_pt1_valid(line):
            valid += 1
    return valid


def part2(data: str) -> int:
    valid: int = 0
    lines = data.strip().split("\n")

    for line in lines:
        if is_pt2_valid(line):
            valid += 1

    return valid


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
