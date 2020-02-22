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

multi_line_string = """
This is a multi-line string.
Every time I type enter, another line is generated.
"""

print(multi_line_string)
print(multi_line_string[1])
print(multi_line_string[51])
print(multi_line_string[5]) # This is a space, which is why the result is blank/empty
print(multi_line_string[1:10])
print(multi_line_string[-10:-1])
print(len(multi_line_string))
# This happens because, in Python, a string is an array

print()

testing_string = " Hello, World "
print(testing_string.lower())
print(testing_string.upper())
print(testing_string.strip())
print(testing_string.strip().lower())
print(testing_string.replace("H", "Z"))
print(testing_string.split(","))
testing_capitalization = "hello"
print(testing_capitalization.capitalize())
testing_title = "hello, world"
print(testing_title.title()) # Turns the first letter of every word into a capital letter
k = "ell"
print(k in testing_string)
print(k not in testing_string)

escape_character_testing = "Hi, my name is \"Neto\""
print(escape_character_testing)
