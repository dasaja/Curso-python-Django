#Ejercicio 1
"""Escribir una función que muestre por pantalla 
el saludo ¡Hola amiga! cada vez que se la invoque."""

def Saludo ():
  print("¡Hola amiga!")
  return

#Saludo()
#Saludo()

#Ejercicio 2
"""Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!."""

def Bienvenida(nombre):
  print("¡ Hola" ,nombre , "!")
  return
#Bienvenida("Daniel")

#Bienvenida("Arturo")
#Bienvenida("Ana")
#Bienvenida("Daniel")

#Ejercicio 3
"""Escribir una función que reciba un número entero positivo y devuelva su factorial."""

def factorial (num1):
  entero = 1
  for i in range(num1):
    entero *= i + 1
  return entero
  
print(factorial(20))  

#Ejercicio 5
"""Escribir una función que calcule el total de una factura tras aplicarle el IVA.
 La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
 Si se invoca la función sin
 pasarle el porcentaje de IVA, deberá aplicar un 21%"""

