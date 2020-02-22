def add(x, y): # These are called parameters
    result = x + y
    print(result)


add(5, 4) # These are called arguments


def say_hello(name, surname):
    print(f"Hello, {name} {surname}!")


say_hello("Neto", "Galindo") # Positional parameter

say_hello(surname="Galindo", name="Neto") # Named arguments or keyword arguments

print()


def addition_sequence(number):
    i = 1
    x = 1
    previous_number = 1
    while i <= number:
        if i == 1:
            i = 2
            x = 2
            print(x)
        i += 1
        new_number = x + previous_number
        previous_number = x
        x = new_number
        print(x)


addition_sequence(5)
