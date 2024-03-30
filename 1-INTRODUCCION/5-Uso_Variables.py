# Uso de variables en Python
# Descripción: En este programa se muestra cómo se utilizan las variables en Python. Se realizará una calculadora simple.
# Autor: Soriyama
# Funciones: input(), print(), type(), int(), float(), str(), bool()
# Operaciones: +, -, *, /, %, **, //, divmod(), and, or, not, ==, !=, <, >, <=, >=, +=, -=, *=, /=
# Tipos de datos de Python: int, float, str, bool
# + suma dos números o concatena dos cadenas.
# - resta dos números.
# * multiplica dos números.
# / divide dos números.
# % obtiene el residuo de una división.
# ** eleva un número a una potencia.
# // obtiene la parte entera de una división.
# divmod() obtiene el cociente y el residuo de una división.
# and devuelve True si ambas condiciones son verdaderas.
# or devuelve True si al menos una de las condiciones es verdadera.
# not devuelve True si la condición es falsa.
# == devuelve True si los valores son iguales.
# != devuelve True si los valores son diferentes.
# < devuelve True si el primer valor es menor que el segundo.
# > devuelve True si el primer valor es mayor que el segundo.
# <= devuelve True si el primer valor es menor o igual que el segundo.
# >= devuelve True si el primer valor es mayor o igual que el segundo.
# += suma un valor ingresado al valor de la variable.
# -= resta un valor ingresado al valor de la variable.
# *= multiplica un valor ingresado al valor de la variable.
# /= divide un valor ingresado al valor de la variable.


# Solicitar el primer número al usuario.
numero1 = int(input("Ingrese el primer número: "))
# Solicitar el segundo número al usuario.
numero2 = int(input("Ingrese el segundo número: "))
# Realizar la operación de suma.
suma = numero1 + numero2

# Realiza una suma al resultado anterior.
suma += int(input("Ingrese un número para sumar al resultado anterior: "))
print("La suma es " + str(suma))

print("Fin del programa.")


