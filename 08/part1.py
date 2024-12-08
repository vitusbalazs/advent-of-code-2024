# Advent of Code 2024
# Day 8: Resonant Collinearity - Part 1
# https://adventofcode.com/2024/day/8

# Vitus Balázs
# https://github.com/vitusbalazs

def main():
    with open('input.txt', 'r') as file:
        lines = [list(line) for line in file.read().strip().split('\n')]

    rows, cols = len(lines), len(lines[0])
    antinodes = [['.'] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            char = lines[i][j]
            if char not in ['.', '#']:
                for k in range(i, rows):
                    start_col = j + 1 if k == i else 0
                    for l in range(start_col, cols):
                        if char == lines[k][l]:
                            row_diff, col_diff = k - i, l - j
                            forward = (k + row_diff, l + col_diff)
                            backward = (i - row_diff, j - col_diff)
                            if 0 <= forward[0] < rows and 0 <= forward[1] < cols:
                                antinodes[forward[0]][forward[1]] = '#'
                            if 0 <= backward[0] < rows and 0 <= backward[1] < cols:
                                antinodes[backward[0]][backward[1]] = '#'

    print(sum(row.count('#') for row in antinodes))


if __name__ == "__main__":
    main()
