person = {'first_name':'Tonny','last_name':'Spark','Age':109,'city':'Amsterdam'}
print(person)

fav_numbers = {'Tonny':109,'James':9,'Marion':3,"Mike":69,'John':13}
print(fav_numbers)

glossary = {'list':'is structure that contains structurized data','integer':' is a numeric value','If statement':'is an evaluated expression that result in true or false','Loop':'is logica that iterate thru list','Dictionary':
'is a solution that make possible combining of key and value'}
for key, value in glossary.items():
    print(f'{key}: \n{value}')