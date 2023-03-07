#b_width : board width
#b_height : board height


import numpy as np
import random


def random_state(b_width = int, b_height = int):
    board = np.random.randint(0,2,size=(b_height,b_width))
    new_board = pretty_print(board)
    return new_board
    

def pretty_print(board):
    new_board = []
    rows = np.shape(board)[0]
    columns = np.shape(board)[1]
    for i in range(rows):
        rows_val = []
        for j in range(columns):
            if board[i,j] == 0:
                rows_val.append(" ")
            else:
                rows_val.append("#")
        new_board.append(rows_val) 

    return new_board    
             



