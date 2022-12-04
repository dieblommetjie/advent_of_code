import re

part_one = 0
part_two = 0

input = open('input.txt').read()

for l in input.split('\n'):
    numbers = list(map(int, re.findall('\d+', l)))

    set_one = set(range(numbers[0], numbers[1]+1))
    set_two = set(range(numbers[2], numbers[3]+1))

    if set_one >= set_two or set_two <= set_one:
        part_one += 1

    if set_one & set_two:
        part_two += 1

print(part_one, part_two)