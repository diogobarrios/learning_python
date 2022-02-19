import random


def get_answer(number):
    if number == 1:
        return 'It is certain'
    elif number == 2:
        return 'It is decidedly so'
    elif number == 3:
        return 'Yes'
    elif number == 4:
        return 'Reply hazy try again'
    elif number == 5:
        return 'Ask again later'
    elif number == 6:
        return 'Concentrate and ask again'
    elif number == 7:
        return 'My reply is no'
    elif number == 8:
        return 'Very doubtful'


# randomly get a number between [1, 8]
# r = random.randint(1, 8)
# Passed the value stored in 'r' to the get_answer()
# fortune = get_answer(r)
# print the answer that was assigned by the variable 'r'
# in fortune
# print(fortune)

# A shorter way to do the same above:
print(get_answer(random.randint(1, 8)))
