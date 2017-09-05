import time
import sys
import os


def getch():
    import tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


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
    table = []
    board = open(filename)
    for i in board.read():
        table.append(i)      
    for i in table:
        print(i, end='')
    

def main():
    level1()
    #illuminati()
    #welcome_screen()
    #how_to_play()


if __name__ == '__main__':
    main()
