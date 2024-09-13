# CALCULATOR CHALLENGE
print('*'*3, 'CALCULATOR CHALLENGE', '*'*3)
# 1. Now that you have learned how to add two numbers, create variables for subtraction.
#    Follow the same steps as the addition process. 
#    Ask the user for two numbers and subtract them. 
#    Print the result in this format: "num1 - num2 = subtract".
#    CLUE: Use subtraction instead of addition in your formula.
print('Subtraction')
subtract_num1 = input('Enter a number: ')
subtract_num_2 = input('Enter a 2nd number: ')

subtract_result = subtract_num1 - subtract_num_2
print(f'{subtract_num1} - {subtract_num_2} = {subtract_result}')
print()

# 2. Create variables for multiplication. 
#    Ask the user for two numbers and multiply them together. 
#    Print the result in this format: "num1 * num2 = multiply".
print('Multiplication')
multiply_num1 = input('Enter a number: ')
multiply_num2 = input('Enter a 2nd number: ')

multiply_result = multiply_num1 * multiply_num2
print(f'{multiply_num1} * {multiply_num2} = {multiply_result}')
print()

# 3. Create variables for division.
#    Ask the user for two numbers and divide the first by the second. 
#    Print the result in this format: "num1 / num2 = divide".
print('Division')
divide_num1 = input('Enter a number: ')
divide_num2 = input('Enter a 2nd number: ') 

division_result = divide_num1 / divide_num2
print(f'{multiply_num1} / {multiply_num2} = {multiply_result}')
print()

