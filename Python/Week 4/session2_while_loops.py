# Sunday 2HR: While Loops

# 1. Introduction
# A while loop is a structure in Python that allows us to repeatedly execute a block of code 
# as long as a specified condition is true. The loop continues until the condition becomes false.

# 2. Basic Structure of a While Loop
# To create a while loop, we use the 'while' keyword followed by a condition:
# while condition:
#     code_block

# 3. Understanding the Condition
# The condition can be any expression that evaluates to True or False. 
# The loop will keep running as long as the condition is true.

# 4. Example of a While Loop
num = 1
while num < 10:  # This condition checks if num is less than 10
    print(num)
    num += 1  # Increment num by 1

# 5. Infinite Loops
# If the condition is never false, the while loop will run indefinitely.
# For example:
# num = 1
# while num:
#     num += 1
#     print(num)  # This will run forever because num is always true.

# 6. Avoiding Infinite Loops
# To prevent an infinite loop, use a proper condition. For example:
num = 1
while num < 10:  # The loop will stop when num reaches 10
    print(num)
    num += 1

# 7. Using Break
# Another way to exit a loop is to use the 'break' keyword. This immediately exits the loop.
num = 1
while num < 10:
    print(num)
    num += 1
    if num == 5:  # When num equals 5, the loop will break
        break

# 8. Summary
# In this lesson, we learned how to create and control while loops, 
# including how to prevent infinite loops and use the break statement.

# 9. Challenges
# Challenge 1: Create a while loop that counts from 1 to 20 and prints each number. 
# Stop the loop when you reach 15.

# Challenge 2: Modify the loop from Challenge 1 to only print even numbers.

# Challenge 3: Write a while loop that asks the user to input a number until they enter a number greater than 100.
# Print out all the numbers they entered.
