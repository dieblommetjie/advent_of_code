
def get_value(x):
    return ord(x) - ord('a') + 1 if x.islower() else ord(x) - ord('A') + 27

rows = open("day3_input.txt").read().strip().split("\n")
part_one = 0
part_two = 0

for line in rows:
    temp = len(line) // 2
    x = set(line[:temp]) & set(line[temp:])
    part_one += get_value(x)

for i in range(0, len(rows), 3):
    line1, line2, line3 = rows[i:i+3]
    x, = set(line1) & set(line2) & set(line3)
    part_two += get_value(x)

print(part_one)
print(part_two)