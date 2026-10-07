numeros = [5, 2, 7, 2, 8, 5, 2, 6, 7]
n = len(numeros)

for i in range(n-1):
    for j in range(n-1-i):
        if numeros[j] > numeros[j+1]:
            temp = numeros[j]
            numeros[j] = numeros[j+1]
            numeros[j+1] = temp

print("Lista después de ser ordenada: " + str(numeros))

sinD = []

for y in range(n-1):
    if numeros[y] == numeros[y + 1]:
            numeros[y] = 0
    
for x in range(n):
    if numeros[x] != 0:
        sinD.append(numeros[x])

print("Lista sin duplicados:" + str(sinD))

