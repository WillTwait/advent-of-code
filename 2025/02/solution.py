import math
import re


def part1(data: str) -> int:
    lines = data.strip().split(",")
    invalid_sum = 0

    for line in lines:
        vals = line.split("-")
        lower, upper = int(vals[0]), int(vals[1])
        # print(f"lower: {lower}, upper: {upper}")

        for i in range(lower, (upper + 1)):
            # print(i)
            str_num = str(i)
            str_len = len(str_num)
            n = math.ceil(str_len / 2)
            pattern = "." * n
            regex = rf"({pattern})\1"
            # print(regex)

            if len(str_num) > 1 and bool(re.search(regex, str_num)):
                # print(str_num)
                invalid_sum += i

    return invalid_sum


def part2(data: str) -> int:
    lines = data.strip().split(",")
    invalid_sum = 0

    for line in lines:
        vals = line.split("-")
        lower, upper = int(vals[0]), int(vals[1])
        print(f"lower: {lower}, upper: {upper}")

        for i in range(lower, (upper + 1)):
            # print(i)
            str_num = str(i)
            str_len = len(str_num)
            regex_patterns: list[str] = []

            max_n = math.ceil(str_len / 2)
            while max_n > 0:
                pattern = "." * max_n
                regex = rf"({pattern})\1"
                max_n -= 1
                regex_patterns.append(regex)

            print(regex_patterns)

            if len(str_num) > 1:
                for pattern in regex_patterns:
                    if bool(re.search(pattern, str_num)):
                        print(i)
                        invalid_sum += i
                # print(str_num)

    return invalid_sum


if __name__ == "__main__":
    with open("example.txt") as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
