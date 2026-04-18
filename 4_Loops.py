magicians = ['alice', 'david', 'caroline']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(f'{magician.title()}, that was an awesome magic spectatle!')
    print(f'We are waiting for your next magic spectatle, dear {magician.title()}.\n')

print('Thank you everyone. That was a trully amazing expirience!')

pizza =['a','b','c']
for pizza in pizza:
    print(f' I like eating {pizza}')
print('I really love pizza a because its first in the alphabet. Pizza b is my least favourite because beeing 2nd is the worst place. Pizza c is third pizza, it is nice to stand on the podium')
print("I do absolutly love pizza!")
mammals=['gepard','Donkey','monkey']
for mammal in mammals:
    print(f'{mammal.title()} is a very useful animal')

print('All mentioned animals are simply wonderful!')

for value in range(1,5):
    print (value)

for value in range(1,6):
    print(value)

numbers =list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)
squares =[]
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

for value in range(1,11):
    squares.append(value**2)

print(f'short {squares}')
print(min(squares))
print(max(squares))
print(sum(squares))

squares =[value**2 for value in range(1,11)]
print(squares)