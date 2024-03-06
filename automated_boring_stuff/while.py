 # Exercise about while loop
 
import logging

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
logging.disable(logging.DEBUG)

while True:
    print("Who are you?")
    name = input()
    if name != 'Diogo':
        logging.debug(name)
        continue
    print("Hello, Diogo. What is the password? (It is a fish.)")
    password = input()
    if password == 'sardinha':
        break
print("Access granted.")