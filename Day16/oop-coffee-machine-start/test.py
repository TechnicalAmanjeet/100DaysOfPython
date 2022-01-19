from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# creating class of coffee maker , Menu item and menu
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

if __name__ == '__main__':
    while True:
        coffee_name = input(f"Which coffee do you want? ( {menu.get_items()} ) : ")

        if coffee_name == "report":
            coffee_maker.report()
            money_machine.report()

        elif coffee_name == "off":
            break

        else:
            item = menu.find_drink(coffee_name)

            if not item == None:
                if coffee_maker.is_resource_sufficient(item):
                    # print(money_machine.make_payment(item.cost))
                    if money_machine.make_payment(item.cost):
                        name = coffee_maker.make_coffee(item)






