from pathlib import Path
from typing import List

lines: List = [number for number in Path("inputs/6_1.txt").read_text().splitlines()]

group = set()
groups = []

# Part 1
for line in lines:
    if line == "":
        groups.append(len(group))
        group = set()
    for c in line:
        group.add(c)

print(sum(groups))

# Part 2
group = []
group_size = 0
groups = []
for line in lines:
    if line == "":
        answers = [c for c in set(group) if group.count(c) == group_size]
        groups.append(len(answers))
        group = []
        group_size = 0
    else:
        group_size += 1
        for c in line:
            group.append(c)

print(sum(groups))
