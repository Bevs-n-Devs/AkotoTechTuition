# Getting User Input
# TODO: https://www.giraffeacademy.com/programming-languages/python/getting-user-input/


# User input allows developers to collect data from people using their programs. 
# By using input(), you can ask the user for information, which gets stored in a variable.
print('What is a User Input?')

name = input("What is your name? ")  # The prompt will ask the user for their name
print(f'Hello {name}!')  # This will print whatever the user enters
print()


# You can store the user’s input into a variable. 
# The data stored in the variable can be used later in the program.
print('Storing User Input in a Variable:')

age = input("What is your age? ")
print(f"You are {age} years old!")  # This will print the user's age
print()


# You can ask for multiple pieces of information using separate input() statements, each storing the data in its own variable.
print('Multiple Input:')

city = input("Where are you from? ")
hobby = input("What is your favourite hobby? ")
# you can have multiple lines in your print message by using triple qoutation marks -> ''' or """"
print(f'''Hello {name}! You are {age} years old.
You are from {city}, and your favourite hobby is {hobby}.''')
print()


# You can also create multiple input statements within a single line of code. 
# The inputs will be stored in a tuple, and you can access each value using indexing.
print('Input with a Tuple (Advanced):')

prompt = input("Where do you study? "), input("What is your favourite subject? ")
print(f'You study at {prompt[0]}, and your favourite subject is {prompt[1]}')
print()



# USER INPUT CHALLENGE
print('*'*3, 'USER INPUT CHALLENGE', '*'*3)

# 1. Ask the user for their name and store it in a variable called `user_name`.
#    Then print a message saying: "Hi, --! Nice to meet you."
#    `--` = This is where your `user_name` variable should be.

# 2. Ask the user for their age and store it in a variable called `user_age`.
#    Now print a message that says: "You are -- years old."
#    `--` = This is where your `user_age` variable should be.

# 3. Ask the user for their favorite color and favorite food.
#    Store the values in `fav_color` and `fav_food` variables.
#    Print a sentence that says: "Your favorite color is -- and your favorite food is --."
#    `--` = This is where your `fav_color` and `fav_food` variables should be.

# 4. Create a single input statement to ask for the user's first name and last name.
#    Store the inputs in a tuple called `full_name`.
#    Print a message that says: "Your full name is -- --."
#    `-- --` = This is where you should print the first and last name using tuple indexing.


# MAD LIBS GAME
print("Welcome to the Mad Libs game! Answer the questions and see the fun story we create!")

# 1. Create an input statement to ask for the user's favorite sport.
#    Store the input in a variable called `fav_sport`.
#    The print message should say: "What's your favorite sport? "

# 2. Create an input statement to ask for the user's favorite food.
#    Store the input in a variable called `fav_food`.
#    The print message should say: "What's your favorite food? "

# 3. Create an input statement to ask for the user's favorite celebrity.
#    Store the input in a variable called `fav_celeb`.
#    The print message should say: "Who's your favorite celebrity? "

# 4. Create an input statement to ask for the user's best friend's name.
#    Store the input in a variable called `best_friend`.
#    The print message should say: "What's your best friend's name? "

# 5. Create an input statement to ask for the user's dream vacation destination.
#    Store the input in a variable called `dream_vacation`.
#    The print message should say: "Where's your dream vacation destination? "

# Now, use the inputs stored in the variables to create a random story.

# 6. Print out the following story using the variables created above.
#    The story should say:
#    "Once upon a time, -- decided to travel to --."
#    "But on the way, -- was invited to a secret -- competition, hosted by none other than --!"
#    "It was the most thrilling game ever, but halfway through, the crowd started chanting for --!"
#    "-- couldn't resist and decided to abandon the game to hunt for the best -- in the city."
#    "In the end, -- never made it to --, but had the time of their life playing -- and enjoying -- with --."
#    Use the variables you created (fav_sport, fav_food, fav_celeb, best_friend, and dream_vacation) to fill in the blanks.
