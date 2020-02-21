def add(x, y):
    print(x + y)


add(5, 8)
# result = add(5, 8) Commented so I won't be getting warnings on my project, but it does NOT result in an error
# print(result) It will return "None", because result will be "none". Notice print(x + y) is void. That means return is
# void. So print will try to print a void value, and then Python returns "None".

# If you want to fix this...

print()


def add(x, y):
    return x + y # return ends the function, so, if you were to add something after the end, it wouldn't be processed


result = add(5, 8)
print(result)

# You can also do as follows

print()

print(add(8, 12))
