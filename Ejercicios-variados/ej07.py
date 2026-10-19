MAX_LIBROS = 3
 # Aquí van tus funciones

def prestar(prestamos, libro, socio):
    
    if esta_prestado(prestamos,libro):
        print("Error: " + libro + "ya esta prestado")

    elif len(libros_de(prestamos, socio)) >= MAX_LIBROS: 
        print("Error: " + socio + " ya tiene 3 libros")


    else:
        prestamos[libro] = socio
        print("Prestamo realizado: " + libro + " -> " + prestamos[libro])
    
def esta_prestado(prestamos, libro):
    if libro in prestamos:
        return True
    else: return False

def libros_de(prestamos, socio):
    listaLibros=[]

    for x in prestamos:
        if prestamos[x]==socio:
            listaLibros.append(x)

    return listaLibros
 
def devolver(prestamos, libro):
    if libro in prestamos:
        print("Socio  que devuelve el libro: " + prestamos[libro])
        del prestamos[libro]
    else:
        print("Este libro no esta prestado")

def socios_con_prestamos(prestamos):
    listaSocios=[]

    for x in prestamos:
        if not prestamos[x] in listaSocios:
            listaSocios.append(prestamos[x])
    return sorted(listaSocios)

def mostrar_prestamos(prestamos):
    print(sorted(prestamos))

prestamos = {}

prestar(prestamos, "Dune", "Ana")
prestar(prestamos, "El Hobbit", "Luis")
prestar(prestamos, "1984", "Ana")
prestar(prestamos, "Dune", "Luis")
prestar(prestamos, "Rebelión en la granja", "Ana")
prestar(prestamos, "Fahrenheit 451", "Ana")
prestar(prestamos, "Fahrenheit 451", "Marta")
mostrar_prestamos(prestamos)

print("¿Está prestado 'Dune'?",
"Sí" if esta_prestado(prestamos, "Dune") else "No")
print("¿Está prestado 'Drácula'?",
"Sí" if esta_prestado(prestamos, "Drácula") else "No")
print("Libros de Ana:", ", ".join(libros_de(prestamos, "Ana")))
print("Socios con préstamos:", ", ".join(socios_con_prestamos(prestamos)))

devolver(prestamos, "1984")
devolver(prestamos, "Drácula")
prestar(prestamos, "Matilda", "Ana")
devolver(prestamos, "El Hobbit")
mostrar_prestamos(prestamos)
print("Socios con préstamos:", ", ".join(socios_con_prestamos(prestamos)))