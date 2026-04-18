class Library:
    def __init__(self, item):
        self.item = item

    def welcome(self):
        print(f"Welcome to {self.item} library !")

class Book(Library):
    def __init__(self, item, title, author):
        super().__init__(item)
        self.author = author
        self.title = title

# Code ko chalane ke liye:
my_book = Book("Punjab University", "Python Guide", "Dr Ahmad")
my_book.welcome()
print(f"Book Name:{my_book.title}")
print(f"Author:{my_book.author}")
