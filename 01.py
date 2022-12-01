#!py -3

with open("01-input.txt", "r") as input_file:
    lines = [l.strip() for l in input_file.readlines()]

class Elf:
    def __init__(self, number, calories):
        self.number = number
        self.calories = calories

accumulated_calories = 0
elf_calories = list()
for l in lines:
    if l == '':
        elf_calories.append(accumulated_calories)
        accumulated_calories = 0
    else:
        accumulated_calories += float(l)

max_calories = max(elf_calories)
print(max_calories)
elf_calories = sorted(elf_calories, reverse=True)
print(sum(elf_calories[0:3]))
