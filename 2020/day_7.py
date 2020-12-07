import re
from collections import defaultdict
from pathlib import Path
from typing import List

lines: List = [number for number in Path("inputs/7_1.txt").read_text().splitlines()]

mainbag_regex = re.compile(r"([a-z]+\s[a-z]+)\sbags\scontain\s(.*)\.")
bags_regex = re.compile(r"([1-9])\s([a-z]+\s[a-z]+)\sbags?")


def parse_input():
    packing_list = defaultdict(list)
    for line in lines:
        m = mainbag_regex.match(line)
        bag, part = m.groups()
        if part == "no other bags":
            continue
        bags = []
        for b in part.split(", "):
            n, name = bags_regex.match(b).groups()
            bags.append((int(n), name))
        packing_list[bag] = bags
    return packing_list


def walk_rules_up(color, bags):
    matches = []
    for bag, packs in bags.items():
        for b in packs:
            if b[1] == color:
                matches.append(bag)
                matches = matches + walk_rules_up(bag, bags)
    return matches


def walk_rules_down(color, bags) -> int:
    return 1 + sum((c * walk_rules_down(b, bags)) for c, b in bags[color])


def part_1():
    bags = parse_input()
    allowed_colors = walk_rules_up("shiny gold", bags)
    print(len(set(allowed_colors)))


def part_2():
    bags = parse_input()
    number = walk_rules_down("shiny gold", bags) - 1
    print(number)


part_2()
