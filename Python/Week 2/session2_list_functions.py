# TODO: https://www.giraffeacademy.com/programming-languages/python/list-functions/
#       https://www.programiz.com/python-programming/online-compiler/

print('Welcome to the session on Python List Functions!')

# 1. Extend Function
#    The extend() function is used to add all the elements of one list (or an iterable) to the end of another list.

list1 = ["apple", "banana", "cherry"]
list2 = ["orange", "grape"]

#    Let's extend list1 by adding all the elements of list2 to it.
list1.extend(list2)
print(list1)  # This will print: ['apple', 'banana', 'cherry', 'orange', 'grape']

#    You can also extend a list by adding new data inside square brackets.
list1.extend([True, 42])
print(list1)  # This will print: ['apple', 'banana', 'cherry', 'orange', 'grape', True, 42]

#    Without square brackets, this would throw an error for non-iterable types.

# 2. Append Function
#    The append() function adds a single item to the end of a list.

fruits = ["apple", "banana", "cherry"]

#    Let's append a new fruit to the list.
fruits.append("orange")
print(fruits)  # This will print: ['apple', 'banana', 'cherry', 'orange']

#    We can also append a list to the end of an existing list.
fruits.append([True, 42])
print(fruits)  # This will print: ['apple', 'banana', 'cherry', 'orange', [True, 42]]

#    Notice that append adds the entire list as a single item at the end.

# 3. Insert Function
#    The insert() function allows us to insert a new item at a specific index in the list.

veggies = ["carrot", "broccoli", "spinach"]

#    Let's insert a new vegetable at index 1 (between 'carrot' and 'broccoli').
veggies.insert(1, "tomato")
print(veggies)  # This will print: ['carrot', 'tomato', 'broccoli', 'spinach']

#    We can also insert a list at a specific index.
veggies.insert(2, ["potato", "onion"])
print(veggies)  # This will print: ['carrot', 'tomato', ['potato', 'onion'], 'broccoli', 'spinach']

# 4. Remove Function
#    The remove() function removes the first occurrence of a specified item from the list.

animals = ["cat", "dog", "rabbit", "dog"]

#    Let's remove "dog" from the list (only the first occurrence).
animals.remove("dog")
print(animals)  # This will print: ['cat', 'rabbit', 'dog']

# 5. Clear Function
#    The clear() function removes all elements from a list, making it an empty list.

numbers = [1, 2, 3, 4, 5]

#    Let's clear the list.
numbers.clear()
print(numbers)  # This will print: []

# 6. Pop Function
#    The pop() function removes and returns the last item in the list by default, or the item at the specified index.

letters = ["a", "b", "c", "d"]

#    Let's pop the last item.
letters.pop()
print(letters)  # This will print: ['a', 'b', 'c']

#    Now, let's pop the item at index 1.
letters.pop(1)
print(letters)  # This will print: ['a', 'c']

# 7. Index Function
#    The index() function returns the index of the first occurrence of the specified value.

colors = ["red", "blue", "green", "blue"]

#    Let's find the index of "blue".
blue_index = colors.index("blue")
print(blue_index)  # This will print: 1 (since the first "blue" is at index 1)

# 8. Count Function
#    The count() function returns the number of times a specified value appears in the list.

numbers = [1, 2, 3, 4, 1, 1, 2]

#    Let's count how many times the number 1 appears.
count_of_ones = numbers.count(1)
print(count_of_ones)  # This will print: 3

# 9. Sort Function
#    The sort() function sorts the list in ascending order (either alphabetically for strings or numerically for numbers).

letters = ["d", "b", "a", "c"]

#    Let's sort the letters in alphabetical order.
letters.sort()
print(letters)  # This will print: ['a', 'b', 'c', 'd']

numbers = [5, 2, 9, 1]

#    Let's sort the numbers in ascending order.
numbers.sort()
print(numbers)  # This will print: [1, 2, 5, 9]

# 10. Reverse Function
#     The reverse() function reverses the current order of the list.

letters.reverse()
print(letters)  # This will print: ['d', 'c', 'b', 'a']

# 11. Copy Function
#     The copy() function creates a copy of the current list.

original_list = ["apple", "banana", "cherry"]
copied_list = original_list.copy()

print(copied_list)  # This will print: ['apple', 'banana', 'cherry']

#     The copied_list is a new list and not linked to the original_list.


# LIST FUNCTIONS CHALLENGE
print('*'*3, 'LIST FUNCTIONS CHALLENGE', '*'*3)
# 1. Create a list of your favorite movies and extend it with a list of your favorite books.
# Challenge: Extend the favorite_books list and print the result

# 2. Append a new movie to the favorite_movies list and then print it.

# 3. Insert a new book at the second position in the list.
# Challenge: Insert a new book at index 1

# 4. Remove a movie from the list and print the updated list.
# Challenge: Remove a movie

# 5. Clear the list of movies and books.
# Challenge: Clear the list

# 6. Create a list of numbers and pop the last item. Then, pop the first item.


# 7. Find the index of a specific item in a list and print it.
colors = ["red", "blue", "green", "yellow"]
# Challenge: Find index of "green" CLUE: use the index() function

# 8. Count how many times a specific number appears in a list.
numbers = [1, 3, 3, 7, 3, 2]
# Challenge: Count how many times the number 3 appears

# 9. Create a list of unsorted numbers, sort it, then reverse the sorted list.
unsorted_numbers = [50, 10, 30, 20, 40]
# Print the sorted the list
# Print the sorted list in reverse

# 10. Copy a list of fruits and print both the original and copied lists.
fruits = ["apple", "banana", "cherry"]
# Challenge: Copy a list
