# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
year_left = 90 - int(age)

month_left = year_left*12

weak_left = year_left*52

days_left = year_left * 365

print(f'You have {days_left} days, {weak_left} weeks, and {month_left} months left.')
