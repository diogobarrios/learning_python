# I want a picture character in a grid

# First do a loop from values in a ListofList
# List = ['.', '.', '0', '0', '.', '.']
# for i in range(len(List)):
#    print(List[i])

# Second, print a list inside a list
# ListofList = [['.', '.', '0', '0', '.', '.'],
#              ['0', '0', '.', '.', '0', '0']]

# dummie way to understand:
# print(ListofList[0][0], end='')
# print(ListofList[1][0])
# print(ListofList[0][1], end='')
# print(ListofList[1][1])
# . . .

# Third, make a function that does the same
def char_to_pic(ListofList):
    # Have to know the range of a list that is inside of the main list
    # because they are all equal, otherwise this won't work.
    range_i = range(len(ListofList))
    range_j = range(len(ListofList[min(range_i)]))
    # loop in a loop to get a matrix
    for j in range_j:
        for i in range_i:
            if i != max(range_i):
                print(ListofList[i][j], end='')
            else:
                print(ListofList[i][j])


# the List of lists:
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Let's play:
char_to_pic(grid)
