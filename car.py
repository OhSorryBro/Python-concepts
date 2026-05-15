"""Class that will be used to present a car"""
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

# class ElectricCar(Car):
#     """It adds characterictics typical to an electric car."""

#     def __init__(self, make, model, year):
#         """Inicialisation of class attributes."""
#         super().__init__(make, model, year)
#         self.battery_size = 40
#         self.battery = Battery()

#     def describe_battery(self):
#         """Printing information about size of the battery."""
#         print(f"This car has {self.battery_size} kWh battery.")

#     def fill_gas_tank(self):
#         """Electric car does not have gas tank."""
#         print(f"This car cannot fill it's gas tank.")

# class Battery:
#     """Simple model of an electric car battery."""
    
#     def __init__(self,battery_size=40):
#         """"""
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """Printing information about battery size."""
#         print(f"This car has battery that is {self.battery_size} kWh.")

#     def get_range(self):
#         """Print actual information about range based on the size of the battery."""
#         if self.battery_size == 40:
#             range = 150
#         elif self.battery_size == 65:
#             range = 225

#         print(f"Range of this car is approx. {range} when the battery is full.")

