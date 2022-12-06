def extraction(temp):
    extracted_stack = [""]*10
    for row in temp[:-1]:
        for i, square in enumerate(row[1::4]):
            if square != " ": extracted_stack[i+1] += square
    return extracted_stack
    
input = open("data05.txt").read()
temp_stack, instructions = [part.split("\n") for part in input.split("\n\n")]
extracted_stack = extraction(temp_stack)

part_one, part_two = extracted_stack[:], extracted_stack[:]
for row in instructions:
    _, num, _, source, _, destination = row.split()
    num = int(num)
    source = int(source)
    destination = int(destination)

    part_one[source], part_one[destination] = part_one[source][num:], part_one[source][:num][::-1] + part_one[destination]
    part_two[source], part_two[destination] = part_two[source][num:], part_two[source][:num] + part_two[destination]

print("Part 1:", "".join(string[0] for string in part_one if string))
print("Part 2:", "".join(string[0] for string in part_two if string))