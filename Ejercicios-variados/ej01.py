lista = [5, 12, 3, 18, 20, 2, 15]
k = 15
m = 3

# for i in range(len(lista) - 1, -1, -1):
#     if lista[i] < k and lista[i] % m == 0:
#         lista.remove(lista[i])
for i in lista:
    if lista[i] < k and lista[i] % m == 0:
        lista.remove(lista[i])
    
print(lista)