from pathlib import Path
from typing import List

rows: List = [
    number
    for number in Path("inputs/13_1.txt").read_text().splitlines()
    if number != ""
]

# part_1
earliest_possible = int(rows[0])
busses = [int(bus) for bus in rows[1].split(",") if bus != "x"]


found = False
timestamp = earliest_possible
while not found:
    for bus in busses:
        if timestamp % bus == 0:
            print(timestamp)
            found = True
    timestamp += 1

# part_2
busses = [(idx, int(bus)) for idx, bus in enumerate(rows[1].split(",")) if bus != "x"]

step = 1
start = 0

while busses:
    for ix, bus in busses[:]:
        if (start + ix) % bus == 0:
            busses.remove((ix, bus))
            step *= bus
        else:
            start += step
            break

print(start)
