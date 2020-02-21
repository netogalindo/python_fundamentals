# It is possible to do the while statement the way we are all accustomed to do, but this way here is more effective
while True:
    user_input = input("Do you want to play (Y/n)? ")

    if user_input == "n":
        print("I understand. Maybe next time!")
        break
    else:
        print("Let's play then!")
        print("*They've played together*")

friends = ["Chandler", "Monica", "Ross", "Rachel", "Phoebe", "Joey"]

print()

for friend in friends:
    print(f"{friend} is my friend!")

print()

grades = [35, 67, 98, 100, 100]
total = 0 # You also use total = sum(grades)
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)
