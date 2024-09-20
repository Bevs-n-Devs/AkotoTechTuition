# Welcome to the session on Python Return Statements!

# 1. Introduction to Return Statements
# A return statement allows a function to give back data after performing its task.
# Unlike print statements, which display output, return statements send data back to the caller.

# 2. Writing a Function with a Return Statement
# The syntax for a function with a return statement looks like this:
# def function_name(parameter):
#     return function_code

# Example of a function that returns a greeting
def say_hi(name, age):
    return f"Hello {name}, you are {age}"

# 3. Printing the Returned Value
# You can print the result of a function by calling it directly in a print statement.
print(say_hi("Sinclair", 35))  # This will print: Hello Sinclair, you are 35

# 4. Storing the Returned Value in a Variable
# To make the code more readable, you can store the returned value in a variable and print that variable.
greeting = say_hi("Sinclair", 35)
print(greeting)  # This will also print: Hello Sinclair, you are 35

# 5. Important Reminder
# Once a return statement is executed, the function exits. 
# Therefore, you cannot use a print statement after a return statement inside the same function.

# Example of incorrect usage
def incorrect_function(parameter):
    return parameter
    # print(parameter)  # This line will not execute because the function has already returned

# 6. Challenges:

# 1. Create a Simple Function
# Write a function called 'calculate_square' that takes a number as a parameter and returns its square.
# Call the function and print the result.

def calculate_square(number):
    return number ** 2

print(calculate_square(4))  # This will print: 16

# 2. Function with Two Parameters
# Write a function called 'multiply' that takes two numbers and returns their product.
# Call the function and print the result.

def multiply(num1, num2):
    return num1 * num2

print(multiply(5, 3))  # This will print: 15

# 3. Function for Full Name
# Create a function called 'full_name' that takes a first name and last name and returns the full name.
# Call the function with your own names.

def full_name(first_name, last_name):
    return f"{first_name} {last_name}"

print(full_name("Sinclair", "Smith"))  # This will print: Sinclair Smith

# 4. Function for Area of Circle
# Create a function called 'calculate_area_circle' that takes the radius as a parameter
# and returns the area of a circle (π * radius^2). Use 3.14 for π.

def calculate_area_circle(radius):
    return 3.14 * (radius ** 2)

print(calculate_area_circle(5))  # This will print: 78.5

# 5. Function for Age Calculation
# Create a function called 'years_until_100' that takes a person's age and returns how many years 
# they have until they turn 100. Call the function with your age.

def years_until_100(age):
    return 100 - age

print(years_until_100(35))  # This will print: 65

# -----------------------------------------------------------------------------------
# Summary:
# - Return statements allow functions to send data back to the caller.
# - You can print the returned value directly or store it in a variable for clarity.
# - Remember that once a return statement is executed, the function exits, so you cannot print after returning.
