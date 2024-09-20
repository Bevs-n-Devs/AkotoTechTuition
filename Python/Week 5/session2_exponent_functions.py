# WEEK 5: Sunday 1HR - Exponent Functions

# 1. Introduction
# In this session, we will create an exponent function using a for loop and the range function.
# This function will allow us to raise a number to the power of another number.

# 2. Using Python's Built-In Method
# We can easily raise a number to a power using Python's built-in operator '**'.
# Example:
base_num = 2
pow_num = 4
result = base_num ** pow_num  # This will give us 16
print(result)  # Output: 16

# 3. Creating Our Own Function
# We will now create our own function to perform exponentiation.
def raise_to_power(base_num, pow_num):
    # Step 1: Initialize the result variable
    result = 1
    
    # Step 2: Create a for loop to multiply the base number
    for index in range(pow_num):
        result *= base_num  # Multiply the result by the base number
    
    # Step 3: Return the final result
    return result

# 4. Testing the Function
# Now we can test our function with a sample input.
print(raise_to_power(2, 4))  # This should output 16
print(raise_to_power(3, 5))  # This should output 243
print(raise_to_power(10, 2))  # This should output 100

# 5. Verification with Built-In Method
# To verify our function, we can use the built-in '**' operator.
print(2 ** 4)  # Output: 16
print(3 ** 5)  # Output: 243
print(10 ** 2)  # Output: 100

# 6. Summary
# In this session, we learned how to create an exponent function using a for loop and the range function.
# We compared our custom function with Python's built-in exponentiation operator.

# 7. Challenges
# Challenge 1: Modify the function to handle negative powers (e.g., 2^-3 should return 0.125).
# Challenge 2: Create a for loop that tests your exponent function with a range of base numbers (1 to 5) and powers (1 to 3).
# Challenge 3: Write a function that calculates the square root of a number using exponentiation (e.g., num ** 0.5).
# Challenge 4: Experiment with larger numbers (e.g., 10^10) and compare the performance and output with the built-in method.
