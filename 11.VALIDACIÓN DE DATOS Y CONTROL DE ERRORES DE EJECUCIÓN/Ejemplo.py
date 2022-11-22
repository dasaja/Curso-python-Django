"""correcto = False 

while not correcto:
  try:
    correcto = True
    n = int(input('Cantidad de datos:'))
  except ValueError:
    correcto = False
    print('Cantidad incorrecta')

s = 0
for i in range(n):
  x = int(input("Ingrese dato: "))
  s += x 
print('Suma: ', s)"""



#Ejemplo 2 try/except

"""try:
  f = open("testfile", "r")
  f.write("Test write this")
except IOError:
  print("Error: Nose pudo encontrar el archivo o leer datos")
else:
  print("Contendio escrito con exito")
  f.close()"""

#Problema 1: ELevar los valores al cuadrado
"""try:
  for i in [2,3,5]:
    print(i**2)
except:
  print("Ocurrio un error")

#Problema 2: División 

x = 5
y= 0

try:
  d = x/y
  print(d)
except ZeroDivisionError:
  print("No se puede dividir por cero")
finally:
  print("Todo listo")"""


#Problema 3: Ingreso 2 resultado el cuadrado = 4

correcto = False

while not correcto:

  try:
    correcto = True
    n = int(input('Ingrese el número entero:'))
    print(n**2)

  except ValueError:
    correcto = False
    print('Cantidad incorrecta') 

#Opción 2

while True:
  try:
    n = int(input("Ingrese un entero: "))
  except:
    print("Ha ocurrido un error !!")
    continue
  else:
    break

print('El numero al cuadrado es: ', n**2)