# Advent of Code 2024
# Day 2: Red-Nosed Reports - Part 1
# https://adventofcode.com/2024/day/2

# Vitus Balázs
# https://github.com/vitusbalazs

def main():
    valid = 0
    with open('input.txt', 'r') as file:
        for line in file:
            row = list(map(int, line.split()))

            increasing = all(b > a for a, b in zip(row, row[1:]))
            decreasing = all(b < a for a, b in zip(row, row[1:]))

            if not increasing and not decreasing:
                continue

            difference = all(1 <= abs(a - b) <= 3 for a,
                             b in zip(row, row[1:]))
            if not difference:
                continue

            valid += 1

    print(valid)


if __name__ == '__main__':
    main()
