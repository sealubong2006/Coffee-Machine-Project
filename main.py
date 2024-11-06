# MENU dictionary defines the coffee options, their required ingredients, and the cost.
MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

# Tracks the total money earned from coffee sales.
profit = 0

# Dictionary representing the current supply of ingredients in the coffee machine.
resources = {"water": 300, "milk": 200, "coffee": 100}


def check_resources(ingredients):
    """
    Checks if there are enough ingredients to make the requested drink.
    Returns True if resources are sufficient, otherwise False.
    """
    for item, amount in ingredients.items():
        if resources.get(item, 0) < amount:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def calculate_payment():
    """
    Asks the user to insert coins and calculates the total amount.
    Returns the total value of the inserted coins.
    """
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return quarters + dimes + nickles + pennies


def process_transaction(cost, payment):
    """
    Checks if the inserted payment is enough to cover the drink's cost.
    If sufficient, calculates change and updates profit. Returns True.
    If insufficient, refunds money and returns False.
    """
    global profit
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
        profit += cost
        return True
    print("Sorry, that's not enough money. Money refunded.")
    return False


def make_drink(name, ingredients):
    """
    Deducts the required ingredients from resources and prints a message
    confirming that the drink has been served.
    """
    for item, amount in ingredients.items():
        resources[item] -= amount
    print(f"Here is your {name} ☕️. Enjoy!")


def coffee_machine():
    """
    Main function that runs the coffee machine program.
    Allows the user to choose a drink, view the report, or turn off the machine.
    Handles each action based on user input.
    """
    global profit
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # Turn off the machine
        if choice == "off":
            print("Turning off the coffee machine.")
            break

        # Display the report of current resources and profit
        elif choice == "report":
            for item, amount in resources.items():
                unit = "ml" if item != "coffee" else "g"
                print(f"{item.capitalize()}: {amount}{unit}")
            print(f"Money: ${profit}")

        # If valid coffee choice is entered
        elif choice in MENU:
            drink = MENU[choice]

            # Check if enough resources are available
            if check_resources(drink["ingredients"]):

                # Get payment and check if it covers the cost
                payment = calculate_payment()
                if process_transaction(drink["cost"], payment):
                    # Make the drink and update resources
                    make_drink(choice, drink["ingredients"])

        # Handle invalid input
        else:
            print("Invalid selection. Please choose espresso, latte, or cappuccino.")


# Run the coffee machine
coffee_machine()
