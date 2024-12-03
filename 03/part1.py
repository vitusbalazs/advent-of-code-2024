# Advent of Code 2024
# Day 3: Mull It Over - Part 1
# https://adventofcode.com/2024/day/3

# Vitus Balázs
# https://github.com/vitusbalazs

import re


def main():
    with open('input.txt', 'r') as file:
        content = file.read().replace('\n', '')
        print(sum(int(x) * int(y)
              for x, y in re.findall(r"mul\((\d+),(\d+)\)", content)))


if __name__ == '__main__':
    main()
