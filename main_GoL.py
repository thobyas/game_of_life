import board_state


def main():
    while True:
        b_width = int(input("Digite ancho: "))
        b_heigth = int(input("Digite alto: "))
        if isinstance(b_width, int):
            if isinstance(b_heigth, int):
                break
        
    board = board_state.random_state(b_width,b_heigth)
    old = board[1]
    next = board[0]
    for i in range(b_heigth):
       print(*old[i][:])
    print("mmmm")
    for i in range(b_heigth):
       print(*next[i][:])

if __name__ == "__main__":
    main()