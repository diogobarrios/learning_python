from user import User, Privileges, Admin

admin = Admin('Diogo', 'Barrios', 'diogo@mail.com', '910000000')
admin.describe_user()
admin.privilege.show_privileges()

user_1 = User('Diogo', 'Barrios', 'diogo@mail.com', '910000000')
user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attemps()

print("\n")
user_2 = User('Bernardo', 'Barrios', 'bernie@mail.com', '910000001')
user_2.describe_user()
user_2.greet_user()