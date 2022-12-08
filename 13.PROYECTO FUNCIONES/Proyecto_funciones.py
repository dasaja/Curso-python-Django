"""
Requerimientos:
1-Dos jugadores deberán poder jugar el juego en la misma computadora
2-Imprimir cada vez que un jugador hace un movimiento.
3-Debe aceptar la entrada de la posición del jugador luego colocar
el símbolo en el tablero.  
"""
"""
Paso1: Escribir una función que pueda imprimir un tablero como
una lista index(1-9) va ser igual a un tablero de 3*3
""" 
def mostrar_tablero(tablero):
  print('   |   |')
  print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])
  print('   |   |')

prueba_tablero = ['#','X','O','X','O','X','O','X','O','X']
mostrar_tablero(prueba_tablero)

"""
Paso2: Escribir una función que pueda escribir la entrada del 
jugador sea "X" - "O", puede usar bucles
"""
def player_input():
  marcador = ''

  while not(marcador == 'X' or marcador == 'O'):
    marcador = input('Jugador 1: ¿Quieres ser X u O? ').upper()

  if marcador == 'X':
    return ('X', 'O')
  else:
    return ('o', 'x')

player_input()

"""
Paso3: Escribir una función que tome el objeto de la lista del 
tablero, un marcador ("X" u "O"), posición (1, 9)
"""
def posicion_marcador (pantalla, marcador, posición):
    pantalla [posición] = marcador
posicion_marcador(prueba_tablero, "$", 8)
mostrar_tablero(prueba_tablero)    

"""
Paso4: Escribir la funcion que pone el tablero y verificar 
si ha ganado
"""
def ganador_check(pantalla, marcador):
   return ((pantalla[7] == marcador and pantalla[8] == marcador and pantalla[9] == marcador) or 
    (pantalla[4] == marcador and pantalla[5] == marcador and pantalla[6] == marcador) or 
    (pantalla[1] == marcador and pantalla[2] == marcador and pantalla[3] == marcador) or
    (pantalla[7] == marcador and pantalla[4] == marcador and pantalla[1] == marcador) or(pantalla[8] == marcador and pantalla[5] == marcador and pantalla[2] == marcador) or 
    (pantalla[9] == marcador and pantalla[6] == marcador and pantalla[3] == marcador) or 
    (pantalla[7] == marcador and pantalla[5] == marcador and pantalla[3] == marcador) or 
    (pantalla[9] == marcador and pantalla[5] == marcador and pantalla[1] == marcador))

print(ganador_check(prueba_tablero, 'X'))    



    

