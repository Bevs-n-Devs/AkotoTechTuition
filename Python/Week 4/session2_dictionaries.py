# Sunday 1HR: Dictionaries

# 1. Introduction
# A dictionary is a special structure that allows you to store data in key-value pairs.
# What are key-value pairs? Essentially, a key is a unique identifier for a value,
# similar to a word and its definition in a dictionary.

# 2. Dictionary Structure
# Example of key-value pairs:
# "word": definition
# "key": value

# 3. Rules for Creating a Dictionary
# - Curly brackets {} are required.
# - Keys must be in quotation marks; values need quotes only if they are strings.
# - Keys must be unique; no duplicate keys allowed.
# - Values can be of any data type, including another dictionary.
# - Separate multiple key-value pairs with commas.
# - As of Python 3.7, dictionaries maintain order; earlier versions do not.
# - Access values through their keys, not by index.

# 4. Creating a Dictionary
# Let's create a dictionary that converts a number to a calendar month:
months = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

# 5. Accessing Dictionary Values
print(months)  # Print the entire dictionary
print(months["1"])  # Accessing a value using a key (prints 'January')

# Another way to access values is by using the .get() method:
print(months.get("1"))  # This also prints 'January'

# 6. Using Default Values with .get()
# You can set a default value for .get(), useful if the key doesn't exist:
print(months.get("13", "Enter a valid month"))  # Will print 'Enter a valid month'

# 7. Storing Current Month and Birthday Month
# Get the current month and the month of your birthday:
my_birthday = months["10"]  # Example: October
this_month = months.get("5")  # Example: May

# Print the months:
print(f"My birthday month: {my_birthday}")
print(f"This month: {this_month}")

# 8. Summary
# In this lesson, we learned how to create and access values in a dictionary,
# as well as how to handle cases where a key may not exist.

# 9. Challenges
# Challenge 1: Create a dictionary that converts numbers 1-5 to their English words (e.g., "1": "One").
# Print the word for the number 3 using both the key access and the .get() method.

# Challenge 2: Add a new entry to your months dictionary for "0" as "Invalid month".
# Test it by printing months.get("0").

# Challenge 3: Write a function that takes a month number as input and returns the month name.
# If the month number is not valid, return a default message "Invalid month number".
