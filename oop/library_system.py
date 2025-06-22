# Objective: Deepen your understanding of inheritance and composition in Python by creating a system that models a library with different types of books.

# Task Description:
# Develop two Python scripts: library_system.py and main.py. In library_system.py, you’ll define a base class Book and two derived classes, EBook and PrintBook, showcasing inheritance. Additionally, implement a Library class demonstrating composition by managing a collection of books.

# library_system.py:
# Base Class - Book:

# Attributes: title (str) and author (str).
# Method: __init__(self, title, author) for initializing book attributes.
# Derived Classes - EBook and PrintBook:

# Both classes inherit from Book.
# EBook additional attribute: file_size (int).
# PrintBook additional attribute: page_count (int).
# Each derived class should have its own __init__ method that properly calls the base class __init__ while also initializing its unique attribute.
# Composition - Library:

# Attributes: books (a list to store instances of Book, EBook, and PrintBook).
# Methods:
# add_book(self, book): Adds a Book, EBook, or PrintBook instance to the library.
# list_books(self): Prints details of each book in the library.

class Book:
    def __init__(self, title: str, author: str) -> None:
        """Constructor to initialize the book's title and author."""
        self.title = title
        self.author = author

    # def __str__(self):
    #     """String representation of the book."""
    #     return f"{self.title} by {self.author}"

    def __repr__(self):
        """Official representation of the Book instance."""
        return f"{self.title}, {self.author}"
    
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int) -> None:
        """Constructor to initialize the EBook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size
    
    def __repr__(self):
        """Official representation of the Book instance."""
        return f"{self.title}, {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int) -> None:
        """Constructor to initialize the PrintBook with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count
    
    def __repr__(self):
        """Official representation of the Book instance."""
        return f"{self.title}, {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self) -> None:
        """Constructor to initialize the library with an empty book collection."""
        self.books = []

    def add_book(self, book: Book) -> None:
        """Adds a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self) -> None:
        """Prints details of each book in the library."""
        for book in self.books:
            book_type = type(book).__name__
            print(f"{book_type}: {book}")   

# book = EBook("1984", "George Orwell", 1.5)

# print(book)  # Expected to use __str__

# Book: Pride and Prejudice by Jane Austen
# EBook: Snow Crash by Neal Stephenson, File Size: 500KB
# PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234