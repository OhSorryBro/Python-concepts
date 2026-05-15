from car import Car
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

