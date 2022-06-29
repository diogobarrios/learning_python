class User:
    """Describe user information"""

    def __init__(self, first_name, last_name, mail, tel_number):
        """Initialize the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.mail = mail
        self.tel_number = tel_number

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


user_1 = User('Diogo', 'Barrios', 'diogo@mail.com', '910000000')
user_1.describe_user()
user_1.greet_user()
print("\n")
user_2 = User('Bernardo', 'Barrios', 'bernie@mail.com', '910000001')
user_2.describe_user()
user_2.greet_user()
