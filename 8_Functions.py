def greet_user(username):
    """Shows simple greeting"""
    print(f"Hello, {username.title()}!")

greet_user('dudu')

# 8.1 – Message
# Create a function named display_messages() that prints one sentence about what you'll learn in this chapter. Call it and make sure the message is displayed correctly.
print("=====")
def display_messages():
    print("Functions are very useful pieces of program, they can ensure that code is re-used.")

display_messages()

# 8.2 – Favorite book
# Create a function named favorite_book() that accepts one parameter title. It should print a message like "One of my favorite books is Alice in Wonderland". Call the function and make sure you pass the book title as an argument.
print("=====")
title = "Alice in Wonderland"
def favourite_book(title):
    print(f"One of my favorite books is {title}")

favourite_book(title)


print("=====")

def describe_pet(pet_name, animal_type ='dog'):
    """Show's information about animal"""
    print(f"\n My animal is {animal_type}.")
    print(f"My {animal_type} has name {pet_name.title()}.")

describe_pet('hamster',"harry")
describe_pet('dog','woffie')
describe_pet('woffie','dog')

describe_pet(animal_type ='hamster', pet_name="harry_v2_Turbo_bob")
describe_pet('bobo')
describe_pet('bobo', 'cat')


# 8.3. T-shirt. Create a function called make_shirt() that accepts a shirt size and the text to be printed on it. The function should print a simple sentence containing information about the ordered shirt: 
# its size and the text to be printed on it.
# DO IT YOURSELF
# During the first function call, prepare the function's arguments positionally. During the second call, use keyword arguments.
print("======")
def make_shirt(shirt_size,text):
    print(f"Shirt size will be: {shirt_size} and text printed on it will be: {text}")

make_shirt("XL",'Dodo is the best')
make_shirt(shirt_size = "XS", text = "This one is for my gf.")

# 8.4. Large shirts. 
# Modify the make_shirt() function so that by default it would produce a large shirt with the text "I love Python" printed on it. 
# Create shirts of various sizes with a large and medium printed text (both with the default text) and with a different text printed on it.
print("======")
def make_shirt(shirt_size = "large", text =" I love Python"):
    print(f"Shirt size will be: {shirt_size} and text on it will be: {text}")

make_shirt("medium")
make_shirt("large")
make_shirt(text = 'Dudu')


# 8.5. Cities. 
# Create a function called describe_city() that accepts the name of a city and a country. The function should display a simple sentence such as "Warsaw is located in Poland". 
# Give the function a parameter that stores the country name, with a default value set to a country of your choice. Call the function for three different cities, at least one of which should not be located in the default country.
print("======")


def describe_city(city_name, country ='Poland'):
    print(f"{city_name.title()} is located in {country}")
describe_city('warsaw')
describe_city('XAXA')
describe_city("New York", "USA")


def get_formatted_name(first_name, last_name):
    """Returns formatted first and last name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


def get_formatted_name(first_name, last_name, middle_name =''):
    """Returns formatted first and last name"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('jimi','hendrix', 'lee')
print(musician)


def build_person (first_name, last_name):
    '''Returns dictionary with information about person'''
    person ={'first': first_name, 'last' : last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)


def build_person (first_name, last_name, age =None):
    '''Returns dictionary with information about person'''
    person ={'first': first_name, 'last' : last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

musician = build_person('Bobo', 'Dodo', 27)
print(musician)

def get_formatted_name(first_name, last_name):
    """Returns formatted full name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\n Please type in your first and last name.")
    print("Type in 'q' to end")
    f_name = input("Name: ")
    if f_name == 'q':
        break
    l_name = input("Surname:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Welcome, {formatted_name}")