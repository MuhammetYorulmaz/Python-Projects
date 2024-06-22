profit = 0
resources = {
    "water": 3,
    "milk": 2000,
    "coffee": 1000,
    "chocolate": 500
}


def is_resources_sufficient(coffee_size, coffee_name, order_ingredients):

    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item} for {coffee_size} {coffee_name}.")
            return False
        return True

# TODO 1: You should add a control system when you should input money values!


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    return total

# TODO 2: The program doesn't read profit values ?
# TODO 3: If the costumer doesn't want to buy coffee after didn't give enough money! You should ask
#  whether still wants to buy or not!


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change != 0:
            print(f"\nHere is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")

        # decision_add_more_money = input(f"Sorry ${payment} not enough money."
        #                                 f"You should pay ${drink['cost'] - payment} more. "
        #                                 f"Would you like to add more coins? y/n: ").lower()
        # if decision_add_more_money == 'y':
        #     payment += process_coins()
        #     print('New payment:', payment)
        #     is_transaction_successful(payment, drink['cost'])
        # else:
        #     print('Thank you!\n')

        return False


def make_coffee(drink_name, order_ingredients):

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink_name} ☕️. Enjoy!")
