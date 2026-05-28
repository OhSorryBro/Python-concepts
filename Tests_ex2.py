# 11.3. Employee
# Prepare a class called Employee. The __init__() method should accept a first name, last name, and annual salary, then store this information as attributes. 
# Create a method called give_raise() that increases the salary by 5000 by default, but also accepts a different amount.
# Prepare a test file for the Employee class. Create two test functions: test_give_default_raise() and test_give_custom_raise(). 
# Start by writing tests that don't use fixtures and make sure they pass. Then prepare test data using a fixture to avoid having to create a new Employee instance in each test function. 
# Run the tests again and make sure both pass.

class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name 
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount = 5000):
        self.annual_salary = self.annual_salary + amount
        return self.annual_salary
