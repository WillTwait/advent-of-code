def part1(data: str) -> int:
    count = 0
    lines = data.strip().split("\n")
    ranges = [tuple(map(int, line.split("-"))) for line in lines if "-" in line]
    vals = [int(line) for line in lines if (line and "-" not in line)]

    for val in vals:
        for range in ranges:
            if range[0] <= val <= range[1]:
                count += 1
                break

    return count


def part2(data: str) -> int:
    count = 0
    lines = data.strip().split("\n")
    ranges = [tuple(map(int, line.split("-"))) for line in lines if "-" in line]

    breakpoint()

    return count


if __name__ == "__main__":
    with open("example.txt") as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
