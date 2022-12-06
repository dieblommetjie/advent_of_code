with open("input.txt") as input:
    input = input.read().strip()
    part_one, part_two = 0, 0

    for i in range(len(input)):
        if len(set(input[i:i + 4])) == 4 and not part_one:
            part_one = i + 4

        elif len(set(input[i:i + 14])) == 14:
            part_two = i + 14
            break

    print(part_one)
    print(part_two)