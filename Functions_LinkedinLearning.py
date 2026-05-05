def bark():
    print("Woof woof!")
    print("I am a dog..")

for x in range(3):
    bark()

def hello(name):
    print(f"Hello {name}!")

hello("sarah")

def add_numbers(num1,num2):
    print(num1+ num2)

add_numbers(1,2)
add_numbers(3,7)

def dog_info(age,name):
    print(f"This dog is {age} and it's named: {name}")

dog_info(3,"bark")


def double(number):
    return number * 2
new_number = double(5)
print(new_number)


def upper(string):
    return string.upper()
new_upper = upper("dudu yeah")
print(new_upper)

names = ['a', 'b', 'c']
for name in names:
    print(upper(name))