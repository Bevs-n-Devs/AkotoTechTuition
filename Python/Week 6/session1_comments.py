# WEEK 6: Saturday 2HR - Comments

# 1. Introduction
# In this session, we will explore the importance of comments in our code.
# Comments help us write notes that explain what our code does, making it easier to understand.

# 2. Using Comments
# You may have noticed the '#' symbol used in the code. This is used to create comments.
# Comments are ignored by Python and are only meant for developers reading the code.
print("Hello world")  # This prints 'Hello world'

# 3. Multi-line Comments
# For longer comments, we can use triple quotes (either single or double).
"""
This is a longer comment.
It can span multiple lines,
which is useful for detailed explanations.
"""
'''
This is another way to write a long comment.
You can use either triple single or triple double quotes.
'''

# 4. Best Practices for Comments
# - Use '#' for inline comments next to your code.
# - Use triple quotes for documentation, especially when writing functions or classes.
# This helps explain what the code is doing for future reference.

# Example of a function with a docstring:
def greeting(name):
    """Says hello to a name given by the user."""
    return f"Hello {name}"

# 5. Testing the Function
print(greeting("Sinclair"))  # Output: Hello Sinclair

# 6. Summary
# In this session, we learned how to use comments effectively in our code.
# Comments improve code readability and help us (and others) understand our work later.

# 7. Challenges
# Challenge 1: Write a function to calculate the area of a rectangle and include comments to explain each step.
# Challenge 2: Create a script that converts Celsius to Fahrenheit, using comments to clarify the conversion formula.
# Challenge 3: Write a multi-line comment describing your favorite programming language and why you like it.
# Challenge 4: Modify the greeting function to accept two names and return a greeting for both, ensuring you document the changes.
