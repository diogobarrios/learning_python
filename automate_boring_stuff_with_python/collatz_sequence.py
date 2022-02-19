# Sequence Collatz

# Collatz Function():
def collatz(number):
    # If the number is even, number // 2
    if number % 2 == 0:
        return number // 2
    # If the number is odd, 3 * number + 1
    else:
        return 3 * number + 1


print('type a number:')
try:
    number = int(input())  # the first input()
    while True:
        # Get the new number from collatz() and assigned to number variable
        number = collatz(number)
        # print the new value
        print(number)
        # if result is not equal to 1 (True), repeat the process
        if number != 1:
            continue
        # if result is equal to 1 (False), print the text in the string and break
        # the while loop
        print('You did it!')
        break
except ValueError:
    print('Error: Invalid argument')
