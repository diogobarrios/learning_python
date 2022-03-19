# This is the original exercise
'''print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too.')
else:
    print('I hope the rest of your day is good.')
'''

# Done with some more options of response!
# create a list of options that can be stdin
feelings = ['great', 'good', 'sad']

print('How are you?')
feeling = input()
if feeling.lower() in feelings:
    # The script will mirror the same feeling.
    print('I fell ' + feeling + ' too.')
else:
    print('I hope the rest of your day is good.')
