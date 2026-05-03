current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = "\n Tell mi something about you, and I will print it on the screen:"
prompt += "\n Type in 'End', to close this program:  "
active = True
message = ""
while active:
    message = input(prompt)
    if message == 'End':
        active = False
    else:
        print(message)

