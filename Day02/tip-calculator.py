# first welcome user for playing this game
print("********** Welcome to the Tip Calculator ***********")
# idea is to
# 1. take total amount to pay as bill , input from user : total_bill
total_bill = float(input("What was the total bill : Rs. "))

# 2. how many people are there with you to whom you can split the bill : total_people
total_people = int(input("How many people to split the bill? "))

# 3. what percentage of tip do you want to give to better. ( 10 / 12 or 15 % )
percentage_tip = float(input("What percentage of tip would you like to give? "))

# now total tip will be
tip = (total_bill * percentage_tip) / 100

# total amount to pay
total_amount = total_bill + tip;

# each person amount to pay  would be
each_person_bill = total_amount/total_people;

print(f"Each person should pay: Rs. {each_person_bill}")
