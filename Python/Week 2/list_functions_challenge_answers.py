# LIST FUNCTIONS CHALLENGE
print('*'*3, 'LIST FUNCTIONS CHALLENGE', '*'*3)
# 1. Create a list of your favorite movies and extend it with a list of your favorite books.
# Challenge: Extend the favorite_books list and print the result 
favorite_movies = ["Inception", "X-Men", "The Matrix"]
favorite_books = ["Clean Code", "Python Cookbook", "Effective Python"]
favorite_movies.extend(favorite_books)
print(favorite_movies)  # Challenge: Extend the list and print the result

# 2. Append a new movie to the favorite_movies list and then print it.
favorite_movies.append("Avatar")
print(favorite_movies)  # Challenge: Append a new movie

# 3. Insert a new book at the second position in the list.
favorite_movies.insert(1, "The Catcher in the Rye")
print(favorite_movies)  # Challenge: Insert a new book at index 1

# 4. Remove a movie from the list and print the updated list.
favorite_movies.remove("Inception")
print(favorite_movies)  # Challenge: Remove a movie

# 5. Clear the list of movies and books.
favorite_movies.clear()
print(favorite_movies)  # Challenge: Clear the list

# 6. Create a list of numbers and pop the last item. Then, pop the first item.
numbers_list = [10, 20, 30, 40]
numbers_list.pop()  # Pop the last item
numbers_list.pop(0)  # Pop the first item
print(numbers_list)  # Challenge: Pop items

# 7. Find the index of a specific item in a list and print it.
colors = ["red", "blue", "green", "yellow"]
print(colors.index("green"))  # Challenge: Find index of "green"

# 8. Count how many times a specific number appears in a list.
numbers = [1, 3, 3, 7, 3, 2]
print(numbers.count(3))  # Challenge: Count how many times the number 3 appears

# 9. Create a list of unsorted numbers, sort it, then reverse the sorted list.
unsorted_numbers = [50, 10, 30, 20, 40]
unsorted_numbers.sort()  # Sort the list
unsorted_numbers.reverse()  # Reverse the sorted list
print(unsorted_numbers)  # Challenge: Sort and reverse

# 10. Copy a list of fruits and print both the original and copied lists.
fruits = ["apple", "banana", "cherry"]
copied_fruits = fruits.copy()
print(f"Original: {fruits}, Copied: {copied_fruits}")  # Challenge: Copy a list
