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
}

# TODO: 1. Print report
def print_report():
    for key, _ in resources.items():
        print(f"{key}: {resources[key]}")
    return

# TODO: 2. Check resources
def check_resources(drink):
    for key, value in MENU[drink]["ingredients"].items():
        if resources[key] < value:
            print(f"Sorry there is not enough {key}.")
            return False
    return True

#TODO: 3. Process coins
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total

#TODO: 4. Check transaction
def check_transaction(drink, total):
    if total < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total > MENU[drink]["cost"]:
        change = total - MENU[drink]['cost']
        print(f"Here is ${change:.2f} in change.")
    return True

#TODO: 5. Make coffee
def make_coffee(drink):
    for key, value in MENU[drink]["ingredients"].items():
        resources[key] -= value
    print(f"Here is your {drink}. Enjoy!")
    return


#TODO: 6. Main function
def main():
    while True:
        drink = input("What would you like? (espresso/latte/cappuccino): ")
        if drink == "off":
            break
        elif drink == "refill":
            for key, _ in resources.items():
                resources[key] = 500
            print("Refilled all resources.")
        elif drink == "report":
            print_report()
        elif drink in MENU:
            if check_resources(drink):
                total = process_coins()
                if check_transaction(drink, total):
                    make_coffee(drink)
        else:
            print("Invalid input.")
    return



if __name__ == "__main__":
    main()
