#José Diaz 19:23
#diccionarios
# tiene una clave y un valor
#se puede acceder a cada elemto solo con su clave

estudiante = {
  "nombre": "Jose Diaz",
  "edad": 30,
  "nota_media": 7.25,
  "repetidor": False
}

#acceder al valor de una clave
edad = estudiante["edad"]
print(edad)
nota_media = estudiante["nota_media"]
print(nota_media)

#actualizar el valor de un clave
estudiante["edad"] = 35
print(estudiante)

#agregar
estudiante["faltas_c"] = 10
print(estudiante)

#actualizar clave y valor
estudiante.update({'aprobados_C':'10'})
print(estudiante)
