from pathlib import Path
import json

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:    
        return None
    
def get_stored_age(path_age):
    if path_age.exists():
        contents = path_age.read_text()
        age = json.loads(contents)
        return age
    else:
        return None
    
def get_new_username(path):
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def get_new_age(path_age):
    age = input("What is your age? ")
    contents = json.dumps(age)
    path_age.write_text(contents)
    return age

def greet_user():
    path = Path('username.json')
    path_age = Path('user_age.json')
    username = get_stored_username(path)
    age = get_stored_age(path_age)
    if username and age:
        print(f"Welcome back, {username}! You are {age} years old.")
    elif username:          # jest username, brak age
        age = get_new_age(path_age)
        print(f"Age saved. Hello {username}, you are {age}.")
    elif age:               # jest age, brak username
        username = get_new_username(path)
        print(f"Name saved. Welcome {username}.")
    else:                   # nic nie ma
        username = get_new_username(path)
        age = get_new_age(path_age)
        print(f"Welcome {username}, age {age} saved.")

greet_user()