# Exercise 1: Build A Simple Library System
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.book_available = True

    def is_book_available(self):
        return "is available" if self.book_available else "is not available"
    
    def __str__(self):
        return f"The book {self.title} by {self.author} {self.is_book_available()}"

class Member:
    def __init__(self, member_name, member_ID):
        self.member_name = member_name
        self.member_ID = member_ID
        self.borrowed_books = []

    def books_borrowed(self):
        [print(book) for book in self.books_borrowed]


    def __str__(self):
        return f"Member Name: {self.name}\n Member ID Number:{self.member_ID}\n Borrowed Books: {self.books_borrowed()}"

class Library:
    
    def __init__(self):
        self.new_book = []
        self.new_member = []

    def add_book(self, book):
        self.new_book.append(book)

    def register_member(self, member):
        self.new_member.append(member)

    def lend_book(self, member, book):
        if book.book_available:
            member.books_borrowed.append(book)
            book.book_available = False
            print(f"You have successfully borrowed {book}")
        else:
            print(f"{book} is unavailable")

    def return_book(self, member, book):
        member.books_borrowed.remove(book)
        return member.books_borrowed()



        

book1 = Book("Behave","Robert Sapolsky")
book2 = Book("1984", "George Orwell") 
book3 = Book("To Kill a Mockingbird", "Harper Lee")
book4 = Book("The Essential Kafka", 'Franz Kafka')
book5 = Book("The Elegant Universe", "Bian Greene")

member1 = Member('Alex', 1234)
member2 = Member("Alice", 3001)
member3 = Member('Amber', 9678)

registration = Library()
registration.register_member(member1)
am_I_a_member = Member()
am_I_a_member(member1)


