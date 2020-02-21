# This would be a simple example

# def divide(dividend, divisor):
#     if divisor == 0:
#         raise ZeroDivisionError("Divisor cannot be zero")
#
#     return dividend / divisor
#
#
# def calculate(*values, operator):
#     return operator(*values)
#
#
# result = calculate(10, 2, operator=divide)
# result2 = calculate(10, 0, operator=divide)
# print(result)
# print(result2)


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Nothing could be found with the value {expected}")


friends = [
    {"name": "Neto Galindo", "age": 35},
    {"name": "Jose Something", "age": 27},
    {"name": "Arthur Whatever", "age": 25}
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Neto Galindo", get_friend_name))
print(search(friends, "Whatever Galindo", get_friend_name))
