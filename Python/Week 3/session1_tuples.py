# Welcome to the session on Python Tuples!

# 1. Introduction to Tuples
# Tuples are similar to lists, but the key difference is that tuples are immutable.
# This means once a tuple is created, its elements cannot be changed or modified.

# Let's create a tuple of numbers
numbers = (2, 589, 53, 83, 5, 39)
# Tuple indexes:   0    1    2   3   4  5

# Accessing elements in a tuple using index
print(numbers[1])  # This will print: 589

# 2. Immutable Nature of Tuples
# Trying to change an element in a tuple will result in an error because tuples are immutable.
# Uncomment the code below to see the error.

# numbers[1] = 60  # This will raise a TypeError because tuples cannot be modified

# 3. Real-World Examples of Tuples
# Tuples can be used for data that doesn't change, like traffic lights, date of birth, gender, etc.

# Example of traffic lights
traffic_lights = ("red", "yellow", "green")
print(traffic_lights)

# Example of a date of birth (day, month, year)
my_dob = (16, 10, 1986)
print(my_dob)

# Example of gender at birth
gender = ("male", "female")
print(gender)

# Example of nationality
nationality = ("British", "French", "Spanish", "Ghanaian", "German")
print(nationality)

# Example of ethnic group
race = ("Black", "White", "Asian", "Mixed")
print(race)

# 4. Combining Tuple Data
# You can create new tuples by combining data from existing tuples and variables.

# Let's create a tuple for a character named "Sinclair"
name = "Sinclair"
Sinclair = (name, nationality[0], my_dob, gender[0], race[0])
print(Sinclair)
# This will print: ('Sinclair', 'British', (16, 10, 1986), 'male', 'Black')

# 5. Accessing Tuple Data
# You can access individual items in a tuple by using their index (just like with lists).

print(Sinclair[0])  # This will print: Sinclair (name)
print(Sinclair[1])  # This will print: British (nationality)

# 6. Tuples Can Hold Different Data Types
# Just like lists, tuples can store multiple types of data (strings, numbers, other tuples, etc.)

# -----------------------------------------------------------------------------------
# Challenges:

# 1. Accessing Tuple Elements
# Create a tuple called 'colors' with the values "red", "blue", "green", "yellow".
# Print the second color in the tuple.
# Try to change the third color to "purple" and see what happens.

colors = ("red", "blue", "green", "yellow")
print(colors[1])  # This will print: blue

# Uncomment the line below to see the error
# colors[2] = "purple"  # This will raise a TypeError because tuples cannot be modified

# 2. Creating a Tuple for a Family Member
# Create a tuple for a family member (e.g., mom) using their name, nationality, date of birth, gender, and race.
# Example: Mom = (mom_name, nationality, dob, gender, race)

mom_name = "Emily"
mom_dob = (25, 12, 1975)
Mom = (mom_name, nationality[1], mom_dob, gender[1], race[1])
print(Mom)  # Example output: ('Emily', 'French', (25, 12, 1975), 'female', 'White')

# 3. Best Friend Tuple
# Using the 'nationality', 'my_dob', 'gender', and 'race' tuples, create a tuple for your best friend.
# Give them a name and fill in their personal details.

best_friend_name = "Alex"
best_friend_dob = (22, 11, 2004)
BestFriend = (best_friend_name, nationality[2], best_friend_dob, gender[0], race[2])
print(BestFriend)  # Example output: ('Alex', 'Spanish', (22, 11, 2004), 'male', 'Asian')

# 4. Create a Tuple of Favorite Things
# Create a tuple called 'favorite_things' with three of your favorite movies and three of your favorite books.
# Print the first movie and the second book.

favorite_things = ("Inception", "Interstellar", "The Matrix", "1984", "Brave New World", "Fahrenheit 451")
print(favorite_things[0])  # This will print: Inception
print(favorite_things[4])  # This will print: Brave New World

# 5. Trying to Modify a Tuple
# Try to add another movie to the 'favorite_things' tuple and observe what happens.
# Uncomment the line below to see the error

# favorite_things[6] = "Avatar"  # This will raise a TypeError because tuples are immutable

# -----------------------------------------------------------------------------------
# Summary:
# - Tuples are immutable, meaning their values cannot be changed after creation.
# - Use tuples when you have data that should not be modified, like dates of birth, names, etc.
# - You can access tuple elements using their index, similar to lists.
# - Tuples can store different data types and can be combined to create new tuples.
