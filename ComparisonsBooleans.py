print(5 == 5) # == is used to compare two things
print(5 == 7)
print(5 > 5)
print(10 != 10)
print(10 <= 10)
print("Neto" == "Neto")
print("Neto" == "Net")

print()

friends = ["Neto", "Arthur"]
abroad = ["Neto", "Arthur"]
print(friends == abroad)
print(friends is abroad) # They have the same value and both are lists, but they are NOT the same thing
print(friends is friends) # In this case, they are the exact same thing

x = 5
print(isinstance(x, int))
