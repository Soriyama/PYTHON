# Título: Datos numéricos y  operaciones
# Description: Operaciones matemáticas básicas en Python
# Tarea: Crear un programa que solicite dos números al usuario y realice las operaciones de suma, resta, multiplicación y división.
# Autor: Soriyama
# Funciones: input(), int(), float(), print()
# Para las variables no es necesario declarar el tipo de dato.
# input() solicita un valor al usuario. Este valor es de tipo cadena.
# int() convierte el valor ingresado a un número entero.
# float() convierte el valor ingresado a un número decimal.
# print() imprime un mensaje en pantalla.
# Se pueden realizar operaciones matemáticas básicas en Python. +, -, *, /, %, **, //, divmod()
# + suma dos números.
# - resta dos números.
# * multiplica dos números.
# / divide dos números.
# % obtiene el residuo de una división.
# ** eleva un número a una potencia.
# // obtiene la parte entera de una división.
# divmod() obtiene el cociente y el residuo de una división.
# Se pueden realizar operaciones matemáticas con variables de diferentes tipos. int, float
# Se pueden realizar operaciones matemáticas en una sola línea.
# En print() se convierten las variables a cadena para poder imprimirlas.

# Solicitar el primer número al usuario.
numero1 = int(input("Ingrese el primer número: "))
# Solicitar el segundo número al usuario.
numero2 = int(input("Ingrese el segundo número: "))
# Realizar la operación de suma.
suma = numero1 + numero2
# Realizar la operación de resta.
resta = numero1 - numero2
# Realizar la operación de multiplicación.
multiplicacion = numero1 * numero2
# Realizar la operación de división.
division = numero1 / numero2
# Realizar la operación de residuo.
residuo = numero1 % numero2
# Realizar la operación de potencia.
potencia = numero1 ** numero2
# Realizar la operación de parte entera.
parte_entera = numero1 // numero2
# Realizar la operación de cociente y residuo.
cociente, residuo = divmod(numero1, numero2)
# Imprimir los resultados de las operaciones.
print("La suma de " + str(numero1) + " y " + str(numero2) + " es " + str(suma))
print("La resta de " + str(numero1) + " y " + str(numero2) + " es " + str(resta))
print("La multiplicación de " + str(numero1) + " y " + str(numero2) + " es " + str(multiplicacion))
print("La división de " + str(numero1) + " y " + str(numero2) + " es " + str(division))
print("El residuo de " + str(numero1) + " y " + str(numero2) + " es " + str(residuo))
print(str(numero1) + " elevado a la " + str(numero2) + " es " + str(potencia))
print("La parte entera de la división de " + str(numero1) + " y " + str(numero2) + " es " + str(parte_entera))
print("El cociente de la división de " + str(numero1) + " y " + str(numero2) + " es " + str(cociente))
print("El residuo de la división de " + str(numero1) + " y " + str(numero2) + " es " + str(residuo))
print("Fin del programa.")
