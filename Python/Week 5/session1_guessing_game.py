# WEEK 5: Saturday 1HR - Guessing Game

# 1. Introduction
# In this session, we will build a guessing game where the user has to guess a secret word (our favorite color).
# The game will count the number of guesses and stop if the user exceeds the allowed number of guesses.

# 2. Setting Up Variables
# First, we need to set up the secret word and initialize our variables:
fav_colour = "blue"          # The secret word to guess
guess = ""                   # Variable to store the user's guess
guess_count = 0              # Counter for the number of guesses
guess_limit = 3              # Maximum number of guesses allowed
out_of_guesses = False       # Boolean to track if the user is out of guesses

# 3. Building the While Loop
# The while loop will run as long as the user has not guessed the favorite color 
# and is not out of guesses.
while guess != fav_colour and not out_of_guesses:
    guess = input("Guess my favorite color: ")  # Prompt user for a guess
    guess_count += 1  # Increment the guess count

    # Check if the user has reached the guess limit
    if guess_count >= guess_limit:
        out_of_guesses = True  # User is out of guesses
        break

# 4. Checking if the user won
if guess == fav_colour:
    print("You WIN!!")

# 5. Summary
# In this lesson, we built a guessing game that utilizes a while loop, if statements, and comparison operators
# to control the flow of the game based on the user's input.

# 6. Challenges
# Challenge 1: Modify the game to allow the user to choose their own favorite color at the start of the game.

# Challenge 2: Add a feature to tell the user how many guesses they have left after each guess.

# Challenge 3: Implement a way for the user to play again without restarting the program.
