# WEEK 6: Sunday 1HR - Try Except

# 1. Introduction
# In this session, we will learn how to handle errors in our Python programs using try and except blocks.
# This helps prevent our program from stopping when it encounters an error.

# 2. What are Try and Except Blocks?
# Try and except blocks allow us to "try" executing a piece of code and "catch" any errors that occur.
# If an error occurs, we can provide a custom error message instead of the program crashing.

# 3. Structure of Try and Except
# We start with the 'try' keyword followed by the code we want to execute.
# If an error occurs, we use 'except' to handle it.

try:
    answer = 10 / int(input("Enter a number: "))  # Try to divide 10 by user input
except ZeroDivisionError:
    print("Cannot divide by 0")  # Handle division by zero
except ValueError:
    print("Please enter a correct number")  # Handle incorrect input
else:
    print(answer)  # Print the answer if no error occurs

# 4. Using Else and Finally
# The 'else' block runs if no exceptions are raised.
# The 'finally' block can be used to execute code regardless of whether an error occurred.

# Example with finally:
try:
    answer = 10 / int(input("Enter a number: "))
except ZeroDivisionError as z:
    print(z)  # Print the ZeroDivisionError message
except ValueError as v:
    print(v)  # Print the ValueError message
else:
    print(answer)  # Print the answer if no error occurs
finally:
    print("This will run no matter what.")  # This message will always print

# 5. Common Errors
# Here are a few common exceptions:
# - SyntaxError: Incorrect syntax in the code
# - IndentationError: Incorrect indentation
# - ValueError: Correct argument type, but wrong value
# For more exceptions, visit: https://www.programiz.com/python-programming/exceptions

# 6. Summary
# In this session, we learned how to use try and except blocks to catch errors in our programs.
# This allows us to handle errors gracefully and provide useful feedback to users.

# 7. Challenges
# Challenge 1: Modify the division example to handle cases where the user enters a floating-point number.
# Challenge 2: Create a program that prompts the user for their age and handles any input errors gracefully.
# Challenge 3: Write a function that reads a file and uses try/except to handle file not found errors.
# Challenge 4: Extend the previous function to also handle permission errors when trying to read the file.
