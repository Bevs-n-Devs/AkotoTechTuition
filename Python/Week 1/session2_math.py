# Math
# TODO: https://www.giraffeacademy.com/programming-languages/python/math/
#       https://www.programiz.com/python-programming/online-compiler/


# In Python, we can use different types of numbers: integers (whole numbers), 
# floats (decimals), and even negative numbers. We can perform basic 
# arithmetic operations like addition, subtraction, multiplication, and division.
print('Types of Numbers:')

int_num1 = 5
int_num2 = -3
float_num1 = 7.5
float_num2 = -2.7

print(int_num1)
print(int_num2)
print(float_num1)
print(float_num2)
print()

# You can do basic math in Python using operators:
# + for addition
# - for subtraction
# * for multiplication
# / for division
print('Basic Math:')

result = 3 + 5  # addition
print(result)   # should print 8
print()


# Python follows the standard order of operations (PEMDAS):
# Parentheses
# Exponents
# MD Multiplication & Division (from left to right)
# AS Addition & Subtraction (from left to right)
# Here is a video if you want to learn more about the order of operations: 
# https://www.khanacademy.org/math/cc-sixth-grade-math/x0267d782:cc-6th-exponents-and-order-of-operations/cc-6th-order-of-operations/v/more-complicated-order-of-operations-example
print('Order of Operations:')

result = 3 + 4 * 5   # multiplication happens first
print(result)        # should print 23
print()


# Change the order using parentheses
result = (3 + 4) * 5
print(result)        # should print 35
print()


# The modulus operator % gives the remainder after dividing two numbers.
print('Modulus Operator:')

# Example of modulus operator
remainder = 10 % 3  # 10 divided by 3 gives a remainder of 1
print(remainder)    # should print 1
print()


# You can store numbers in variables and use them later in calculations.
print('Storing Numbers in Variables:')

my_num = 15
print(my_num)       # should print 15
print()


# To use a number in a string, you need to convert it using str().
print('Converting Numbers to Strings:')

# Convert a number to a string and concatenate
my_num = 10
print("The number is " + str(my_num))  # should print "The number is 10"

# SIDENOTE: if we use an f-string in this case we would NOT need to convert it to a string
# because f-strings automatically converts any value to a string
print(f'The number is {my_num}')
print()


# Python provides built-in functions to perform common math operations:
# abs(num) – returns the absolute value
# pow(num1, num2) – raises num1 to the power of num2
# max() – returns the largest value
# min() – returns the smallest value
# round() – rounds a number to the nearest integer
print('Math Functions:')

print(abs(-5))        # should print 5
print(pow(2, 3))      # should print 8
print(max(3, 9, 1))   # should print 9
print(min(3, 9, 1))   # should print 1
print(round(4.6))     # should print 5
print()


# You can import additional math functions from Python’s math module.
print('Importing Math Functions:')

# Import specific functions from the math module
from math import floor, ceil, sqrt

print(floor(4.9))  # should print 4
print(ceil(4.1))   # should print 5
print(sqrt(16))    # should print 4.0
print()



# MATH CHALLENGE
print('*'*3, 'MATH CHALLENGE', '*'*3)

# 1. Create two variables, `num1` and `num2`, and store the values 8 and 3 in them.
#    Perform the following operations using these variables and print the results:
#    a) Add `num1` and `num2`
#    b) Subtract `num2` from `num1`
#    c) Multiply `num1` and `num2`
#    d) Divide `num1` by `num2`
#    The print message should display the results of each operation.

# 2. Create a variable called `total_cookies` and store the value 17 in it.
#    Create another variable called `people` and store the value 4 in it.
#    Create a variable called `result` and use the modulus operator to find 
#    out how many cookies would be left over, if the cookies were divided evenly among the people.
#    The print message should say: "There are -- cookies left over."
#    `--` = This is where the result variable should be.

# 3. Use the following numbers to test math functions:
#    a) Find the absolute value of -10 using `abs()`
#    b) Raise 2 to the power of 5 using `pow()`
#    c) Find the maximum number between 25, 3, and 99 using `max()`
#    d) Round the float number 6.75 to the nearest integer using `round()`
#    Print the results of each math function.

# 4. Import the following functions from the math module: `floor`, `ceil`, `sqrt`.
#    Use them to perform the following:
#    a) Use `floor()` to round down the number 8.9
#    b) Use `ceil()` to round up the number 2.1
#    c) Use `sqrt()` to find the square root of 64
#    Print the results for each function.
