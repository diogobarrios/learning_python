# Exercise 33: While Loops

i = 0
numbers = []

print("What number you want to start?")
# While-loop works with int so I've to
# coerce the stdin char to int.
x = int(input("> "))

while i < x:
    print(f"At the top i is {i}")
    numbers.append(i)

    # i = i + 1
    i += 1
    print("Numbers now: ", numbers)

    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
