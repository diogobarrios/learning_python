# Sequence Collatz
def collatz(number):
    # If the number is even, number // 2
    if number % 2 == 0:
        return number // 2
    # If the number is odd, 3 * number + 1
    else:
        return 3 * number + 1


while collatz < 1:
    print('type a number:')
    number = int(input())
    result = collatz(number)
    print(result)
