import re
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple


def parse_input():
    parse_regex = re.compile(r"([A-Z])([0-9]+)")

    def parse_lines():
        for number in Path("inputs/12_1.txt").read_text().splitlines():
            if number == "":
                continue
            match = parse_regex.match(number)
            yield match.groups()

    return [(line[0], int(line[1])) for line in parse_lines()]


input = parse_input()


@dataclass
class Ship:
    last_direction: str = "E"
    pos: Tuple[int, int] = (0, 0)
    cardinals = {"N": (1, 0), "E": (0, 1), "S": (-1, 0), "W": (0, -1)}
    flip_cardinals = {"N": (-1, 1), "E": (1, -1), "S": (-1, 1), "W": (1, -1)}
    waypoint: Tuple[int, int] = (1, 10)

    def turn(self, direction: str, degrees: int):
        cardinals = ["N", "E", "S", "W"]
        steps = int(degrees / 90 % 4)
        if direction == "R":
            res = cardinals.index(self.last_direction) + steps
            if res >= len(cardinals):
                res = res - 4
            self.last_direction = cardinals[res]
        if direction == "L":
            res = cardinals.index(self.last_direction) - steps
            if res < 0:
                res = res + 4
            self.last_direction = cardinals[res]

    def move(self, direction: str, distance: int):
        if direction in self.cardinals:
            plan = self.cardinals[direction]
        else:
            plan = self.cardinals[self.last_direction]

        self.pos = (
            self.pos[0] + (plan[0] * distance),
            self.pos[1] + (plan[1] * distance),
        )

    def move_to_waypoint(self, times: int):
        for _ in range(times):
            self.pos = self.pos[0] + self.waypoint[0], self.pos[1] + self.waypoint[1]

    def move_waypoint(self, direction: str, distance: int):
        plan = self.cardinals[direction]

        self.waypoint = (
            self.waypoint[0] + (plan[0] * distance),
            self.waypoint[1] + (plan[1] * distance),
        )

    def rotate_waypoint(self, direction: str, degrees: int):
        degrees = int(degrees % 360)
        if direction == "R":
            if degrees == 90:
                self.waypoint = (self.waypoint[1] * -1, self.waypoint[0])

            if degrees == 180:
                self.waypoint = (self.waypoint[0] * -1, self.waypoint[1] * -1)

            if degrees == 270:
                self.waypoint = (self.waypoint[1], self.waypoint[0] * -1)
        if direction == "L":
            if degrees == 90:
                self.waypoint = (self.waypoint[1], self.waypoint[0] * -1)

            if degrees == 180:
                self.waypoint = (self.waypoint[0] * -1, self.waypoint[1] * -1)

            if degrees == 270:
                self.waypoint = (self.waypoint[1] * -1, self.waypoint[0])

    def manhattan_distance(self):
        return abs(self.pos[0]) + abs(self.pos[1])


def part_1():
    ship = Ship()

    for line in input:
        if line[0] in ("L", "R"):
            ship.turn(line[0], line[1])
        else:
            ship.move(line[0], line[1])

    print(ship.manhattan_distance())


def part_2():
    ship = Ship()
    for line in input:
        if line[0] in ("L", "R"):
            ship.rotate_waypoint(line[0], line[1])

            print(ship.waypoint)
        elif line[0] in ship.cardinals:
            ship.move_waypoint(line[0], line[1])
        else:
            ship.move_to_waypoint(line[1])
    print(ship.pos)
    print(ship.waypoint)
    print(ship.manhattan_distance())


part_2()
