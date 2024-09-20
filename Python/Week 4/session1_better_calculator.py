# Saturday 2HR: Better Calculator

# 1. Introduction
# In this session, we will build a better calculator using conditional logic with if statements
# and comparison operators. This calculator will allow users to enter two numbers and a math operator
# to receive an answer. We will also display the calculation performed using f-strings.

# 2. Getting User Input
# First, we'll get the necessary inputs from the user: two numbers and a math operator.
num1 = float(input("Enter the first number (num1): "))  # Convert input to float
calculate = input("Enter a math operation (+, -, x, /): ")  # Get the math operator
num2 = float(input("Enter the second number (num2): "))  # Convert input to float

# 3. Performing Calculations with Conditional Logic
# We will use if statements to determine which operation to perform.
if calculate == "+":
    result = num1 + num2
    print(f"{num1} {calculate} {num2} = {result}")  # Print the calculation
elif calculate == "-":
    result = num1 - num2
    print(f"{num1} {calculate} {num2} = {result}")  # Print the calculation
elif calculate == "x" or calculate == "*":
    result = num1 * num2
    print(f"{num1} {calculate} {num2} = {result}")  # Print the calculation
elif calculate == "/":
    if num2 != 0:  # Check for division by zero
        result = num1 / num2
        print(f"{num1} {calculate} {num2} = {result}")  # Print the calculation
    else:
        print("Error: Cannot divide by zero!")  # Handle division by zero
else:
    print("Invalid operator. Please select a valid math operator.")  # Invalid operator message

# 4. Handling Invalid Input
# If the user enters a word instead of a number, an error will occur.
# For example, if we enter a string in num1 or num2, it will raise a ValueError.

# Uncomment the following lines to test with invalid inputs
# num1 = float(input("Enter the first number (num1): "))  # If you enter a word, this will raise an error
# num2 = float(input("Enter the second number (num2): "))  # Same here

# 5. Summary
# In this lesson, we learned how to create a basic calculator that performs addition, subtraction,
# multiplication, and division based on user input. We also handled invalid operators and division by zero.
