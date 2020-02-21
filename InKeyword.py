friends = ["ross", "rachel", "chandler", "joey", "phoebe", "monica"]
print("chandler" in friends)

user_choice = input("What is your favorite Friend's character? ").lower()

if user_choice not in friends:
    print("Your character is not in our list.")
else:
    print(f"Nice! We also love {user_choice.capitalize()}.")

print("rix" in "The Matrix")
print("rics" in "The Matrix")
