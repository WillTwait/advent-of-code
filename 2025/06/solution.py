def part1(data: str) -> int:
    lines = data.strip().split()
    math_row = [i for i in lines if i in ("+", "*")]
    col_len = len(math_row)

    total = 0

    for i in range(col_len):
        math_set = lines[i::col_len]
        nums = [int(num) for num in math_set[:-1]]
        operator = math_set[-1]

        if operator == "+":
            result = sum(nums)
            total += result
        if operator == "*":
            result = 1
            for i in nums:
                result = result * i
            total += result

    return total


def part2(data: str) -> int:
    lines = data.strip().split("\n")
    return 0


if __name__ == "__main__":
    with open("example.txt") as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
