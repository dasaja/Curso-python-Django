#Metodos diccionarios

estudiante = {
  "nombre": "Jose Diaz",
  "edad": 30,
  "nota_media": 7.25,
  "repetidor": False
}

#meotodo que devuelve las claves del diccionario
print(estudiante.keys())

#metodo me permite obtener los valores
print(estudiante.values())

#metodo pop
print(estudiante.pop("nombre"))
print(estudiante)

#metodo de limpiar todo el diccionario
estudiante.clear()
print(estudiante)

#Verifica si la clave de mi diccionario existe solo entero
numeros = {
  "nombre": "Andres",
  6: 600
}
clave = "nombres"
print( clave in numeros)

#permite borrar
del numeros["nombre"]
print(numeros)

#metodo pop
edades = {
  "jose": 30,
  "daniel": 25
}

edades.pop("jose")
print(edades)

