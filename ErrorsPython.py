# Errors help you track down problems and where and how they happened
# It's not ideal to be showing error results to users, but it's great to use them when you're testing the program


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero")
    return dividend / divisor


grades = []

print ("Welcome to the Average Grades program")

try: # This is the part of the code that can raise an error
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e: # This is processed if an error happens
    print(e) # This prints the error. You don't have to do this.
    print("There are no grades in your list yet") # This handles the error for you to do what you want
else: # This is processed if there are no errors
    print(f"The average grade is {average}")
finally: # This is processed every time
    print("Thank you!")

# Other error classes are TypeError, ValueError, RuntimeError, etc
