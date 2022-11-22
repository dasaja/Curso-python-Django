"""
VALIDACION DE DATOS Y CONTROL DE ERRORES DE EJECUCION
"""

#DADO UN NUMERO ENTERO , DETERMINE CUANTAS CIFRAS TIENE

# n = int(input("Ingrese un entero positivo: "))
# c = 0

# while n>0:
#   n = n//10
#   c = c + 1
# print('cantidad de cifras: ', c)


#Ejemplos 
#x = 1/0
#ZeroDivisionError: division by cero

#x = 2*t+1
#NameError: name 't' is not defined

#x = int(input('Ingrese un entero: '))
#ValueError: invalid literal for int() with base 10: '4.5'

#from funciones import *
#ModuleNotFoundError: No module named 'funciones'


#try:
 #escribir las instrucciones que se desea detectar (excepcion) 

#except error:
  #escribir las instruciones que deseamos realizar si 
  #hay una exception



#try:
  #operacines control del codigo
  #except ExceptionI:
  #Si hay ExcepcionI, se ejecuta este bloque
  #except ExceptionII:
    #Si hay ExcepcionII, se ejecuta este bloque
  #else:
    #si no hay excepcion, ejecuta este blqoue

#try:
  #operacines control del codigo
  #except ExceptionI:
  #Si hay ExcepcionI, se ejecuta este bloque
  #except ExceptionII:
    #Si hay ExcepcionII, se ejecuta este bloque
  #else:
    #si no hay excepcion, ejecuta este blqoue

try:
  f = open("testfile", "r")
  f.write("Test write this")
except IOError:
  print("Error: Nose pudo encontrar el archivo o leer datos")
else:
  print("Contendio escrito con exito")
  f.close()


#finally
#=> Siempre se ejecuta independientemente si hubo o no la exeption 

try:
  f = open("testfile", "w")
  f.write("Texto de prueba")
  f.close()
finally:
  print("Este bloque siempre se ejecuta")  