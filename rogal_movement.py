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


def switch(tablica, row, column, new_row, new_column, level):
    tasks = ['6*8-4*5', '2+2*2', '5+6*7-1*2*3', '2*6+7*9-2*4', '8*15-12*6', '98*72-75*94', '68*23-55*27']
    answers = ['20', '6', '41', '67', '48', '6', '79']
    task_number = random.randint(0, 7)
    #if new_row <= len(tablica[0]-2) and new_column <= len(new_column)-1
    if tablica[new_row][new_column] == '#': #tu warunek, jeśli new_col nie przekracza zakresu i == '#'
        return (row, column, level)
    elif tablica[new_row][new_column] == '%':
        a = input(tasks[task_number]+": ")
        if a == answers[task_number]:
            print("good")
        else:
            print("bad")
        return (row, column, level)
    elif tablica[new_row][new_column] == 'O':
        return (row, column, level+1)
    else:
        # temp = tablica[row][column]
        # tablica[row][column] = tablica[new_row][new_column]
        # tablica[new_row][new_column] = temp
        tablica[new_row][new_column] = tablica[row][column]
        tablica[row][column] = '.'
        return (new_row, new_column, level)


def movement(inp, tablica, row, column, column_len, row_len, level):

    if inp == 'w':
        if row == 0:
            return switch(tablica, row, column, row+column_len, column, level)
        return switch(tablica, row, column, row-1, column, level)
    elif inp == 's':
        if row == column_len:
            return switch(tablica, row, column, row-column_len, column, level)
        return switch(tablica, row, column, row+1, column, level)
    elif inp == 'd':
        if column == row_len:
            return switch(tablica, row, column, row, column-row_len, level)
        return switch(tablica, row, column, row, column+1, level)
    elif inp == 'a':
        if column == 0:
            return switch(tablica, row, column, row, column+row_len, level)
        return switch(tablica, row, column, row, column-1, level)

    return (row, column, level)


def main():
    os.system('clear')
    #illuminati()
    #welcome_screen()
    #how_to_play()
    tablica = []
    file_paths = ["/home/robstep/Documents/AARogue/map.txt", "/home/robstep/Documents/AARogue/map_lvl_2.txt"]
    tablica = make_a_bord(file_paths[0])
    
    board_len_column = len(tablica) - 1  # len-1, bo indeksuje sie od 0, czyli 
    board_len_row = len(tablica[0]) - 2  # len-2, bo znak nowej linii + indeksuje sie od 0, czyli

    user = '@'
    user_position_coordinates = (1, 1, 1)

    tablica[user_position_coordinates[0]][user_position_coordinates[1]] = user
    print_board(tablica)

    user_move = ''
    while user_move != 'q':
        user_move = getch()
        os.system('clear')
        user_position_coordinates = movement(user_move, tablica, user_position_coordinates[0], user_position_coordinates[1], board_len_column, board_len_row, user_position_coordinates[2])
        if user_position_coordinates[2] == 2:
            tablica = make_a_bord(file_paths[1])
            board_len_column = len(tablica) - 1
            board_len_row = len(tablica[0]) - 2
            tablica[user_position_coordinates[0]][user_position_coordinates[1]] = user

        print_board(tablica)
        print(user_position_coordinates, board_len_column, board_len_row)


main()
