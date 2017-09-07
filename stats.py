def display_player_stats(player_stats, level):
    keys = ('Keys: ', player_stats['Keys'])
    luck = ('Luck:  ', player_stats['Luck'])
    guess = ('Guess', player_stats['Guess'])
    life = ('Life:  ', player_stats['Life'])
    if level == 1:
        print(keys, luck)
    if level == 2 or level == 3:
        print(keys, luck, life, guess)
