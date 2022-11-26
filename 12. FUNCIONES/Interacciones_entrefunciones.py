# Interacciones entre funciones
#shuffle => barajear o dar la vuelta a una lista

from random import shuffle

"""example = [1,2,3,4,5]
shuffle(example)

print(example)"""

Lista = ["","0",""]

def barajear_lista(Lista):
    shuffle(Lista)
    return Lista

def jugador_adivinador():
    adivinar = ""
    while adivinar not in ["0", "1", "2"]:
        adivinar = input("Elige un número que va 0, 1 o 2: ")
    
    return int(adivinar)

def verificar_acierto (Lista, adivinar):
    if Lista[adivinar] == "0":
        print("Adivinanza correcta")
        #Se puede hacer un print para saber la posición o respuesta
        print(["","0",""])
    else:
        print("Equivocado, intenta nuevamente")
        print(Lista)

Lista_mezclada = barajear_lista(Lista)
adivinar = jugador_adivinador()

verificar_acierto(Lista_mezclada, adivinar)       