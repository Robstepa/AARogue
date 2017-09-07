import infoprint
import firstlvl
import thirdlvl
import secondlvl
import conditionscheck
import os
import hero_creation
import time
import halloffame


def main():
    os.system('clear')
    infoprint.illuminati()
    infoprint.welcome_screen()

    file_paths = ["map.txt", "map_lvl_2.txt", "map_lvl_boss.txt", "halloffame.csv"]
    player_stats = {'Keys': 0, 'Luck': 1, 'Life': 10, 'Guess': 0, 'Points': 0}
    print_info = ["info1.txt", "info2.txt", "info3.txt"]

    hero = hero_creation.choose_avatar()
    user_name = hero_creation.choose_nickname()
    time_point = time.time()

    infoprint.info_lvl(print_info[0])

    check = firstlvl.round(player_stats, file_paths[0], hero)
    if check[0]:
        infoprint.info_lvl(print_info[1])
        check = secondlvl.round(player_stats, file_paths[1], hero)
        if check[0]:
            infoprint.info_lvl(print_info[2])
            check = thirdlvl.round(player_stats, file_paths[2], hero)
            if check[0]:
                game_over_time = time.time()
                game_time = (game_over_time - time_point) // 1
                halloffame.export_score(file_paths[3], player_stats, user_name, game_time)
                infoprint.final_screen("win.txt")
                halloffame.import_score(file_paths[3])
                return


if __name__ == '__main__':
    main()
