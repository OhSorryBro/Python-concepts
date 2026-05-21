# 10.11. Favorite Number
# Create a program that asks the user for their favorite number. Use json.dumps() to save that number to a file. 
# Then write a separate program that reads the favorite number back and displays a message in the style: "I know your favorite number! It's ___."
from pathlib import Path
import json

path = Path('fav_number.json')
def fav_number_asker(path):
    fav_number = input("Type in your favourite number: ")
    content = json.dumps(fav_number)
    path.write_text(content)

def fav_number_reader(path):
    content = path.read_text()
    fav_number = json.loads(content)
    print(f"I know your favorite number! It's {fav_number}")

# fav_number_asker(path)
# fav_number_reader(path)

# 10.12. Remembered Favorite Number
# Both programs combined into one file. When you run the exercise, it connects the favorite number with the user. 
# If the favorite number saved by the previous program exists, display it to the user and ask them to confirm it's correct, then save it to the file. If it doesn't exist, ask the user for their favorite number and save it to the file. 
# Make sure it works correctly.
print("=====")

def fav_number(path):
    if path.exists():
        content = path.read_text()
        fav_number = json.loads(content)
        print(f"{fav_number} is your fav number.")
    else:
        content = input(f"Please type in your fav number: ")
        content_json = json.dumps(content)
        path.write_text(content_json)

fav_number(path)

# 10.13. User Dictionary
# Write a program remember_me.py that stores only one piece of information — the username. Expand it to include two more pieces of information about the user. 
# Then request all that data using json.loads(), save the dictionary to a file, and later read it back using json.loads(). The program should then display a summary of the data about the user.
print("=====")



# 10.14. User Verification
# In the latest version of remember_me.py, it's assumed that the user has already provided their name, or that the program is being run for the first time. Modify the program to handle the case where the current user is not the person who last used it.
# In the greet_user() function, before greeting the existing user with an appropriate message, ask them whether the name on file is correct. If it isn't, call get_new_username() to obtain the correct name.
print("=====")


