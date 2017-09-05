import time
import sys
import os


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
    text.close()
    os.system('clear')


def level1(filename="map.txt"):
    board = open(filename)
    floor1 = []
    for char in board.read():
        sys.stdout.write(char)
        sys.stdout.flush()
    print(floor1)


def main():
    level1()
    #illuminati()
    #welcome_screen()
    #how_to_play()


if __name__ == '__main__':
    main()
