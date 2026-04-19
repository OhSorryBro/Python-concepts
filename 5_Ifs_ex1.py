car='Subaru'
print("Is car =='subaru'? I guess its true")
print(car=='Subaru')
print("Is car == 'audi'? I guess its false")
print(car=='audi')
car=='subaru'
car.lower()=='subaru'.lower()
26 == 26
26 == 27
26>27
22 and 23 < 30
22 or 23 >22
numbers=range(0,10)
10 in numbers
11 not in numbers

age=19
if age>=18:
    print(f'You can vote.')
    print('Did you already registered so you will be able to vote?')
else:
    print("Sorry you are too young to be able to vote")
    print("You can register when you are at least 18")

age=12
if age<4:
    print("Ticket price is 0")
elif age<18:
    print("Ticket price is 25")
else:
    print("Ticket price is 40")

if age<4:
    price = 0
elif age<18:
    price = 25
elif age<65:
    price =40
else:
    price =20

print(f'Ticket price is {price}')

requested_toppings =['muschrooms','double cheese']
if 'muschrooms' in requested_toppings:
    print("Adding muschrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni")
if 'double cheese' in requested_toppings:
    print("Adding double cheese")
print("Pizza is ready!")
print('=================')

available_toppings =['mushrooms','olive','bacon','pepperoni','pineapple','double cheese']

requested_toppings =['mushrooms','bacon','double cheese','fries']
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f'Adding {requested_topping}.')
        else:
            print(f'We do not have an option to add {requested_topping}.')
else:
    print('Are you sure that you wish to order pizza without any toppings?')

print("\nYour pizza is ready")

