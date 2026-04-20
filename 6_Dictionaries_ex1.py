user_0 = {
    'username':'jkowalski',
    'first':'jan',
    'last':'kowalski',
}

for key, value in user_0.items():
    print(f'\nKey: {key}')
    print(f'Value: {value}')

fav_languages = {
    'jan':'python',
    'sarah':'c',
    'edward':'rust',
    'paul':'python',
}

for name, language in fav_languages.items():
    print(f'Favourite programming language user {name.title()} is {language.title()}.')

for name in fav_languages.keys():
    print(name.title())

friends = ['paul','sarah']
for name in fav_languages.keys():
    print(f'Welcome, {name.title()}.')

    if name in friends:
        language = fav_languages[name].title()
        print(f'\tWelcome, {name.title()}! I know that your favourite programming language is {language}.')

if 'el' not in fav_languages.keys():
    print('El, please fill up our questionary')