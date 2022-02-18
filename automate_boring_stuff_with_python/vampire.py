if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not and undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie')

# the order of the if statements matter!
# If i change the order between the third and
# the second condition, anything greater than 100
# will satisfy and would print "You are not Alice, grannie."
