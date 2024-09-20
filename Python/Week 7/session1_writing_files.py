# WEEK 7: Writing and Appending Files

# In this session, we will learn how to write to and append data to files in Python.

# Step 1: Appending Data to an Existing File
# We will append a new employee to 'employees.txt'.

# Open the existing file in append mode ('a').
employee_file = open("employees.txt", "a")

# Write a new employee entry. Using '\n' ensures the entry starts on a new line.
employee_file.write("\nJohn - Customer Service")

# Close the file after writing.
employee_file.close()

# Step 2: Writing Data to a New File
# Now we will create a new file and write data to it.

# Open a new file in write mode ('w'). This will create a new file if it doesn't exist.
new_file = open("my_info.txt", "w")

# Write personal information to the file.
new_file.write("Name: Jane Doe\n")
new_file.write("Age: 30\n")
new_file.write("City: New York\n")

# Close the new file.
new_file.close()

# Step 3: Appending Additional Data to the New File
# Let's append some additional data to 'my_info.txt'.

# Open the file again in append mode ('a').
new_file = open("my_info.txt", "a")

# Add favorite color and sport.
new_file.write("Favorite Color: Blue\n")
new_file.write("Favorite Sport: Basketball\n")

# Close the file after appending.
new_file.close()

# Step 4: Reading the New File to Verify
# Open 'my_info.txt' in read mode ('r') to check the contents.
new_file = open("my_info.txt", "r")

# Print the contents of the file.
for line in new_file.readlines():
    print(line.strip())  # Use strip() to remove any extra newline characters

# Close the file after reading.
new_file.close()

# Challenges
# Challenge 1: Modify the script to append another employee to 'employees.txt'.
# Challenge 2: Create a new file called 'hobbies.txt' and write down at least three hobbies.
# Challenge 3: After writing to 'hobbies.txt', read it back and print each hobby on a separate line.
# Challenge 4: Implement error handling using try-except to manage cases where the file might not be accessible or writable.
