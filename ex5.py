import random

rd = int(input("Введіть кількість рядків: "))
st = int(input("Введіть кількість стовпців: "))

mat = [[random.randint(-5, 5) for z in range(st)] for i in range(rd)]
count_zero_tuple = 0

print("Матриця: ")
for i in mat:
    print(i)

for num_st in range(st):
    for num_rd in range(rd):
        if mat[num_rd][num_st] == 0:
            count_zero_tuple += 1
            break

print("Кількість стовпців з нульовим елементом ", count_zero_tuple)