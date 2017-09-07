import os
import importboard
import movement
from stats import display_player_stats
import time
import random
import infoprint


def round(player_stats, file_path, hero):
    os.system('clear')

    tablica = []
    tablica = importboard.make_a_bord(file_path)

    board_len_column = len(tablica) - 1  # len-1, bo indeksuje sie od 0
    board_len_row = len(tablica[0]) - 2  # len-2, bo znak nowej linii + indeksuje sie od 0

    
    user_position_coordinates = (1, 1, 2)

    tablica[user_position_coordinates[0]][user_position_coordinates[1]] = hero
    infoprint.print_board(tablica)
    display_player_stats(player_stats, user_position_coordinates[2])

    time_point = time.time()
    user_move = ''
    index_r = 0
    index_c = 0
    flag = 0

    while user_move != 'q' and player_stats['Life'] > 0 and user_position_coordinates[2] < 3:
        user_move = movement.getch()
        os.system('clear')
        user_position_coordinates = movement.movement(user_move, tablica, user_position_coordinates[0], user_position_coordinates[1], board_len_column, board_len_row, user_position_coordinates[2], player_stats)

        if flag == 0:
            index_r = random.randint(0, len(tablica[0])-1)
            index_c = random.randint(0, len(tablica)-1)
            while tablica[index_c][index_r] == '#' or tablica[index_c][index_r] == '\n' or tablica[index_c][index_r] == '@':
                index_r = random.randint(0, len(tablica[0])-1)
                index_c = random.randint(0, len(tablica)-1)
            tablica[index_c][index_r] = '?'
            flag = 1
            time_point = time.time()

        if time.time() >= time_point + 10:
            tablica[index_c][index_r] = '.'
            flag = 0

        infoprint.print_board(tablica)
        display_player_stats(player_stats, user_position_coordinates[2])

    # if player_stats['Life'] == 0:
    #     os.system('clear')
    #     infoprint.lose_screen()
    if user_position_coordinates[2] == 3:
        os.system('clear')
        return (True, player_stats)
    else:
        os.system('clear')
        infoprint.lose_screen()
        return (False, player_stats)
