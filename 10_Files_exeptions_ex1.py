# 10.1. Getting to Know Python. 
# Open a text editor, create an empty file and type a few sentences summarizing what you've learned about Python so far. 
# Start each line with the phrase "In Python you can...". Save the file as learning_python.txt in the same directory. Write a program that reads the file and displays its contents. 
# Display the contents of the file once through reading the entire file, and once by iterating through the list using a loop.
import pathlib
path = pathlib.Path("learning_python.txt")
content =''
contents = path.read_text()
to_read = contents.splitlines()
for line in to_read:
    content += line
    print(line)
print('---')
print(content)
print(contents)

# 10.2. Getting to Know C. 
# The replace() method can be used to replace any free-form word in a text string with a completely different word. Here's a short example showing how the word dog can be replaced with the word cat:
#  message = "My favorite animal is dog."
# >>> message.replace('dog', 'cat')
# 'My favorite animal is dog.'
# Read each line of the previously created learning_python.txt file, 
# then replace every occurrence of the word Python with the name of another programming language, such as C. Display each modified line on screen.
print("=====")
path = pathlib.Path("learning_python.txt")
contents = path.read_text()
to_read = contents.splitlines()
result =''
for line in to_read:
    line = line.replace('Python','C')
    result += line
    result += '\n'
print(result)
# 10.3. Simpler code. 
# The file_reader.py program introduced in this section uses a temporary variable lines, then iterates through it using splitlines(). 
# You can skip this temporary variable and iterate directly over the list returned by splitlines():
# pythonfor line in contents.splitlines():
# Remove the temporary variable from all programs in these sections to make them more concise.
print("=====")


path = pathlib.Path('pi_million_digits.txt')
contents = path.read_text().rstrip()
print(contents)
path_example = pathlib.Path('text_files/name_of_the_file.txt')

contents = path.read_text()
pi_string=''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))
birthday = input("Type in your birthday date in format ddmmyy\t")
if birthday in pi_string:
    print("Your birthday is in pi")
else:
    print("At an available window with data, your birthday was not located.")

