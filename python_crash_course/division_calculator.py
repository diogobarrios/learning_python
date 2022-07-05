print("Give me two numbers, and I'll divide them.")

while True:
    print("Enter 'q' to quit.")
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = float(first_number) / float(second_number)
    except (ZeroDivisionError, ValueError):
        print("You have to use only integers > 0!")
    else:
        print(answer)