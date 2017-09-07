import infoprint
import firstlvl
import secondlvl
import conditionscheck
import os


def main():
    os.system('clear')
    #infoprint.illuminati()
    #infoprint.welcome_screen()
    #infoprint.how_to_play()
    # tu wybór postaci i przekazanie jako arg do funkcji
    if firstlvl.round():
        # tu info o następnym lvlu
        if secondlvl.round():
            # tu info o następnym lvlu
            # if third lvl:
                # printWin, halloffame itp
                # return

if __name__ == '__main__':
    main()
