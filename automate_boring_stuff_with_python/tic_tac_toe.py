# tic tac toe game

# First we create a variable with the nine strings that
# are the possibilities of the game to put 'X' or 'O'

# This represents an empty tic-tac-toe board
board = {'tL': ' ', 'tM': ' ', 'tR': ' ',
         'mL': ' ', 'mM': ' ', 'mR': ' ',
         'lL': ' ', 'lM': ' ', 'lR': ' '}

# Function to print the tic-tac-toe board game:


def print_board(the_board):
    print(the_board['tL'] + '|' + the_board['tM'] + '|' + the_board['tR'])
    print('-+-+-')
    print(the_board['mL'] + '|' + the_board['mM'] + '|' + the_board['mR'])
    print('-+-+-')
    print(the_board['lL'] + '|' + the_board['lM'] + '|' + the_board['lR'])


# using the print_board function that has the structure of the board to print
# the values of the board dictionary

# starting with the variable turn as 'X' but could be 'O'
turn = 'X'
# For all possibilities spaces that tic-tac-toe has, we wil choose
# what is the space using the coded keys
for i in range(9):
    # print board tic-tac-toe game after each move
    print_board(board)
    print('Example: if you want to put in the top-left, use: "tL"')
    print('Can be used: t/m/l with L/M/R')
    print('Turn for ' + turn + '. Move on which space?')
    # the dictionary key is store on move variable
    move = input()
    # then puts 'X' as value the pre-determined key
    board[move] = turn
    # finally we change for anonther player, and that one will
    # use 'O' value, if is in use, will change for the default 'X' value
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
# print tic-tac-toe game after finish the for loop
print_board(board)
