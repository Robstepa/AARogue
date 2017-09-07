import os

def choose_avatar():
    while True:
        try:
            character = int(input("1. @\n2. ∆\n3. $\nChoose your character: "))
            if character == 1:
                user = '@'
            elif character == 2:
                user = '∆'
            elif character == 3:
                user = '$'
            else:
                raise ValueError
        except ValueError:
            print("Choose a character using nubers 1-3: ")
        else:
            os.system('clear')
            return user


def choose_nickname():
    user_name = ''
    while True:
        try:
            user_name = input("Enter your nickname: ")
            if len(user_name) < 8 and len(user_name) > 0:
                os.system('clear')
                return user_name
            else:
                raise ValueError
        except ValueError:
            print("Your name is too long or too short")
    

