#LAMBA -MAP- FILTER
#Integra función de datos y 

#MAP
"""
MAP=> permite asignar una función a un obejto iterable.
"""
"""def cuadrado(num):
    return num **2
print(cuadrado(2)) 

numeros = [1,2,3,4,5]
#map(cuadrado de números)
print(list(map(cuadrado, numeros)))"""

#Resuelto correcto
"""def cuadrado(num):
  return num **2

numeros = [1,2,3,4,5]

print(list(map(cuadrado, numeros)))"""


#Ejercicio dos
"""def Letras_par(mystring):
    if len(mystring) %2 == 0:
        return "par"
    else:
        return mystring [0]

nombre = ["John", "Jose" , "Kelly", "Daniel", "Ana"]

print(list(map(Letras_par, nombre)))"""


#Resuelto
"""def letras_par(mystring):
  if len(mystring) %2 == 0:
    return 'par'
  else:
    return mystring[0]

nombre = ['John', 'Jose', 'Kelly', 'Daniel','Ana']

print(list(map(letras_par,nombre)))"""


#FILTER
"""
Filter => Es una función que permite el filtro de valores 
teniendo un objeto iterable
"""
"""def validar_par(num):
    
numeros = [0,1,2,3,4,5,6,7,8,9,10]

print(list(filter(validar_par, numeros)))"""


#Validando los multiplos de 5
def multiplos_decinco(num2):
    return num2 % 5 == 0
numeros = [0,1,2,3,4,5,6,7,8,9,10]

print(list(filter(multiplos_decinco, numeros)))



#LAMBDA
"""
Lambda => Permiten crear funciones anonimas, 
sin definir las funciones, no tiene un bloque de declaraciones.
Maneja tareas más grandes.
"""
def cuadrado(num): result = num**2
print(cuadrado(2))    
lambda num: num**2

#Función
cuadrado = lambda num: num**2
#Ejecutar
print(cuadrado(2))
print(cuadrado(3))


#Usar map y lambda para sacar el cuadro

numeros = [0,1,2,3,4,5]

lambda num: num**2

print(list(map(lambda num: num**2, numeros)))



#Filtrar pares usando lambda

numeros = [0,1,2,3,4,5,6,7,8,9,10]

print(list(filter(lambda num: num % 2 == 0, numeros)))



#RESUELTO POR EL PROFESOR
"""
lambda => funcion anonima, no tiene un bloque de declaraciones, maneja tareas mas grandes.
"""
numeros = [1,2,3,4,5,7,8,9,10]

print(list(map(lambda num: num ** 2, numeros)))


caracter = lambda s: s[::-1]
print(caracter('hola'))