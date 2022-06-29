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


user_1 = User('Diogo', 'Barrios', 'diogo@mail.com', '910000000')
user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attemps()

# print("\n")
# user_2 = User('Bernardo', 'Barrios', 'bernie@mail.com', '910000001')
# user_2.describe_user()
# user_2.greet_user()
