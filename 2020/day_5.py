from pathlib import Path
from typing import List

lines: List = [number for number in Path("inputs/5_1.txt").read_text().splitlines()]


def walk_rows(search_string: str, max_number: int, up: str, down: str):
    rows = [i for i in range(0, max_number)]

    for char in search_string:
        center = int(len(rows) / 2)
        if char == down:
            rows = rows[:center]
        if char == up:
            rows = rows[center:]
    assert len(rows) == 1
    return rows[0]


# Part 1
ids = []
for line in lines:
    row = walk_rows(line[:7], 128, "B", "F")
    column = walk_rows(line[7:], 8, "R", "L")
    ids.append(row * 8 + column)

# Part 2
all_ids = []

for row in range(0, 127):
    for column in range(0, 8):
        all_ids.append(row * 8 + column)

free_seats = set(all_ids) - set(ids)

for seat in free_seats:
    if seat - 1 in ids and seat + 1 in ids:
        print(seat)
