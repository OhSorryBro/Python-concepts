class User:
    """"""
    def __init__(self,first_name,last_name,password,age):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.age = age
        self.login_attempts = 0
    def describe_user(self):
        print(f"User name is: {self.first_name.title()} {self.last_name.title()}. His password is: {self.password} and he is {self.age} old")

    def greet_user(self):
        print(f"Welcome {self.first_name.title()} {self.last_name.title()}.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


