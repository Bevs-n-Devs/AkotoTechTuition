# WEEK 6: Saturday 1HR - Building A Translator

# 1. Introduction
# In this session, we will build a translator app that converts a word or phrase into a coded message 
# by changing some letters around. This can help us create our own coded language!

# 2. Creating the Function
# Let's start by defining a function called 'coded_message' that takes one parameter (the text to convert).
def coded_message(text):
    translation = ""  # Step 1: Create an empty string for the translated message
    
    # Step 2: Loop through each letter in the text
    for letter in text:
        # Step 3: Check if the letter is a vowel
        if letter in "AEIOUaeiou":
            translation += "s"  # Change vowel to 's'
        else:
            translation += letter  # Keep the letter as is
            
    return translation  # Step 4: Return the translated text

# 3. Testing the Function
# Create a variable with the message we want to encode
message = "Hello World"
print(coded_message(message))  # Output: Hslls Wsrld

# 4. Additional Challenge
# Now, let's modify the function to change every "c", "t", and "d" to "meow".
def coded_message_extended(text):
    translation = ""
    for letter in text:
        if letter in "AEIOUaeiou":
            translation += "s"  # Change vowels to 's'
        elif letter in "ctdCTD":
            translation += "meow"  # Change 'c', 't', 'd' to 'meow'
        else:
            translation += letter  # Keep other letters as is
            
    return translation

# Test the extended function
extended_message = "The cat climbed up the tree but couldn't get back down."
print(coded_message_extended(extended_message))

# 5. Summary
# In this session, we learned how to build a simple translator function that encodes messages 
# by replacing certain letters. This can be useful for creating coded messages!

# 6. Challenges
# Challenge 1: Modify the original function to replace every consonant with the letter 'x'.
# Challenge 2: Create your own coded message function that changes specific letters into symbols (e.g., "a" to "@", "s" to "$").
# Challenge 3: Write a function that takes a sentence and encodes it using two different sets of rules, returning both encoded messages.
# Challenge 4: Create a program that allows a user to input a message and choose which letters to replace, and with what.
