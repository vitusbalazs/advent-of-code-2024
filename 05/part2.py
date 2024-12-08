# Advent of Code 2024
# Day 5: Print Queue - Part 2
# https://adventofcode.com/2024/day/5

# Vitus Balázs
# https://github.com/vitusbalazs

from copy import deepcopy
from collections import defaultdict

# got stuck, inspiration: https://github.com/Grecil/ElegantAoC24/blob/main/05B.py


def main():
    middle = 0
    file = open('input.txt', 'r')

    rules, updates = file.read().split("\n\n")
    rules = [rule.split("|") for rule in rules.split("\n")]
    updates = [update.split(",") for update in updates.split("\n")]

    rule_dictionary = defaultdict(set)
    for a, b in rules:
        rule_dictionary[a].add(b)

    for i in updates:
        if any(a in i and b in i and i.index(a) > i.index(b) for a, b in rules):
            update_set = set(i)
            valid_dependents = {j: rule_dictionary[j] & update_set for j in i}
            sorted_elements = sorted(valid_dependents, key=lambda k: len(
                valid_dependents[k]), reverse=True)
            middle += int(sorted_elements[len(sorted_elements)//2])

    print(middle)


if __name__ == '__main__':
    main()
