import board_state
import keyboard
import time
import os


def main():
    while True:
        b_width = int(input("Digite ancho: "))
        b_heigth = int(input("Digite alto: "))
        if isinstance(b_width, int):
            if isinstance(b_heigth, int):
                break
    
    
    while True:
        os.system("cls") # Clearing the Screen
        board = board_state.random_state(b_width,b_heigth)  
        for i in range(b_heigth):
            print(*board[i][:])
        time.sleep(0.5)
        if keyboard.is_pressed("o") :
            break
        

if __name__ == "__main__":
    main()