import os
import importboard
import movement
from stats import display_player_stats
import time
import random
import infoprint


def round():

    player_stats = {'Books': 0, 'Luck': 1, 'Life': 10}
    tablica = []
    file_paths = ["map.txt", "map_lvl_2.txt"]
    tablica = importboard.make_a_bord(file_paths[1])

    board_len_column = len(tablica) - 1  # len-1, bo indeksuje sie od 0
    board_len_row = len(tablica[0]) - 2  # len-2, bo znak nowej linii + indeksuje sie od 0

    user = '@'
    user_position_coordinates = (1, 1, 1)

    tablica[user_position_coordinates[0]][user_position_coordinates[1]] = user
    infoprint.print_board(tablica)

    time_point = time.time()
    user_move = ''
    index_r = 0
    index_c = 0
    flag = 0

    while user_move != 'q' and player_stats['Life'] > 0:
        user_move = movement.getch()
        os.system('clear')
        user_position_coordinates = movement.movement(user_move, tablica, user_position_coordinates[0], user_position_coordinates[1], board_len_column, board_len_row, user_position_coordinates[2], player_stats)

        if flag == 0:
            index_r = random.randint(0, len(tablica[0])-1)
            index_c = random.randint(0, len(tablica)-1)
            while tablica[index_c][index_r] == '#':
                index_r = random.randint(0, len(tablica[0])-1)
                index_c = random.randint(0, len(tablica)-1)
            tablica[index_c][index_r] = '?'
            flag = 1
            time_point = time.time()

        if time.time() >= time_point + 2:
            tablica[index_c][index_r] = '.'
            flag = 0
        infoprint.print_board(tablica)

    if player_stats['Life'] == 0:
        os.system('clear')
        infoprint.lose_screen()
