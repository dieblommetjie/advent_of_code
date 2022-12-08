directory = {'/':0}
start = ['/']
with open("input.txt", "r") as f:
    for row in f.readlines():
        rows = row[:-1].split(" ")
        if rows[0] == '$':
            if rows[1] == 'cd':
                if rows[2] == '..':
                    start.pop()
                elif rows[2] == '/':
                    start = ['/']
                else:
                    start.append(rows[2])
        elif rows[0] == 'dir':
            directory["".join(start) + rows[1]] = 0
        else:
            directory["".join(start)] += int(rows[0])
            for i in range(1, len(start)):
                directory["".join(start[:-i])] += int(rows[0])
print(sum(v for v in directory.values() if v <= 100000))
print(min(v for v in directory.values() if v >= directory['/'] - 40000000))