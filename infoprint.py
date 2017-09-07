import os
import time
import sys
import movement


def info_lvl(filename):
    text = open(filename)
    for char in text.read():
        sys.stdout.write(char)
        sys.stdout.flush()
    text.close
    movement.getch()
    os.system('clear')


def illuminati(filename="illuminati.txt"):
    art = open(filename)
    print(art.read())
    time.sleep(5)
    art.close()
    os.system('clear')


def welcome_screen(filename="welcome.txt"):
    text = open(filename)
    for char in text.read():
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    text.close
    movement.getch()
    os.system('clear')


def final_screen(filename="lose.txt"):
    text = open(filename)
    for char in text.read():
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(5)
    text.close()
    os.system('clear')


def print_board(tablica):
    for row in range(len(tablica)):
        for column in range(len(tablica[row])):
            if tablica[row][column] == "#":
                print("\033[0;32m"+tablica[row][column], end='')
            elif tablica[row][column] == "K":
                print("\033[0;31m"+tablica[row][column], end='')
            elif tablica[row][column] == "|":
                print("\033[0;33m"+tablica[row][column], end='')
            else:
                print("\033[0;0m"+tablica[row][column], end='')
