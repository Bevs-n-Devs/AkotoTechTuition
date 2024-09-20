# Welcome to the session on Python If Statements!

# 1. Introduction to If Statements
# If statements are used for conditional logic in programs, allowing them to make decisions based on conditions.
# When a condition is true, the code block inside the if statement runs.

# 2. Creating an If Statement
# The basic structure of an if statement is:
# if condition:
#     run_code

# Example of an if statement
is_male = True

if is_male:
    print("You are a male")  # This will print because is_male is True

# 3. Using Else with If Statements
# You can add an else statement to provide an alternative action when the condition is false.

is_male = False

if is_male:
    print("You are a male")
else:
    print("You are not a male")  # This will print because is_male is False

# 4. Using Elif for Multiple Conditions
# The elif statement allows you to check multiple conditions.

colour1 = False
colour2 = True
colour3 = False
colour4 = False

if colour1:
    print("Your colour is blue")
elif colour2:
    print("Your colour is red")  # This will print because colour2 is True
elif colour3:
    print("Your colour is green")
elif colour4:
    print("Your colour is yellow")
else:
    print("You did not pick a colour")

# 5. Understanding Indentation
# Indentation is crucial in Python. Ensure code within the if, elif, and else blocks is indented with 4 spaces.

# 6. Using 'or' to Combine Conditions
# The 'or' keyword allows for executing code if at least one condition is true.

colour1 = False
colour2 = True

if colour1 or colour2:
    print("You selected blue or red")  # This will print
else:
    print("No colours were selected")

# 7. Using 'and' to Require Multiple True Conditions
# The 'and' keyword requires all conditions to be true for the code to execute.

colour1 = True
colour2 = True

if colour1 and colour2:
    print("You selected blue and red")  # This will print
else:
    print("No colours were selected")

# 8. Challenges:

# 1. Create an If Statement
# Write an if statement to check if a number is positive or negative.
number = -5
if number > 0:
    print("The number is positive")
else:
    print("The number is negative")  # This will print

# 2. Using Elif
# Write a program that checks the value of a variable and prints different messages based on the value.
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")  # This will print
else:
    print("Grade: D or F")

# 3. Multiple Conditions with 'or'
# Create variables for different fruits and check if any of them are true.
apple = False
banana = True
orange = False

if apple or banana:
    print("You selected an apple or a banana")  # This will print
else:
    print("No fruits selected")

# 4. Multiple Conditions with 'and'
# Check if a person is both a student and an employee.
is_student = True
is_employee = True

if is_student and is_employee:
    print("You are both a student and an employee")  # This will print
else:
    print("You are either not a student or not an employee")

# 5. Explore Conditions
# Experiment by changing the values of the variables used in the previous examples. 
# What happens when you set all conditions to False? Try to print messages accordingly!

# -----------------------------------------------------------------------------------
# Summary:
# - If statements allow you to execute code based on conditions.
# - Use else and elif to provide alternatives.
# - Indentation is crucial in Python for code structure.
# - Use 'or' and 'and' to combine conditions effectively.
