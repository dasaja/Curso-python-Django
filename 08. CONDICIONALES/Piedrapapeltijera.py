import random

piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

juego_imagenes = [piedra, papel, tijera]

#eleccion del usuario                      
eleccion_usuario = int(input("¿Que eliges? Escribe 0 para Piedra, 1 para Papel o 2 para Tijera.\n"))
print(juego_imagenes[eleccion_usuario])

#eleccion de la computadora
#random es utilizado para valores aleatorios
eleccion_computadora = random.randint(0, 2)
print("Eleccion de la computadora")
print(juego_imagenes[eleccion_computadora])

#condiciones del juego
if eleccion_usuario >= 3 or eleccion_usuario < 0:
  print("!Escribimos un numero invalido, pierdes!")

elif eleccion_usuario == 0 and eleccion_computadora == 2:
  print("Tu Ganas! 🍷")

elif eleccion_computadora == 0 and eleccion_usuario == 2:
  print("Tu  Pierdes! 😑")

elif eleccion_computadora > eleccion_usuario:
  print("Tu Pierdes! 😑")

elif eleccion_usuario > eleccion_computadora:
  print("Tu Ganas! 🍷")

elif eleccion_computadora == eleccion_usuario:
  print("Esto es Empate 🆙")








