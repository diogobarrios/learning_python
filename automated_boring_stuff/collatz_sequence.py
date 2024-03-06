def collatz() -> str:
    """collatz sequence"""
    
    # Initialize with 0
    # Avoids raising UnboundLocalError Exception
    number = 0
    print("Enter a positive integer number:")
    
    while True:
        try:
            number = int(input())
        except (ValueError, TypeError) as e:
            print("Please provide a positive integer number.")
            continue
        else:
            # False when number = 0
            if number:
                while number != 1:
                    # even number
                    if number % 2 == 0:
                        number = number // 2
                        print(number)
                        continue
                    # odd number
                    if number % 2 == 1:
                        number = 3 * number + 1
                        print(number)
            else:
                # Continue if was provided 0 or 1 to not stop the challenge
                print("Provide another positive integer number.")
                continue
           
            # break the first while statement
            print("Do you want to continue?(Y/n)")
            answer = str(input())    
            
            if answer.lower() == 'y':
                print("Provide positive integer number.")
                continue
            elif answer.lower() == 'n':
                    break
            else:
                # if the answer is not neither 'y' nor 'n'
                print("Didn't understand.\nClosing...")
                break
                
    
        