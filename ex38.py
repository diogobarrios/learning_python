# Exercise 38: Doing Things to Lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# Call split on ten_things and save on stuff
# split(ten_things)
stuff = ten_things.split(' ')

# List
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

# 6 items
print("length of stuff: ", len(stuff))

while len(stuff) != 10:
    # Call pop on more_stuff and saves on next_one
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff")

print(stuff[1])
print(stuff[-1])  # whoa! fancy
print(stuff.pop())
print(' '.join(stuff))  # what? cool!
print('#'.join(stuff[3:5]))  # super stellar
