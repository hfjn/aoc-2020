from collections import defaultdict

starting_numbers = [0, 13, 1, 16, 6, 17]

numbers = defaultdict(list)


last_said = None

for turn in range(0, 30000000):
    if turn < len(starting_numbers):
        last_said = starting_numbers[turn]

    elif len(numbers[last_said]) > 1:
        last_said = numbers[last_said][-1] - numbers[last_said][-2]

    else:
        last_said = 0
    numbers[last_said].append(turn)

print(last_said)
