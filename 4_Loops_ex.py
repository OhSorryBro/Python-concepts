to20 =[]
for number in range(1,21):
    print(number)
numbers_to_milion = list(range(1,1_000_001))
#for number in numbers_to_milion:
#    print(number)
min_check =min(numbers_to_milion)
max_check =max(numbers_to_milion)
sum_check =sum(numbers_to_milion)
print(sum_check)
non_even_numbers =list(range(1,21,2))
for number in non_even_numbers:
    print(number)

weird_list = [value**2 for value in range(3,30)]
for v in weird_list:
    print(v)

to_power_3 = [value**3 for value in range(1,11)]
for n in to_power_3:
    print(n)

players =['Carol', 'Martyna','Mike','Flower','Ell']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print("Here are tree first players at our team")
for player in players[:3]:
    print(player.title())

my_foods =['pizza','falafel','carrot cake']
friend_foods =my_foods[:]
print(f"My favourite dishes are:{my_foods}")

print(f"\nMy friend's favourite dishes are:{friend_foods}")
my_foods.append('cannolo')
friend_foods.append('Ice cream')
print(f"My favourite dishes are:{my_foods}")

print(f"\nMy friend's favourite dishes are:{friend_foods}")

my_foods = friend_foods
print(my_foods)

