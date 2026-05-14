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
    
my_new_car = Car('audi','a4', 2025)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(30)
my_new_car.read_odometer()
my_new_car.update_odometer(3)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()