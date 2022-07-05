import json

# load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        f.write('\n')
    return username

def validate_username(username):
    """Check if it's new username or not"""
    validate = input("What is you name that is stored? ")
    if username.lower() != validate.lower():
            print("You are a new user, let's remember you next time!")
            validate = get_new_username()
    else:
        None
    return validate

def greet_user():
    """Greet the user by the name."""
    username = get_stored_username()
    if username:
        validate = validate_username(username)
        print(f"We'll remember you when you come back, {validate}")
    elif username:
        print(f"Welcome Back, {username}!")
    else:
        username = get_new_username()        
        print(f"We'll remember you when you come back, {username}")
    
greet_user()