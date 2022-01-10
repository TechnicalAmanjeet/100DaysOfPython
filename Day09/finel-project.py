import os

# project : build a sailent bid program

# creating a dictionary where we will store key value pair as name and the bid
bid = {}

# function to bid annoumasly
def sailent_bid():
    user_name = input("What is Your Name? : ")
    user_bid = int(input("what's Your bid? : $"))
    bid.update({user_name:user_bid})
    print(bid)



print("Welcome to the secret auction game")
sailent_bid()

while True:
    is_bieders = input("Are There any other bider's? Type 'yes' or 'no' : ")
    if is_bieders == 'yes':
        # os.system('clear')
        sailent_bid()
    elif is_bieders == 'no':
        break
    else:
        print("please write spelling correctly!!")

max_bid = 0
max_bid_biders = ""

for biders,bid in bid.items():
    if bid > max_bid:
        max_bid = bid
        max_bid_biders = biders

print(f"The winner is {max_bid_biders} and his/her bid is ${max_bid}")