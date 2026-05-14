# 9.4. Number of Customers Served.
# Start with the program created in exercise 9.1. Add an attribute called number_served with a default value of 0. 
# Create an instance of the class called restaurant, change this value and display it later. Display the number of customers served by the restaurant.
# Add a method called set_number_served(), allowing you to define the number of customers served. Call this method with various values along with the number of customers served.
# Add a method called increment_number_served(), allowing you to increment the number of customers served. Call this method and display it.

class Restaurant:
    """"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant is open between 12:00 and 13:00")

    def set_number_served(self,number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

restaurant_1 = Restaurant("Dodo","Unknown")
restaurant_1.number_served = 5
print(restaurant_1.number_served)
restaurant_1.set_number_served(10)
restaurant_1.set_number_served(12)
restaurant_1.increment_number_served(2)
print(restaurant_1.number_served)

# 9.5. Login Attempts.
# Start with the program created in exercise 9.3. Add a method called increment_login_attempts(), allowing you to increment the value of login_attempts. 
# Add a second method called reset_login_attempts(), which will zero out the value of login_attempts. Create an instance of the User class and call the increment_login_attempts() method multiple times to be sure about its 
# value login_attempts. Display the value of login_attempts, then call the reset_login_attempts() method and verify that its value is indeed 0.
print("=====")

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

user_1 = User('dodo', 'toto', 123,12)
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)
