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


person = {'first_name':'Tonny','last_name':'Spark','Age':109,'city':'Amsterdam'}
person_1 = {'first_name':'Johny','last_name':'Bark','Age':10,'city':'Bravia'}
person_2 = {'first_name':'Bro','last_name':'Talk','Age':69,'city':'Lenovo'}

print('=====')
#6.7
#People. Start with the program created in exercise 6.1. 
#Create two new dictionaries representing different people, and then place all three dictionaries in a list called people. 
#Iterate through the list and display information about each person.
people = [person, person_1, person_2]

for person_from_people in people:
    print(f'{person_from_people['first_name'].title()} {person_from_people['last_name'].title()} lives in {person_from_people['city'].title()} and is {person_from_people['Age']} years old.')


#6.8
# Pets. Create several dictionaries and give them names of animals. In each dictionary, store information about the pets, including the owner
# Then place these dictionaries in a list called pets. Iterate through the list and display all information about each pet.




#6.9
# Favorite places. Create a dictionary called favorite_places. Think of three names and use them as the dictionary keys. Assign each person three favorite places.
# To make the exercise more interesting, you can ask some friends to give their favorite places. Iterate through the dictionary and display the names of all people along with their favorite places.



#6.10
# Favorite numbers. Modify the program created in exercise 6.2 from the previous chapter. Now each person can have more than just one favorite number. 
# Display all people along with their favorite numbers.