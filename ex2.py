def opsum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += (-1) ** i * i
    return sum

def dob_tuple_el(tp):
    dob = 1
    for i in tp:
        dob *= i
    return dob

n = int(input("Введіть n: "))

mat = []

for i in range(1, n + 1):
    rd = []
    for j in range(1, n + 1):
        if i * j < 3:
            rd.append(i + j)
        elif i * j >= 3:
            rd.append(opsum(j))
    mat.append(rd)

rd_of_max = 0
max_el = 0

for i,l in enumerate(mat):
    if i < len(mat[0]):
        if l[i] > max_el:
            max_el = l[i]
            rd_of_max = i

print("Матриця: ", end='\n\n')
for i in mat:
    print(i)
print()
print("Максимальний елемент головної діагоналі: ", max_el)
print("Добуток елементів рядка з максимальним елементом головної діагоналі: ", dob_tuple_el(mat[rd_of_max]))