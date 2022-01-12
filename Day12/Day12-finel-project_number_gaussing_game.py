
# writing of function

# 1. generate a random number
import random
from art import logo


# 1. generate random number beetween low and high
def generate_random_number(low=1,high=100):
    return random.randint(low,high)

# 2. when program start this code will going to execute.
def greet_the_game():
    print(logo)
    print("\n\n ***** Welcome to number gaussing game ******\n")
    print("I'm Thinking of a number beetween 1 and 100!")

# 3. get user max life , depends on usere whether he choose,
#     a. easy => 10 life
#     b. medium => 8 life
#     c. hard => 5 life

def get_user_life():
    user_choice = input("""
    1. Type 'e' : easy ( 10 life )
    2. Type 'm' : medium ( 8 life )
    3. Type 'h' : hard ( 5 life )
    Choose a Difficulty. : """)

    if user_choice == 'e': return 10
    elif user_choice == 'm': return 8
    elif user_choice == 'h': return 5
    else:
        print("please enter correct choice.")
        # // recurcively call this till we get correct user input
        return get_user_life()

# it compares user gauss to original gauss and tells
def compare_gauss(user_gauss):
    if gauss_number == user_gauss:
        print(f"you get it right!! original number is {gauss_number}")
        return True
    elif gauss_number > user_gauss:
        print("Your gauss is low!!")
    else:
        print("your gauss is too high!!")
    return False

# this fuction ask user to make a gauss
def make_a_gauss():
    global no_of_life
    print(f"\n You have {no_of_life} attempt remaining to gauss the number.")
    # no of life for user =0 => user loss the game
    if no_of_life == 0:
        print("\n oops!! You are dead! you lost this game.")
        print(f"the original number is {gauss_number}")
        return True

    user_gauss = int(input("Make a gauss : "))
    # return  true if user_gauss is equal to original gauss_number

    if compare_gauss(user_gauss):
        return True
    no_of_life -= 1
    return False



# program execution starts from here

if __name__ == '__main__':

    game_start = True
    while game_start:
        # execute the program
        greet_the_game()

        no_of_life = get_user_life()
        print(no_of_life)

        # number which user have to gauss
        gauss_number = generate_random_number()

        print(gauss_number)
        # user gauss and comparision
        while not make_a_gauss():
            continue

        while True:
            user_choice = input("\n\nDo you want to play this game again? Type 'y' to play or 'n' to exit : ")
            if user_choice == 'n':
                game_start = False
                break
            elif user_choice == 'y':
                game_start = True
                break
            else:
                print("Please write correct value!!")

    print("\n***** Thank you so much for playing this game ******")





