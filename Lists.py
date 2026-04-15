bicycles = ["trekking", "mountain-bike" ,"mike's Bike"]
print (bicycles)
#for each bicycle in bicycles
#    print bicycle
print (bicycles[1])
print (bicycles[0].title())
#So if we want to take 1st and 3rd we have to print:
print(bicycles[0].title())
print(bicycles[2].title())
#printing last object of the list
print(f" Thief's favourite bicycle is the {bicycles[-1].title()}")
names =['adam','szymon','john']
print(names[0].title())
print(names[1].title())
print(names[-1].title())
grettings='Hello in hell dear '
print(grettings,names[0].title())
print(grettings,names[1].title())
print(grettings,names[2].title())
#Modyfing the list
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)

motorcycles2 = []
motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')
print(motorcycles2)
motorcycles2.insert(0,'ducati')
print(motorcycles2)

#removing from list
del motorcycles2[0]
print(motorcycles2)
del motorcycles2[1]
print(motorcycles2)
popped_motorcycle = motorcycles2.pop()
print('xx')
print(popped_motorcycle)
print(motorcycles2)
last_bought = motorcycles2.copy()
last_bought_popped = last_bought.pop()
print(f'last bought list popped is: {last_bought_popped}')
print(f'last bought list is: {last_bought}')
print(f'motorcycles2 list is: {motorcycles2}')
letters = ['a','b','c','d']
print(letters)
letters.pop(2)
print(letters)
letters.remove('b')
print(letters)

motorcycles3 = ['honda','yamaha','suzuki','ducati']
print(motorcycles3)
too_expensive = 'ducati'
motorcycles3.remove(too_expensive)
print(motorcycles3)
print(f' Bike {too_expensive} is too expensive do keep it on the list.')