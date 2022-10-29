#Otros metos utiles de string
palabra = "ecuador"
frutas = ['manzana', 'banana', 'uvas', 'vamso a caminar', 'vamso a caminar']
#devuelve la longitud del string
print(len(palabra))
#convertir a mayusculas
print(palabra.upper())
#convertir a minisculas
print(palabra.lower())
#convierte la primera letra en mayuscula 
print(palabra.title())

#devuelve el numero de veces repetida el string
print(frutas.count("vamso a caminar"))
#devuelde un indice de la primera aparicion
print(palabra.find('e'))
#cambia el valor viejo por el nuevo
x = palabra
print(x)
x = palabra.replace("ecuador", "mexico")
print(x)
