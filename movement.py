import os
import tty
import time #potrzebne tu do zliczania czasu?
import termios
import random
import conditionscheck
import sys


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


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

    return conditionscheck.switch(tablica, row, column, new_row, new_column, level, player_stats)



