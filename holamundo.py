# EJERCICIOS CLASE
# 1.
# Si un año divisible por 4 es un año bisiesto, excepto los años divisibles por 100, a menos que también sean divisibles por 400.

# numeros = [842, 19403112, 7, 501894, 0, 83109, 4294967295, 14, 62001, 9182736]

# for numero in numeros:
#     if numero % 4 == 0:
#         if numero % 100 == 0:
#             if numero % 400 == 0:
#                 print(f"{numero} es un año bisiesto.")
#             else:
#                 print(f"{numero} no es un año bisiesto.")
#         else:
#             print(f"{numero} es un año bisiesto.")
#     else:
#         print(f"{numero} no es un año bisiesto.")



# 2.
# lista = [4, 2, 7, 0,6 , 5, 4, 3, 2]
# contador = 0
# maximo = 0

# for i in range(1, len(lista)):

#     if lista[i] < lista[i - 1]:
#         contador += 1
#         maximo = contador
#     else:
#         if contador > maximo:
#             maximo = contador
#         contador = 1

# print("La secuencia mas larga de numeros descendentes es de:", maximo)



# 3.
# lista = [2, 1, 0, 0, 1, 2]
# i = 0
# j = len(lista) - i - 1
# esCapicua = True
# while (j >= i and esCapicua != False) :
#     if lista[i] != lista[j]:
#         esCapicua = False
#     i += 1
#     j -= 1
#     print("Es igual")



# 4. Ejercicio de diccionarios




# EJERCICIOS CLASSROOM

# 1. Va mostrando el ultimo valor asignado a la variable
# mensaje = "Hola Mundo"
# print(mensaje)
# mensaje = "Hola Mundo 2"
# print(mensaje)

# 2.
# 1_message = "Hi there"
# greeting message = "Hello"
# print = "Good morning"
# n = "Ada Lovelace"


# 3. No esta escrito bien el message en el print
# message = "Hello Python Crash Course reader!"
# print(mesage)

# 4. Con el lower no dara fallos de si hay mayuscula o empieza con mayuscula
# palabra = "AdA Lovelace"
# print(palabra.lower())
# print(palabra.upper())
# print(palabra.title())


# 5. Se busca unir las dos palabras del nombre con el f"{}{}"
# first_name = "ada"
# last_name = "lovelace"

# full_name = f"{first_name} {last_name}"
# print(full_name)

# message = f"¡Hola, {full_name.title()}! Es un gusto saludarte."
# print(message)


# 6. En la variable mensaje se usan las comillas simples en el f porque las dobles se usan para nombrar la cita como si fuera dicho por otra persona
# famoso = "Albert Einstein"

# cita = "A person who never made a mistake never tried anything new."

# mensaje = f'{famoso} once said, "{cita}"\nOne of Python\'s strengths is its diverse and supportive community.'

# print(mensaje)


# 7. Se usa \n para el salto de linea y \t para dejar margen
# print("Languages:\n\tPython\n\tC\n\tJavaScript")


# 8. Ejercicio para practicar el strip , que elimina espacios en blanco
# name = "\t\n  Ada Lovelace  \t\n"

# print("--- Nombre original (con saltos y tabulaciones) ---")
# print(name)

# print("--- Usando lstrip() (limpia la izquierda) ---")
# print(name.lstrip())

# print("--- Usando rstrip() (limpia la derecha) ---")
# print(name.rstrip())

# print("--- Usando strip() (limpia ambos lados) ---")
# print(name.strip())

# print("--- Demostración de inmutabilidad ---")
# print("El valor original sigue intacto:", name)

# name = name.strip()
# print("Nuevo valor guardado permanentemente:", name)

# print("--- Resultado de las comparaciones ---")
# print("python " == "python")
# print("python ".strip() == "python")


# 9. Funciones para eliminar prefijos y sufijos
# nostarch_url = "https://nostarch.com"
# print(nostarch_url)
# simple_url = nostarch_url.removeprefix("https://")
# print(simple_url)
# filename = "python_notes.txt"
# print(filename.removesuffix(".txt"))


# 10. Practica de operaciones, la division da decimales porque trata los valores como float
# numero = 10
# print(4+4,12-4,2*4,16/2,3 ** 2, 10 ** 6, 2 + 3 * 4 and (2 + 3) * 4,numero)