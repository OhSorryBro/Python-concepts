# TRY IT YOURSELF
# 8.12. Sandwiches. 
# Write a function that accepts a list of items a customer wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that's being ordered. 
# Call the function three times, using a different number of arguments each time.
def make_sandwich(*items):
    print(f"Preparing sandwich with {items}")

make_sandwich("Onion")
make_sandwich("Onion","butter")
make_sandwich("Onion","butter",'jam')
# 8.13. User Profile. 
# Start with a copy of the user_profile.py program from earlier in this chapter. 
# Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.
print("=====")

def build_profile (first, last, **user_info):
    """Building dictionary containing all user information."""
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

build_profile('Dodo','Bobo',Age = 12,Status = 'Yelly', Color = 'Green')
build_profile('Mr. Evil','From Saint house',Group = 'Crazy', Status = 'Unknown', Color = 'Unknown')
build_profile("Rachet", "Silverhand", Age = 639, Status = "Dead", Color = "Rotten-white")
# 8.14. Cars. 
# Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. 
# It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. 
# Your function should work for a call like this one:
# pythoncar = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that's returned to make sure all the information was stored correctly.
print("=====")

def make_car(manufacturer, model, **kwargs):
    """Building dictionary containing all car information"""
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

pythoncar_1 = make_car('subaru', 'outback', color='blue', tow_package=True)
print(pythoncar_1)
