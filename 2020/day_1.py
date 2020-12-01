from itertools import product
from pathlib import Path
from typing import List

numbers: List[int] = [
    int(number) for number in Path("inputs/1_1.txt").read_text().splitlines()
]


def part_1():
    for n in product(numbers, numbers):
        if sum(n) == 2020:
            return n[0] * n[1]


def part_2():
    for n in product(numbers, numbers, numbers):
        if sum(n) == 2020:
            return n[0] * n[1] * n[2]


if __name__ == "__main__":
    print(part_1())
    print(part_2())
