from collections import defaultdict
from pathlib import Path
from typing import List

numbers: List = [
    int(number)
    for number in Path("inputs/10_1.txt").read_text().splitlines()
    if number != ""
]
occurrences = defaultdict(int)
numbers.sort()


def part_1():
    for number_id, number in enumerate(numbers):
        if number_id == 0:
            continue
        occurrences[number - numbers[number_id - 1]] += 1

    print((occurrences[1] + 1) * (occurrences[3] + 1))


paths = defaultdict(int)


def traverse(curr, numbers: List[int], goal) -> int:
    if goal - numbers[curr] <= 3:
        return 1
    if paths[curr] == 0:
        paths[curr] = sum(
            [
                traverse(curr + i, numbers, goal)
                for i in range(0, 4)
                if curr + i < len(numbers)
                and 0 < numbers[curr + i] - numbers[curr] <= 3
            ]
        )
    return paths[curr]


# Part 2
numbers += [0]
numbers.sort()

found = traverse(0, numbers, max(numbers) + 3)
print(found)
