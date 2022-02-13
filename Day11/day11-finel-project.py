import random

while True:
    print("\n\n***** Game Start ******* \n\n")
    user_decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")

    if user_decision == 'y':
        # write code for play the game.
        user_card = []
        computers_card = []
        user_card.append(random.randint(1,10))
        user_card.append(random.randint(1,10))
        computers_card.append(random.randint(1,10))


        while True:
            print(f"Your card's : {user_card}")
            print(f"computer's first card : {computers_card}")

            user_decision = input("Type 'y' to get another card , type 'n' to pass : ")


            if user_decision == 'y':
                user_card.append(random.randint(1, 10))
                computers_card.append(random.randint(1, 10))

            elif user_decision == 'n':
                break

            else:
                print("please type correct value!!")

            if sum(user_card)>21:
                print("you loss!!")
                break

        computers_card.append(random.randint(1, 10))
        print(f"your finel hand : {user_card}")
        print(f"computer's finel hand : {computers_card}")

        if sum(user_card) > sum(computers_card):
            print("You Won!!")

        elif sum(user_card) < sum(computers_card):
            print("you loss!!")

        else:
            print("match Draw!!")


    elif user_decision == 'n':
        print("\n**** Thank you so much for visiting this game ****")
        break
    else:
        print("please write correct input")