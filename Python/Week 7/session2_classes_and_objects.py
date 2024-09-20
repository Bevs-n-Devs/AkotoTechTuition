# WEEK 7: Classes and Objects in Python

# In this session, we will learn about classes and objects in Python.
# Classes help organize and structure your code, especially in Object-Oriented Programming (OOP).

# What is a class?
# A class is a blueprint for creating objects (instances). It allows you to define your own data types.

# Example: Creating a Book class
class Book:
    # Constructor to initialize class attributes
    def __init__(self, title, author, pages, year):
        self.title = title    # Title of the book
        self.author = author  # Author of the book
        self.pages = pages    # Number of pages in the book
        self.year = year      # Year of publication

# Creating instances (objects) of the Book class
book1 = Book("The Fellowship of the Ring", "J R R Tolkien", 423, 1954)
book2 = Book("The Hobbit", "J R R Tolkien", 310, 1937)
book3 = Book("Python Cookbook 3rd Edition", "Mark Lutz", 706, 2013)

# Accessing attributes of the book instances
print(f"Title: {book1.title}, Author: {book1.author}, Pages: {book1.pages}, Year: {book1.year}")
print(f"Title: {book2.title}, Author: {book2.author}, Pages: {book2.pages}, Year: {book2.year}")
print(f"Title: {book3.title}, Author: {book3.author}, Pages: {book3.pages}, Year: {book3.year}")

# Creating a book object with attributes in a different order using keyword arguments
book4 = Book(year=2022, pages=1000, author="Sinclair Akoto", title="My Python Course")

# Accessing attributes of the new instance
print(f"Title: {book4.title}, Author: {book4.author}, Pages: {book4.pages}, Year: {book4.year}")

# Important Notes:
# - 'self' is a reference to the current instance of the class and is used to access class attributes.
# - You can create multiple instances of the same class with different data.

# Challenges
# Challenge 1: Extend the Book class to include a method that returns a summary of the book.
# Challenge 2: Create another class called 'Library' that holds a list of books and methods to add or remove books.
# Challenge 3: Implement a method in the Library class that prints all book titles in the library.
# Challenge 4: Create instances of the Library class and test the methods you implemented.

