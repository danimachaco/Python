# ALGORITMO DE LA BURBUJA
# a = [3, 8, 7, 1, 5]
# n=len(a)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if a[j] > a[j+1]:
#             temp = a[j]
#             a[j] = a[j+1]
#             a[j+1] = temp

#     print(a)


m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [7, 8, 9]
]

m2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1],
    [6, 5, 4]
]

mTotal=[[0 for a in range(len(m1[0]))] for a in range(len(m1))]

for i in range(len(m1)):
    for j in range(len(m1[i])):
        suma = m2[i][j] + m1[i][j]
        mTotal[i][j] = suma

print(mTotal)


