# Composition is a counterpart to inheritance, to build classes that use other classes


class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"This bookshelf has {len(self.books)} books."

    def book_list(self):
        x = 0
        for book in self.books:
            print(f"{x+1}. {book.name}")
            x += 1
            if x == len(self.books):
                return "All books have been listed"


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book_one = Book("Harry Potter")
book_two = Book("Python 101")
shelf = Bookshelf(book_one, book_two)

print(shelf)
print(shelf.books) # Returns objects in that weird way
# But...
print(shelf.book_list())
