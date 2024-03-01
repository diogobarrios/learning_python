 # Exercise about while loop
 
while True:
    print("Who are you?")
    name = input()
    if name != 'Diogo':
        continue
    print("Hello, Diogo. What is the password? (It is a fish.)")
    password = input()
    if password != 'sardinha':
        break
print("Access granted.")