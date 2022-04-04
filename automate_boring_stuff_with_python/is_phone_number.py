#! python3


def is_phone_number(text):
    # The code checks that the string is exactly 12 characters
    if len(text) != 12:
        return False
    for i in range(0, 3):
        # Checks that the area code(the first three characters in text)
        # consists of only numeric characters
        if not text[i].isdecimal():
            return False
    # The number must have the first hyphen after the area code
    if text[3] != '-':
        return False
    for i in range(4, 7):
        # three more numeric characters
        if not text[i].isdecimal():
            return False
    # then another hyphen
    if text[7] != '-':
        return False
    for i in range(8, 12):
        # Finally four more numbers
        if not text[i].isdecimal():
            return False
    # If the program execution manages to get past all the Checks
    # it returns TRUE
    return True


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office'
for i in range(len(message)):
    # On each iteration of the for loop a new chunk of 12 characters
    # from message is assigned to the variable chunk
    chunk = message[i:i+12]
    # Passes chunk to is_phone_number() function to see whether it
    # matches the phone number pattern
    if is_phone_number(chunk):
        print('Phone number found:' + chunk)
print('Done')
