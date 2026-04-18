cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

car='Audi'
car.lower()=='audi'

requested_topping ='muschrooms'
if requested_topping !='muschroms':
    print('Woops! Something went wrong.')

age=18
print(age==18)

answer = 17
if answer !=42:
    print('That is not an correct answer!')
if answer <42:
    print('That is not an correct answer!')
if answer >42:
    print('That is not an correct answer!')

age_0= 22
age_1= 18
age_0>= 21 and age_1>= 21
age_0>= 21 or age_1>= 21
age_1= 22
age_0>= 21 and age_1>= 21

requested_toppings=['p','o','a']
'p' in requested_toppings
'pepperoni' in requested_toppings

banned_users =['Andrew','Caroline','David']
user='Maria'
if user not in banned_users:
    print(f'{user.title()}, you can reply, if you dare.')

