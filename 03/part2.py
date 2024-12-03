# Advent of Code 2024
# Day 3: Mull It Over - Part 2
# https://adventofcode.com/2024/day/3

# Vitus Balázs
# https://github.com/vitusbalazs

import re


def main():
    with open('input.txt', 'r') as file:
        content = file.read().replace('\n', '')
        filtered = re.sub(
            r"don't\(\).*?do\(\)", "", content, flags=re.DOTALL)
        filtered = re.sub(r"don't\(\).*?$", "", filtered, re.DOTALL)

        print(sum(int(x) * int(y)
              for x, y in re.findall(r"mul\((\d+),(\d+)\)", filtered)))


if __name__ == '__main__':
    main()
