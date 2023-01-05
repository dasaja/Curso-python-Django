"""
Requerimientos:
1-Dos jugadores deberán poder jugar el juego en la misma computadora
2-Imprimir cada vez que un jugador hace un movimiento.
3-Debe aceptar la entrada de la posición del jugador luego colocar
el símbolo en el tablero.  
"""
import random
"""
Paso1: Escribir una función que pueda imprimir un tablero como
una lista index(1-9) va ser igual a un tablero de 3x3
""" 
def mostrar_tablero(board):
   
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

test_board = ['#','X','O','X','O','X','O','X','O','X']
mostrar_tablero(test_board)

"""
Paso2: Escribir una función que pueda escribir la entrada del 
jugador sea "X" - "O", puede usar bucles
"""
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Quieres ser X o O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#player_input()

"""
Paso3: Escribir una función que tome el objeto de la lista del 
tablero, un marcador ("X" u "O"), posición (1, 9)
"""
def lugar_marcador(board, marker, position):
    board[position] = marker
#posicion_marcador(prueba_tablero, "$", 8)
#mostrar_tablero(prueba_tablero)    

"""
Paso4: Escribir la funcion que pone el tablero y verificar 
si ha ganado
"""
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle 
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

#print(ganador_check(prueba_tablero, 'X'))    


""" 
Paso5: Escribir la función que use el módulo aleatorio
"""
def escoger_primero():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

"""
Paso6. Escribir una función que devuelva un valor boleano
para indicar el espacio vacio
"""
def verificar_espacio(board, position):
    
    return board[position] == ' '

"""
Paso 7: Escribir una función que verifique si el tablero está
lleno o caso contrario.
"""  
def full_verificar_check(board):
    for i in range(1,10):
        if verificar_espacio(board, i):
            return False
    return True

"""
Paso8: Escriba una función que solicite la posición del jugador
(como un número del 1 al 9)
"""
def escoger_jugador(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not verificar_espacio(board, position):
        position = int(input('Elige tu proxima posicion: (1-9) '))
        
    return position

"""
Paso 9: Escribir una funcion que le pregunte al jugador si quiere volver a jugar
"""
def repetir():
    
    return input('Quieres volver a jugar? Enter Yes or No: ').lower().startswith('y')
"""
 Paso 10: Crear el ejecutor del juego
""" 
print('Bienvenido al juego 3 en raya')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = escoger_primero()
    print(turn + ' ira primero.')
    
    play_game = input('Estas listo para jugar? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            mostrar_tablero(theBoard)
            position = escoger_jugador(theBoard)
            lugar_marcador(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                mostrar_tablero(theBoard)
                print('Felicidades! tu has gando el juego!')
                game_on = False
            else:
               if full_verificar_check(theBoard):
                    mostrar_tablero(theBoard)
                    print('El juego empatado!')
                    break
               else:
                   turn = 'Player 2'
        else:
            # Player2's turn.
            
               mostrar_tablero(theBoard)
               position = escoger_jugador(theBoard)
               lugar_marcador(theBoard, player2_marker, position)                
               if win_check(theBoard, player2_marker):
                mostrar_tablero(theBoard)
                print('Player 2 ha ganado!')
                game_on = False
               else:
                 if full_verificar_check(theBoard):
                    mostrar_tablero(theBoard)
                    print('El juego es empatado!')
                    break
                 else:
                    turn = 'Player 1'

    if not repetir():
        break


      