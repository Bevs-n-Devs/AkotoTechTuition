# WEEK 7: Understanding Modules in Python

# In this session, we will look at what modules are and how we can use them.

# A module is a Python file that we can import into our current Python file.
# It allows us to access variables, functions, and other elements from that file without rewriting the code.

# Example module: hello.py
# This file contains a variable for the user's name and age, and two functions.

# hello.py content:
# user = "John"
# user_age = 75
# def hello_world():
#     return "Hello world!"
# def greet(name, age):
#     return f"Hello {name}, you are {age}"

# Now, let's create a new Python file called user.py to use the hello module.

# Step 1: Import the whole module
import hello

# Call the hello_world function from the hello module
print(hello.hello_world())

# Step 2: Import specific functions and variables
# It's a good practice to only import what you need from a module.
from hello import *  # This imports everything from hello.py

# Using the imported functions
new_user = "Sinclair"
new_age = 35
print(greet(new_user, new_age))  # Prints greeting with new variables
print(greet(user, user_age))      # Prints greeting with old variables

# Step 3: Using pip to install external modules
# Pip is a package installer for Python, allowing you to download and install external modules.

# Check if pip is installed
# You can run this command in your terminal:
# pip --version

# If pip is not installed, follow these steps to install it:
# Step 1: 
# Windows: C:> py -m ensurepip --upgrade
# MacOS: $ python -m ensurepip --upgrade
# Linux: $ python -m ensurepip --upgrade

# Step 2:
# Then, install pip using:
# Windows: C:> py get-pip.py
# MacOS: $ python get-pip.py
# Linux: $ python get-pip.py

# Step 4: Installing external modules using pip
# To install a module, use the following command in your terminal:
# pip install module_name

# Example installations:
# Install Flask: pip install -U Flask
# Install PyGame: pip install pygame

# Step 5: Explore Python modules
# For a list of built-in modules, check: https://docs.python.org/3/py-modindex.html
# For third-party modules, check: https://pypi.org/

# Challenges
# Challenge 1: Create a new module called `math_utils.py` with functions for basic arithmetic (add, subtract).
# Challenge 2: Import your `math_utils` module into a new file and use the functions you created.
# Challenge 3: Use pip to install an external module of your choice and write a simple script that utilizes it.
# Challenge 4: Research a built-in module you haven't used yet and create a small program that demonstrates its use.
