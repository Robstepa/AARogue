import random
import hotwarmcold


def switch(tablica, row, column, new_row, new_column, level, player_stats):
    tasks = ['6*8-4*5', '2+2*2', '5+6*7-1*2*3', '2*6+7*9-2*4', '8*15-12*6', '98*72-75*94', '68*23-55*27']
    answers = ['28', '6', '41', '67', '48', '6', '79']
    task_number = random.randint(0, 6)
    if level == 1 and tablica[new_row][new_column] == '#':
        return (row, column, level)

    if level == 2 and tablica[new_row][new_column] == '#':
        player_stats['Life'] -= 1
        return (row, column, level)

    if level == 3 and tablica[new_row][new_column] == '#':
        return (row, column, level)

    if player_stats['Books'] == 3 and level == 1:
            tablica[2][11] = 'O'

    if player_stats['Guess'] == 3 and level == 2:
            tablica[4][11] = 'O'

    if level == 3 and tablica[new_row][new_column] == '*':
        if hotwarmcold.boss_fight(player_stats['Guess'] + player_stats['Luck']):
            tablica[9][10] = 'O'
            return (row, column, level)
        else:
            return (row, column, level+1)

    if level == 1 and tablica[new_row][new_column] == '|':
        tablica[new_row][new_column] = '.'
        answer = input(tasks[task_number]+": ")
        if answer == answers[task_number]:
            print("Good")
            player_stats['Luck'] += 1
            player_stats['Points'] += 1
        else:
            print("Bad")
            player_stats['Luck'] -= 1
        return (row, column, level)

    if tablica[new_row][new_column] == 'K':
        tablica[new_row][new_column] = '.'
        player_stats['Books'] += 1
        player_stats['Points'] += 1
        return (row, column, level)

    if tablica[new_row][new_column] == '?':
        tablica[new_row][new_column] = '.'
        if player_stats['Guess'] < 3:
            player_stats['Guess'] += 1
            player_stats['Points'] += 1
        return (row, column, level)

    if tablica[new_row][new_column] == 'O':
        player_stats['Books'] -= 1
        return (row, column, level+1)

    tablica[new_row][new_column] = tablica[row][column]
    tablica[row][column] = '.'
    return (new_row, new_column, level)
