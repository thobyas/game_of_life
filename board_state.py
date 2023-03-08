#b_width : board width
#b_height : board height


import numpy as np
import random


def random_state(b_width = int, b_height = int):
    board = np.random.randint(0,2,size=(b_height,b_width))
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
    rows = np.shape(inicial_board)[0]
    columns = np.shape(inicial_board)[1]
    
    test_board = np.append(np.zeros(rows, dtype= int))
        
            



