import random
import os


def choose_number():
    count = 0
    digit_list = []

    while count < 2:
        digit = random.randint(0, 9)
        if digit in digit_list:
            continue
        else:
            digit_list.append(str(digit))
            count += 1
    print(digit_list)
    return digit_list


def input_user():

    while True:
        number = input("Pick a number: ")
        try:
            int(number)
            if len(number) != 2:
                raise ValueError
        except ValueError:
            print("Input has to be two digits integer. Try again.")
        else:
            break

    return number


def compar_numbers(digit_list, digit_number):
    hot = 0
    warm = 0
    for i in range(len(digit_list)):
        if digit_list[i] == digit_number[i]:
            hot += 1
            print("hot")

    for i in range(len(digit_list)):
        if digit_list[i] == digit_number[i]:
            continue
        elif digit_number[i] in digit_list:
            warm += 1
            print("warm")

    if warm == 0 and hot == 0:
        print("Cold")

    return hot


def boss_fight(tries_count):

    digit_list = choose_number()
    print("You have only one chance. Use it wisely.")

    while tries_count > 0:
        print(tries_count, "tries left.")
        digit_number = input_user()
        hot = compar_numbers(digit_list, digit_number)
        if hot == 2:
            os.system('clear')
            return True
        tries_count -= 1
    os.system('clear')
    return False


