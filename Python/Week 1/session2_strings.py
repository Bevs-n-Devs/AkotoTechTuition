# Strings
# TODO: https://www.giraffeacademy.com/programming-languages/python/strings/

# A string is basically plain text that we use in our code. 
# Any text you want in your program is stored as a string. 
# You can create a string by putting your text between double quotes " or single quotes '.
print('Creating a string:')

hello = 'Hello world!'
print(hello)

greeting = "Hello world!"
print(greeting)
print()

# We can create a new line in a string using \n. The backslash (\) is called an escape character. 
# It tells Python to handle the character that comes next in a special way.
print('Escape Line & Escape Characters:')

message = "Hello, \nWelcome to today's session!"
print(message)


# You can join (or concatenate) two strings together using the + operator.
print('String Concatenation')

first_name = 'Yaw'
last_name = 'Akoto'
full_name = first_name + ' ' + last_name                # if we don't add a space it will read  YawAkoto
print(full_name)
print()


# Python has many built-in functions that can help you work with strings. 
# Functions are pieces of code that perform tasks. 
# 
# Here are some useful string functions:
#       .lower() = Converts the string to lowercase.
#       .upper() = Converts the string to uppercase.
#       .isupper() = Returns True if all characters are uppercase, otherwise returns False.
#       .islower() = Returns True if all characters are lowercase, otherwise returns False.
print('String Function Methods:')

my_text = "Python Programming"
print(my_text.lower())                                  # Converts to lowercase
print(my_text.upper())                                  # Converts to uppercase
print(my_text.isupper())                                # Checks if all characters are uppercase (False)
print()


# len() = This function gives the length (number of characters) of a string.
# index() = We can find where a specific character or word is located in string (the countr starts from 0)
print('Finding the Length of a String:')

text = "hello"
print(len(text))                                        # Output: 5, as there are 5 characters in "hello"
print(text[0])                                          # Output: h (index starts at 0)
print()

my_var = "hello world"
print(my_var.index("w"))                                # Output: 6 (the 'w' starts at index 6)


# The .replace() function allows us to replace parts of a string with something else.
print('Replacing Parts of a String')

my_var = "Akoto Tech"
new_var = my_var.replace("Tech", "Tuition")
print(new_var)                                          # Output: Akoto Tuition


# String formatting is a way to construct and display strings dynamically by inserting variables 
# or values into a string template. It allows you to create strings that include dynamic content, 
# making it easier to build complex messages and outputs.
print('String Formatting')

# f-string method
name = "Yaw"
age = 37
print(f"My name is {name} and I am {age} years old.")

# .format() method
message = "Hello, {}! Welcome to today's {}."
print(message.format(name, "Python session"))
print()


# CHALLENGE
print('*'*3, 'STRING CHALLENGE', '*'*3)

# 1. Create a variable called `greeting` and store the string "Hello, world!" in it.
#    Now print out the `greeting` variable.
#    The print message should display: "Hello, world!"
#    `--` = This is where your `greeting` variable should be.

# 2. Create two variables: `first_name` and `last_name`. Store your first name in `first_name`
#    and your last name in `last_name`. Concatenate these variables with a space in between
#    to create a `full_name` variable.
#    Now print out the `full_name` variable.
#    The print message should display: "John Doe" (if your names are John and Doe)
#    `--` = This is where your `full_name` variable should be.

# 3. Create a variable called `text` and store the string "Python Programming" in it.
#    Print the length of `text` using the `len()` function.
#    Also print the character at index `0` of the `text` variable.
#    The length message should display: "17" (length of "Python Programming")
#    The character at index `0` should be: "P"
#    `--` = These are the results of using `len(text)` and `text[0]`.

# MadLibs Exercise
# 1. Create a Mad Libs story where the user inputs:
#    - a noun
#    - a verb
#    - an adjective
#    - a place
#    Use these inputs to complete the story:
#    "One day, a {adjective} {noun} decided to {verb} to {place}. It was an adventure they would never forget!"
#    Print out the completed story with the user’s inputs.
#    The print message should display something like:
#    "One day, a fluffy cat decided to run to the park. It was an adventure they would never forget!"
#    `--` = This is where the user’s inputs should be inserted into the story.
