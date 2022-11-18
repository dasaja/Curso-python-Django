#1 de un texto se impriman palabras que conmience con 's'

"""st = "La suma total de dos valores s daria como resultado la sumatoria de los valores"

for p in st.split():
  if p[0] == 's':
    print(p)"""


#2 imprimir valores de 0 al 10 y me muestre los pares   

"""for i in range (0, 11, 2):
    print(i)"""

#3 Revise la cadena y verifique si la longitud de la palabra es par o impar

st = "Escribe cada palabra de esta oración que tenga un número par de letras"   
     
"""for w in st.split():
  if len(w)%2 == 0:
    print(w, "<--- longitud par")
  else:
    print(w, "<-- longitud Impar")"""


#4 ejercicio

"""
Escriba un programa que imprima los números enteros del 1 al 100. Pero para los múltiplos de tres, imprima "Fizz" en lugar del número, y para los múltiplos de cinco, imprima "Buzz". Para números que son múltiplos de tres y cinco, escriba "FizzBuzz".
"""

for num in range(1,101):
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  elif num %3 == 0:
    print("Fizz")
  elif num %5 == 0:
    print("Buzz")
  else:
    print(num)

#5 Desafio de juego de adivinanzas
import random

num = random.randint(1, 100)

print("Bienvenido a adivinar")
print("Estoy pensando en un número entre 1 y 100")
print("si tu suposcion está a más de 10 de mi número, te diré que tienes FRÍO")
print("Si tu suposicion está dentro de 10 de mi número, le diré que está CALIENTE")
print("Si tu suposicion está más lejos que su conjetura más reciente, diré que se está volviendo MÁS FRÍO")
print("Si tu suposicion está más cerca que su conjetura más reciente, diré que está Más Caliente")


#Desafio juego de adivinanzas
import random

num = random.randint(1, 100)

print("Bienvenido a adivinar")
print("Estoy pensando en un número entre 1 y 100")
print("si tu suposcion está a más de 10 de mi número, te diré que tienes FRÍO")
print("Si tu suposicion está dentro de 10 de mi número, le diré que está CALIENTE")
print("Si tu suposicion está más lejos que su conjetura más reciente, diré que se está volviendo MÁS FRÍO")
print("Si tu suposicion está más cerca que su conjetura más reciente, d
==========
while True:

  adivinar = int(input("Estoy pensando en un numero entre 1 y 100.\n ¿Cual es tu suposion?"))

  if adivinar < 1 or adivinar > 100:
    print("FUERA DE LOS LIMITES intentalo de nuevo")
    continue

  #aqui comparamos la adivinaza del jugador con nuestro numero
  if adivinar == num:
    print(f"Enhorabuena, lo adivinaste en solo {len(suposiciones)} Oportunidades!!")
    break

#Si la suposicion es incorecta , agregar la suposicion ala lista
  suposiciones.append(adivinar)

  if suposiciones[-2]:
    if abs(num-adivinar) < abs(num-suposiciones[-2]):
      print("Caliente")
    else:
      print("Mas Frio")
  else:
    if abs(num-adivinar) <= 10:
      print("Tibio")
    else:
      print("Frio")



