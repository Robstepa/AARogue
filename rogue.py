import infoprint
import firstlvl
import thirdlvl
import secondlvl
import conditionscheck
import os
import hero_creation
import time
import halloffame
import inffooooo


def main():
    os.system('clear')
    infoprint.illuminati()
    infoprint.welcome_screen()
    infoprint.how_to_play()
    # tu wybór postaci i przekazanie jako arg do funkcji
    file_paths = ["map.txt", "map_lvl_2.txt", "map_lvl_boss.txt", "halloffame.csv"]
    player_stats = {'Keys': 0, 'Luck': 1, 'Life': 10, 'Guess': 0, 'Points': 0}

    hero = hero_creation.choose_avatar()
    user_name = hero_creation.choose_nickname()
    time_point = time.time()

    inffooooo.i()

    check = firstlvl.round(player_stats, file_paths[0], hero)
    if check[0]:
        check = secondlvl.round(player_stats, file_paths[1], hero)
        # tu info o następnym lvlu
        if check[0]:
            check = thirdlvl.round(player_stats, file_paths[2], hero)
            # tu info o następnym lvlu
            if check[0]:
                game_over_time = time.time()
                game_time = (game_over_time - time_point) // 1
                halloffame.export_score(file_paths[3], player_stats, user_name, game_time)
                infoprint.win_screen()
                halloffame.import_score(file_paths[3])
                return


if __name__ == '__main__':
    main()
