elf_blocks = open('day1_input.txt').read().strip().split("\n\n")
elf_totals = []

for each_elf in elf_blocks:
    elf_totals.append(sum(int(x) for x in each_elf.split("\n")))

print(max(elf_totals))
