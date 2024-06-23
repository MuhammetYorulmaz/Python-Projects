import json
from utils import resources, is_resources_sufficient, process_coins, is_transaction_successful, make_coffee


def coffee_machine():
    with open('data/menu.json', 'r') as file:
        menu = json.load(file)
    size_of_coffees = '/'.join([list(value.keys()) for key, value in menu.items()][0])
    type_of_coffees = '/'.join(list(menu.keys()))

    machine_condition = True
    while machine_condition:
        choice_coffee = input(f"What would you like? ({type_of_coffees}) or exit: ").lower()

        if choice_coffee in type_of_coffees.split('/'):

            size_condition = True
            while size_condition:
                choice_size_of_coffee = input(f"Which size would you like? ({size_of_coffees}): ").lower()
                if choice_size_of_coffee in size_of_coffees.split('/'):

                    drink = menu[choice_coffee][choice_size_of_coffee]
                    if is_resources_sufficient(choice_size_of_coffee, choice_coffee, drink['ingredients']):
                        print(f"\nPrice of {choice_size_of_coffee} {choice_coffee} is ${drink['cost']}.")
                        payment = process_coins()
                        if is_transaction_successful(payment, drink['cost']):
                            make_coffee(choice_coffee, drink['ingredients'])

                            continue_for_another_order = input("\nWould you like to order more coffee? (y/n): ").lower()
                            if continue_for_another_order == 'n':
                                print("Thank you!")
                                machine_condition = False

                    size_condition = False
                else:
                    print("You chose a coffee size that not on the menu!")
        elif choice_coffee == 'report':
            print('\nStock of Products:')
            for key, value in resources.items():
                print(f"{key.capitalize()}: {value}")
            # print(f"Profit: ${profit} \n")
        elif choice_coffee == 'exit':
            print("Successfully exited the program")
            machine_condition = False
        else:
            print("You chose a coffee that not on the menu!\n")
