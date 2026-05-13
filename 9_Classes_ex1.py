# 9.1. Restaurant. 
# Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: 
# a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, 
# and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
print("=====")
class Restaurant:
    """"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant is open between 12:00 and 13:00")

dodos_world = Restaurant('Dodos_world','Noone dare to check')
dodos_world.describe_restaurant()
dodos_world.open_restaurant()

# 9.2. Three Restaurants. 
# Start with your class from Exercise 9.1. Create three different instances from the class, and call describe_restaurant() 
# for each instance.
print("=====")
restaurant_1 = Restaurant('Restaurant_1','A')
restaurant_2 = Restaurant("Restaurant_2",'B')
restaurant_3 = Restaurant('Restaurant_3','C')
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

# 9.3. Users. 
# Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes 
# that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user's 
# information. Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.
print("=====")
class User:
    """"""
    def __init__(self,first_name,last_name,password,age):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.age = age
    def describe_user(self):
        print(f"User name is: {self.first_name.title()} {self.last_name.title()}. His password is: {self.password} and he is {self.age} old")

    def greet_user(self):
        print(f"Welcome {self.first_name.title()} {self.last_name.title()}.")

user_1 = User('johny','silverhand',123,130)
user_2 = User('Mr','bean','haha',32)
user_3 = User('Eric', 'Matthes','Python,rocks!@',56)

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()