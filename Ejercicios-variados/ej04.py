filas = int(input("introduce numero de filas "))
columnas = int(input("introduce numero de columnas "))
c = 1
mOriginal = [[0 for a in range(columnas)] for a in range(filas)]
mTrasp = [[0 for a in range(len(mOriginal[0]))] for a in range(len(mOriginal))]

print("Matriz original")
for a in range(columnas):
    for b in range(filas):
        mOriginal[a][b] = c
        c+=1

print(mOriginal)

print("")

print("Matriz traspuesta")
for x in range(filas):
    for d in range(columnas):
        mTrasp[d][x] = mOriginal[x][d] 

print(mTrasp)

    

