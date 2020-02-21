age = int(input("Enter your age: "))

age_in_months = age * 12
age_in_seconds = (age * 365 * 24 * 60 * 60) + (age * (round(age / 4, 0)) * 24 * 60 * 60)

print(f"You have lived for {age_in_months} months.")
print(f"You have lived for {age_in_seconds} seconds.")
