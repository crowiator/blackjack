
import random
logo = ''' _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\/
                       _/ |                
                      |__/                 '''

import random
import os

""" RETURN RANDOM CARD"""


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


""" Calculate score for current list(user or computer)"""


def calculate_score(list):
    if sum(list) == 21 and len(list) == 2:
        return 0

    if sum(list) == 21 and 11 in list:
        list.remove(11)
        list.append(1)

    return sum(list)


"COMPARE 2 LISTS AND PRINT RESULT"


def compare(user_score, computer_score):
    if computer_score == user_score:
        print("It is a draw.")
    elif computer_score == 0:
        print("You lose")
    elif user_score == 0:
        print("You win")
    elif user_score > 21:
        print("You lose")
    elif computer_score > 21:
        print("You win")
    else:
        if abs(21 - user_score) < abs(21 - computer_score):
            print("You win")
        else:
            print("You lose")


start = True
while start:
    print(logo)
    user_cards = []
    computer_cards = []
    run = True
    for x in range(1, 3):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while run:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your card: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        if computer_score == 0 or user_score == 0 or user_score > 21:
            run = False
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == 'y':
                user_cards.append(deal_card())
            else:
                run = False

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score {computer_score}")
    compare(user_score, computer_score)
    restart_game = input("Do you want to resart the game? Y or N ").lower()
    if restart_game == "y":
        start = True
        os.system("clear")
    else:
        start = False

