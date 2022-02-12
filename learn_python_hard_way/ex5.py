# Exercise 5: More Variables and Printing
name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# f for "format"
# this string needs to be formatted. Put these variables in there.
print(f"Let's talk about {name}")
print(f"He's {height} inches tall")
print(f"He's {weight} pounds heavy")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# This is convert inches to centimeters
inch_to_cm = 2.54
height_cm = round(74.0 * inch_to_cm)
# This is convert pounds to kilograms
pound_to_kg = 0.45359237
weight_kg = round(180.0 * pound_to_kg)

print(f"He's {height_cm} centimeters tall and he weights {weight_kg} kilograms")
