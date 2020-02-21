def add(x, y=8): # x is a required parameter, and y is an optional parameter
    print(x + y)


add(5)
add(x=5) # It's the same thing as the one on line 5
# add(y=5) This one would result in an error
add(x=5, y=5) # Perfectly acceptable
# add(x=5, y) It will result in an error because you can't put a positional argument after a keyword argument

default_y = 3


def add(x, y=default_y): # Don't do this
    result = x + y
    print(result)


add(2)

default_y = 4
add(2) # This is the reason why you shouldn't do that. If you do that on the function, the result will stay the same,
# because the parameter's value is defined when the function is created. This means that, even after you define
# default_y as 4, it continues being 3.
