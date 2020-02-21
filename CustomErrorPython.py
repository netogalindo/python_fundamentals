class TooManyPagesReadError(ValueError): # You need to make them a child of an Error class or of the Exception class
    pass # You don't need to anything, because the parent class already have everything needed to raise an error


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages, out of {self.page_count}"
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} but this book only has {self.page_count} pages"
            )
        self.pages_read += pages
        print(f"You have read {self.pages_read} out of {self.page_count}")


python101 = Book("Python 101", 50)

try:
    python101.read(35)
    python101.read(50)
except TooManyPagesReadError as e:
    print(e)
