# Título: Entradas y Salidas
# Description: Entradas y salidas en Python
# Tarea: Crear un programa que solicite un número al usuario y lo imprima en pantalla usando comodines y formato.
# Autor: Soriyama
# Funciones: input(), print(), %, format()
# input() solicita un valor al usuario. Este valor es de tipo cadena.
# print() imprime un mensaje en pantalla.
# % es un comodín que se utiliza para formatear cadenas.
# format() es un método que se utiliza para formatear cadenas.
# Se pueden utilizar comodines para formatear cadenas. %d, %f, %s
# %d se utiliza para formatear números enteros.
# %f se utiliza para formatear números decimales.
# %s se utiliza para formatear cadenas.
# Se pueden utilizar comodines en una cadena para formatearla.

# Solicitar un entero al usuario.
numero = int(input("Ingrese un número entero: "))

# Solicita el número decimal.
decimal = float(input("Ingrese un número decimal: "))
# Solicita una cadena, nombre.
nombre = input("Ingrese su nombre: ")

# Imprime el contenido de las variables usando comodines.
print("El número entero es %d, el número decimal es %f y el nombre es %s" % (numero, decimal, nombre))

# Imprime el contenido de las variables usando format().
print("El número entero es {}, el número decimal es {} y el nombre es {}".format(numero, decimal, nombre))

print("Fin del programa.")

