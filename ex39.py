# Exercise 39: Dictionaries, Oh Lovely Dictionaries

# List
things = ['a', 'b', 'c', 'd']
# Will print index 1 = b
print(things[1])

# changing the index 1 = z
things[1] = 'z'

# Will print index 1 = z
print(things[1])

# The new List with 'z'
print(things)

# Dictionary can be called the index's
# with anything

stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
print(stuff['name'])
# will print a string 'Zed'

print(stuff['age'])
# will print a int 39

print(stuff['height'])
# will print a int 74

# Adding a new var 'city' as 'SF'
stuff['city'] = 'SF'

print(stuff['city'])
# will print a string 'SF'

print("Adding to dict 'stuff' a key '1' to a value 'Wow'")
stuff[1] = 'Wow'
print(stuff[1])

print("Adding to a dict 'stuff' a key '2' to a value 'Neato'")
stuff[2] = 'Neato'
print(stuff[2])

print("Dict 'stuff'")
print(stuff)

print("Now we delete the new entries because doesn't make sense.")
print("Using 'del'")
del stuff['city']
del stuff[1]
del stuff[2]

print("The Dict as was!")
print(stuff)

# ------------------------ #

# continue and clean above to do the new one
