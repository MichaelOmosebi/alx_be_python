# Objective: Master Python magic methods by implementing a Book class that incorporates constructors (__init__), destructors (__del__), and the representation methods (__str__ and __repr__).

# Task Description:
# Create a Python script named book_class.py. In this script, define a Book class that uses specific magic methods to enhance its functionality. This class will model a book with attributes for the title, author, and publication year.

# Requirements for Book Class in book_class.py:
# Attributes:

# title (str): The title of the book.
# author (str): The author of the book.
# year (int): The publication year of the book.
# Magic Methods:

# Constructor (__init__): Initializes a Book instance with title, author, and year.
# Destructor (__del__): Prints "Deleting (title of the book)" upon object deletion.
# String Representation (__str__): Returns a string in the format "(title) by (author), published in (year)".
# Official Representation (__repr__): Returns a string that would recreate the Book instance: f"Book('{self.title}', '{self.author}', {self.year})".

class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        """Constructor to initialize the book's title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor that prints a message when the book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """method that allows user print infirmation about the class"""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Official representation of the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
