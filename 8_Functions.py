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

