import os
import importboard
import movement
from stats import display_player_stats
import infoprint
import secondlvl    #??? po co to tu


def round(player_stats, file_path, hero):
    os.system('clear')
    tablica = []
    tablica = importboard.make_a_bord(file_path)

    board_len_column = len(tablica) - 1  # len-1, bo indeksuje sie od 0
    board_len_row = len(tablica[0]) - 2  # len-2, bo znak nowej linii + indeksuje sie od 0

    user_position_coordinates = (2, 10, 3)
    # number_to_guess = choose_number()
    # gateway = sum_of_numbers(number_to_guess)

    tablica[user_position_coordinates[0]][user_position_coordinates[1]] = hero
    infoprint.print_board(tablica)
    display_player_stats(player_stats, user_position_coordinates[2])

    user_move = ''
    while user_move != 'q' and player_stats['Luck'] > 0 and user_position_coordinates[2] < 4:
        user_move = movement.getch()
        os.system('clear')
        user_position_coordinates = movement.movement(user_move, tablica, user_position_coordinates[0], user_position_coordinates[1], board_len_column, board_len_row, user_position_coordinates[2], player_stats)
        infoprint.print_board(tablica)
        display_player_stats(player_stats, user_position_coordinates[2])


    if user_position_coordinates[2] == 4 and player_stats['Keys'] == 0:
        os.system('clear')
        return (True, player_stats)
    else:
        os.system('clear')
        infoprint.lose_screen()
        return (False, player_stats)


    
