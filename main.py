from data import resources
from data import MENU


def print_report():
    print("The resources in the machine;")
    for i in resources:
        print(f"{i}, {resources[i]}")


# TODO: 2. check resources for the drink
def check_resources(drink):
    enough = True
    for i in MENU[drink]["ingredients"]:
        for j in resources:
            if j == i and resources[j] < MENU[drink]["ingredients"][i]:
                enough = False
    return enough


def reduce_resources(drink):
    for i in MENU[drink]["ingredients"]:
        for j in resources:
            if j == i:
                resources[j] -= MENU[drink]["ingredients"][i]


def order():
    drink = input("Press 'OFF' to turn off\nPress 'REPORT' for ingredients report\nWhat drink would you like to order? (espresso/latte/cappuccino): ")
    if drink.upper() == "OFF":
        print("Machine has been turned off.")
        return
    if drink.upper() == "REPORT":
        print_report()
        order()
    if not (check_resources(drink)):
        print(f"There are not enough resources for {drink}, try ordering something else")
        order()
    drink.lower()
    print("Please insert coins")
    quarters = int(input("How manu quarters? ($0.25): "))
    dimes = int(input("How manu dimes? ($0.1): "))
    nickles = int(input("How manu nickles? ($0.05): "))
    pennies = int(input("How manu dimes? ($0.01): "))
    money = 0
    money += quarters * 0.25
    money += dimes * 0.1
    money += nickles * 0.05
    money += pennies * 0.01
    cost = MENU[drink]['cost']
    if money < cost:
        print("You did not insert enough money, refunding!")
        order()
    elif money == cost:
        print("Here's your coffee, enjoy! ☕️ ")
    else:
        change = money - cost
        print(f"Here's your change (${change}), enjoy your coffee! ☕️")
    reduce_resources(drink)
    print_report()
    order()


order()