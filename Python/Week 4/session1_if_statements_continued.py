# WEEK 4: If Statements (continued) - Comparison Operators

# 1. Introduction to Comparison Operators
# Comparison operators are used to compare two values (numbers, strings, booleans).
# Depending on the result, the code will execute different actions.

# 2. List of Comparison Operators
# - Greater than: >             (A > B)   If the first value is GREATER than the second value
# - Less than: <                (A < B)   If the first value is LESS than the second value
# - Greater or equal to: >=     (A >= B)  If the first value is GREATER OR EQUAL to the second value
# - Less or equal to: <=        (A <= B)  If the first value is LESS OR EQUAL to the second value
# - Equal to: ==                (A == B)  If the first value is EQUAL to the second value
# - Not equal to: !=            (A != B)  If the first value is NOT EQUAL to the second value

# 3. Example: Finding the Maximum Number
# We will create a function that takes three numbers and returns the largest using comparison operators.
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return f"Max number: {num1}"
    elif num2 >= num1 and num2 >= num3:
        return f"Max number: {num2}"
    else:
        return f"Max number: {num3}"

# Testing the function
print(max_num(3, 19, 7))  # This will return "Max number: 19"

# 4. Example: Picking a Colour
# A function that prompts the user to pick a colour and returns a message based on the choice.
def pick_colour():
    colour = input("Pick a colour (1 = red, 2 = blue, 3 = green, 4 = purple): ")
    if colour == "1":
        return "You picked red!"
    elif colour == "2":
        return "You picked blue!"
    elif colour == "3":
        return "You picked green!"
    elif colour == "4":
        return "You picked purple!"
    else:
        return "Select a number from 1 - 4"

# Uncomment the next line to run the function and see the result
# print(pick_colour())

# 5. Example: Checking for Equality with !=
# Comparing two variables to check if they are not equal.
animal1 = "cat"
animal2 = "dog"

if animal1 != animal2:
    print("These animals are not the same!")  # This will print
else:
    print("These animals are identical")

# Change animal2 to "cat" and see what happens
# animal2 = "cat"

# 6. Challenges:
# 1. Create a function named compare_numbers that takes two numbers as parameters
#    and prints which number is larger. If they are equal, print "The numbers are equal."

def compare_numbers(num1, num2):
    if num1 > num2:
        print(f"{num1} is larger than {num2}.")
    elif num1 < num2:
        print(f"{num2} is larger than {num1}.")
    else:
        print("The numbers are equal.")

# Test the function
compare_numbers(10, 20)  # Change the values to test different scenarios

# 2. Write a function called check_animal that takes an animal name as a parameter
#    and prints whether it is a cat or not. Use the != operator to compare.

def check_animal(animal):
    if animal != "cat":
        print(f"{animal} is not a cat.")
    else:
        print("This is a cat!")

# Test the function
check_animal("dog")  # Change the argument to test with different animals

# 3. Create a program that asks for a user's age and checks if they are an adult (18 or older).
#    Print appropriate messages based on the comparison.

def check_age():
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are not an adult.")

# Uncomment the next line to run the function
# check_age()

# -----------------------------------------------------------------------------------
# Summary:
# - Comparison operators help in making decisions in code.
# - You can use if, elif, and else statements with these operators to execute different actions.
