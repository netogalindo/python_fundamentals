x = 5 # A variable
x = (5, 11) # A tuple
x = 5, 11 # Another way of defining a tuple. This is accepted.

# But, what if you want to define two variables, instead of a tuple with two variables?
x, y = 5, 11 # Python is smart enough to understand x = 5 and y = 11

# Let's say you have a tuple (5, 11)
tup = 5, 11
# If you say x and y = tup, you assign values to x and y by using the values in the tuple
x, y = tup

print(x, y)

print()

person = ("Neto", 36, "QA Analyst")
name, _, profession = person
# The Python community has defined a rule where you use "_" to say a variable should not be used

print(name, profession)

print()

head, *tail = [1, 2, 3, 4, 5]
# * is a symbol for "collecting". It means you are collecting?destructuring all these values into the variable tail

print(head)
print(tail)

*head, tail = [1, 2, 3, 4, 5]

print(head)
print(tail)
