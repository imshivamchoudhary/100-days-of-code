# Write a Library class with no_of_books and books as two instance variables.
# Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods.
# Show that your program doesnt persist the books after the program is stopped!

class Library:
    def __init__(self):
        self.noBooks=0
        self.books=[]
    def addBook(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)
    def showBooks(self):
        print(f"Total number of books in the library is {self.noBooks} the books are")
        for book in self.books:
            print(book)
e=Library()
e.addBook('Python')
e.addBook('Java')
e.addBook('C++')
e.showBooks()