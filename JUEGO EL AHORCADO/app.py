"""import random 


#TODO-1
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3
#Importación del logo hangman_art.py - inicio
from hangman_art import logo 
print(logo)

#testing
#print(f"Psst, la solución es {chosen_word}.")

#crear los espacios en blanco _____
display = []
for _ in range(word_lenght):
    display += "_"

while not end_of_game:
    guess = input("Adivina una letra: ").lower()

    #TODO-4
#Verificar si el usuario ha ingresado una letra que ya se adivinó
    if guess in display:
       print("Ya lo has adivinado {guess}")

#Comprobar la letra que vamos adivinar
    for position in range (word_lenght):
      letter = chosen_word[position]

      if letter == guess:
         display[position] = letter

 # SI la letra no esta en la palabra elegida mensaje de error
    if guess not in chosen_word:
       print(f"No adivinaste {guess},  esta no es la palabra. Pierde una vida")


 #TODO-5
       lives -= 1
       if lives == 0:
         end_of_game = True
         print("Tú Perdiste")
         print(f"Psst, la solución es {chosen_word}.")

#Unir todos los elementos de la lista a un palabra completa
    print( f"{"". join(display)}" )

#Comprobar si el usuario llenó todas las letras para formar la palabra

    if "_" not in display:
      end_of_game = True
      print(etapas[])
       

#TODO-2
#Importar las etapas del Hangman_art.py
from hangman_art import etapas
print(etapas[lives])"""

import random
#TODO-1: - 
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hagman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
from hangman_art import logo
print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

#TODO-4: - 
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - 
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Tu pierdes.")
            print(f'Pssst, the solution is {chosen_word}.')

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("Tu ganaste.")

    #TODO-2: - 
    from hangman_art import etapas
    print(etapas[lives])




