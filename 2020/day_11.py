from pathlib import Path
from typing import List

mapping = {"L": 0, ".": None}


def parse_input():
    rows: List = [
        number
        for number in Path("inputs/11_1.txt").read_text().splitlines()
        if number != ""
    ]

    return [[mapping[col] for col in row] for row in rows]


def get(x, y, parsed):
    if x < 0 or y < 0 or y >= len(parsed[0]) or x >= len(parsed):
        return 0
    return parsed[x][y] if parsed[x][y] else 0

def check(x, y, parsed):
    seat = parsed[x][y]
    if seat is None:
        return None
    seats_around = [
        get(x - 1, y, parsed),
        get(x - 1, y - 1, parsed),
        get(x, y - 1, parsed),
        get(x + 1, y, parsed),
        get(x, y + 1, parsed),
        get(x + 1, y + 1, parsed),
        get(x - 1, y + 1, parsed),
        get(x + 1, y - 1, parsed),
    ]
    if seat == 0 and sum(seats_around) == 0:
        return 1
    elif seat == 1 and sum(seats_around) >= 4:
        return 0
    else:
        return seat


def check_2(x, y, parsed):
    seat = parsed[x][y]
    if seat is None:
        return None
    visible_seats = []
    if seat == 0 and sum(seats_around) == 0:
        return 1
    elif seat == 1 and sum(seats_around) >= 4:
        return 0
    else:
        return seat


def simulate(parsed):
    result = [[None for _ in range(len(parsed[0]))] for _ in range(len(parsed))]
    changed = 0
    for x in range(len(parsed)):
        for y in range(len(parsed[x])):
            result[x][y] = check(x, y, parsed)
            if result[x][y] != parsed[x][y]:
                changed += 1

    return result, changed


def find_neighbors(x, y, mat):
    for


def part_1():
    parsed = parse_input()
    result, changed = simulate(parsed)

    while True:
        result, changed = simulate(result)
        if changed == 0:
            break
    print(sum([col for row in result for col in row if col]))

def part_2():
    parsed = parse_input()
    seats_to_check = {}
    for x in range(len(parsed)):
        for y in range(len(parsed[x])):


part_1()
