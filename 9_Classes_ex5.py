# 9.13. Die. 
# Create a class called Die with one attribute named sides, with a default value of 6. Create a method called roll_die() that prints a randomly generated number between 1 and the number of sides. 
# Create a six-sided die and simulate rolling it 10 times.
# Then create dice with 10 and 20 sides. Roll each new die 10 times.
import random
class Die():
    def __init__(self,sides = 6):
        self.value = 6
        self.sides = sides
    def roll_die(self):
        self.value = random.randint(1,self.sides)
        print(self.value)
i = 0
die_1 = Die()
die_2 = Die(10)
die_3 = Die(20)
while i < 10:
    i = i + 1
    die_1.roll_die()
print("=====")
i = 0
while i < 10:
    i = i + 1
    die_2.roll_die()
print("=====")
i = 0
while i < 10:
    i = i + 1
    die_3.roll_die()

# 9.14. Lottery. 
# Create a list or tuple containing a series of ten numbers and five letters. 
# Randomly select four numbers or letters from the list, then print a message saying that any ticket containing those matching numbers or letters wins a prize.
print("=====")
result =[]
list_of_data = [10,11,12,13,14,15,16,17,18,19,'a','b','c','d','e']
def roll():
    result =[]
    for _ in range(4):
        list_of_data_to_choose = list_of_data[:]
        choice = random.randint(0,14)
        result.append(list_of_data_to_choose.pop(choice))
    return result
#print(result)
# 9.15. Lottery Analysis. 
# Use a loop to determine how difficult it is to win the lottery you modeled in the previous exercise. Create a list or tuple called my_ticket. 
# Then define a loop that keeps drawing numbers until they match your ticket. Print a message stating how many loop iterations it took before your ticket's numbers came up.
print("=====")
tries = 0
my_ticket =['a', 'b',10,11]
while my_ticket != result:
    tries += 1
    result = roll()
print(f"I took {tries} tries.")


# 9.16. Python Module of the Week. 
# One of the best resources for exploring Python's standard library is the website Python Module of the Week. 
# Go to https://pymotw.com/3/ and browse the table of contents. Find a module that looks interesting and read about it. Also explore the documentation for the random module.
print("=====")



