import os
import sys
import tty
import time
import termios
import random
from stats import display_player_stats


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


def switch(tablica, row, column, new_row, new_column, level, player_stats):
    tasks = ['6*8-4*5', '2+2*2', '5+6*7-1*2*3', '2*6+7*9-2*4', '8*15-12*6', '98*72-75*94', '68*23-55*27']
    answers = ['20', '6', '41', '67', '48', '6', '79']
    task_number = random.randint(0, 6)
    if tablica[new_row][new_column] == '#':  # tu warunek, jeśli new_col nie przekracza zakresu i == '#'
        return (row, column, level)
    elif tablica[new_row][new_column] == '%':
        tablica[new_row][new_column] = '.'
        answer = input(tasks[task_number]+": ")
        if answer == answers[task_number]:
            print("Good")
            player_stats['Luck'] += 1
        else:
            print("Bad")
            player_stats['Luck'] -= 1
        return (row, column, level)
    elif tablica[new_row][new_column] == 'O':
        return (row, column, level+1)
    else:
        tablica[new_row][new_column] = tablica[row][column]
        tablica[row][column] = '.'
        return (new_row, new_column, level)


def movement(inp, tablica, row, column, column_len, row_len, level, player_stats):
    new_row = row
    new_column = column
    if inp == 'w':
        if row == 0:
            new_row = row+column_len
        new_row = row-1
    elif inp == 's':
        if row == column_len:
            new_row = row-column_len
        new_row = row+1
    elif inp == 'd':
        if column == row_len:
            new_column = column-row_len
        new_column = column+1
    elif inp == 'a':
        if column == 0:
            new_column = column+row_len
        new_column = column-1
    else:
        return (row, column, level)

    return switch(tablica, row, column, new_row, new_column, level, player_stats)


def main():
    os.system('clear')
    # illuminati()
    # welcome_screen()
    # how_to_play()
    player_stats = {'Books': 0, 'Luck': 1, 'Life': 0}

    tablica = []
    file_paths = ["map.txt", "map_lvl_2.txt"]
    tablica = make_a_bord(file_paths[0])
    
    board_len_column = len(tablica) - 1  # len-1, bo indeksuje sie od 0, czyli 
    board_len_row = len(tablica[0]) - 2  # len-2, bo znak nowej linii + indeksuje sie od 0, czyli

    user = '@'
    user_position_coordinates = (1, 1, 1)

    tablica[user_position_coordinates[0]][user_position_coordinates[1]] = user
    print_board(tablica)

    user_move = ''
    while user_move != 'q':
        display_player_stats(player_stats)
        user_move = getch()
        os.system('clear')
        user_position_coordinates = movement(user_move, tablica, user_position_coordinates[0], user_position_coordinates[1], board_len_column, board_len_row, user_position_coordinates[2], player_stats)
        if user_position_coordinates[2] == 2:
            display_player_stats(player_stats)
            tablica = make_a_bord(file_paths[1])
            board_len_column = len(tablica) - 1
            board_len_row = len(tablica[0]) - 2
            tablica[user_position_coordinates[0]][user_position_coordinates[1]] = user

        print_board(tablica)
        print(user_position_coordinates, board_len_column, board_len_row)


main()
