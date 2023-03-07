#b_width : board width
#b_height : board height


import numpy as np
import random


def random_state(b_width = int, b_height = int):
    board = np.random.randint(0,2,size=(b_height,b_width))
    return board
    

       


# for i in range(num):
#         matx.append(" ")
#     for j in range(num):
#         maty.append(matx.copy())
