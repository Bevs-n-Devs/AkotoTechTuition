# USER INPUT CHALLENGE
print('*'*3, 'USER INPUT CHALLENGE', '*'*3)

# 1. Ask the user for their name and store it in a variable called `user_name`.
#    Then print a message saying: "Hi, --! Nice to meet you."
#    `--` = This is where your `user_name` variable should be.
user_name = input('What is your name? ')
print(f'Hi {user_name}! Nicer to meet you.')
print()


# 2. Ask the user for their age and store it in a variable called `user_age`.
#    Now print a message that says: "You are -- years old."
#    `--` = This is where your `user_age` variable should be.
user_age = input('What is your age? ')
print(f'You are {user_age} years old.')
print()


# 3. Ask the user for their favorite color and favorite food.
#    Store the values in `fav_colour` and `fav_colour` variables.
#    Print a sentence that says: "Your favorite color is -- and your favorite food is --."
#    `--` = This is where your `fav_colour` and `fav_food` variables should be.
fav_colour = input('What is your favourite colour? ')
fav_food = input('What\'s your favourite food? ')

print(f'Your favorite color is {fav_colour} and your favorite food is {fav_food}.')
print()

# 4. Create a single input statement to ask for the user's first name and last name.
#    Store the inputs in a tuple called `full_name`.
#    Print a message that says: "Your full name is -- --."
#    `-- --` = This is where you should print the first and last name using tuple indexing.
full_name = input('What is your first name? '), input('What is your last name? ')
print(f'Your full name is {full_name[0]}, {full_name[1]}')


# MAD LIBS GAME
print("Welcome to the Mad Libs game! Answer the questions and see the fun story we create!")

# 1. Create an input statement to ask for the user's favorite sport.
#    Store the input in a variable called `fav_sport`.
#    The print message should say: "What's your favorite sport? 
fav_sport = input('What\s your favourite sport? ')

# 2. Create an input statement to ask for the user's favorite food.
#    Store the input in a variable called `fav_food`.
#    The print message should say: "What's your favorite food? "
fav_food = input('What\'s your favourite food? ')

# 3. Create an input statement to ask for the user's favorite celebrity.
#    Store the input in a variable called `fav_celeb`.
#    The print message should say: "Who's your favorite celebrity? "
fav_celeb = input('Who\'s your favourite celebrity? ')

# 4. Create an input statement to ask for the user's best friend's name.
#    Store the input in a variable called `best_friend`.
#    The print message should say: "What's your best friend's name? "
best_friend = input('What\'s your bet friend\'s name? ')

# 5. Create an input statement to ask for the user's dream vacation destination.
#    Store the input in a variable called `dream_vacation`.
#    The print message should say: "Where's your dream vacation destination? "
dream_vacation = input('Where\'s your dream vacation destination? ')

# Now, use the inputs stored in the variables to create a random story.

# 6. Print out the following story using the variables created above.
#    The story should say:
#    "Once upon a time, -- decided to travel to --."
#    "But on the way, -- was invited to a secret -- competition, hosted by none other than --!"
#    "It was the most thrilling game ever, but halfway through, the crowd started chanting for --!"
#    "-- couldn't resist and decided to abandon the game to hunt for the best -- in the city."
#    "In the end, -- never made it to --, but had the time of their life playing -- and enjoying -- with --."
#    Use the variables you created (fav_sport, fav_food, fav_celeb, best_friend, and dream_vacation) to fill in the blanks.

# I will use the multiple-line technique in my print message using '''
print(
    f'''
    Mad Libs story:

    Once upon a time, {best_friend} decided to travel to {dream_vacation}.
    But on the way, {best_friend} was invited to a secret {fav_sport} competition, hosted by none other than {fav_celeb}!
    It was the most thrilling game ever, but halfway through, the crowd started chanting for {fav_food}!
    {best_friend} couldn't resist and decided to abandon the game to hunt for the best {fav_food} in the city.
    In the end, {best_friend} never made it to {dream_vacation}, but had the time of their life playing {fav_sport} and enjoying {fav_food} with {fav_celeb}.
    '''
)