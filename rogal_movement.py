import os


def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


# def make_a_bord(column_len, row_len):
#     tablica = []

#     for column in range(column_len):
#         tablica.append([])
#         for row in range(row_len):
#             if column == 2 or row == 3:
#                 tablica[column].append('#')
#             else:
#                 tablica[column].append('_')
#     return tablica


def make_a_bord(file_name):
    file_content = open(file_name)
    list_from_file = file_content.readlines()
    file_content.close()

    board = []
    for lista in list_from_file:
        one_line = []
        for char in lista:
            one_line.append(char)
        board.append(one_line)

    # for lista in board:
    #     for i in lista:
    #         print(i, end='')
    return board

def print_board(tablica):
    for row in range(len(tablica)):
        for column in range(len(tablica[row])):
            print(tablica[row][column], end='')


def switch(tablica, row, column, new_row, new_column):

    if tablica[new_row][new_column] == '#':
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
    tablica = []
    # board_len_column = 5
    # board_len_row = 8
    # tablica = make_a_bord(board_len_column, board_len_row)
    file_path = "/home/ania/Pulpit/assingments/AARogue/map.txt"
    tablica = make_a_bord(file_path)
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

        
main()   #CASE SENSITIVITY?