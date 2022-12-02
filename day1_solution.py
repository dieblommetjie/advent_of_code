elf_blocks = open('day1_input.txt').read().strip().split("\n\n")
elf_totals = []

for each_elf in elf_blocks:
    elf_totals.append(sum(int(x) for x in each_elf.split("\n")))
elf_totals = sorted(elf_totals, reverse=True)

print(max(elf_totals))
print(elf_totals[0]+elf_totals[1]+elf_totals[2])
