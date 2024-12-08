# Advent of Code 2024
# Day 8: Resonant Collinearity - Part 2
# https://adventofcode.com/2024/day/8

# Vitus Balázs
# https://github.com/vitusbalazs

def propagate(lines, antinodes, start, direction, rows, cols):
    x, y = start
    dx, dy = direction
    while 0 <= x < rows and 0 <= y < cols:
        antinodes[x][y] = '#'
        x += dx
        y += dy


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

                            propagate(lines, antinodes, (i, j), (-row_diff, -col_diff), rows, cols)
                            propagate(lines, antinodes, (k, l), (row_diff, col_diff), rows, cols)

    print(sum(row.count('#') for row in antinodes))


if __name__ == "__main__":
    main()
