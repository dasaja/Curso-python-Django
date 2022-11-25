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

"""def sumar(num1, num2):
  return num1 + num2 


def restar(num1, num2):
  return num1- num2


def multiplicar(num1, num2):
  return num1 * num2

def dividir(num1, num2):
  return num1 / num2


resultado = dividir(5,5)
print(resultado)"""

#Ejemplo 2

"""def verificar_par(numero):
  return numero % 2 == 0


r = verificar_par(2)
print(r)

r2 = verificar_par(5)
print(r2)"""

#Ejercicio 3
"""def verificar_pares_lista(num_list):
  for number in num_list:
    if number % 2 == 0:
      return True 
    else:
      pass
  return False

r = verificar_pares_lista([2,5,6])
print(r)"""

#Devolver todos los números pares en una lista
#[1,2,3,4,5,6]
#Mostrar todos los pares   
#[2,4,6]
#Arreglar ejercicio
"""def verificar_pares_lista(num_list):
  lista_numeros()
  for number in num_list:
    if number % 2 == 0:
      return number.append(verificar_pares_lista)
    else:
      pass
  
r = verificar_pares_lista([1,2,3,4,5,6])
print(r)
"""

#Ejercicio Profe

"""def check_par_list(num_list):
    
    even_numbers = []
    
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
        
    return even_numbers

r = check_par_list([1,3,5,2,6,8])
print(r)"""


#Ejercicio profe 2
"""def f(x): return 2*x**2+1

print(f(2))"""

#Crear dos funciones : 1ra retorne los cuadrados.
#función 2 que retorne los cubos.
def f(n):
  y = n**2
  return y

def x(n):
  c = n**3
  return c

r1 = f(3)
print(r1)

r2 = x(2)
print(r2)


#parametros por omision
def fun(a,b=0):
  print(a,b)

print(fun(3,5))
print(fun(3))


