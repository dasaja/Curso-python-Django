"""
Escribir un programa que guarde en una variable el diccionario 
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y 
muestre su símbolo o un mensaje de aviso 
si la divisa no está en el diccionario.
"""

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce la Divisa: ")
print(monedas.get(moneda.tittle(), "La divisa no está"))

Profe
monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
modena = input("Introduce la divisa: ")
print(monedas.get(modena.title(), "La divisa no esta"))

#ejercio2
"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y 
teléfono y lo guarde en un diccionario. 
Despúes debe mostrar por pantalla el mensaje
 `<nombre> tiene <edad> años, vive en <dirección> 
y su número de teléfono es <teléfono>`. 
"""

nombre = input("Indique su nombre:")
edad = input("Coloque su edad:")
dirección = input("Coloque su dirección:")
telefono = input("Coloque su teléfono")
