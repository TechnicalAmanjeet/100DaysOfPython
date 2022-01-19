from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# creating class of coffee maker , Menu item and menu
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:
    user_input = int(input("""
    Type 1. To print report.
    Type 2. To order new coffee.
    Type 3. Turn off the coffee machine.

    Enter your Choice : """))

    if user_input == 1:
        # solve problem of none in user input
        # print(coffee_maker.report())
        # print(money_machine.report())
        coffee_maker.report()
        money_machine.report()

    elif user_input == 2:
        coffee_name = input(f"Which coffee do you want? ( {menu.get_items()} ) : ")

        item = menu.find_drink(coffee_name)

        if not item == None:
            if coffee_maker.is_resource_sufficient(item):
                # print(money_machine.make_payment(item.cost))
                if money_machine.make_payment(item.cost):
                    name = coffee_maker.make_coffee(item)

    elif user_input == 3:
        break

    else:
        print("You entered wrong choice!")


print("***** Thanks for playing this game! *****")





