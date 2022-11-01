#ejercios en listas
#dada la siguiuente lista [12,23,5,29,92,64] realiza las siguientes oerpaciones y se ve mostrando la lista resultante

""" 
1. Elimina el ultimo numero y anadelo al pricipio
[64,12,23,5,29,92]
2. Mueve el segundo elemento a la ultima posicion.
3. Anade el numero 14 al comienzo de la lista
4. Suma todos los numeros de la lista y anade el resultado al final de la lista 
5. Fusiona la lista actual con la siguiente: [4, 11, 32]
6. Elimina todos los numeros de la lista
"""

from re import L


Lista = [12,23,5,29,92,64]
Lista.pop()
print(Lista)

Lista2 = Lista 
Lista2.insert(0,64)
print(Lista)

Lista.insert(0,14)
print(Lista)

suma = (14 + 64 + 12 + 23 + 5 + 29 + 92)
print(suma)

Lista3 = Lista
Lista.append(239)
print(Lista)

valores = (4, 11,32)
Lista.extend(valores)
print(Lista)

Lista.clear()
print(Lista)
