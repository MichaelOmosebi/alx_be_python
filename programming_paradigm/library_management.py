# Implement a Book class with public attributes title and author, and a private attribute _is_checked_out to track its availability.
# Implement a Library class with a private list _books to store instances of Book. Include methods to add_book, check_out_book(title), return_book(title), and list_available_books.

# Your Book class should provide methods to check a book out and return it, affecting its availability.
# Your Library class needs to manage a collection of books, including adding new books to the collection, checking a book out (which marks it as unavailable), returning it (making it available again), and listing all available books.
# Implementing these functionalities requires careful thought about how objects interact with each other in terms of state and behavior.
# Use the provided main.py for testing your implementation. The expected outputs give you a clear indication of how your program should behave if implemented correctly.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        #print(f"Added book: {book.title} by {book.author}")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                #print(f"Checked out book: {book.title}")
                return True
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                #print(f"Returned book: {book.title}")
                return True
        return False

    def list_available_books(self):
        available_books = [book.title for book in self._books if book.is_available()]
        #print("Available books:")
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
        return available_books