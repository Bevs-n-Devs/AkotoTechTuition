# MATH CHALLENGE
print('*'*3, 'MATH CHALLENGE', '*'*3)

# 1. Create two variables, `num1` and `num2`, and store the values 8 and 3 in them.
#    Perform the following operations using these variables and print the results:
#    a) Add `num1` and `num2`
#    b) Subtract `num2` from `num1`
#    c) Multiply `num1` and `num2`
#    d) Divide `num1` by `num2`
#    The print message should display the results of each operation.
num1 = 8
num2 = 3

print('Add:', num1 + num2)
print('Subtract:', num2 - num2)
print('Multiply:', num1 * num2)
print('Divide:', num1 / num2)
print()

# 2. Create a variable called `total_cookies` and store the value 17 in it.
#    Create another variable called `people` and store the value 4 in it.
#    Create a variable called `result` and use the modulus operator to find 
#    out how many cookies would be left over, if the cookies were divided evenly among the people.
#    The print message should say: "There are -- cookies left over."
#    `--` = This is where the result variable should be.
total_cookies = 178
people = 4
result = total_cookies % people

print(f'There are {result} cookies left.')
print()


# 3. Use the following numbers to test math functions:
#    a) Find the absolute value of -10 using `abs()`
#    b) Raise 2 to the power of 5 using `pow()`
#    c) Find the maximum number between 25, 3, and 99 using `max()`
#    d) Round the float number 6.75 to the nearest integer using `round()`
#    Print the results of each math function.
print('Absolute:', abs(-10))
print('Power of:', pow(2,5))
print('Max:', max(25, 3, 99))
print('Round:', round(6.75))
print()


# 4. Import the following functions from the math module: `floor`, `ceil`, `sqrt`.
#    Use them to perform the following:
#    a) Use `floor()` to round down the number 8.9
#    b) Use `ceil()` to round up the number 2.1
#    c) Use `sqrt()` to find the square root of 64
#    Print the results for each function.
from math import floor, ceil, sqrt

print('Round DOWN:', floor(8.9))
print('Round UP', ceil(2.1))
print('Squre Root:', sqrt(64))