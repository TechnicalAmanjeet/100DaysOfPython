# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round((weight / (height ** 2)),2)

if bmi <= 18.5:
  print("you are underweight.")
elif bmi<=25:
  print("you have a noraml weight")
elif bmi <=30:
  print("you are slightly overweight")
elif bmi <=35:
  print("you are obese.")
else:
  print("you are clinically obese.")





