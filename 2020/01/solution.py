def part1(data: str) -> int:
    lines = data.strip().split("\n")

    # GOAL: find 2 values that sum to 2020, and multiply then

    # iterate through list, checking what number satisfies sum
    value_set = {int(i) for i in lines}

    for i in value_set:
        pair = 2020 - i

        if pair in value_set:
            return i * pair

    raise ValueError("No valid pairs")


def part2(data: str) -> int:
    lines = data.strip().split("\n")

    # GOAL: find 3 values that sum to 2020, and multiply then

    # take i, subtract from 2020, then do same check as part 1 to see

    value_set = {int(i) for i in lines}

    for i in value_set:
        sum = 2020 - i
        new_set = value_set - {sum}
        for n in new_set:
            final_sum = sum - n

            if final_sum in new_set:
                return i * n * final_sum

    raise ValueError("No valid pairs")


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
