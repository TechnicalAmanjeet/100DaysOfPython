#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

seed = int(input("Enter a seed number : "))
random.seed(seed)

coin_toss = random.randint(0,1)

if coin_toss == 0:
  print("Heads")
else:
  print("Tails")









