# Advent of Code 2024
# Day 1: Historian Hysteria - Part 1
# https://adventofcode.com/2024/day/1

# Vitus Balázs
# https://github.com/vitusbalazs

def main():
    left_list = []
    right_list = []

    with open('input.txt', 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    print(sum(abs(l - r) for l, r in zip(sorted(left_list), sorted(right_list))))

if __name__ == '__main__':
    main()