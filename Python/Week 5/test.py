
guess = ""  # Initialize guess
guess_count = 0  # Track the number of guesses
guess_limit = 3  # Set the limit of guesses
out_of_guesses = False  # Control the loop
fav_colour = "blue"  # Replace with your favorite color

# While loop to check for guesses and whether the user has guesses left
while guess != fav_colour and not out_of_guesses:
    guess = input("Guess my favorite color: ")  # Prompt user for a guess
    guess_count += 1  # Increment the guess count
    remaining_guesses = guess_limit - guess_count
    print(f'You have {remaining_guesses} guesses left')

    # Check if the user has reached the guess limit
    if guess_count >= guess_limit:
        out_of_guesses = True  # User is out of guesses
    
    # Check if the user guessed correctly
    if guess == fav_colour:
        print("You WIN!!")
    elif out_of_guesses:
        print("Out of guesses, YOU LOSE!")