#b_width : board width
#b_height : board height


import numpy as np
import random


def random_state(b_width = int, b_height = int):
    board = np.random.randint(0,2,size=(b_height,b_width))
    new_board = next_board_state(board)
    #new_board = render(board)
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
    zeros_row = np.zeros(shape = (1,columns), dtype=int)
    columns_row = np.zeros(shape = (rows+1,1), dtype=int)
    test_board = np.append(zeros_row, inicial_board, axis = 0)
    #test_board = np.append(inicial_board, zeros_row, axis = 0)
    test_board = np.append(columns_row, test_board, axis = 1)
    test_board = np.append(test_board, columns_row, axis = 1)

    return test_board
        
            



