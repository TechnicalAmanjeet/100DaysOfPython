# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
first = 0
last = 0

name1 = name1.lower()
name2 = name2.lower()

first += name1.count('t')
first += name1.count('r')
first += name1.count('u')
first += name1.count('e')

first += name2.count('t')
first += name2.count('r')
first += name2.count('u')
first += name2.count('e')

last += name1.count('l')
last += name1.count('o')
last += name1.count('v')
last += name1.count('e')

last += name2.count('l')
last += name2.count('o')
last += name2.count('v')
last += name2.count('e')

love_score = first*10 + last

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")

elif love_score > 40 and love_score < 50:
  print(f"Your score is {love_score}, you are alright together.")

else:
  print(f"Your score is {love_score}.")



