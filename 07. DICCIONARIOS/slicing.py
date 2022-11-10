alumnos = {
  'nombre':['Jose', 'maria'],
  'edad':20,
  'notas': [13,15,16,18]
}

print(alumnos['notas'])
print(alumnos['notas'][0])
print(alumnos['nombre'][1].upper())

#anidacion de diccionarios
d = {'direccion':{'provincia':{'nombre': 'Loja'}}}
print(d)
print(d['direccion']['provincia']['nombre'])

#metodo para retornar una tupla 
print(d.items())