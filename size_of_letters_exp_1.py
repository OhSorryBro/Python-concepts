# personal welcome.
name = "JoHn"
print(f"Hello {name}, welcome to Python Crash Course!")
print(f"Hello {name.title()}, welcome to Python Crash Course!")
print(f"Hello {name.upper()}, welcome to Python Crash Course!")
print(f"Hello {name.lower()}, welcome to Python Crash Course!")

# Find quote, name and format is name, said: "quote."
name = "elon musk"
quote = "Constantly seek criticism. A well thought out critique of whatever you’re doing is as valuable as gold."

print(f'{name.title()} has said:"{quote}"')

# Removing white spaces
name = "\telon musk\t\n"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# Sufixes & Prefixes removal

file_name = "size_of_letters_exp_1.py"
print(fileName.removesuffix(".py"))
print(fileName.removeprefix("size_of_letters_"))