import random


def switch(tablica, row, column, new_row, new_column, level, player_stats):
    tasks = ['6*8-4*5', '2+2*2', '5+6*7-1*2*3', '2*6+7*9-2*4', '8*15-12*6', '98*72-75*94', '68*23-55*27']
    answers = ['20', '6', '41', '67', '48', '6', '79']
    task_number = random.randint(0, 6)
    if tablica[new_row][new_column] == '#':
        return (row, column, level)
    elif tablica[new_row][new_column] == '%':
        tablica[new_row][new_column] = '.'
        answer = input(tasks[task_number]+": ")
        if answer == answers[task_number]:
            print("Good")
            player_stats['Luck'] += 1
        else:
            print("Bad")
            player_stats['Life'] -= 1
        return (row, column, level)
    elif tablica[new_row][new_column] == 'O':
        return (row, column, level+1)
    else:
        tablica[new_row][new_column] = tablica[row][column]
        tablica[row][column] = '.'
        return (new_row, new_column, level)
