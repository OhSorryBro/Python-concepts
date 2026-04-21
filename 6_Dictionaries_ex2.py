languages = {'python','rust','python','c'}

fav_languages = {
    'jan': 'python',
    'sarah': 'c',
    'ed': 'rush',
    'paul': 'python',
}

people_for_questionary =['jan','sarah','ed','paul','john1','john2']

# Task iterate thru people_for_questionary if person has already answered and is in fav_languages. 
# Print thank you for answer. if key is not found, print request to join the questionary
print('===')
for person in people_for_questionary:
    if person in fav_languages.keys():
        print(f'Thank you for your answer {person.title()}')
    else:
        print(f'{person.title()}, please answer our questions')