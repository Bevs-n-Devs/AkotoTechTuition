# Welcome to the session on Python Functions!

# 1. Introduction to Functions
# Functions are a collection of code that performs a specific task.
# They allow you to write code once and reuse it, reducing repetition.
# Functions also help organize your code into manageable chunks.

# 2. Writing a Function
# The syntax to create a function looks like this:
# def function_name():
#     function_code

# Let's create a simple function called 'say_hi'.
def say_hi():
    print("Hello user!")

# Calling the function to see its output
say_hi()  # This will print: Hello user!

# 3. Function Parameters
# Functions can take parameters, which are pieces of information you give to the function.
# If a function requires parameters, you must provide them when calling the function.

# Example of a function with a parameter
def say_hi_with_name(name):
    print(f"Hello {name}")

# Calling the function with a string as a parameter
say_hi_with_name("Sinclair")  # This will print: Hello Sinclair

# You can also pass variables as parameters
my_name = "Sinclair"
say_hi_with_name(my_name)  # This will still print: Hello Sinclair

# 4. Multiple Parameters
# Functions can accept multiple parameters.
# Let's create a function that also takes age as a second parameter.

def say_hi_with_name_and_age(name, age):
    print(f"Hello {name}, you are {age}")

# Calling the function with two parameters
say_hi_with_name_and_age("Sinclair", 35)  # This will print: Hello Sinclair, you are 35

# 5. Benefits of Using Functions
# Using functions makes your code easier to read and maintain.
# You can reuse functions with different arguments without rewriting code.

# -----------------------------------------------------------------------------------
# Challenges:

# 1. Create a Simple Function
# Write a function called 'greet_user' that prints "Welcome to the program!".
# Call the function to see the output.

def greet_user():
    print("Welcome to the program!")

greet_user()  # This will print: Welcome to the program!

# 2. Function with One Parameter
# Create a function called 'introduce_yourself' that takes a name as a parameter
# and prints "My name is {name}." Call the function with your own name.

def introduce_yourself(name):
    print(f"My name is {name}.")

introduce_yourself("YourName")  # Replace 'YourName' with your actual name

# 3. Function with Two Parameters
# Create a function called 'describe_pet' that takes a pet's name and type (e.g., dog, cat)
# and prints "I have a {type} named {name}." Call the function with your pet's details.

def describe_pet(name, pet_type):
    print(f"I have a {pet_type} named {name}.")

describe_pet("Buddy", "dog")  # Example output: I have a dog named Buddy.

# 4. Function for Addition
# Create a function called 'add_numbers' that takes two numbers as parameters
# and returns their sum. Call the function and print the result.

def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(10, 5)
print(result)  # This will print: 15

# 5. Function for Area of Rectangle
# Create a function called 'calculate_area' that takes width and height as parameters
# and returns the area of the rectangle (width * height). Call the function with values.

def calculate_area(width, height):
    return width * height

area = calculate_area(5, 10)
print(area)  # This will print: 50

# -----------------------------------------------------------------------------------
# Summary:
# - Functions are reusable blocks of code that perform specific tasks.
# - You can pass parameters to functions to customize their behavior.
# - Functions help to organize your code and make it easier to read and maintain.
# - You can create functions with one or more parameters, and call them whenever needed.
