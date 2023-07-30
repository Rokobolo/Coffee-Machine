from menu import MENU
# Testobolo on NEW

def print_report(resources):
    for key in resources:
        if key == 'coffee':
            print(f"{key.title()}: {resources[key]}g")
        elif key == 'money':
            print(f"{key.title()}: ${resources[key]}")
        else:
            print(f"{key.title()}: {resources[key]}ml")


def check_resources(menu_item, resources):
    ingredients = MENU[menu_item]['ingredients']
    for item in ingredients:
        quantity_required = ingredients[item]
        # print(quantity_required)  # test code
        if quantity_required > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def insert_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def return_change(money, cost, choice):
    """money = how much inserted, cost = cost of the beverage, choice = user choice"""
    if money == cost:
        print(f"Here's your {choice}")
    elif money > cost:
        print(f"Here's your {choice}")
        print(f"Take your change: ${round(money - cost,2)}")
    else:
        print("Sorry, not enough money inserted. Money refunded.")
        return False
    return True


def use_resources(choice, resources, cost):
    for key in MENU[choice]['ingredients']:
        resources[key] -= MENU[choice]['ingredients'][key]
    resources['money'] += cost


def coffe_machine():
    coffe_option = list(MENU.keys())
    can_proceed = True
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0,
    }

    while can_proceed:
        enough_money = False
        user_choice = input("What would you like? espresso/latte/cappuccino: ").lower()
        if user_choice == "report":
            print_report(resources)
        elif user_choice == "off":
            can_proceed = False
        elif user_choice in coffe_option:
            drink_cost = MENU[user_choice]['cost']
            enough_ingredients = check_resources(user_choice, resources)
            if enough_ingredients:
                while not enough_money:
                    money = insert_money()
                    enough_money = return_change(money, drink_cost, user_choice)
                use_resources(user_choice, resources, drink_cost)


coffe_machine()
