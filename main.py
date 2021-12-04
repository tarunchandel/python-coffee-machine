from math import ceil

from menu import MENU
from menu import resources


def print_report():
    for key, value in resources.items():
        print(key, ":", value)


# checks if there are enough resources to make the coffee
def check_ingredients(coffee):
    ingredients = coffee["ingredients"]
    for key, value in ingredients.items():
        if ingredients[key] >= resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


# deducts the resources as per the coffee ingredients
def deduct_resources(coffee):
    ingredients = coffee["ingredients"]
    for key, value in ingredients.items():
        resources[key] -= ingredients[key]


def collect_coins(cost):
    print(f"Please pay ${cost}. We only accept coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    calculate_coins_value(quarters, dimes, nickles, pennies, cost)


def calculate_coins_value(q, d, n, p, cost):
    user_paid = ceil((q * .25) + (d * .1) + (n * .05) + (p * .01))
    change = user_paid - cost
    if change > 0:
        print(f"Here is your change ${change}.")
    else:
        print(f"Please pay ${-change} more.")
        collect_coins(-change)


# bills the coffee
def bill_coffee(coffee):
    cost = coffee["cost"]
    collect_coins(cost)

    # adding money to resources
    resources["money"] += cost


# Preparing Coffee: Checking ingredients, billing coffee and then handing over the coffee.
def prepare_coffee(choice):
    if check_ingredients(MENU[choice]):
        bill_coffee(MENU[choice])
        deduct_resources(MENU[choice])
        print(f"Here is your {choice}. Enjoy!")


machine_on_flag = True
while machine_on_flag:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        print("Switched off!")
        machine_on_flag = False
    elif user_choice == "report":
        print_report()
    else:
        prepare_coffee(user_choice)
