# TODO: https://www.giraffeacademy.com/programming-languages/python/lists/
#       https://www.programiz.com/python-programming/online-compiler/

# Welcome message
print("Welcome to the lesson on Python Lists!")

# 1. Lists are like containers that can hold multiple items of any data type, such as strings, integers, floats, etc.
#    To create a list, we use square brackets [] and place our data inside, separated by commas.
#    Each item in the list has an index number, starting from 0. 

# Let's create a list of favorite foods.
fav_food = ["pizza", "pasta", "burgers"]

# 2. Now, let's explore how to access items in the list using their index number.
#    For example, to get the first item (pizza), we use index 0.
print(fav_food[0])  # This will print "pizza"

#    To get the second item (pasta), we use index 1.
print(fav_food[1])  # This will print "pasta"

#    To get the third item (burgers), we use index 2.
print(fav_food[2])  # This will print "burgers"

# 3. Let's practice with another list! This time, we'll create a list of countries.
countries = ["Ghana", "England", "France", "Spain"]

#    What if we want to get "Spain"? Use index 3.
print(countries[3])  # This will print "Spain"

#    What if we want to get "Ghana"? Use index 0.
print(countries[0])  # This will print "Ghana"

# 4. A list can hold different data types, even other lists! Let's see how we can have a list with various types.
mixed_list = ["Ghana", 10, True, 8.6, fav_food]

#    The list contains strings, integers, booleans, floats, and another list.
#    We can still access the data using index numbers.

#    To get the boolean True, we use index 2.
print(mixed_list[2])  # This will print "True"

#    To access the `fav_food` list, we use index 4.
print(mixed_list[4])  # This will print the entire fav_food list: ['pizza', 'pasta', 'burgers']

#    What if we want to access the pizza from the `fav_food` list inside the `mixed_list`?
#    We would need to chain the indexes: mixed_list[4][0]
print(mixed_list[4][0])  # This will print "pizza"

# 5. Python allows us to have lists within lists, also known as multi-dimensional or nested lists.
#    Let's create a 2D list (list of lists).
nested_list = [[1, 16, 86], ["John", "Jane", "Julie"], [True, "England", 10]]

#    To access an entire list within the `nested_list`, just use its index.
print(nested_list[0])  # This will print [1, 16, 86]

#    What if we want the number 16 from the first list?
#    We need to use two indexes: first to select the list, then to select the item.
print(nested_list[0][1])  # This will print 16

#    What if we want to get "Julie" from the second list?
print(nested_list[1][2])  # This will print "Julie"

#    What if we want to get the boolean True from the third list?
print(nested_list[2][0])  # This will print "True"

#    Now, let's practice more:
#    What if we want to get "England"?
print(nested_list[2][1])  # This will print "England"

#    What if we want to get "John"?
print(nested_list[1][0])  # This will print "John"

#    What if we want to get the number 86?
print(nested_list[0][2])  # This will print 86


# LISTS CHALLENGE
print('*'*3, 'LISTS CHALLENGE', '*'*3)
# 1. Let's practice swapping data in a list.
#    Change the first three items in `nested_list` to new strings: "Yaw", "Akoto", and "Tech".
#    Print out the new list to see the changes.  This will print ['Yaw', 'Akoto', 'Tech']


# 2. Try adding a new item to the list by accessing an index that doesn't exist yet, e.g., nested_list[3].
#    This will result in an error, as you cannot add an item this way. You can only replace existing items.
#    Adding new items to a list requires special methods, which we will cover later.
