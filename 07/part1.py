# Advent of Code 2024
# Day 7: Bridge Repair - Part 1
# https://adventofcode.com/2024/day/7

# Vitus Balázs
# https://github.com/vitusbalazs

def check_expression(left, right, index, current_value):
    if index == len(right):
        return current_value == left

    add_result = check_expression(
        left, right, index + 1, current_value + right[index])
    mult_result = check_expression(
        left, right, index + 1, current_value * right[index])

    return add_result or mult_result


def main():
    possible = 0
    with open('input.txt', 'r') as file:
        for line in file:
            left = int(line.split(": ")[0])
            right = list(map(int, line.split(": ")[1].split(" ")))

            if check_expression(left, right, 1, right[0]):
                possible += left

    print(possible)


if __name__ == "__main__":
    main()
