# Coffee Machine Program

This program simulates a coffee machine that allows users to purchase coffee, check ingredient availability, and view the machine's financial report. 

## Features

1. **Coffee Options**: The machine offers three types of coffee - Espresso, Latte, and Cappuccino.
2. **Resource Management**: The machine tracks the available quantity of water, milk, and coffee. It updates resources after each purchase.
3. **Coin Processing**: Users pay by inserting quarters, dimes, nickels, and pennies, with the program calculating the total.
4. **Transaction Handling**: The program verifies if the inserted money is sufficient for the selected coffee. If enough, it processes the transaction; if not, it refunds the money.
5. **Reporting**: Users can request a report to view current resources and total profit.
6. **Turn Off Option**: Users can turn off the coffee machine with the `"off"` command.

## How to Use

1. **Run the Program**: Start the program, which will continue to prompt for user input.
2. **Choose an Option**:
   - Type `"espresso"`, `"latte"`, or `"cappuccino"` to order a coffee.
   - Type `"report"` to view the current ingredient levels and profit.
   - Type `"off"` to turn off the machine.

3. **Inserting Coins**: If ordering a coffee, you’ll be prompted to insert coins (quarters, dimes, nickels, and pennies). Enter the number of each, and the machine calculates the total.
4. **Receive Change**: If the amount entered is more than the coffee cost, the machine gives change.

## Code Structure

1. **`MENU` Dictionary**: Stores coffee options, required ingredients, and cost.
2. **Global Variables**:
   - `profit`: Tracks total earnings.
   - `resources`: Tracks current levels of ingredients.
3. **Functions**:
   - `check_resources()`: Checks if ingredients are sufficient to make the requested drink.
   - `calculate_payment()`: Prompts for coin input and calculates total payment.
   - `process_transaction()`: Confirms if payment is sufficient and updates profit.
   - `make_drink()`: Reduces ingredients for the requested drink and serves it.
   - `coffee_machine()`: Main loop handling user commands and managing the coffee-making process.

## Example Usage

```plaintext
What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.5 in change.
Here is your latte ☕️. Enjoy!
```

## Requirements

No special libraries are required to run this code. It runs directly in Python 3.

---

Happy brewing! ☕️
```
