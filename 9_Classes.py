class Dog:
    """Simple model of dog"""
    def __init__(self, name,age):
        """Inicialisation of attributes name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulation that god sits after receiving an order"""
        print(f"{self.name.title()} sits now.")

    def roll_over(self):
        """Simulation that dog ley on the back after receiving an order"""
        print(f"{self.name.title()} now lay on the back")

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 5)
print(f"My dog's name is {my_dog.name.title()}.")
print(f"{my_dog.name.title()} is {my_dog.age} year old")
my_dog.sit()
my_dog.roll_over()

print(f"Your dog's name is {your_dog.name.title()}.")
print(f"{your_dog.name.title()} is {your_dog.age} year old")
your_dog.sit()