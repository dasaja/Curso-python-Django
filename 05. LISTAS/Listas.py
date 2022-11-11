""" Listas
=> permiten guardar mas de un elemento dentro de una variable y
ademas puede hacerlo con diferentes tipos de datos 
"""

#Lista vacia 
lista_vacia = []

#lista con valores
alumnos = ["Maria","Veronica", "Anai", "Daniel"]
     
#acceder alos elementos
print(alumnos[0]) #muestra 0 elemento
print(alumnos[1]) #muestra 1 elemento
print(alumnos[2]) #muestra 1 elemento
print(alumnos[-1]) #muestra 3 elemento

#cambiar un elemento 
alumnos[0] = "Elena"
alumnos[-1] = "Jose"
print(alumnos)
