def export_score(filename="halloffame.csv",):
    export = open(filename, 'a')
    data_to_export = ''
    points = 0
    for score in player_stats:
        data_to_export += ((score + ',')*player_stats[score])
        for point in data_to_export:
            if score == 'Points':
                points += 1
    points = points // 7
    export.write(''.join(user_name) + ": " + str(points) + " points" + "\n")
    print(''.join(user_name) + ": " + str(points) + " points" + "\n")
    export.close()


def import_score(filename="halloffame.csv"):
    import_file = open(filename)
    for i in import_file:
        print(''.join(import_file.readlines()[-10:]), end='')