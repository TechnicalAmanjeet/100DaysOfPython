# q. generate password
import random

print("********* Welcome to Password generator **********")

# Mathod 1. Ask user only length of password

# password_length = int(input("How many letters would you want in your password? : "))
# password = ""
#
# for i in range(password_length):
#     random_number = random.randint(33, 126)
#     password+=(chr(random_number))
# print(f"Your Password is : {password}")


# Mathod 2. Ask user how many upper alphabeth , lower alphabeth , numbers and character want in his/her password

password = ""
uppercase_letter = int(input("How many upper case letters would you want in your password : "))
lowercase_letter = int(input("How many lower case letters would you like in your password : "))
numbers = int(input("How many numbers would you like in your password : "))
symbols = int(input("How many symbols would you want in your password : "))

# uppercase loop
for i in range(uppercase_letter):
    password += chr(random.randint(65,90))

# lowercase_loop
for i in range(lowercase_letter):
    password += chr(random.randint(97,122))

# numbers
for i in range(numbers):
    password += chr(random.randint(48,57))

# symbools
for i in range(symbols):
    password += chr(random.randint(33,47))

print(f"Your password : {password}")


# note : how to randomise them all other type letter at other place i.e
# password of uppercase or lowercase or numbers or symbols must not in secquence.

# solution of above problem is shuffel mathod of random.shuffle()
# this mathod works on list only i think.
password_list = []
for passwd in password:
    password_list.append(passwd)

# print(password_list)

random.shuffle(password_list)
advance_password = "".join(password_list)
print(f'advance password : {advance_password}')