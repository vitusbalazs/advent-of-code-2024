# Advent of Code 2024
# Day 2: Red-Nosed Reports - Part 2
# https://adventofcode.com/2024/day/2

# Vitus Balázs
# https://github.com/vitusbalazs

def check_safe(row):
    increasing = all(b > a for a, b in zip(row, row[1:]))
    decreasing = all(b < a for a, b in zip(row, row[1:]))

    if not increasing and not decreasing:
        return False

    difference = all(1 <= abs(a - b) <= 3 for a, b in zip(row, row[1:]))
    if not difference:
        return False
    
    return True

def main():
    valid = 0
    with open('input.txt', 'r') as file:
        for line in file:
            row = list(map(int, line.split()))

            if check_safe(row):
                valid += 1
            else:
                for i in range(len(row)):
                    if check_safe(row[:i] + row[i+1:]):
                        valid += 1
                        break

    print(valid)


if __name__ == '__main__':
    main()