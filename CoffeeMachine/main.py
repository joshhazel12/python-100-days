from data import starting_ingredients, drinks


def process_coins():
    print("Please insert coins.")
    total = int(input("Input how many pennies: ")) * 0.01
    total += int(input("Input how many nickels: ")) * 0.05
    total += int(input("Input how many dimes: ")) * 0.1
    total += int(input("Input how many quarters: ")) * 0.25

    return total


def is_resource_sufficient(order_ingredients):
    """Check if there are enough resources to make the drink."""
    for item in order_ingredients:
        if item in starting_ingredients:
            if order_ingredients[item] > starting_ingredients[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
            elif starting_ingredients[item] == 0:
                print(f"Sorry, {item} is not available.")
                return False
    return True


def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change == 0:
            return True
        else:
            global profit
            profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(order_ingredients, drink_name):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        if item in starting_ingredients:
            starting_ingredients[item] -= order_ingredients[item]
    print(f"Here's your {drink_name}, enjoy!☕")


profit = 0
is_on = True


while is_on:
    while True:
        choice = input("What would you like to order? (espresso/latte/cappuccino) ")
        if choice == "report":
            while choice == "report":
                print(f"Water: {starting_ingredients['Water']}ml")
                print(f"Milk: {starting_ingredients['Milk']}ml")
                print(f"Coffee: {starting_ingredients['Coffee']}g")
                print(f"Money: ${profit}")
                second_choice = input("What would you like to order?"
                                      "(espresso/latte/cappuccino")
        elif choice == "off":
            print("Goodbye")
            is_on = False
            break
        elif choice in ["espresso", "latte", "cappuccino"]:
            choice_of_drink = drinks.get(choice.capitalize())
            if is_resource_sufficient(order_ingredients={'Water': starting_ingredients['Water'],
                                                         'Milk': starting_ingredients['Milk'],
                                                         'Coffee': starting_ingredients['Coffee']}):
                if is_transaction_successful(money_received=process_coins(),
                                             drink_cost=choice_of_drink['Cost']):
                    make_coffee(order_ingredients=choice_of_drink, drink_name=choice)
        else:
            print("Invalid input. Please try again. ")
