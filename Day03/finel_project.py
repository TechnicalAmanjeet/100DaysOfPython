print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# taking input from user for turning left and right
user_choise = input("where do you want to turn? ( left or right ) : ")

# idea => user chooses = left => then go another level in the game
# or   => user chooses = right or anything else => Fall into a hole and game over

user_choise = user_choise.lower()


if(user_choise == "left"):
    print("\nGood! You finished ur first level by taking a good turn.")

    input("Press Enter to go to next level.")

    user_choise = input("\nThere is river in front of you. what do you want to do? ( swim or wait ) : ")

    user_choise = user_choise.lower()

    # idea => user_choise = wait => then he/she will go into the next level
    # user_choise = swim or anything else => Game over bcz Attacked by trout.

    if(user_choise == "wait"):
        print("\nGood! You just finished ur second level by making a good decision.")

        input("Press enter to go to next level.")

        user_choise = input("\nThis is the finel level stage. so take your decision wisely. now! There are three door's in front of you. choose one door from it ( red or blue or yellow ) : ")

        user_choise = user_choise.lower()

        # idea => user_choise = red => burned by fire
        #      => user_choise = blue => Eaten by beasts.
        #      => user_choise = yellow => you win!!

        if(user_choise == "red"):
            print("\noops! Wrong decision. There is fire inside this room..")

            print("\n\n\t\t\t\t********** Game Over *************")

        elif(user_choise == "blue"):
            print("\noops! totally wrong decision. There is a lots of beasts inside the this room.")
            print("\n\n\t\t\t\t********** Game Over *************")

        elif(user_choise == "yellow"):
            print("\nYey!! You have taken a good decision.")

            print("\n\n\t\t\t ************ You Won **************")

        else:
            print("\nWrong choice. There is no room of " + str(user_choise) + " color gate. so you lost this game.")

            print("\n\n\t\t\t\t********** Game Over *************")




    else:
        print("\noops! Attacked by trout. you haven't survived")

        print("\n\n\t\t\t\t********** Game Over *************")

else:
    print("\noops! You Fall into the hole.")
    print("\n\n\t\t\t\t********** Game Over *************")



print("\n\n\ *********** Thank You So much for Playing this game ************** ")









