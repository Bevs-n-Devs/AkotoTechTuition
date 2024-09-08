# Variables
# TODO: https://www.giraffeacademy.com/programming-languages/python/variables/


# A variable is like a container where we can save information to use later in our code. 
# This makes it easier to change or update information in one place, instead of finding it everywhere in your program.
print('Creating a variable:')
name = 'Yaw'
print(name)

print('Hello world, hello',name)
print()


# Instead of manually changing a value everywhere in your program, you can just update the variable. 
# This is what makes variables useful in coding!
print('Updating a variable:')
age = '20'
print("Original age:", age)

# now we update the age
age = 37
print("updated age:", age)
print()


# Variables can store different types of data. Let’s see a few examples.
print('Different Types of variables:')

greeting = 'Hello world!'       # string (text)
age = 37                        # integer (whole number)
height = 5.11                   # float (decimal number)
is_student = True               # boolean (True/False)

print(greeting)
print(age)
print(height)
print(is_student)
print()

# We can even use variables in caluclations - more will be donne in a later session
print('Variables in calculations:')

num1 = 10
num2 = 5

total = num1 + num2

print('The total is:', total)
print()


# VARIABLE CHALLENGE
print('*'*3, 'VARIABLE CHALLENGE', '*'*3)

# 1. Create a variable called `my_name` and store your name in it, then print out the message.
#    The print message should say: "Hello, my name is --"
#    `--` = This is where your `my_name` variable should be.

# 2. Calculate your age by creating a variable called `current_year` and save the current 
#    year in it. Now create another variable called `birth_year` and save the year that you were born in.
#    Create a variable called `age` to do the calculation by subtracting `birth_year` 
#    from `current_year` like this: current_year - birth_year.
#    Now print out your age. The print message should say: "I am -- years old." 
#    `--` = This is where your `age` variable should be. 
#    CLUE: Look at how I have used print statements in previous examples for guidance.

# 3. Create a variable called `fav_number`, store your favourite number in it, and then create 
#    another variable called `result` where we multiply your favourite number by 2. (Remember, * is used for multiplication).
#    Now print out the result. The print message should say: "My favourite number doubled is --"
#    `--` = This is where your `result` variable should be.
