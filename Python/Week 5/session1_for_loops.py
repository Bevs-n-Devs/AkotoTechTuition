# WEEK 5: Saturday 2HR - For Loops

# 1. Introduction
# For loops allow us to iterate over various collections of items in Python.
# They are commonly used to loop through sequences like strings, lists, tuples, and dictionaries.

# 2. Basic Structure of a For Loop
# The basic syntax of a for loop is:
# for item in sequence:
#     # code block
# Here, 'item' is a variable that takes on the value of each element in the sequence.

# 3. Examples of For Loops

# * For Loop on Strings *
sequence = "Sinclair"
for data in sequence:
    print(data)  # This prints each letter of the string on a new line.

# * For Loop with Numbers *
sequence = 10
for data in range(0, sequence):
    print(data)  # This prints numbers from 0 to 9 (stops before 10).

# * For Loops with Lists *
sequence = ["Sinclair", 10, 18, "October", True, "London"]
for data in sequence:
    print(data)  # This prints each item in the list on a new line.

# * For Loops with Dictionaries *
sequence = {"name": "Sinclair", "age": 35, "occupation": "developer", "city": "London"}
# Print key-value pairs
for data in sequence.items():
    print(data)  # Prints each key-value pair as a tuple.

# Print just the keys
for key in sequence.keys():
    print(key)  # Prints only the keys.

# Print just the values
for value in sequence.values():
    print(value)  # Prints only the values.

# 4. Summary
# In this lesson, we covered how to use for loops to iterate over different data types including strings, numbers, lists, and dictionaries.
# We learned how to access each element and perform operations on them.

# 5. Challenges
# Challenge 1: Create a for loop that prints the squares of numbers from 1 to 10.

# Challenge 2: Given a list of names, write a for loop that prints a greeting for each name.

# Challenge 3: Create a dictionary of favorite foods with people’s names as keys and their favorite foods as values.
# Write a for loop that prints a statement like "Alice's favorite food is Pizza."

# Challenge 4: Modify the loop that prints key-value pairs in the dictionary to format the output nicely, e.g., "Name: Sinclair, Age: 35".
