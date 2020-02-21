name = input("Enter your name: ")
print(name)

print()

number_input = input("Type a number: ")
number_in_int = int(number_input)
triple_value = number_in_int * 3
divided_by_three_value = number_in_int / 3

print(triple_value) # If the value were a string, it would have printed the number 3 times
print(f"{divided_by_three_value:.2f}") # If the value were a string, it would have caused an error
# In this last one, I could also have used round

print(f"Multiplied by 3 equals: {triple_value} and divided by 3 equals: {divided_by_three_value:.2f}")
