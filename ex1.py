import random

rd = int(input("Введіть кількість рядків: "))
st = int(input("Введіть кількість стовпців: "))

mat = [[random.randint(-5, 5) for z in range(st)] for i in range(rd)]
dob = 1
ind = False

for x in mat[0::2]:
    for y in x[0::2]:
        if y < 0:
            ind = True
            dob *= y


if ind:
    print(dob)
else:
    print(0)
