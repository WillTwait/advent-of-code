# my brute pt 1 before figuring out pt 2 algo

# def part1(data: str) -> int:
#     lines = data.strip().split("\n")
#     total_joltage = 0

#     for line in lines:
#         num_arr = [int(i) for i in line]

#         # fetch first digit max and its index
#         # cant be last digit, bc want to make 2 digit
#         m1 = 0
#         m1_index = 0
#         for i, num in enumerate(num_arr[0:-1]):
#             if num > m1:
#                 m1 = num
#                 m1_index = i

#         m2 = 0
#         for num in num_arr[m1_index + 1 :]:
#             if num > m2:
#                 m2 = num
#         # print(f"max: {m1} at {m1_index}")

#         joltage = int(str(m1) + str(m2))
#         total_joltage += joltage

#     return total_joltage


def highest_valid(
    indexed_list: list[tuple[int, int]], vals_left: int, prev_i: int
) -> tuple[int, int]:
    # must leave at least as many values in list as we have vals left, and has to be after previous battery index
    candidates = [
        i
        for i in indexed_list
        if (((len(indexed_list) - i[0]) >= vals_left) and (i[0] > prev_i))
    ]
    best = max(candidates, key=lambda p: p[1])

    return best


def get_joltage(data: str, num_batteries: int) -> int:
    lines = data.strip().split("\n")
    total_joltage = 0

    for line in lines:
        jolt_list: list[int] = []
        vals_left = num_batteries
        prev_i = -1
        indexed_list = list(enumerate([int(i) for i in line]))

        while len(jolt_list) < num_batteries:
            jolt = highest_valid(indexed_list, vals_left, prev_i)
            jolt_list.append(jolt[1])
            vals_left -= 1
            prev_i = jolt[0]

        joltage = int("".join(str(i) for i in jolt_list))
        total_joltage += joltage

    return total_joltage


def part1(data: str) -> int:
    return get_joltage(data, 2)


def part2(data: str) -> int:
    return get_joltage(data, 12)


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
