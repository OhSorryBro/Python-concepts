# 10.6. Addition. 
# One of the most common problems during numeric data entry is that users provide text instead of numbers. 
# When this type of error occurs, you'll get a ValueError. Write a program that asks the user to enter two numbers, then tries to convert them to int type and displays the result. 
# Catch the ValueError if the data provided is not a number, and display a friendly error message. Test the program by entering first numbers, then text instead of numbers.

# def addition():
#     try:
#         num_1 = int(input("Number 1: "))
#         num_2 = int(input("Number 2: "))
#         print(num_1 + num_2)
#     except ValueError:
#         print("This is a VERY friendly reminder that you must type in numeric value or else.. it will not work.")

# addition()

# 10.7. Addition calculator. 
# Wrap the code from exercise 10.6 in a while loop so the user can continue entering numbers even after an error — display white to allow the user to keep entering numbers instead of text.
# print("=====")
# active = True
# while active:
#     try:
#         num_1 = int(input("Number 1: "))
#         num_2 = int(input("Number 2: "))
#         print(num_1 + num_2)
#     except ValueError:
#         print("This is a VERY friendly reminder that you must type in numeric value or else.. it will not work.")

# 10.8. Cats and dogs. 
# Create two files named cats.txt and dogs.txt. In the first, put at least three cat names; in the second, at least three dog names. 
# Write a program that tries to read the contents of both files and display them on screen. 
# Use try-except to catch all FileNotFoundError errors and display an appropriate error message when a requested file doesn't exist. 
# Move one of the created files to a different directory and confirm the except block works correctly.
# print("=====")
# from pathlib import Path 
# def read_dog_cat():
#     try:
#         filenames = ['dogs.txt', 'cats.txt']
#         for filename in filenames:
#             path =Path(filename)
#             content = path.read_text(encoding='utf-8')
#             contents = content.split()
#             for content in contents:
#                 print(content)
#     except FileNotFoundError:
#         print(f"{path} is not found.")

# read_dog_cat()

# 10.9. Silent cats and dogs. 
# Modify the except block from the previous exercise so that a missing file causes only a silent failure.
# print("=====")
# from pathlib import Path 
# def read_dog_cat():
#     try:
#         filenames = ['dogs.txt', 'cats.txt']
#         for filename in filenames:
#             path =Path(filename)
#             content = path.read_text(encoding='utf-8')
#             contents = content.split()
#             for content in contents:
#                 print(content)
#     except FileNotFoundError:
#         pass

# read_dog_cat()

# 10.10. Most common words. 
# Visit Project Gutenberg (http://www.gutenberg.org/) and choose a few books to analyze. 
# Download the text files or copy plain text from the browser into a text file. Use the count() method to check how many times a given word appears in a string.
#  Write a program that reads the downloaded files and counts how many times the word the appears in each. 
# The result will be approximate since it also counts words containing 'the', e.g. 'them'. Try counting 'the ' (with a space) and see how much smaller the number is.
# I dont want to download books, not needed growth of my github.
print("=====")
from pathlib import Path 
def read_dog_cat():
    try:
        filenames = ['dogs.txt', 'cats.txt']
        for filename in filenames:
            path =Path(filename)
            content = path.read_text(encoding='utf-8')
            contents = content.split()
            number = content.count('the')
            number_2 = content.count('the ')
            for content_2 in contents:
                print(content_2)
            print(f' In {filename} there are {number} of "the" and {number_2} of "the " inside')
            
    except FileNotFoundError:
        pass

read_dog_cat()
