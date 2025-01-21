class Book:
    '''The Book class represents individual books with attributes such as title, author, and availability status.'''
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.availability_status = True

    def __str__(self):
        return f"Book Title: {self.title}; Author: {self.author}; Availability = {self.availability_status}"
        

class Member:
    '''The Member class models library members with attributes like name, member ID, and a list of borrowed books.'''
    def __init__(self, name, member_ID):
        self.name = name
        self.member_ID = member_ID
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.availability_status:
            self.borrowed_books.append(book)
            book.availability_status = False
        else:
            print(f"{book.title} is not available.")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.availability_status = True
        else:
            print(f"{book.title} is not borrowed by {self.name}.")
        
    def __str__(self):
        borrowed_book_titles = [book.title for book in self.borrowed_books]
        return f"Member Name: {self.name}; Member ID: {self.member_ID}; Books Borrowed: {borrowed_book_titles}"

class Library:
    '''The Library class manages the library's collection of books and members.'''
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)
        
    def print_books(self):
        for book in self.books:
            print(book)

    def print_members(self):
        for member in self.members:
            print(member)

# Create book instances 
book1 = Book("Behave", "Robert Sapolsky")
book2 = Book("1984", "George Orwell") 
book3 = Book("To Kill a Mockingbird", "Harper Lee")
book4 = Book("The Essential Kafka", "Franz Kafka")
book5 = Book("The Elegant Universe", "Brian Greene")

# Create member instances 
member1 = Member("Alex", 1234)
member2 = Member("Alice", 3001)

# Library instance
library = Library()

# Add books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)

# Register members
library.register_member(member1)
library.register_member(member2)

# Member one borrows a book
member1.borrow_book(book1)
# Member two tries to borrow the same book and finds it's unavailable
member2.borrow_book(book1)
member2.borrow_book(book4)
member2.borrow_book(book2)

# Print members and their borrowed books
print(member1)
print(member2)

# Member one returns the book
member1.return_book(book1)

# Print library books and members
print("\nLibrary Books:")
library.print_books()
print("\nLibrary Members:")
library.print_members()
