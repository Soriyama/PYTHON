# Título: Introducción
# Description: Introducción a la programación en Python
# Tarea: Crear un programa que solicite la edad al usuario y determine si es mayor o menor de edad.
# Autor: Soriyama
# Funciones: input(), int(), if, else, print()
# Para las variables no es necesario declarar el tipo de dato.
# input() solicita un valor al usuario. Este valor es de tipo cadena.
# int() convierte el valor ingresado a un número entero.
# if evalúa una condición, si es verdadera ejecuta el bloque de código que está dentro de él.
# else se ejecuta si la condición del if es falsa.
# print() imprime un mensaje en pantalla.
# Las tabulaciones indican que un bloque de código está dentro de otro.
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Usted es mayor de edad.")
else:
    print("Usted es menor de edad.")
print("Fin del programa.")

# Path: 1-INTRODUCCION/2-Variables.py