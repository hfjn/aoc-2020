import re
from pathlib import Path
from typing import List

lines: List = [number for number in Path("inputs/2_1.txt").read_text().splitlines()]

regex = re.compile(r"([\d]*)-([\d]*)\s(\w):\s([\w]*)")


def get_matches(line: str):
    matches = regex.match(line)
    return (
        int(matches.group(1)),
        int(matches.group(2)),
        matches.group(3),
        matches.group(4),
    )


def part_1():
    count = 0
    for line in lines:
        min_number, max_number, character, password = get_matches(line)
        if min_number <= password.count(character) <= max_number:
            count += 1
    print(count)


def part_2():
    count = 0
    for line in lines:
        pos_1, pos_2, character, password = get_matches(line)
        positions = [idx + 1 for idx, c in enumerate(password) if c == character]
        if pos_1 in positions and pos_2 not in positions:
            count += 1
        elif pos_1 not in positions and pos_2 in positions:
            count += 1
    print(count)


part_1()
part_2()
