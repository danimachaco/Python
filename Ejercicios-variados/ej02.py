mazo_jugador1 = [2, 4, 6, 8, 10, 1]
mazo_jugador2 = [1, 3, 5, 7, 9, 15]
posicion = 0

print("Mazo jugador 1:" + str(mazo_jugador1))
print("Mazo jugador 2:" + str(mazo_jugador2))

while len(mazo_jugador1) > 0 and len(mazo_jugador2) > 0:
    print("Jugador 1 juega: " + str(mazo_jugador1[posicion]))
    print("Jugador 2 juega: " + str(mazo_jugador2[posicion]))

    if mazo_jugador1[posicion] > mazo_jugador2[posicion]:
        print("Jugador 1 gana la ronda")

        mazo_jugador1.append(mazo_jugador1[posicion])
        mazo_jugador1.append(mazo_jugador2[posicion])
        mazo_jugador1.remove(mazo_jugador1[posicion])
        mazo_jugador2.remove(mazo_jugador2[posicion])

        print("Estado actual del mazo Jugador 1:" + str(mazo_jugador1))
        print("Estado actual del mazo Jugador 2:" + str(mazo_jugador2))
    else:
        print("Jugador 2 gana la ronda")

        mazo_jugador2.remove(mazo_jugador2[posicion])
        mazo_jugador2.append(mazo_jugador1[posicion])
        mazo_jugador2.append(mazo_jugador2[posicion])
        mazo_jugador1.remove(mazo_jugador1[posicion])

        print("Estado actual del mazo Jugador 1:" + str(mazo_jugador1))
        print("Estado actual del mazo Jugador 2:" + str(mazo_jugador2))

        print("---------------------------------------------------")

if len(mazo_jugador1)>len(mazo_jugador2):
    print("El jugador 1 gana la partida")
else:
    print("El jugador 2 gana la partida")