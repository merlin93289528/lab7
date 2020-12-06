import random

n = int(input("Введіть n: "))

a = [[random.randint(-5, 5) for z in range(n)] for i in range(n)]
b = [[random.randint(-5, 5) for z in range(n)] for i in range(n)]
c = [[x + y for x, y in zip(i, j)] for i, j in zip(a, b)]

print("Матриця A: ")
for i in a:
    print(i)

print("Матриця B: ")
for i in b:
    print(i)

print("Матриця C: ")
for i in c:
    print(i)