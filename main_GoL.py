import board_state


def main():
    while True:
        b_width = int(input("Digite ancho: "))
        b_heigth = int(input("Digite alto: "))
        if isinstance(b_width, int):
            if isinstance(b_heigth, int):
                break
        
    tablero = board_state.random_state(b_width,b_heigth)
    print(tablero)

if __name__ == "__main__":
    main()