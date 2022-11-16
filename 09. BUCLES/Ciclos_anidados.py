#crear proyecto barras
#ciclos anidados

from random import *

for i in range(10):
  n = randint(1,20)
  barra = ''
  for j in range(1, n+1):
    barra +=  '*'
  print('%4d ' %n, barra)

#Ciclos anidados

from random import *

for i in range(10):
    n = randint(1,20)
    barra = ""
    for j in range (1, n +1):
        barra = barra + "*"
    print("%4d" %n, barra) 

#pareja de numeros

for a in [1,2,3]:
    print(a)
  for b in [1,2,3]:
    print(b)

#pareja de números

for a in [1,2,3]:
    for b in [1,2,3]:
        print(a,b)


#meses
for m in ['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']:
  print('Mes: ', m)
  for s in range(1,5):
    print('Semana: ', s)


# WHILE
#Factores primos de un numeros entero
x = int(input('Ingresar el dato: '))
n = 2
while n<=x:
  while x%n == 0:
    print('Divisor: ', n)   
    x=x/n 
  n=n+1

  #FOR
  #a2 + b2 = c2

for a in range(1,21):
  for b in range(1,21):
    for c in range(1,21):
      if a**2+b**2==c**2:
        print(a,b,c)

 #verifica tautologia
for a in [True, False]:
  for b in [True, False]:
    for c in[True , False]:
      p = not((a and b)) or (a or c)
      print(a,b,c, " = ",p)       

 #FOR 
 #break 
#Simulador lanzamiento de un dado
from random import *
n = int(input('Cantidad maxima de lanzamientos: '))
for i in range(n):
  x = randint(1, 6)
  print(x)
  if x == 5:
    print("Lanzamiento en el cual salio el 5: ", i + 1)
    break     

#break /operadores utilitarios
salida = False
for i in range(1,10):
  for j in range(1,10):
    n=2*i**3+3*j**2
    if n%7 ==0:
      print(i,j,n)
      salida = True
      break
  if salida:
    break

#uso continue /operadores utilitarios

x = [23,45,-34,27,-82,56]
s = 0
for n in x:
  if n<0:
    continue
  s =s+n
print(s)

#pass /operadores utilitarios
m = 20
if m in [1,3,5,7,8,10,12]:
  print("Mes de 31 dias")
else:
  pass


