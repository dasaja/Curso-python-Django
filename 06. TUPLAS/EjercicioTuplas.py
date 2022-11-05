#(LISTAS - TUPLAS) 
"""
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla. 
"""

Materias = [ "Matemáticas", "Física", "Química", "Historia", "Lengua"]
print(Materias)

print(f"Yo estudio :" , (Materias[1]))
print(f"Yo estudio :" , (Materias[2]))
print(f"Yo estudio :" , (Materias[3]))
print(f"Yo estudio :" , (Materias[4]))

"""
Escribir un programa que pregunte al usuario los números 
ganadores de la lotería primitiva, los almacene en 
una lista y los muestre por pantalla ordenados de menor a mayor.
"""
#Num1 = int(input("Ingrese el primer número"))
#Num2 = int(input("Ingrese el segundo número"))
#Num3 = int(input("Ingrese el tercer número"))
"""
Escribir un programa que pregunte al usuario los 
números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla
"""
ganadores = input("Ingrese numeros ganadores: ")
usuarios = []

usuarios.append(ganadores)
print(usuarios)

"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""

word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
print(word)

reversed_word = list(reversed_word)
reversed_word.reverse()
print(reversed_word)