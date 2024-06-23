resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
    "chocolate": 500,
    "profit": 0
}


def is_resources_sufficient(coffee_size: str, coffee_name: str, order_ingredients: dict) -> bool:
    """
    Checks if the resources are sufficient to fulfill the coffee order.

    Args:
        coffee_size (str): The size of the coffee ordered (e.g., "tall", "grande").
        coffee_name (str): The name of the coffee ordered (e.g., "latte", "espresso").
        order_ingredients (dict): A dictionary containing the required amount of each ingredient.

    Returns:
        bool: True if resources are sufficient, False otherwise.

    Prints:
        A message indicating if there is not enough of a specific ingredient.
    """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item} for {coffee_size} {coffee_name}.")
            return False
        return True


def process_coins() -> float:
    """
    Calculates the total value of coins inserted by the user.

    This function prompts the user to input the number of quarters, dimes, and nickels.
    It ensures that the inputs are valid non-negative integers and calculates the
    total monetary value based on the inputs.

    Returns:
        float: The total value of the inserted coins in dollars.
    """
    def get_valid_input(prompt: str) -> int:
        """
        Prompts the user for input and validates that it is a non-negative integer.

        Args:
            prompt (str): The input prompt message.

        Returns:
            int: The validated non-negative integer input from the user.
        """
        while True:
            try:
                value = int(input(prompt))
                if value < 0:
                    raise ValueError("The value must be non-negative.")
                return value
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid integer.")

    print("Please insert coins.")
    total = get_valid_input("How many quarters?: ") * 0.25
    total += get_valid_input("How many dimes?: ") * 0.1
    total += get_valid_input("How many nickels?: ") * 0.05

    return total


# TODO 3: If the costumer doesn't want to buy coffee after didn't give enough money! You should ask
#  whether still wants to buy or not!


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change != 0:
            print(f"\nHere is ${change} in change.")
        # global profit
        resources['profit'] += drink_cost
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


def make_coffee(drink_name: str, order_ingredients: dict):
    """
    Deducts the required ingredients from the available resources and prepares the coffee.

    Args:
        drink_name (str): The name of the coffee drink being prepared.
        order_ingredients (dict): A dictionary containing the amount of each ingredient needed for the order.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink_name} ☕️. Enjoy!")
