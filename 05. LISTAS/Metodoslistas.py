#Metodos con listas
#append => insertar un valor al final de la lista
alumnos = ["Jose", "Daniel"]
alumnos.append("Maria")

#insert => instar un valor en la posicion 0
alumnos.insert(1, "Emilia")
print(alumnos)

#remove => eleminar la primera aparicion del elemento
#alumnos.remove("Jose")
#print(alumnos)

#pop => eliminar el ultimo elemto de la lista
alumnos.pop()
#print(alumnos)

#clear => elimina toda la lista
#alumnos.clear()
#print(alumnos)

#index => devolver el indice buscado
alumnos.index

#sort => permite ordenar elementos
alumnos.sort()
print(alumnos)

numeros = [2,3,6,9,7,8,1,4]
numeros.sort()
print(numeros)

#sorted => permite sacar una copia ordenada de la lista
sorted(numeros)
print(numeros) 
 
#reverse => permite ordenar la lista en orden inverso
numeros.reverse()
print(numeros)

#copy => devolver una copia de la lista
numeros.copy()
print(numeros)

#extend => fusionar dos listas
alumnos.extend(numeros)
print(alumnos)