#CREAR PROGRAMA DE GALLETAS DE ANIMALES
"""Escribir una función que toma una cadena de 
dos palabras y devuelva True si ambas palabras 
comienzan con la misma letra

=====Salida de consola =====
Galletas_animales("Llueve Llama") -- True
Galletas_animales("Llueve gotas)-- False
"""
"""def galletas_animales(text):
    lista_palabra = text.split()
    #print(lista_palabra) debuguer para hacer pruebas de los ejercicios.
    return lista_palabra [0][0] == lista_palabra [1][0]

print(galletas_animales("Llueve gato"))"""

#Ejercicio Profe
"""def galletas_animales(text):
  lista_palabra = text.split()
  print(lista_palabra)
  return lista_palabra[0][0] == lista_palabra[1][0]

print(galletas_animales('llueve llave'))"""

"""Dados 2 números enteros, devuelva True 
si la suma de los 2 enteros es 20 o si uno
de los enteros es 20. DE lo contrario, devuelve False

====Salida de consola====
hacer_veinte(20,10) -->True
hacer_veinte(12,8) --> True
hacer_veinte(2,3) --> False

"""
#Ejercicio Daniel
"""def Hacer_veinte(a,b):
    if a == 20 or b == 20 or a+b == 20:
     print(True)
    else:
     return(False)


print(Hacer_veinte(20,10))
print(Hacer_veinte(3,10))
print(Hacer_veinte(9,11))"""

#Corrección del código / Profe
"""def hacer_veinte(n1,n2):
  return (n1 + n2) == 20 or n1==20 or n2==20

print(hacer_veinte(20,10))
print(hacer_veinte(12,8))
print(hacer_veinte(3,2))"""

#Ejercicio 3
"""
Escriba una función que escriba en Mayuscula
la primera y cuarta letra de un nombre

====Salida de consola====
old_macdonald("macdonald")
"MacDonald """

def old_macdonald(name):
  if len(name) > 3:
    return name[:3].capitalize() + name[3:].capitalize()

  else:
    return '¡El nombre es muy corto!'

print(old_macdonald('macdonald'))

#Ejercicio Corrección/Profe

def old_macdonald(name):
  if len(name) > 3:
    return name[:3].capitalize() + name[3:].capitalize()
  else:
    return '¡El nombre es muy corto!'

print(old_macdonald('macdonald'))