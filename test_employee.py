from Tests_ex2 import Employee
import pytest

@pytest.fixture
def employee():
    employee = Employee('Tonny', "Bobo", 2000)
    return employee

def test_give_default_raise(employee):
    new_salary = employee.give_raise()
    assert new_salary == 7000
    
def test_give_custom_raise(employee):
    new_salary = employee.give_raise(2000)
    assert new_salary == 4000