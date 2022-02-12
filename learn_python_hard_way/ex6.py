# Exercise 6: Strings and Text

# basic variables
types_of_people = 10
x = f"There are {types_of_people} types of people"

# basics variables and a nested variable
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

# Here is a new thing,
# varible with a boolean
hilarous = True
# create a new variable with a empty curly braces
joke_evaluation = "Isn't that joke so funny?! {}"
# print it with .format()
print(joke_evaluation.format(hilarous))

w = "This is the left side of..."
e = "a string with a right side."

# This is new to with a plus operator
# that creates one string
print(w + e)
