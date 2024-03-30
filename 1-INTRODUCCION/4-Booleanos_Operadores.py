# Booleanos y operadores lógicos
# Descripción: En este programa se muestra cómo se utilizan los booleanos y los operadores lógicos en Python.
# Autor: Soriyama
# Funciones: input(), print()
# Tipos de datos de Python: bool
# Los booleanos son un tipo de dato que puede tener dos valores: True o False.
# Los operadores lógicos son: and, or, not, ==, !=, <, >, <=, >=
# Se pueden realizar operaciones lógicas con booleanos.
# Se pueden realizar operaciones lógicas con variables de diferentes tipos.
# Se pueden realizar operaciones lógicas en una sola línea.
# Se pueden comparar variables de diferentes tipos.
# and devuelve True si ambas condiciones son verdaderas.
# or devuelve True si al menos una de las condiciones es verdadera.
# not devuelve True si la condición es falsa.
# == devuelve True si los valores son iguales.
# != devuelve True si los valores son diferentes.
# < devuelve True si el primer valor es menor que el segundo.
# > devuelve True si el primer valor es mayor que el segundo.
# <= devuelve True si el primer valor es menor o igual que el segundo.
# >= devuelve True si el primer valor es mayor o igual que el segundo.

# Solicitar un valor al usuario.
valor = int(input("Ingrese un valor: "))

# Comparar si el valor es mayor o igual que 10 y menor o igual que 20.
if valor >= 10 and valor <= 20:
    print("El valor está entre 10 y 20.")
else:
    print("El valor no está entre 10 y 20.")

estado = bool(input("Ingrese 1 o 0: "))

# Comparar si el estado es verdadero.
if estado == True:
    print("El estado es verdadero.")
else:
    print("El estado es falso.")

print("Fin del programa.")
