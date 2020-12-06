import random

n = int(input("Введіть n: "))

mat = [[random.randint(-5, 5) for z in range(n)] for i in range(n)]
index_of_max = 0
max_seq = 0

print("Mатриця: ")
for i in mat:
    print(i)

for i in mat:
    for x in i:
        if i.count(x) > max_seq:
            max_seq = i.count(x)
            index_of_max = mat.index(i)

print("Номер рядка з максимальною кількістю однакових елементів ", index_of_max + 1)