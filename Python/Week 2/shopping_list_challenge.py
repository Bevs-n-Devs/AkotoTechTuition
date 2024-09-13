# SHOPPING LIST CHALLENGE
print('*'*3, 'SHOPPING LIST CHALLENGE', '*'*3)
# 1. Extend the program to ask for a quantity for each item.
#    Multiply the price by the quantity and store the result in a new variable `total_item1`, `total_item2`, and `total_item3`.
#    Then, update the `total_cost` to add up the total cost for each item (price * quantity).
#    Print the final total using an f-string.
#    CLUE: You will need to use the multiplication operator (*) for price and quantity.

item1 = input("Enter the name of your first item: ")
price1 = float(input(f"Enter the price of {item1}: "))

item2 = input("Enter the name of your second item: ")
price2 = float(input(f"Enter the price of {item2}: "))

item3 = input("Enter the name of your third item: ")
price3 = float(input(f"Enter the price of {item3}: "))


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
#    For example: 8% for London, 5% for Birmingham, and 7% for Manchester.
#    Print the final total including sales tax using an f-string.

location = input("Where are you located? (London, Birmingham, Manchester): ").lower()

if location == "london":
    tax = total_cost * 0.08
elif location == "birmingham":
    tax = total_cost * 0.05
elif location == "manchester":
    tax = total_cost * 0.07
else:
    tax = 0
    print("No sales tax applied for your location.")

total_cost += tax
print(f"The total cost after applying sales tax for {location.title()} is: ${total_cost:.2f}")
