#b_width : board width
#b_height : board height

import random


def random_state(b_width = int, b_height = int):
    board = []
    for i in range(b_width):
        board.append(random.randint(0,1))
        for j in range(b_height):
            pass

       


# for i in range(num):
#         matx.append(" ")
#     for j in range(num):
#         maty.append(matx.copy())
