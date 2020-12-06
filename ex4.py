import random

n = int(input('Введіть n: '))
mat = [[random.randint(-5, 5) for z in range(n)] for i in range(n)]

print("Початкова матриця: ")
for i in mat:
    print(i)

for num_st in range(n):
    if num_st % 2 != 0:
        st = []
        for num_rd in range(n):
            st.append(mat[num_rd][num_st])
        st.sort()
        for num_rd in range(n):
            mat[num_rd][num_st] = st[num_rd]

print("Кінцева матриця: ")
for i in mat:
    print(i)