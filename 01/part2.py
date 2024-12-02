# Advent of Code 2024
# Day 1: Historian Hysteria - Part 2
# https://adventofcode.com/2024/day/1

# Vitus Balázs
# https://github.com/vitusbalazs

def main():
    left_list = []
    right_dict = {}

    with open('input.txt', 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_dict[right] = right_dict.get(right, 0) + 1

    print(sum(left * right_dict.get(left, 0) for left in left_list))


if __name__ == '__main__':
    main()