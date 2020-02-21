def add(x, y): # These are called parameters
    result = x + y
    print(result)


add(5, 4) # These are called arguments


def say_hello(name, surname):
    print(f"Hello, {name} {surname}!")


say_hello("Neto", "Galindo") # Positional parameter

say_hello(surname="Galindo", name="Neto") # Named arguments or keyword arguments
