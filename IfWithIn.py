print("Hello!!!")
print("This is a game where you pick a number and see if you guessed one of the numbers, in a list of magic numbers!")

user_decision = input("Do you want to play (Yes or No)? ")

if user_decision in ("y", "Y", "yes", "Yes", "YES"): # In this case, it's a tuple, but it doesn't have to be
    magic_number = {1, 3, 9}
    user_input = int(input("Enter an integer number from 0 to 9: "))

    if user_input in magic_number:
        print("You have guessed correctly!")
    else:
        print("Aw! You guess wrong. Better luck next time!")
else:
    print("That's a shame! Maybe you'll want to play next time. Have a nice day!")

print()

print("Maybe you'd like to play a game where there's only one magic number.")

number = 4
user_number = int(input("Please enter any number from 1 to 5: "))

if abs(number - user_number) == 1:
    print("You're off by one!")
elif number == user_number:
    print("You've guessed the number correctly!")
else:
    print("Better luck next time!")
