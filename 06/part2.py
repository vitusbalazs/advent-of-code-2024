# Advent of Code 2024
# Day 6: Guard Gallivant - Part 2
# https://adventofcode.com/2024/day/6

# Vitus Balázs
# https://github.com/vitusbalazs

from copy import deepcopy


def solve(i, j, lines, directions, direction):
    visited = [(i, j, direction)]

    while i > 0 and i < len(lines) - 1 and j > 0 and j < len(lines) - 1:
        next_dir = directions[direction]['shift']
        if lines[i + next_dir[0]][j + next_dir[1]] != '#':
            # move
            lines[i + next_dir[0]][j + next_dir[1]] = lines[i][j]
            i += next_dir[0]
            j += next_dir[1]
            if (i, j, direction) in visited:
                return True
            visited += [(i, j, direction)]
        else:
            # rotate
            direction = directions[direction]['next_dir']

    return False


def main():
    directions = {
        '^': {
            'shift': (-1, 0),
            'next_dir': '>'
        },
        '>': {
            'shift': (0, 1),
            'next_dir': 'v'
        },
        'v': {
            'shift': (1, 0),
            'next_dir': '<'
        },
        '<': {
            'shift': (0, -1),
            'next_dir': '^'
        }
    }
    file = open('input.txt', 'r')
    lines = file.read().split('\n')
    lines = [list(line) for line in lines]
    file.close()
    direction = '^'
    # find ^
    i, j = next(((i, s.index(direction))
                for i, s in enumerate(lines) if direction in s), (-1, -1))

    blocked = 0

    for k in range(len(lines)):
        for l in range(len(lines[k])):
            print(k, l)
            if lines[k][l] in [direction, '#']:
                continue
            temp_lines = deepcopy(lines)
            temp_lines[k][l] = '#'
            if solve(i, j, temp_lines, directions, direction):
                blocked += 1
            temp_lines = []

    print(blocked)


if __name__ == '__main__':
    main()
