lista = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]

print("Introduce la posición del elemento")
posicion = int(input())

if posicion >= len(lista):
    print("no se puede agrandar la lista")
else:
    print("Introduce el elemento")
    elemento = int(input())

    print(lista)

    lista.insert(posicion, elemento)
    lista.remove(lista[len(lista)-1])

    print(lista)



