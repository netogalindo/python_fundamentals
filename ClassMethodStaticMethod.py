class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static method")


test = ClassTest()
test.instance_method()
ClassTest.class_method() # Python is passing the class itself as a parameter, automatically
ClassTest.static_method()


print()


class Book:
    TYPES = ("hardcover", "paperback") # This is a variable (A tuple) inside of a class

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100) # You can use Book instead of cls

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight) # Same here, but not advisable in either


print(Book.TYPES)

book = Book.hardcover("Harry Potter", 1500)
light_book = Book.paperback("Python 101", 600)

print(book)
print(light_book)

print()


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        name = f"{store.name} - franchise"
        return cls(name)
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        stock = int(store.stock_price())
        return f"{store.name}, total stock price: {stock}"
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'


store1 = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

print(Store.franchise(store1).name)
print(Store.franchise(store2).name)

print(Store.store_details(store1))
print(Store.store_details(store2))
