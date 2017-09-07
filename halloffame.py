def export_score(filename, player_stats, user_name, game_time):
    export = open(filename, 'a')
    export.write(''.join(user_name) + ": " + str(player_stats['Points']) + " points" + " and it took you " + str(game_time) + " sec" + "\n")
    print(''.join(user_name) + ": " + str(player_stats['Points']) + " points" + " and it took you " + str(game_time) + " sec" + "\n")
    export.close()


def import_score(filename):
    import_file = open(filename)
    for i in import_file:
        print(''.join(import_file.readlines()[-10:]), end='')
