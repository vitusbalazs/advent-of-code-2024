# Advent of Code 2024
# Day 6: Guard Gallivant - Part 1
# https://adventofcode.com/2024/day/6

# Vitus Balázs
# https://github.com/vitusbalazs

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
    # find ^
    i, j = next(((i, s.index('^'))
                for i, s in enumerate(lines) if '^' in s), (-1, -1))

    while i > 0 and i < len(lines) - 1 and j > 0 and j < len(lines) - 1:
        next_dir = directions[lines[i][j]]['shift']
        if lines[i + next_dir[0]][j + next_dir[1]] != '#':
            # move
            lines[i + next_dir[0]][j + next_dir[1]] = lines[i][j]
            lines[i][j] = 'X'
            i += next_dir[0]
            j += next_dir[1]
        else:
            # rotate
            lines[i][j] = directions[lines[i][j]]['next_dir']

    moves = sum(sum(1 for j in i if j == 'X') for i in lines) + 1

    print(moves)


if __name__ == '__main__':
    main()
