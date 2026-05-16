from pathlib import Path
import math

path = Path('pi_million_digits.txt')
contents = path.read_text().rstrip()
print(contents)
path_example = Path('text_files/name_of_the_file.txt')

contents = path.read_text()
lines = contents.splitlines()
pi_string=''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))
birthday = input("Type in your birthday date in format ddmmyy\t")
if birthday in pi_string:
    print("Your birthday is in pi")
else:
    print("At an available window with data, your birthday was not located.")

