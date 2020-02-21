def named(**kwargs):
    print(kwargs)


details = {"name": "Neto", "age": 36}

named(**details)

print()


def print_nicely(**kwargs):
    named(**kwargs)
    for kwarg, value in kwargs.items():
        print(f"{kwarg}, {value}")


print_nicely(name="Neto", age=36)

print()


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 2, 3, name="Neto", age=36)

