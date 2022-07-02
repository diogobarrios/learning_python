class User:
    """Describe user information"""

    def __init__(self, first_name, last_name, mail, tel_number):
        """Initialize the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.mail = mail
        self.tel_number = tel_number
        self.login_attempts = 0

    def describe_user(self):
        """User information"""
        print("-" * 10 + "Summary" + "-" * 10)
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Mail: {self.mail}")
        print(f"Mobile Number: {self.tel_number}")
        print("-" * 27)

    def greet_user(self):
        """Greeting the user"""
        print(f"Greetings {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        """Increment attempts of an unsuccessful login"""
        self.login_attempts += 1
        print(
            f"Wrong username/password left: {3 - self.login_attempts} attempts")

    def reset_login_attemps(self):
        """Reset the login_attempts counter to intial value"""
        self.login_attempts = 0
        print("Let's reset the counter to have with 3 attempts again")
        print(f"Counter: {self.login_attempts}")

class Privileges:
    """Stores all information about privileges"""
    
    def __init__(self):
        privileges = ['can delete a post','can ban user', 'can execute the root']
        self.privileges = privileges

    def show_privileges(self):
        """Describe what privileges the Admin has"""
        print("These are some privileges of the Admin")
        for p in self.privileges:
            print(f"{p}")

class Admin(User):
    """Describing the attributes from the special User"""

    def __init__(self, first_name, last_name, mail, tel_number):
        """Initialize the attributes Admin"""
        super().__init__(first_name, last_name, mail, tel_number)
        self.privilege = Privileges()
