import os
import importboard
import movement
from stats import display_player_stats
import infoprint


def round():
    os.system('clear')
    player_stats = {'Books': 0, 'Luck': 1, 'Life': 10}
    tablica = []
    file_paths = ["map.txt", "map_lvl_2.txt"]
    tablica = importboard.make_a_bord(file_paths[0])

    board_len_column = len(tablica) - 1  # len-1, bo indeksuje sie od 0
    board_len_row = len(tablica[0]) - 2  # len-2, bo znak nowej linii + indeksuje sie od 0

    user = '@'
    user_position_coordinates = (1, 1, 1)

    tablica[user_position_coordinates[0]][user_position_coordinates[1]] = user
    infoprint.print_board(tablica)

    user_move = ''
    while user_move != 'q' and player_stats['Life'] > 0:
        display_player_stats(player_stats)
        user_move = movement.getch()
        os.system('clear')
        user_position_coordinates = movement.movement(user_move, tablica, user_position_coordinates[0], user_position_coordinates[1], board_len_column, board_len_row, user_position_coordinates[2], player_stats)

        infoprint.print_board(tablica)

    if player_stats['Life'] == 0:
        os.system('clear')
        infoprint.lose_screen()
