name = "Bob"
greeting = "Hello, Bob"

print(greeting)

name = "Rolf"

print(greeting)

greeting = f"Hello, {name}"
# It could also be greeting = "Hello, " + name, but both options work with the value at the exact time, so it's good,
# for example, for not having to create a variable for it at all

print(greeting)
print("Hello, " + name)

print()
name = "Bob"
greeting = "Hello, {}" # This is called a template
with_name = greeting.format(name) # You could have used "Rolf" here, or Bob, or even other types of variables

print(with_name)

longer_phrase = "Hello, {}. Today is {}. The number you're thinking right now is {}."
formatted = longer_phrase
with_info = formatted.format("Neto", "Friday", 8)

print(with_info)
