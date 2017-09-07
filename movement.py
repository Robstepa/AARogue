import os
import tty
import time
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
    if inp == 'w':
        if row == 0:
            return conditionscheck.switch(tablica, row, column, row+column_len, column, level, player_stats)
        return conditionscheck.switch(tablica, row, column, row-1, column, level, player_stats)
    elif inp == 's':
        if row == column_len:
            return conditionscheck.switch(tablica, row, column, row-column_len, column, level, player_stats)
        return conditionscheck.switch(tablica, row, column, row+1, column, level, player_stats)
    elif inp == 'd':
        if column == row_len:
            return conditionscheck.switch(tablica, row, column, row, column-row_len, level, player_stats)
        return conditionscheck.switch(tablica, row, column, row, column+1, level, player_stats)
    elif inp == 'a':
        if column == 0:
            return conditionscheck.switch(tablica, row, column, row, column+row_len, level, player_stats)
        return conditionscheck.switch(tablica, row, column, row, column-1, level, player_stats)

    return (row, column, level)




