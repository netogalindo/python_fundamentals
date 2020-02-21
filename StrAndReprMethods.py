class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age} years old."

    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>" # Some of these symbols are just to be clearer to a programmer
    # This method is used, for example, with the debugger functionality. If you want to try it, comment the __str__
    # method, and this one is called instead. Once again: It's more used to show information to developers, not to
    # users. Like any other method, you can also call it with neto.__repr__().

# You don't need to call magic methods. The init method, for example, happens automatically when you create an object.


neto = Person("Neto", 35)
print(neto) # If you don't define a method for this, Python, by itself, prints a string representing the neto object
# created. That's why it's a weird result.
print(neto.__repr__())
