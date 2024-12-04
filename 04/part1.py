# Advent of Code 2024
# Day 4: Ceres Search - Part 1
# https://adventofcode.com/2024/day/4

# Vitus Balázs
# https://github.com/vitusbalazs

def test_xmas(lines, i, j):
    valid_xmas = 0
    x = len(lines)
    y = len(lines[0])

    # row
    if j + 3 < y:
        if lines[i][j] == 'X' and lines[i][j+1] == 'M' and lines[i][j+2] == 'A' and lines[i][j+3] == 'S':
            valid_xmas += 1

    # row backwards:
    if j - 3 >= 0:
        if lines[i][j] == 'X' and lines[i][j-1] == 'M' and lines[i][j-2] == 'A' and lines[i][j-3] == 'S':
            valid_xmas += 1

    # column
    if i + 3 < x:
        if lines[i][j] == 'X' and lines[i+1][j] == 'M' and lines[i+2][j] == 'A' and lines[i+3][j] == 'S':
            valid_xmas += 1

    # column backwards
    if i - 3 >= 0:
        if lines[i][j] == 'X' and lines[i-1][j] == 'M' and lines[i-2][j] == 'A' and lines[i-3][j] == 'S':
            valid_xmas += 1

    # down right
    if i + 3 < x and j + 3 < y:
        if lines[i][j] == 'X' and lines[i+1][j+1] == 'M' and lines[i+2][j+2] == 'A' and lines[i+3][j+3] == 'S':
            valid_xmas += 1

    # down left
    if i + 3 < x and j - 3 >= 0:
        if lines[i][j] == 'X' and lines[i+1][j-1] == 'M' and lines[i+2][j-2] == 'A' and lines[i+3][j-3] == 'S':
            valid_xmas += 1

    # up right
    if i - 3 >= 0 and j + 3 < y:
        if lines[i][j] == 'X' and lines[i-1][j+1] == 'M' and lines[i-2][j+2] == 'A' and lines[i-3][j+3] == 'S':
            valid_xmas += 1

    # up left
    if i - 3 >= 0 and j - 3 >= 0:
        if lines[i][j] == 'X' and lines[i-1][j-1] == 'M' and lines[i-2][j-2] == 'A' and lines[i-3][j-3] == 'S':
            valid_xmas += 1

    return valid_xmas


def main():
    correct = 0

    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file]
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                correct += test_xmas(lines, i, j)

    print(correct)


if __name__ == "__main__":
    main()
