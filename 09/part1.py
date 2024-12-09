# Advent of Code 2024
# Day 9: Disk Fragmenter - Part 1
# https://adventofcode.com/2024/day/9

# Vitus Balázs
# https://github.com/vitusbalazs

def main():
    with open('input.txt', 'r') as file:
        numbers = [int(num) for num in file.read().strip()]

    solution = []
    increment = 0
    space = False

    for i in numbers:
        solution.extend(['.' if space else increment] * i)
        if not space:
            increment += 1
        space = not space

    i = 0
    j = len(solution) - 1

    while i < j:
        if solution[i] == '.' and not solution[j] == '.':
            solution[i], solution[j] = solution[j], solution[i]
            i += 1
            j -= 1
        elif not solution[i] == '.':
            i += 1
        elif solution[j] == '.':
            j -= 1

    while solution and solution[-1] == '.':
        solution.pop()

    print(sum(i * solution[i] for i in range(len(solution))))

if __name__ == "__main__":
    main()
