def introduce(filename="illuminati.txt"):
    art1 = open(filename)
    print(art1.read())
    print("You`re a math student, but you wanna to become MASTER.\n")
    print("You need to collect 'operations' to defeat your worst ENEMIES")
    art1.close()


def game():
    restart = True

    while restart:
        board = []
        height = 50
        width = 140
        for i in range(height):
            board.append([])
            for w in range(width):
                if i == 0 or i == (height-1):
                    board[i].append('#')
                elif w == 0 or w == (width - 1):
                    board[i].append('#')
                else:
                    board[i].append('.')
        
        for n in board:
            print("".join(n))
        break    
    

def main():
    introduce()
    game()


main()