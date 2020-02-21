friends = {"Neto", "Jose", "Arthur"}
abroad = {"Neto", "Arthur"}
local_friends = friends.difference(abroad)

print(local_friends)

local_friends = abroad.difference(friends)

print(local_friends) # The result is the notation for an empty set

print()

local_friends = {"Neto"}
abroad_friends = {"Jose", "Arthur"}

friends = local_friends.union(abroad_friends)
print(friends)

art = {"Neto", "Jose", "Arthur"}
science = {"Neto", "Jose"}

print()

both = art.intersection(science)
print(both)
