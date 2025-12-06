def explore(x: int, y: int, map: list[list[str]]) -> int:
    count = 0
    h = len(map)
    w = len(map[0])
    # above
    # if (y-1) >= 0:

    # below

    # left

    # right


def part1(data: str) -> int:
    lines = data.strip().split("\n")
    grid = [line for line in lines]
    h = len(grid)
    w = len(grid[0])
    top = "." * (w + 2)
    padded_grid = [top] + ["." + row + "." for row in grid] + [top]
    # print(padded_grid)
    # print(padded_grid[1:-1])

    total = 0

    for y, row in enumerate(padded_grid):
        print(row)
        for x, col in enumerate(row):
            print(col)
            count = 0
            if col == "@":
                # check top
                # print(x, y)
                # print(padded_grid[y - 1][x - 1 : x + 2])
                # print(padded_grid[y - 1][x - 1 : x + 2])
                count += padded_grid[y - 1][x - 1 : x + 2].count("@")
                print(f"top: {padded_grid[y - 1][x - 1 : x + 2].count('@')}")

                # check left
                # print(padded_grid[y][x - 1].count("@"))
                count += padded_grid[y][x - 1].count("@")
                print(f"left: {padded_grid[y][x - 1].count('@')}")

                # check right
                # print(padded_grid[y][x - 1])
                count += padded_grid[y][x + 1].count("@")
                print(f"right: {padded_grid[y][x - 1].count('@')}")

                # check bottom
                # print(padded_grid[y + 1][x - 1 : x + 2])
                count += padded_grid[y + 1][x - 1 : x + 2].count("@")

                if count < 4:
                    print(f"whammy at {x - 1}, {y - 1}")
                    total += 1

    # print(grid)
    return total


def part2(data: str) -> int:
    lines = data.strip().split("\n")
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
