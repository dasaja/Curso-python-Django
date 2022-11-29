#Ejercicio 1
"""Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!."""

print("¡Hola Mundo!")

#Ejercicio 2 
"""Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable."""

Variable = "¡Hola Mundo!"
print(Variable)

#Ejercicio 3
"""Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido."""

Nombre = input("Cuál es tu nombre?:" "\n")
print("¡ Hola", Nombre,"!" )

#Ejercicio 4
"""Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética (3+2/2*5)al cuadrado """

Resultado = (((3+2)/(2*5))**2)
print(Resultado)

#Ejercicio 5
"""Escribir un programa que pregunte al usuario 
por el número de horas trabajadas y el coste por hora. 
Después debe 
mostrar por pantalla la paga que le corresponde."""

Num_horas = int(input("Cuál es el número de horas trabajadas?: "))
Coste_horas = float(input("Cuál es el costo por hora?: "))
paga = Num_horas * Coste_horas

print("Tu pago es", paga)
