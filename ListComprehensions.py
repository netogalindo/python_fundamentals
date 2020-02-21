numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers] # This is a list comprehension. They should be kept short.

print(doubled)

friends = ["Neto", "Nathan", "Jose", "Arthur", "Nora"]
starts_with_n = [friend for friend in friends if friend.startswith("N")] # If comes at the end

print(starts_with_n)

print("Friends: ", id(numbers), " Starts_With_N: ", id(starts_with_n))
