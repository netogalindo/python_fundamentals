user = [
    (0, "Neto", "password"),
    (1, "Jose", "jose123"),
    (2, "Arthur", "arthurpass1"),
    (3, "Ana", "12345")
]

username_mapping = {user[1]: user for user in user}

print(username_mapping)

print(username_mapping["Neto"])

# To do a login function, that's what you would do

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("You are logged in!")
else:
    print("There has been a problem. Your password is wrong.")

