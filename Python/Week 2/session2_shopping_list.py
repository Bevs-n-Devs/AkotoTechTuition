# TODO: https://www.programiz.com/python-programming/online-compiler/

# Welcome message
print("Welcome to the Shopping List Calculator!")

# 1. We will build a program where the user can enter items and their prices, and then we will calculate the total cost.
#    First, let's create variables for three items that the user wants to purchase.
#    Use input() to ask for the name of each item. 
#    Store the inputs in variables `item1`, `item2`, and `item3`.

item1 = input("Enter the name of your first item: ")
item2 = input("Enter the name of your second item: ")
item3 = input("Enter the name of your third item: ")

# 2. Now, ask the user to input the price of each item. 
#    Store the prices in variables `price1`, `price2`, and `price3`.
#    Remember that prices are numbers, so convert the inputs into float values to allow for calculations.

price1 = float(input(f"Enter the price of {item1}: "))
price2 = float(input(f"Enter the price of {item2}: "))
price3 = float(input(f"Enter the price of {item3}: "))

# 3. Create a variable called `total_cost` that adds all the item prices together.
#    Print out the total cost using an f-string.
#    CLUE: You can use the addition operator (+) to add the prices and print the result.

total_cost = price1 + price2 + price3
print(f"The total cost of {item1}, {item2}, and {item3} is: ${total_cost:.2f}")

# Explanation:
# We are using an F-string to print the item names and the total cost in one statement.
# The `.2f` formatting ensures that the total is shown to two decimal places, like in real-world prices.


# SHOPPING LIST CHALLENGE
print('*'*3, 'SHOPPING LIST CHALLENGE', '*'*3)
# 1. Extend the program to ask for a quantity for each item.
#    Multiply the price by the quantity and store the result in a new variable `total_item1`, `total_item2`, and `total_item3`.
#    Then, update the `total_cost` to add up the total cost for each item (price * quantity).
#    Print the final total using an f-string.
#    CLUE: You will need to use the multiplication operator (*) for price and quantity.

quantity1 = int(input(f"How many of {item1} would you like to buy? "))
quantity2 = int(input(f"How many of {item2} would you like to buy? "))
quantity3 = int(input(f"How many of {item3} would you like to buy? "))

total_item1 = price1 * quantity1
total_item2 = price2 * quantity2
total_item3 = price3 * quantity3

total_cost = total_item1 + total_item2 + total_item3
print(f"The total cost of {quantity1} {item1}(s), {quantity2} {item2}(s), and {quantity3} {item3}(s) is: ${total_cost:.2f}")

# 2. Add a discount feature! 
#    Ask the user if they have a discount code and apply a 10% discount to the total cost if they do.
#    If the user says 'yes', calculate a discounted total by subtracting 10% from the total cost. 
#    Print out the discounted total using an f-string.
#    CLUE: 10% can be calculated using the formula: `discount = total_cost * 0.10`.

discount_code = input("Do you have a discount code? (yes or no): ").lower()

if discount_code == "yes":
    discount = total_cost * 0.10
    total_cost -= discount
    print(f"Your discount has been applied! The new total is: ${total_cost:.2f}")
else:
    print(f"No discount applied. The total remains: ${total_cost:.2f}")

# 3. Advanced Challenge: Add sales tax.
#    Ask the user for their location and apply a different sales tax rate depending on the location.
#    For example: 8% for New York, 5% for California, and 7% for Florida.
#    Print the final total including sales tax using an f-string.

location = input("Where are you located? (London, Birmingham, Manchester): ").lower()

if location == "london":
    pass
