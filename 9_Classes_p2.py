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
    
my_new_car = Car('audi','a4', 2025)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()