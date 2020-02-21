def multiply(*args):
    total = 1
    for n in args:
        total = total * n
    return total


print(multiply(1, 3, 5, 2))
print(multiply(10))


def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))


def apply(*args, operator):
    if operator == "*":
        return multiply(*args) # The * is necessary, because if not used, args will be considered a tuple, and a tuple *
        # 1 is the tuple itself. The tuple keeps being multiplied by one, and that's why the result ends up being the
        # tuple
    elif operator == "+":
        return sum(args)
    else:
        return print("No operator could be found for your option.")


print(apply(3, 5, operator="*"))

