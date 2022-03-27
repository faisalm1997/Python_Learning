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

# TODO: 1. Prompt user asking 'What would you like? (espresso/latte/cappuccino):
# TODO: 2. Turn off the coffee machine by entering 'off' in the prompt.
# TODO: 3. Print report of the resources.
# TODO: 4. Check if resources are sufficient.
# TODO: 5. Process coins based on quarters, dimes, nickles and pennies.
# TODO: 6. Check if the transaction was sufficient.
# TODO: 7. Make coffee and change resources in coffee machine.

cash = 0
 
 
def report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g\nMoney: ${cash}")
 
 
def money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total
 
 
def update_resources(choice):
    for e in MENU[choice]['ingredients']:
        resources[e] = resources[e] - MENU[choice]['ingredients'][e]
    global cash
    cash = cash + MENU[choice]['cost']
    report()
 
 
def check_resources(choice):
    if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        for e in MENU[choice]['ingredients']:
            if resources[e] > MENU[choice]['ingredients'][e]:
                change = round(money() - MENU[choice]['cost'], 2)
                if change > 0:
                    print(f"Here is your change: ${change}")
                    print(f"Here is your ☕, enjoy.")
                else:
                    print("Not enough money.")
                    check_resources(choice)
                update_resources(choice)
                coffee_machine()
            else:
                print(f"Sorry, not enough {e}")
                coffee_machine()
    else:
        print("Sorry I didn't understand. Try Again")
        coffee_machine()
 
 
def coffee_machine():
    working = True
    while working:
        choice = input("What would you like? espresso/latte/cappuccino: ").lower()
        check_resources(choice)
 
coffee_machine()