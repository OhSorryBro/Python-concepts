users = ["Admin","user1","user2","USER3","user4"]
if users:
    for user in users:
        if user == 'Admin':
            print("Hello, another day at work huh? Do you wish to see today's raport?")
        else:
            print(f"Hello,{user}. Thank you for logging in.")
else:
    print('We need to find some users.')

users=[]
if users:
    for user in users:
        if user == 'Admin':
            print("Hello, another day at work huh? Do you wish to see today's raport?")
        else:
            print(f"Hello,  {user}. Thank you for logging in.")
else:
    print('We need to find some users.')

current_users = ["user1","user2","USER3","user4","user5"]
new_users = ["user1","user6"]
current_users_lowered = [ user.lower() for user in current_users]

for user in new_users:
    if user in current_users_lowered:
        print(f'Chosen username "{user}" is already in user. Plese try another one.')
    else:
        print(f'Chosen username "{user}" is available.')

numbers=range(1,10)
for number in numbers:
    if number == 1:
        print(f"\n{number}st")
    elif number == 2:
        print(f"\n{number}nd")
    elif number == 3:
        print(f"\n{number}rd")
    else:
        print(f"\n{number}th")
        
