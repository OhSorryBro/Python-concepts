person = {'first_name':'Tonny','last_name':'Spark','Age':109,'city':'Amsterdam'}
print(person)

fav_numbers = {'Tonny':109,'James':9,'Marion':3,"Mike":69,'John':13}
print(fav_numbers)

glossary = {'list':'is structure that contains structurized data','integer':' is a numeric value','If statement':'is an evaluated expression that result in true or false','Loop':'is logica that iterate thru list','Dictionary':
'is a solution that make possible combining of key and value'}
for key, value in glossary.items():
    print(f'{key}: \n{value}')
    
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
