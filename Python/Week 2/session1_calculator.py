# Building A Calculator  
# TODO: https://www.giraffeacademy.com/programming-languages/python/creating-a-calculator/ 
#       https://www.programiz.com/python-programming/online-compiler/


# Introduction message
print("Welcome to the Basic Calculator!")

# 1. Create two input variables where the user can enter numbers.
#    Store these inputs in variables called `num1` and `num2`.
#    The input messages should say: "Enter a number: " and "Enter a 2nd number: "
#    CLUE: Use the input() function to get the values from the user.
print('Addition')
num1 = input("Enter a number: ")
num2 = input("Enter a 2nd number: ")

# 2. Convert `num1` and `num2` to float so we can add them together.
#    We need to convert the inputs because Python stores them as strings by default.
#    Use the float() function to convert the inputs.
num1 = float(num1)
num2 = float(num2)
print()

# 3. Create a variable called `add` that stores the result of adding `num1` and `num2`.
#    After adding the numbers, print the result in the format: "num1 + num2 = add".
#    Use an F-string to format your print statement.
#    CLUE: Use the format f"{num1} + {num2} = {add}".
add = num1 + num2
print(f"{num1} + {num2} = {add}")
print()

# Explanation: 
# We are using what is called an F-string to include the variables directly inside the string.
# Just put an `f` before the quotation marks, and inside curly brackets `{}`, 
# you can reference your variable name. It makes it easy to display variables with text!

# 4. *Advanced* Challenge: Instead of converting the inputs after creating the variables,
#    you can combine the input and conversion steps in one line.
#    Create the inputs as a tuple and convert them to floats at the same time. 
#    Store them in a variable called `add`. 
#    Then add the two numbers from the tuple and store the result in `result`. 
#    Finally, print the result in the same format as before.
add = float(input("Enter a number: ")), float(input("Enter a 2nd number: "))
result = add[0] + add[1]
print(f"{add[0]} + {add[1]} = {result}")


# CALCULATOR CHALLENGE
print('*'*3, 'CALCULATOR CHALLENGE', '*'*3)
# 1. Now that you have learned how to add two numbers, create variables for subtraction.
#    Follow the same steps as the addition process. 
#    Ask the user for two numbers and subtract them. 
#    Print the result in this format: "num1 - num2 = subtract".
#    CLUE: Use subtraction instead of addition in your formula.

# 2. Create variables for multiplication. 
#    Ask the user for two numbers and multiply them together. 
#    Print the result in this format: "num1 * num2 = multiply".

# 3. Create variables for division.
#    Ask the user for two numbers and divide the first by the second. 
#    Print the result in this format: "num1 / num2 = divide".