import data


def check_resources():
    coffee_water = data.MENU[choice]["ingredients"]["water"]
    coffee_coffee = data.MENU[choice]["ingredients"]["coffee"]
    if choice == "espresso":
        coffee_milk = 0
    else:
        coffee_milk = data.MENU[choice]["ingredients"]["milk"]
    if water < coffee_water:
        print("Sorry there is not enough water.")
        return False
    elif coffee < coffee_coffee:
        print("Sorry there is not enough coffee.")
        return False
    elif milk < coffee_milk:
        print("Sorry there is not enough milk.")
        return False
    return True


# quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
def coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 + pennies
    return total


def make_coffee():
    if check_resources():
        total = coins()
        cost = data.MENU[choice]["cost"]
        if total >= cost:
            print(f"Here is ${round(total - cost, 2)} in change.")
            print(f"Here is your {choice} ☕. Enjoy!")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")


exit_ = False
water = data.resources["water"]
milk = data.resources["milk"]
coffee = data.resources["coffee"]
money = 0
while not exit_:
    choice = input("What would you like? (espresso/latte/cappuccino):\n")
    if choice == "report":
        print(f"water: {water}ml,\nmilk: {milk}ml\ncoffee: {coffee}g\nmoney: ${money}\n")
    elif choice == "off":
        exit_ = True
    else:
        if make_coffee():
            money += data.MENU[choice]["cost"]
            water -= data.MENU[choice]["ingredients"]["water"]
            if choice == "espresso":
                milk -= 0
            else:
                milk -= data.MENU[choice]["ingredients"]["milk"]
            coffee -= data.MENU[choice]["ingredients"]["coffee"]
