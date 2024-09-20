# WEEK 7: Saturday 1HR - Reading Files

# In this session, we will learn how to read from an external file in Python.
# This skill is essential for creating programs and working in a professional environment.

# Step 1: Opening a File
# We will use the 'open()' function to open a file. 
# The path can be absolute, relative, or just the file name if it's in the same directory.

# Example of opening a file in the same directory:
employee_file = open("employees.txt", "r")  # 'r' means read mode

# Step 2: Reading the File
# To read all lines at once, we can use the 'readlines()' method.
print(employee_file.readlines())  # This prints all data in a list format

# If we want to access a specific line:
print(employee_file.readlines()[1])  # This prints the second line from the file

# If we want to read one line at a time, we can use 'readline()':
print(employee_file.readline())  # This prints the first line
print(employee_file.readline())  # This prints the second line

# To print all lines without storing them in a list, we can use a for loop:
employee_file = open("employees.txt", "r")  # Reopen the file
for employee in employee_file.readlines():
    print(employee)

# Step 3: Closing the File
# It's essential to close the file after we are done to free up system resources.
employee_file.close()

# Challenges
# Challenge 1: Create a text file named "test.txt" with your own content.
# Challenge 2: Modify the script to open "test.txt" and print its contents line by line.
# Challenge 3: Implement error handling using try-except to manage cases where the file might not exist.
# Challenge 4: Add a feature to count and print the total number of lines in "test.txt".
