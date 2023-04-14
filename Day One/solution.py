#Getting data and parsing input file into a list of strings
with open('..\Concurso Banco do Brasil\Advent\Day One\input.in') as file:
    data = [i for i in file.read().strip().split("\n")]

#Traversing every STRING in DATA
max = 0     # Elf with greatest calorie count
max2 = 0    # Elf with second greatest calorie count
max3 = 0    # Elf with third greatest calorie count
count = 0
for item in data:
    if item == '':
        count = 0
    else:
        num = int(item)
        count += num
    if count > max:
        max = count
    elif count > max2:
        max2 = count
    elif count > max3:
        max3 = count

part2 = max + max2 + max3

print(max)
print(max,max2,max3)
print(part2)

