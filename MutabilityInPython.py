a = []
b = a

c = 8597
d = 8597

a.append(35)

print(id(a))
print(id(b))
print(id(c))
print(id(d))

print(a)
print(b)
print(c)
print(d)

# Remember: Tuples are immutable
# Strings, Integers, Floats and Booleans are also immutable

c = 8598

print(id(c))
print(id(d))
