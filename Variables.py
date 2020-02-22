import random

x = 15
price = 9.99
discount = 0.2

result = price * (1 - discount)

print(result)

name = "Bob"
name = "Rolf"

print(name)
print(name * 2) # This is the same as name + name

a = 25
b = a # It's the same as b = 25

print(a)
print(b)

b = 17 # It changes b, but not a

print(a)
print(b)

"""
This is a multi-line comment
This is a multi-line comment
This is a multi-line comment
"""

y = z = j = 5

print(y)
print(z)
print(j)

y = "Neto", "Jose", "Arthur" # This is a tuple
print(y)
print(type(y))


def using_global_keyword():
    global n
    n = "Hi. I'm a global variable inside of a function"


using_global_keyword()
print(n)

w = int(5) # This is how you specify a data type
print(w)
print(type(w))
w = float(w) # This is how you convert a data type
print(w)
print(type(w))

# This randomizes a number. You have to import random to be able to do this.
print(random.randrange(1, 10)) # 10 does not count
