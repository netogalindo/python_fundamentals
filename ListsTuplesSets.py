list_example = ["Neto", "Jose", "Arthur"]
# You can modify a list and have duplicate elements
# Also, it keeps the order of elements

tuple_example = ("Neto", "Jose", "Arthur")
# You can't modify a tuple
# Also, it keeps the order of elements

set_example = {"Neto", "Jose", "Arthur"}
# You can't have duplicate elements in a set
# The order of the elements is not guaranteed

print(list_example[0])
print(tuple_example[0])
# print(set_example[0]) This doesn't work because they don't have any order

list_example[2] = "Andre"
print(list_example)
print(tuple_example)
print(set_example)
print()

# tuple_example[0] = "Jorge" This doesn't work because tuple does not allow item assignment
# set_example[0] = "Jorge" This doesn't work because set does not allow item assignment (It has no order)

list_example.append("Jorge")
print(list_example)

list_example.remove("Andre")
print(list_example)

set_example.add("Andre") # It's add, not append, because sets have no end, since they have no order
print(set_example)
set_example.add("Andre") # It's ignored, since there can be no duplicate elements on a set
print(set_example)

print()
print(list_example)
print(tuple_example)
print(set_example)
