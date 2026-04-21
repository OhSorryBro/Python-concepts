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


people_for_questionary =['jan','sarah','ed','paul','john1','john2']

fav_languages = {
    'jan': 'python',
    'sarah': 'c',
    'ed': 'rush',
    'paul': 'python',
}
for name in sorted(fav_languages.keys()):
    print(f'{name.title()}, thank you for your answer.')

print('Following programming languages were chosen as answers:')
for language in fav_languages.values():
    print(language.title())
print('===')

# only unique values:
for language in set(fav_languages.values()):
    print(language.title())

# set:
languages = {'python','rust','python','c'}
print(languages)

rivers = {
    'The Nile' : 'Egypt',
    'The Amazon River' : 'Brazil',
    'The Thames' : 'United Kingdom',
}
for key,value in rivers.items():
    print(f'{key.title()} flows thru {value.title()}.')

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)


