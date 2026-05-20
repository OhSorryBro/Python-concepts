from pathlib import Path
import json

path = Path('username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:    
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"Your name is saved and will be used later. {username}.")