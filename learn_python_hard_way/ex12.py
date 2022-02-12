# Exercise 12 Prompting People

# But input() can have a stdout
# to receive a stdin, and therefore associate
# stdin to a variable
age = input("How old are you? ")
# space in the final before double quote
# works aesthetically, to receive the stdin
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
