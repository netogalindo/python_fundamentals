# Dictionaries are used to associate keys and values together

friends_ages = {"Neto": 35, "Arthur": 25, "Jose": 28}

print(friends_ages)

friends_ages["Ana"] = 31

print()

print(friends_ages["Arthur"])
print(friends_ages["Ana"])
print(friends_ages)

print()

friends_ages["Neto"] = 36

print(friends_ages)

print()

friends = [
    {"name": "Neto", "age": 36},
    {"name": "Arthur", "age": 25},
    {"name": "Jose", "age": 28},
    {"name": "Ana", "age": 31}
]

print(friends)
print(friends[1])
print(friends[1]["name"])

print()

for friend in friends:
    print(friend)

student_attendance = {"Neto": 90, "Arthur": 70, "Jose": 85} # The name is a tag, and the int is the value

for student, attendance in student_attendance.items(): # This is destructuring
    print(f"{student}: {attendance}%")

print()

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))