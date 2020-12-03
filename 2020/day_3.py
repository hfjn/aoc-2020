from pathlib import Path
from typing import List

lines: List = [number for number in Path("inputs/3_1.txt").read_text().splitlines()]


class Position:
    x: int = 0
    y: int = 0


def make_move(pos: Position, down=0, right=0):
    pos.x += down
    pos.y += right
    return pos


def position_is_tree(pos: Position):
    y = pos.y
    line = lines[pos.x]
    if y >= len(line):
        y = y - int(y / len(line)) * len(line)
    return line[y] == "#"


def should_stop(pos: Position):
    return pos.x >= len(lines)


def traverse(down: int, right: int):
    pos = Position()
    trees = 0

    while True:
        pos = make_move(pos, down=down, right=right)
        if should_stop(pos):
            break
        if position_is_tree(pos):
            trees += 1

    return trees


def part_1():
    print(traverse(1, 3))


def part_2():
    print(
        traverse(1, 1)
        * traverse(1, 3)
        * traverse(1, 5)
        * traverse(1, 7)
        * traverse(2, 1)
    )


part_1()
part_2()
