# WEEK 5: Sunday 2HR - 2D Arrays & Nested Loops

# 1. Introduction
# Nested loops are loops within a loop. They can be either for loops or while loops, 
# and are used to handle data structures that contain other data structures.

# 2. Understanding Nested Lists (2D Arrays)
# A nested list is also known as a 2D list. Here’s how a 2D list (or grid) looks:
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# This creates a grid-like structure with rows and columns.

# 3. Accessing Data in Nested Lists
# To access individual elements, we use two sets of square brackets.
print(number_grid[0][1])  # Output: 2 (first row, second column)
print(number_grid[2][0])  # Output: 7 (third row, first column)
print(number_grid[1][2])  # Output: 6 (second row, third column)

# Example: Accessing other elements
print(number_grid[0][0])  # Output: 1 (first row, first column)
print(number_grid[3][0])  # Output: 0 (fourth row, first column)

# 4. Looping Through Nested Lists
# We can use nested for loops to iterate through each element in a 2D list.
for rows in number_grid:          # Loop through each row
    for cols in rows:            # Loop through each column in the current row
        print(cols)              # This will print all values in each list on a separate line

# 5. Summary
# In this session, we learned about nested loops and how to access and manipulate 
# data in 2D arrays (nested lists). This allows us to handle complex data structures.

# 6. Challenges
# Challenge 1: Modify the code to calculate and print the sum of all numbers in the number_grid.
# Challenge 2: Create a 2D list of your favorite movies categorized by genre (e.g., action, comedy).
# Challenge 3: Write a function that takes a 2D list as input and returns the total number of elements in it.
# Challenge 4: Create a pattern using nested loops (e.g., a multiplication table or a triangle of asterisks).
