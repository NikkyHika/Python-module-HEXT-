import sys
import os

def hex_to_ansi_background(hex_color):
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
    return f"\033[48;2;{r};{g};{b}m"

def hex_to_ansi(hex_color):
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
    return f"\033[38;2;{r};{g};{b}m"

def setForeColor(hex_color):
    color = hex_to_ansi(hex_color)
    print(f"{color}", end="")


def setBackColor(hex_color):
    color = hex_to_ansi_background(hex_color)
    print(f"{color}", end="")

def resetForeColor():
    print("\033[39m", end="")

def resetBackColor():
    print("\033[49m", end="")

def resetColor():
    print("\033[39m", end="")
    print("\033[49m", end="")

def main():
    color = '000000'
    while True:
        os.system("cls")
        print("color: ", end="")
        setBackColor("#" + color)
        print("     ")
        resetColor()
        color = input('enter hex-code: #')

if __name__ == '__main__':
    main()
