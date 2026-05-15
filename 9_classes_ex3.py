# 9.6 – Ice Cream Stand
# An ice cream stand is a specific type of restaurant. Define a class called IceCreamStand inheriting from the Restaurant class created in exercise 9.1 or 9.4. Any version of the class will work. 
# Add an attribute called flavors that stores a list of ice cream flavors. Define a method called display_flavors that displays the available flavors. Create an instance of the IceCreamStand class and call the new method.
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

class IceCreamStand(Restaurant):
    ''''''
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)

Icey_res = IceCreamStand('Icey_res', "ice cream",['chocolate','vanilia','blueberry'])
Icey_res.display_flavors()
# 9.7 – Admin
# An administrator is a special type of user. Define a class called Admin inheriting from the User class created in exercise 9.3 or 9.5. 
# Add a privileges attribute storing a list of strings such as "can add post", "can delete post", or "can ban user". Define a method called show_privileges() that displays the list of admin privileges. 
# Create an instance of the Admin class and call the new method.
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

class Admin(User):
    """"""

    def __init__(self,first_name,last_name,password,age):
        super().__init__(first_name,last_name,password,age)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):        
        print(self.privileges)

admin_1 = Admin('first','with last name', 'you will not see it', 13)
admin_1.show_privileges()
# 9.8 – Privileges
# Define a separate class called Privileges. This class should have one attribute (privileges) storing a list of strings, as shown in the previous exercise. 
# Move the show_privileges() method to the new class. Create an instance of Privileges as an attribute in the Admin class. Then create a new instance of Admin and use show_privileges() to display the privileges.

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)
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

class Admin(User):
    """"""

    def __init__(self,first_name,last_name,password,age):
        super().__init__(first_name,last_name,password,age)
        self.privileges = Privileges(['can add post', 'can delete post', 'can ban user'])

admin_2 = Admin('first','with last name', 'you will not see it', 13)
admin_2.privileges.show_privileges()

# 9.9 – Battery Upgrade
# Start from the latest version of the electric_car.py program created in this section. Add a new method called upgrade_battery() to the Battery class. 
# This method should check the battery capacity and set it to 65 if it is currently different. 
# Create an electric car instance with a default battery capacity, call get_range(), then call upgrade_battery(), and call get_range() again. You should notice an increase in the car's range.

class Car:
    """Simple representation of a car."""

    def __init__(self, make, model, year):
        """Initialisation of attributes describing a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return formated description of a car"""
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()
    
    def read_odometer(self):
        """Prints information about an odometer."""
        print(f"This car has {self.odometer_reading} km.")

    def update_odometer(self, mileage):
        """Updating value of odometer."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("It is not allowed to put lower reading than existing.")

    def increment_odometer(self,kilometers):
        """Incrementing odometer by a given number of km."""
        self.odometer_reading += kilometers

    def fill_gas_tank(self):
        """Car will fill it's gas tank."""
        print(f"Filling up the gas tank.")


class ElectricCar(Car):
    """It adds characterictics typical to an electric car."""

    def __init__(self, make, model, year):
        """Inicialisation of class attributes."""
        super().__init__(make, model, year)
        self.battery_size = 40
        self.battery = Battery()

    def describe_battery(self):
        """Printing information about size of the battery."""
        print(f"This car has {self.battery_size} kWh battery.")

    def fill_gas_tank(self):
        """Electric car does not have gas tank."""
        print(f"This car cannot fill it's gas tank.")

class Battery:
    """Simple model of an electric car battery."""
    
    def __init__(self,battery_size=40):
        """"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Printing information about battery size."""
        print(f"This car has battery that is {self.battery_size} kWh.")

    def get_range(self):
        """Print actual information about range based on the size of the battery."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"Range of this car is approx. {range} when the battery is full.")

    def upgrade_battery(self):
        """Upgrading the battery."""
        if self.battery_size != 65:
            self.battery_size = 65

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()