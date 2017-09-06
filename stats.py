def display_player_stats(player_stats):
    books = ('Books: ', player_stats['Books'])
    luck = ('Luck:  ', player_stats['Luck'])
    life = ('Life:  ', player_stats['Life'])
    print(books, luck, life)