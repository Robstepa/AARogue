import os
import sys
import tty
import time
import termios
import random


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
    os.system('clear')


def how_to_play(filename="info.txt"):
    text = open(filename)
    for char in text.read():
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(5)
    text.close()
    os.system('clear')


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def make_a_bord(file_name='map.txt'):
    file_content = open(file_name)
    list_from_file = file_content.readlines()
    file_content.close()

    board = []
    for lista in list_from_file:
        one_line = []
        for char in lista:
            one_line.append(char)
        board.append(one_line)

    return board


def print_board(tablica):
    for row in range(len(tablica)):
        for column in range(len(tablica[row])):
            print(tablica[row][column], end='')


def switch(tablica, row, column, new_row, new_column):
    tasks = ['2+2', '4+4', '5+5']
    answers = ['4', '8', '10']
    task_number = random.randint(0, 2)
    if tablica[new_row][new_column] == '#':
        return (row, column)
    elif tablica[new_row][new_column] == '%':
        a = input(tasks[task_number]+": ")
        if a == answers[task_number]:
            print("good")
        else:
            print("bad")
        return (row, column)
    else:
        temp = tablica[row][column]
        tablica[row][column] = tablica[new_row][new_column]
        tablica[new_row][new_column] = temp
        return (new_row, new_column)


def movement(inp, tablica, row, column, column_len, row_len):

    if inp == 'w':
        if row == 0:
            return switch(tablica, row, column, row+column_len, column)
        return switch(tablica, row, column, row-1, column)
    elif inp == 's':
        if row == column_len:
            return switch(tablica, row, column, row-column_len, column)
        return switch(tablica, row, column, row+1, column)
    elif inp == 'd':
        if column == row_len:
            return switch(tablica, row, column, row, column-row_len)
        return switch(tablica, row, column, row, column+1)
    elif inp == 'a':
        if column == 0:
            return switch(tablica, row, column, row, column+row_len)
        return switch(tablica, row, column, row, column-1)

    return (row, column)


def main():
    os.system('clear')
    illuminati()
    welcome_screen()
    how_to_play()
    tablica = []
    tablica = make_a_bord()
    board_len_column = len(tablica)
    board_len_row = len(tablica[0])

    user = '@'
    user_position_coordinates = (1, 1)

    tablica[user_position_coordinates[0]][user_position_coordinates[1]] = user
    print_board(tablica)

    user_move = ''
    while user_move != 'q':
        user_move = getch()
        os.system('clear')
        user_position_coordinates = movement(user_move, tablica, user_position_coordinates[0], user_position_coordinates[1], board_len_column-1, board_len_row-1)
        print_board(tablica)


main()
