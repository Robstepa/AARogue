def display_player_stats(player_stats):
    books = ('Books: ', player_stats['Books'])
    luck = ('Luck:  ', player_stats['Luck'])
    guess = ('Guess', player_stats['Guess'])
    life = ('Life:  ', player_stats['Life'])
    print(books, luck, guess, life)
