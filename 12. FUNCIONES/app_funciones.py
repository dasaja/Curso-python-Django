#METODOS 
#definicion => realiza acciones especificas es un objeto.
"""lista = [1,2,3,4]
print(lista)
lista.append(5)
print(lista)"""

#FUNCIONES 
#definicion => blques de codigo 

#sintaxis de la funcion
#palabra clave llamada (def)
#() llamar a una funcion
#(a, b) acepta parametros
#usa return 
#agregamos la logica 
#agregar multiples return 
#agregar blucles for
#desempaquetamiento de tuplas
#interaccion entre funciones

#Estructura básica 
#def name_de_funcion(a , b):

#crear una funcion simple
"""def decir_hola():
  print('Hola')

#llamar la funcion
decir_hola()
decir_hola()"""

#Parámetro
#crear una funcion simple
#aceptan parametros
"""def saludar(name):
  print(f'Hola {name}')

#llamar la funcion
saludar('Daniel')"""


"""def decir_Adios(name):
  print( f"Adios {name}" )
  
decir_Adios("Daniel") """

#crear un return
#crear funcion sumar

def sumar(num1, num2):
  return num1 + num2 


def restar(num1, num2):
  return num1- num2


def multiplicar(num1, num2):
  return num1 * num2

def dividir(num1, num2):
  return num1 / num2


resultado = restar(5,5)
print(resultado)
