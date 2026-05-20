# 10.6. Addition. 
# One of the most common problems during numeric data entry is that users provide text instead of numbers. 
# When this type of error occurs, you'll get a ValueError. Write a program that asks the user to enter two numbers, then tries to convert them to int type and displays the result. 
# Catch the ValueError if the data provided is not a number, and display a friendly error message. Test the program by entering first numbers, then text instead of numbers.



# 10.7. Addition calculator. 
# Wrap the code from exercise 10.6 in a while loop so the user can continue entering numbers even after an error — display white to allow the user to keep entering numbers instead of text.
print("=====")


# 10.8. Cats and dogs. 
# Create two files named cats.txt and dogs.txt. In the first, put at least three cat names; in the second, at least three dog names. 
# Write a program that tries to read the contents of both files and display them on screen. 
# Use try-except to catch all FileNotFoundError errors and display an appropriate error message when a requested file doesn't exist. 
# Move one of the created files to a different directory and confirm the except block works correctly.
print("=====")


# 10.9. Silent cats and dogs. 
# Modify the except block from the previous exercise so that a missing file causes only a silent failure.
print("=====")


# 10.10. Most common words. 
# Visit Project Gutenberg (http://www.gutenberg.org/) and choose a few books to analyze. 
# Download the text files or copy plain text from the browser into a text file. Use the count() method to check how many times a given word appears in a string.
#  Write a program that reads the downloaded files and counts how many times the word the appears in each. 
# The result will be approximate since it also counts words containing 'the', e.g. 'them'. Try counting 'the ' (with a space) and see how much smaller the number is.
print("=====")

