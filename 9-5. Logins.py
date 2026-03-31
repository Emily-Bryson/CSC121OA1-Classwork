class User:
    """A simple attempt to model a user profile."""
    def __init__(self, first_name, last_name, username, email):
        """"Initialize the user's attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0
    def describe_user(self):
        """Print a summary of the user's information."""
        print(f" User Profile: {self.username}")
        print(f" Full Name: {self.first_name}")
        print(f" Email: {self.email}")
    def greet_user(self):
        """"Print a personalized greeting to the user."""
        print(f"Welcome back, {self.first_name}!")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
user1 = User('Logan', 'Toney', 'Ltoney22', 'logantoney.lt22@gmail.com' )       
user2 = User('Ozzy', 'Osbourne', 'OzzyOz26', 'ozzyozcrazy@gmail.com')
user3 = User('Analillia', 'Martin', 'AnalillaM24', 'analillia.lilly@gmail.com')
user4 = User('Callie', 'Mayne', 'CalMayne21', 'Callie.mayne@gmail.com')

user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Login attempts: {user1.login_attempts}")
user1.reset_login_attempts()
print(f"Reset login attempts: {user1.login_attempts}")

user2.describe_user()
user2.greet_user()
user2.increment_login_attempts()
user2.increment_login_attempts()
user2.increment_login_attempts()
print(f"Login attempts: {user2.login_attempts}")
user2.reset_login_attempts
print(f"Reset login attempts: {user2.login_attempts}")

user3.describe_user()
user3.greet_user()
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()
print(f"Login attempts: {user3.login_attempts}")
user3.reset_login_attempts
print(f"Reset login attempts: {user3.login_attempts}")

user4.describe_user()
user4.greet_user()
user4.increment_login_attempts()
user4.increment_login_attempts()
user4.increment_login_attempts()
print(f"Login attempts: {user4.login_attempts}")
user4.reset_login_attempts
print(f"Reset login attempts: {user4.login_attempts}")