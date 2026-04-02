class Book:
    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.avbl = is_available
    
    def borrow(self):
        if self.avbl:
            self.avbl = False
            print(f"Borrowed: {self.title}")
        else:
            print("Already Borrowed!")

    def return_book(self):
        self.avbl = True
        print(f"Returned: {self.title}")


class Library:
    def __init__(self, name):
        self.name =name
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def available_books(self):
        print("\nAvailable Books:")
        for b in self.books:
            if b.avbl:
                print(b.title)
    
    def search(self, title):
        for b in self.books:
            if title.lower() == b.title.lower():
                print(f"Found: {b.title} by {b.author}")
                return 
        print("Book not Found")

# Expected interaction:
b1 = Book('Python Basics', 'John', True)
b2 = Book('Data Science', 'Sara', True)
b3 = Book('Web Dev',      'Mike', True)

lib = Library('City Library')
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

b1.borrow()               # Borrowed: Python Basics
b1.borrow()               # Already borrowed!
lib.available_books()     # Data Science, Web Dev
b1.return_book()          # Returned: Python Basics
lib.available_books()     # Python Basics, Data Science, Web Dev
lib.search('data science') # Found: Data Science by Sara
