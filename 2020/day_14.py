import re
from copy import deepcopy
from pathlib import Path
from typing import List

rows: List = [
    number
    for number in Path("inputs/14_1.txt").read_text().splitlines()
    if number != ""
]

mem_regex = re.compile(r"mem\[(\d+)\]\s=\s(\d+)")


def apply_mask(val, mask):
    bin_val = bin(int(val))
    bin_val = bin_val.replace("0b", "")
    missing = len(mask) - len(bin_val)
    leading_zeroes = ["0" for _ in range(missing)]

    bin_val = leading_zeroes + [c for c in bin_val]

    for ix, m in enumerate(mask):
        if m == "X":
            continue
        bin_val[ix] = m
    return int("0b" + "".join(bin_val), 2)


def apply_memory_mask(val, mask):
    bin_val = bin(int(val))
    bin_val = bin_val.replace("0b", "")
    missing = len(mask) - len(bin_val)
    leading_zeroes = ["0" for _ in range(missing)]

    bin_val = leading_zeroes + [c for c in bin_val]

    for ix, m in enumerate(mask):
        if m == '0':
            continue
        bin_val[ix] = m

    def apply_floating(floating_bin_val):
        found = []
        for i, m in enumerate(floating_bin_val):
            if m == "X":
                zero = deepcopy(floating_bin_val)
                one = deepcopy(floating_bin_val)
                zero[i] = "0"
                found += apply_floating(zero)
                one[i] = "1"
                found += apply_floating(one)

                return found
        found.append(floating_bin_val)
        return found

    res = apply_floating(bin_val)

    for floating in apply_floating(bin_val):
        yield int("0b" + "".join(floating), 2)


memory = {}
memory2 = {}

for row in rows:
    if row == "":
        continue
    if row.startswith("mask"):
        mask = row.replace("mask = ", "")
    else:
        matches = mem_regex.match(row)
        pos, original_val = matches.groups()
        val = apply_mask(original_val, mask)
        for pos in apply_memory_mask(pos, mask):
            memory2[pos] = int(original_val)
        memory[pos] = val

print(sum(memory.values()))
print(sum(memory2.values()))
