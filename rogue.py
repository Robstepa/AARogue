import os
import importboard
import movement
import stats
import firstlvl
import conditionscheck
import importboard
import infoprint
import movement


def main():
    infoprint.illuminati()
    infoprint.welcome_screen()
    infoprint.how_to_play()
    importboard.make_a_bord()
    conditionscheck.switch()
    stats.display_player_stats()
    firstlvl.print_board()
    firstlvl.round()

main()
