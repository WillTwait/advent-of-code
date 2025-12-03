def clicks(code: str) -> int:
    direction = code[0]
    amount = int(code[1:]) if direction == "R" else -int(code[1:])
    return amount


def turn_dial(code: str, pos: int) -> int:
    amount = clicks(code)
    tot = pos + amount

    return tot


def part1(data: str) -> int:
    current = 50
    count = 0
    lines = data.strip().split("\n")

    for line in lines:
        loc = turn_dial(line, current) % 100

        if loc == 0:
            count += 1
        current = loc
    return count


def part2(data: str) -> int:
    current = 50
    count = 0
    lines = data.strip().split("\n")

    for line in lines:
        direction = line[0]
        loc = turn_dial(line, current)

        pos_on_dial = loc % 100
        print(f"{line} to point at {pos_on_dial}")

        crosses = abs(loc // 100)
        if crosses:
            print(f"crosses: {crosses}")

        # floor grabs negative, returning cross here
        if (direction == "L") & (current == 0):
            crosses -= 1

        # floor grabs 1, returning an extra cross
        if (direction == "R") & (pos_on_dial == 0):
            crosses -= 1

        count += crosses

        if crosses:
            print(f"**new count(cross)**: {count}")

        # if you land on 0, count it
        if pos_on_dial == 0:
            count += 1
            print(f"**new count (land)**: {count}")

        current = pos_on_dial

    return count


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
