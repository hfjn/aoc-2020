import itertools
from pathlib import Path
from typing import List

lines: List = [
    int(number)
    for number in Path("inputs/9_1.txt").read_text().splitlines()
    if number != ""
]


def find_adders(number_list: List[int], curr_number: int):
    number_list = number_list + [curr_number]
    number_list.sort()
    i = number_list.index(curr_number)
    number_list = number_list[:i]

    assert curr_number not in number_list
    for a, b in itertools.combinations(number_list, 2):
        if a + b == curr_number:
            return a, b
    return None


def find_contiguous_set(numbers_list: List[int], curr_number: int):
    for i in range(len(numbers_list)):
        result = list(itertools.accumulate(lines[i:]))
        if curr_number in result:
            return lines[i : i + result.index(curr_number) + 1]


# Part 1
for i in range(25, len(lines)):
    res = find_adders(lines[(i - 25) : i], lines[i])
    if not res:
        not_found = lines[i]
        print(lines[i])

        # Part 2
        result = find_contiguous_set(lines, not_found)
        assert sum(result) == not_found
        print(f"{min(result)} + {max(result)} = {min(result)+max(result)}")
