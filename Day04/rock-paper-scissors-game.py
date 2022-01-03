rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

item_for_game = [rock,paper,scissors]

import random

computer_choice = random.randint(0,2)

print("**** Welcome to rock , paper and scissor game *******")
user_choice = int(input("\nwhat is your choice? 0 for rock, 1 for paper and 3 for scissor : "))

if not ( user_choice==0 or user_choice==1 or user_choice==2):
    print("Wrong choice! please read option correctly!!")
    exit(0)

print(f"Your choice is {user_choice}")

print(f"\n {item_for_game[user_choice]}")

print(f"\n Computer Choice is {computer_choice}")

print(f"\n {item_for_game[computer_choice]}")

# rock => 0 , paper => 1 and scicer => 2

if user_choice == computer_choice:
    print("\n\n****** Draw!! *******")
elif user_choice == 0:
    if computer_choice == 1:
        print("\n\n **** Computer Won!!! ****")
    else:
        print("\n\n **** You Won!! ****")
elif user_choice == 1:
    if computer_choice == 0:
        print("\n\n **** You Won!! ****")
    else:
        print("\n\n **** Computer Won!!! ****")
elif user_choice == 2:
    if computer_choice == 0:
        print("\n\n **** Computer Won!!! ****")
    else:
        print("\n\n **** You Won!! ****")


print("\n\n ***** Thank you for playing this game ******")
