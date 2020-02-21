# A lambda function is a function without a name, and its only purpose is to return values

# add = lambda x, y: x + y Can be done, but not advisable, because lambda functions exist to be used without a name

# print(add(5, 4))

print((lambda x, y: x + y)(5, 4))

print()

sequence = [1, 3, 5, 9]
# doubled = [(lambda x: x * 2)(x) for x in sequence] Could be done like this
doubled = list(map(lambda x: x * 2, sequence))

print(doubled)
