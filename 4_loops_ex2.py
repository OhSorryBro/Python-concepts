my_foods =['pizza','falafel','carrot cake','ice cream','potato mash']
print(f'First tree elements of the list are:{my_foods[:3]}')
print(f'Middle tree elements of the list are:{my_foods[1:4]}')
print(f'Last tree elements of the list are:{my_foods[-3:]}')
pizza =['a','b','c']
friends_pizza = pizza[:]
pizza.insert(0,'0')
friends_pizza.insert(-1,'d')
print(f"My favourite pizza's are:")
for pizza in pizza:
    print(pizza)
print("My friend's favourite pizza's are:")
for pizza_1 in friends_pizza:
    print(pizza_1)

dimensions =(200,50)
print("Starting x and y are:")
print(dimensions[0])
print(dimensions[1])
my_t =(3,)
dimensions =(400,100)
print("New dimensions are:")
for dimension in dimensions:
    print(dimension)

boufet =("Hot-dog","Curry","Pizza","Meatballs","Eggballs")
for food in boufet:
    print(food)
boufet =["Hotto-doggo","Curry","Pizza-lavista","Meatballs","Eggballs"]
for food in boufet:
    print(food)