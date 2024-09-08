# STRING CHALLENGE
print('*'*3, 'STRING CHALLENGE', '*'*3)

# 1. Create a variable called `greeting` and store the string "Hello world!" in it.
#    Now print out the `greeting` variable.
#    The print message should display: "Hello, world!"
greeting = 'Hello wolrd!'

print(greeting)



# 2. Create two variables: `first_name` and `last_name`. Store your first name in `first_name`
#    and your last name in `last_name`. Concatenate these variables with a space in between
#    to create a `full_name` variable.
#    Now print out the `full_name` variable.
#    The print message should display: "My name is --."
#    `--` = This is where your `full_name` variable should be.
#    For this challenge you can use string concatenation (joining strings together), f-strings, or string formatting for the print message.
first_name = 'Yaw'
last_name = 'Akoto'
full_name = first_name + ' ' + last_name

# string concatenation
print('My name is ' + full_name)

# f-string
print(f'My name is {full_name}')

# string formating
message = 'My name is {}'
print(message.format(full_name))



# 3. Create a variable called `text` and store the string "Python Programming" in it.
#    Print the length of `text` using the `len()` function.
#    Also print the character at index `0` of the `text` variable.
#    The length message should display: "18" (length of "Python Programming")
#    The character at index `0` should be: "P"
#    These are the results of using `len(text)` and `text[0]`.
text = 'Python Programming'

print(len(text))
print(text[0])



# MadLibs Exercise
# 4. Create a Mad Libs story where the user inputs:
#    - a noun (people, places, or things)
#    - a verb (describe an action, state, or occurrence)
#    - an adjective (describes or defines a noun)
#    - a place
#    Use these inputs to complete the story:
#    "One day, a {adjective} {noun} decided to {verb} to {place}. It was an adventure they would never forget!"
#    Print out the completed story with the user’s inputs.
#    The print message should display something like:
#    "One day, a -- -- decided to -- to the --. It was an adventure they would never forget!"
#    `--` = This is where the user’s inputs should be inserted into the story.
#    You can use string concatenation (joining strings together), f-strings, or string formatting for the print message.
noun = 'river'
verb = 'jump'
adjective = 'mysterious'
place = 'Tokyo, Japan'

# string concatenation
print('One day, a ' + adjective + ' ' + noun + ' decided to ' + verb + ' to ' + place + '. It was an adventure they would never forget!')

# f-string
print(f'One day, a {adjective} {noun} decided to {verb} to {place}. It was an adventure they would never forget!')

# string formatting
message = 'One day, a {} {} decided to {} to {}. It was an adventure they would never forget!'
print(message.format(adjective, noun, verb, place))