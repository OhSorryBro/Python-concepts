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