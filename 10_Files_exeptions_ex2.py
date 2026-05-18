# 10.4. Guest – 
# Create a program that asks the user for their name. When the user provides it, write the name to a file called guest.txt.

from pathlib import Path
print("Please type in your name:")
answer = input()
path = Path('guest.txt')
path.write_text(answer)

# 10.5. Guest book – 
# Create a while loop in which each user will be asked to provide their name. 
# When the user provides it, display a greeting on screen, and add a line to a file called guest_book.txt. Make sure that each entry is written on a new line in the file.
active = True
path = Path('guest_book.txt')
answers =''
while active:
    print("To exit type in 'e'. Please type in your name:")
    answer = input()
    if answer != 'e':
        answers += (answer)
        answers += ('\n')
    else:
        active = False
print(answers)
path.write_text(answers)