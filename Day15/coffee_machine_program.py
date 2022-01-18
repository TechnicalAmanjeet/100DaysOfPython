from ingredient import *

# function of program starts here
# 1. print report

def print_report():
    """ it takes nothing as input and only it prints the available resourcess
        which we have at that moument"""
    for keys in resources:
        print(f"{keys} : {resources[keys]}")


# 2. function to convert take coin from user and covert it into doller and return it back
def insert_coin():
    """ take four type of coin i.e ( quarter , nikle , dime , penny ) as
        input and then convert it into doller and return that doller."""
    print("please insert coins!")
    quarter = float(input("How many quarters? : "))
    nickle = float(input("How many nickles? : "))
    dime = float(input("How many dimes? : "))
    penny = float(input("How many pennys? : "))
    # print(quarter*0.25,nickle*0.05,dime*0.10,penny*0.01)
    money_in_doller = (quarter * 0.25) + (nickle * 0.05) + (dime* 0.10) + ( penny * 0.01 )

    print(f"Here is ${money_in_doller} in change.")
    return money_in_doller

# check whether coffee machine have suffiecient report or not
# idea it take's input as coffee_name and as a out it return true if sufficient resources are there else return false




def sufficient_ingredient(coffee_name):
    """ idea it take's input as coffee_name and as a out it return
        true if sufficient resources are there else return false"""
    coffee = MENU[coffee_name]
    keys = ["ingredients","cost"]

    coffee_ingredient = coffee[keys[0]]
    coffee_cost = coffee[keys[1]]

    print(coffee_ingredient,coffee_cost)

    # resource_is_okay = True

    for key in coffee_ingredient:
        # print(key,coffee_ingredient[key],resources[key])
        if coffee_ingredient[key] >= resources[key]:
            # resource_is_okay = False
            print(f"Sorry! There is not enough {coffee_ingredient[key]}")
            return False

    return True


# function to check whether user provided money is enough to make coffee or not
def check_money(coffee_name,user_money):
    """ function to check whether user provided money is enough to
        make coffee or not"""
    coffee_cost = MENU[coffee_name]["cost"]
    if coffee_cost >= user_money:
        print(f"Sorry! You haven't Provided enough money to make {coffee_name}. ")
        print(f"{coffee_cost} money refunded.")
        return False

    print(f"heres your change. ${user_money - coffee_cost}")
    return True

def decrease_resource(coffee_name):
    """ decrease the quintity of ingredients in resources."""
    coffee = MENU[coffee_name]
    keys = ["ingredients", "cost"]

    coffee_ingredient = coffee[keys[0]]
    coffee_cost = coffee[keys[1]]

    for key in coffee_ingredient:
        resources[key] -= coffee_ingredient[key]

    resources["cost"] += coffee_cost


def buy_coffee():
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    user_money = insert_coin()

    if check_money(coffee,user_money):
        if sufficient_ingredient(coffee):
            print(f"Heres your {coffee} ☕. Enjoy! ")
            decrease_resource(coffee)




# coffee machine game code
def coffee_machine_game():

    user_choice = int(input("""
Type 1. print report.
Type 2. Turn off the coffee machine.
Type 3. Buy coffee.
Type 4. Exit the program.
        
Enter your Choice : """))

    if user_choice == 1:
        print_report()

    elif user_choice == 2:
        print("Closing the coffee machine!")
        return False

    elif user_choice == 3:
        # write a code to buy a coffee
        buy_coffee()

    elif user_choice == 4:
        return False

    else:
        print("you have entered wrong choice!!")

    return True






# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    start_game = True
    while start_game:
        start_game = coffee_machine_game()

    print("*** Thank you So Much for Playing This Game ***")
