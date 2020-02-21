def hello():
    print("Hello!")


hello()

print("Welcome to the Age in Seconds program")


def user_age_in_seconds():
    age = int(input("Enter your age, please: "))
    age_in_seconds = (age * 365 * 24 * 60 * 60) + (age * (round(age / 4, 0)) * 24 * 60 * 60)
    print(age_in_seconds)


user_age_in_seconds()

print("Goodbye!")
