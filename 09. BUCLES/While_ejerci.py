#Ejercicio 1

"""
20 = 10100
"""

n = int(input('Ingrese un entero positivo: ' ))
b = ''
while n > 0:
  d = n%2
  n = n//2
  b = str(d)+b
print('Numero binario: ', b)


#Ejercicio 2

#juego de la rana
from random import * 
x =0
y=0

i=0

while -5<x<5 and -5<y<5:
  d= randint(1,4)
  i+=1
  if d ==1:
    x = x + 1
  elif d == 2:
    x = x - 1
  elif d == 3:
    y = y + 1
  else:
    y = y-1
  print(x , y)

print('Cantidad de intentos: ', i)


#Ejercicio 3

#lanzar dado

from random import*
c=0
x =0
while x!=5:
  x=randint(1,6)
  print(x)
  c += 1
print('Lanzamiento en el cual salio el 5: ',c)

#Ejercicio 4

from random import *

x = randint(1, 100)
i=0
salida = False

while not salida:
  i=i+1
  n=int(input('Adivine el numero: '))
  if n == x:
    print('Adivino en ', i, 'intentos')
    salida=True
  else:
    if n < x:
      print('Muy pequeno el valor')
    else:
      print('Muy grande el valor')
      