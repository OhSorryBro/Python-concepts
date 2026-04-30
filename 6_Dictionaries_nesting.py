alien_0 = {'color':'green', 'points':'5'}
alien_1 = {'color':'yellow', 'points':'10'}
alien_2 = {'color':'red', 'points':'15'}

aliens = [alien_0, alien_1,alien_2]

for alien in aliens:
    print(alien)

print('===\n')

aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','points':5, 'speed':'slow'}
    aliens.append(new_alien)

print("First 5 aliens are:")
for alien in aliens[:5]:
    print(alien)

print(f"\nNumber of all aliens: {len(aliens)}")
print('\n===')
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien ['color'] = 'yellow'
        alien ['speed'] = 'medium'
        alien ['points'] = 10
    elif alien['color'] == 'yellow':
        alien ['color'] = 'red'
        alien ['speed'] = 'fast'
        alien ['points'] = 15

for alien in aliens [:5]:
    print(alien)

print('\n===')

pizza = {'crust':'thick',
         'toppings':['mushrooms', 'double cheese'],
         }
print(f'You ordered pizza on {pizza["crust"]} crust with following toppings:')
for topping in pizza['toppings']:
    print(f'\t *{topping}')
print('\n===')

favorite_languages = {
    'jan':['python', 'rust'],
    'sarah':['c'],
    'ed':['rust', 'go'],
    'paul':['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f'{name.title()} likes only {languages[0].title()}')
    else:
        print(f'Favorite programming languages of user {name.title()} are:')
        for language in languages:
            print(f'\t{language.title()}')

users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
    },
    'mcurie':{
        'first':'maria',
        'last':'skłodowska-curie',
        'location':'parice'
    }
}

for username, user_info in users.items():
    print(f'\n User name: {username}')
    full_name = f'{user_info['first']} {user_info['last']}'
    location = user_info['location']

    print(f'\t Full name: {full_name.title()}')
    print(f'\t City: {location.title()}')