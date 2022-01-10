import os

from logo import logo
from os import system

# project : Calculator

# function to calculate output and return it
def calculator(num1,operator,num2):
    if operator == '+': return num1+num2
    elif operator == '-': return num1-num2
    elif operator == '*': return num1*num2
    elif operator == '/': return num1/num2
    elif operator == '//': return num1//num2
    elif operator == '%': return num1%num2
    else: print(f"{operator} is not a valid operator!")

def taking_input_from_user_m1():
    num1 = int(input("Enter first number : "))
    print("+\n-\n*\n/\n%\n//")
    operator = input("Pick an operation : ")
    num2 = int(input("What's the next number : "))
    return [num1,operator,num2]

def taking_input_from_user_m2(num1):
    print("+\n-\n*\n/\n%\n//")
    operator = input("Pick an operation : ")
    num2 = int(input("What's the next number : "))
    return [num1, operator, num2]


if __name__ == '__main__':
    print("********** Calculator Game ************ \n")
    print(logo)
    input_from_user = taking_input_from_user_m1()
    num1 = input_from_user[0]
    operator = input_from_user[1]
    num2 = input_from_user[2]
    output = calculator(num1,operator,num2)
    print(f"{num1} {operator} {num2} = {output}")

    while True:
        os.system('cls')
        print(logo)
        print(f"""
        ********** Calculator Game ************ \n
        Type 1: To continue calculating with {output}.
        Type 2: To Start a new calculation.
        Type 3: exit.""")

        user_input = int(input("Pick your choice : "))
        if user_input == 1:
            input_from_user2 = taking_input_from_user_m2(output)
            num1 = input_from_user2[0]
            operator = input_from_user2[1]
            num2 = input_from_user2[2]
            output = calculator(num1, operator, num2)
            print(f"{num1} {operator} {num2} = {output}")

        elif user_input == 2:
            input_from_user = taking_input_from_user_m1()
            num1 = input_from_user[0]
            operator = input_from_user[1]
            num2 = input_from_user[2]
            output = calculator(num1, operator, num2)
            print(f"{num1} {operator} {num2} = {output}")

        elif user_input==3:
            break
        else:
            print("Please enter correct option!")


print("\n ****** ThankYou So Much for playing this Game *******")
