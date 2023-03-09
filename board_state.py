#b_width : board width
#b_height : board height


import numpy as np
import random


def random_state(b_width = int, b_height = int):
    board = np.random.randint(0,2,size=(b_height,b_width)) #inicializo con eltablero con los estados    
    new_board = next_board_state(board)
    new_board = render(board)
    return new_board
    

def render(board):
    render_board = []
    rows = np.shape(board)[0]
    columns = np.shape(board)[1]
    for i in range(rows):
        rows_val = []
        for j in range(columns):
            if board[i,j] == 0:
                rows_val.append(" ")
            else:
                rows_val.append("#")
        render_board.append(rows_val) 

    return render_board    
             
def next_board_state(inicial_board):
    next_row =[]

    #Creo un marco de 0 para evitar contar las esquinas (Problemas para crear marco inferior)
    test_board = []
    rows = np.shape(inicial_board)[0]
    columns = np.shape(inicial_board)[1]
    zeros_row = np.zeros(shape = (1,columns), dtype=int)
    columns_row = np.zeros(shape = (rows+1,1), dtype=int)
    test_board = np.append(zeros_row, inicial_board, axis = 0)
    #test_board = np.append(inicial_board, zeros_row, axis = 0) # no funiciona correctamente
    test_board = np.append(columns_row, test_board, axis = 1)
    test_board = np.append(test_board, columns_row, axis = 1)

    #Calculo el estado
    next_board = []
    for i in range(rows): 
        next_row = []
        if i != rows-1:
            for j in range(columns):
                next_state = 0
                next_state = test_board[i][j]+test_board[i][j+1]+test_board[i][j+2]+test_board[i+1][j]+test_board[i+2][j]+test_board[i+1][j+2]+test_board[i+2][j+2]+test_board[i+2][j+1]
                if test_board[i+1][j+1] == 0:
                    if next_state == 3:
                        next_row.append(1)
                    else:
                        next_row.append(0)
                else:
                    if (next_state < 2) or (next_state > 3):
                        next_row.append(0)
                    else:
                        next_row.append(1)
            next_board.append(next_row)
        else:
            #Prueba de ultima fila
            for j in range(columns):
                next_state = 0
                next_state = test_board[i][j]+test_board[i][j+1]+test_board[i][j+2]+test_board[i+1][j]+test_board[i+1][j+2]
                if test_board[i+1][j+1] == 0:
                    if next_state == 3:
                        next_row.append(1)
                    else:
                        next_row.append(0)
                else:
                    if (next_state < 2) or (next_state > 3):
                        next_row.append(0)
                    else:
                        next_row.append(1)
            next_board.append(next_row)
    return next_board
        
            



