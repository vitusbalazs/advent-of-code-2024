# Advent of Code 2024
# Day 5: Print Queue - Part 1
# https://adventofcode.com/2024/day/5

# Vitus Balázs
# https://github.com/vitusbalazs

def main():
    middle = 0
    file = open('input.txt', 'r')

    rules, updates = file.read().split("\n\n")
    rules = [rule.split("|") for rule in rules.split("\n")]
    updates = [update.split(",") for update in updates.split("\n")]

    for i in updates:
        correct = True
        for j, k in rules:
            if not correct:
                break
            if j in i and k in i and i.index(j) > i.index(k):
                correct = False

        if correct:
            middle += int(i[len(i)//2])

    print(middle)


if __name__ == '__main__':
    main()
