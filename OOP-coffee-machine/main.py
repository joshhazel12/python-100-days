from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to drink? ({options}) ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        print("Goodbye")
        is_on = False
        break
    elif choice in ["espresso", "latte", "cappuccino"]:
        drink = menu.find_drink(choice)
        can_make = coffee_maker.is_resource_sufficient(drink)
        if can_make and money_machine.make_payment(drink):
            coffee_maker.make_coffee(drink)
