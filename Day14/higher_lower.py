import os
import random

import art
from art import *
from  data import  data

# function to generate second choice
# idea is to generate second choice which is diff. from first choice
def generate_second_choice(first):
    while True:
        second_choice = random.choice(data)
        if not first == second_choice:
            return second_choice

# gives output whether user's answer is right or wrong
# right => return true else return false
def game_play(first,second):
    # print(first[name])
    # print(second)
    print(f"Compare A : {first['name']}, a {first['description']}, from {first['country']}.")
    print(art.vs)
    print(f"Compare B : {second['name']}, a {second['description']}, from {second['country']}.")

    user_ans = input("\nWho has more follower's? Type 'A' or 'B' : ").upper()

    if user_ans == 'A' and first['follower_count'] > second['follower_count']:
        return True
    elif user_ans == 'B' and first['follower_count'] < second['follower_count']:
        return True
    return False



def initiate_choice():
    global first_choice,second_choice
    first_choice = second_choice
    second_choice = generate_second_choice(first_choice)  # generating second choice
    user_live = game_play(first_choice, second_choice)

    return user_live

def increase_count():
    global finel_count
    os.system('cls')
    finel_count += 1

    print(logo)
    print(f"You are right! Current Score : {finel_count}")

def end_statement():
    os.system('cls')
    print(logo)
    print(f"Sorry, That's Wrong! finel Score : {finel_count}")


# # generating first choice for the first time
# first_choice = random.choice(data)
# # counting user finel score
# finel_count = 0
#
# # print(f"First Choice : {first_choice}")
# # second_choice = generate_second_choice(first_choice)
# # print(f"second choice : {second_choice}")
# # game_play(first_choice,second_choice)

if __name__ == '__main__':
    play_game = True

    while play_game:
        print(logo)
        finel_count = 0  # keep track of user score
        first_choice = random.choice(data)  # gernerating first choice from data
        second_choice = generate_second_choice(first_choice)  # generating second choice
        user_live = game_play(first_choice,second_choice)

        while user_live:
            increase_count()
            user_live = initiate_choice()

        end_statement()

        play_game = input("\nDo You Want to play this game again? Type 'y' for Yes or 'n' for No : ").lower()
        if not play_game == 'y':
            play_game =False

    print("\n\n***** Thank you so much for playing this game *****")


