import sys
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def resources_update(chosen_coffee):
    coffees_water = MENU[chosen_coffee]["ingredients"]["water"]
    if chosen_coffee == "latte" or chosen_coffee == "cappuccino":
        coffees_milk = MENU[chosen_coffee]["ingredients"]["milk"]
    coffees_coffee = MENU[chosen_coffee]["ingredients"]["coffee"]

    resources["water"] -= coffees_water
    if chosen_coffee == "latte" or chosen_coffee == "cappuccino":
        resources["milk"] -= coffees_milk
    resources["coffee"] -= coffees_coffee



def money_calculating(quarters_money, dimes_money, nickles_money, pennies_money, chosen_coffee):
    total_money = (quarters_money * 0.25) + (dimes_money * 0.1) + (nickles_money * 0.05) + (pennies_money * 0.01)
    coffee_cost = MENU[chosen_coffee]["cost"]
    remaining_money = total_money - coffee_cost
    remaining_money = round(remaining_money, 2)
    if remaining_money < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif remaining_money == 0:
        print(f"Here is your {chosen_coffee} ☕ Enjoy!")
        resources["money"] += coffee_cost
        return True
    elif remaining_money > 0:
        print(f"Here is ${remaining_money} dollars in change.")
        print(f"Here is your {chosen_coffee} ☕ Enjoy!")
        resources["money"] += coffee_cost
        return True



def resources_control(coffee):
    coffees_water = MENU[coffee]["ingredients"]["water"]
    if coffee == "latte" or coffee == "cappuccino":
        coffees_milk = MENU[coffee]["ingredients"]["milk"]
    coffees_coffee = MENU[coffee]["ingredients"]["coffee"]

    if coffee == "latte" or coffee == "cappuccino":
        if coffees_water <= resources["water"] and coffees_milk <= resources["milk"] and coffees_coffee <= resources["coffee"]:
            print("Please insert coins.")
            return True
        elif coffees_water > resources["water"]:
            print("Sorry there is not enough water.")
            return False
        elif coffees_milk > resources["milk"]:
            print("Sorry there is not enough milk")
            return False
        elif coffees_coffee > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            return False
    elif coffee == "espresso":
        if coffees_water <= resources["water"] and coffees_coffee <= resources["coffee"]:
            print("Please insert coins.")
            return True
        elif coffees_water > resources["water"]:
            print("Sorry there is not enough water.")
            return False
        elif coffees_coffee > resources["coffee"]:
            print("Sorry there is not enough coffee.")
            return False



def check_prompt(prompt):
    if prompt == "report":
        for i in resources:
            if i != "coffee" and i!= "money":
                print(f"{i}".capitalize() + f": {resources[i]}ml")
            elif i == "coffee":
                print(f"{i}".capitalize() + f": {resources[i]}gr")
            elif i == "money":
                print(f"{i}".capitalize() + f": ${resources[i]}")
        return False
    elif prompt == "off":
        sys.exit()
    elif prompt == "espresso" or prompt == "latte" or prompt == "cappuccino":
        return resources_control(prompt)



while True:
    user_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    continue_status = check_prompt(user_prompt)
    if continue_status:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        delivery_coffee = money_calculating(quarters, dimes, nickles, pennies, user_prompt)
        if delivery_coffee:
            resources_update(user_prompt)