places = ['britain','arizona','chicago','downtown','edenburg']
print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

print('===========')

places = ['britain','arizona','chicago','downtown','edenburg']
print(places)
#insert
places.insert(3,'winrar')

print(places)
#append
places.append('zip')

print(places)
#del
del places[3]
print(places)
#pop
places.pop(-1)

print(places)
#remove
places.remove('edenburg')

print(places)
#sort
places.sort()

print(places)
#reverse
places.reverse()

print(places)
#len
ammount = len(places)
print(ammount)
