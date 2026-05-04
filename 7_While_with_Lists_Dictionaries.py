unconfirmed_users = ['alice', 'bart', 'catherine']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verification of user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\n Following users are verified: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'cat', 'dog','fish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

responses = {}

polling_active = True
while polling_active:
    name = input(f'\n What is your name? ')
    response = input('Where do you wish to go? ')

    responses[name] = response

    repeat = input('Does anyone wish to join the polling? (yes/no) ')

    if repeat == 'no':
        polling_active = False

print('\n Results are:')
for name, response in responses.items():
    print(f'{name} wish to go to {response}.')