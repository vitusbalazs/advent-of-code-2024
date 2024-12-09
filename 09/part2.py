# Advent of Code 2024
# Day 9: Disk Fragmenter - Part 2
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

    print(solution)

    j = len(solution) - 1

    while j > 1:
        if solution[j] != '.': 
            k = j - 1
            while solution[k] == solution[j]:
                k -= 1
            length = j - k
            k = k + 1

            i = 0
            while i < len(solution):
                if i > j:
                    break
                print('checking for', solution[j], 'with length', length, 'at position', i, i+length)
                if solution[i] == '.' and all(char == '.' for char in solution[i:i + length]):
                    break
                i += 1

            if i < j:
                solution[i:i+length], solution[k:k+length] = solution[k:k+length], solution[i:i+length]


            j -= length
        else:
            j -= 1

    summ = sum(i * solution[i] for i in range(len(solution)) if solution[i] != '.')
    print(summ)

if __name__ == "__main__":
    main()
