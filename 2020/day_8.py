import re
from pathlib import Path
from typing import List, Tuple

from isort._future import dataclass

lines: List = [number for number in Path("inputs/8_1.txt").read_text().splitlines()]

line_regex = re.compile(r"([a-z]{3})\s([-+][0-9]*)")


@dataclass
class Instruction:
    operation: str
    argument: int
    seen: int = 0


def parse() -> List[Instruction]:
    instructions = []
    for line in lines:
        if line:
            matches = line_regex.match(line).groups()
            instructions.append(Instruction(matches[0], int(matches[1])))
    return instructions


def execute(instructions: List[Instruction]) -> Tuple[int, bool]:
    accumulator = 0
    index = 0
    while index < len(instructions):
        instruction = instructions[index]
        if instruction.seen == 1:
            return accumulator, True
        if instruction.operation == "acc":
            accumulator += instruction.argument
            index += 1
        if instruction.operation == "jmp":
            index += instruction.argument
        if instruction.operation == "nop":
            index += 1
        instruction.seen += 1
    return accumulator, False


def part_1():
    instructions = parse()
    print(execute(instructions))


def part_2():
    instructions = parse()
    for i, instruction in enumerate(instructions):
        if instruction.operation == "jmp" or instruction.operation == "nop":
            copied = parse()
            instruction.operation = "jmp" if instruction.operation == "nop" else "nop"
            copied[i] = instruction
            acc, inf = execute(copied)
            if not inf:
                print(acc)


part_2()
