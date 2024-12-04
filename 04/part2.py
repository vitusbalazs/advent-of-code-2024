# Advent of Code 2024
# Day 4: Ceres Search - Part 2
# https://adventofcode.com/2024/day/4

# Vitus Balázs
# https://github.com/vitusbalazs

def test_xmas(lines, i, j):
    diag1, diag2 = False, False

    if (lines[i-1][j-1] == 'M' and lines[i+1][j+1] == 'S') or (lines[i-1][j-1] == 'S' and lines[i+1][j+1] == 'M'):
        diag1 = True

    if (lines[i-1][j+1] == 'M' and lines[i+1][j-1] == 'S') or (lines[i-1][j+1] == 'S' and lines[i+1][j-1] == 'M'):
        diag2 = True

    return diag1 and diag2


def main():
    correct = 0

    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file]
        for i in range(1, len(lines) - 1):
            for j in range(1, len(lines[i]) - 1):
                if lines[i][j] == 'A' and test_xmas(lines, i, j):
                    correct += 1

    print(correct)


if __name__ == "__main__":
    main()
