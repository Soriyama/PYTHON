# Titulo: Variables
# Description: Variables en Python
# Tarea: Crear un programa que solicite el nombre al usuario y su edad y lo imprima en pantalla junto con su tipo de dato.
# Autor: Soriyama
# Funciones: input(), print()
# Para las variables no es necesario declarar el tipo de dato.
# Tipos de datos de Python: int, float, str, bool, list, tuple, dict, set
# input() solicita un valor al usuario. Este valor es de tipo cadena.
# print() imprime un mensaje en pantalla.
# Las variables son contenedores de datos. Se pueden almacenar diferentes tipos de datos en una variable.
# Se pueden reasignar valores a una variable.
# Se pueden concatenar variables de tipo cadena. + es el operador de concatenación.
# Se pueden convertir variables de un tipo a otro. int(), float(), str(), bool()
# Se pueden imprimir variables de diferentes tipos en una sola línea.
# Se pueden asignar varios valores a diferentes variables en una sola línea.
# Se pueden asignar el mismo valor a diferentes variables en una sola línea.

# Solicitar el nombre al usuario.
nombre = input("Ingrese su nombre: ")
# Solicitar la edad al usuario.
edad = int(input("Ingrese su edad: "))
# Imprimir el nombre y la edad del usuario.
print("Su nombre es " + nombre)
print("Su edad es " + str(edad) + " años.")
# Imprimir el tipo de dato de la variable nombre.
print("El tipo de dato de la variable nombre es " + str(type(nombre)))
# Imprimir el tipo de dato de la variable edad.
print("El tipo de dato de la variable edad es " + str(type(edad)))