# 7.4. Pizza toppings. Create an infinite loop that asks the user to enter a series of pizza toppings. The loop should terminate when the word 'end' is entered. As the user keeps entering toppings, 
# the loop should display a message confirming that the given ingredient has been added to the pizza.
print("To finish adding toppings, Type in 'end'")
toppings =[]
active = True
while active:
    topping = input("Please type in the topping: ")
    if topping == 'end':
        break
    else:
        toppings.append(topping)
        print(f"We added {topping}")

print(toppings)

# 7.5. Cinema tickets. The price of a cinema ticket depends on the viewer's age. If the viewer is under 3 years old, the ticket is free. For children aged 3 to 12, the ticket costs 10 PLN. 
# For people over 12, the ticket price is 15 PLN. Create a loop that asks the user for their age, then displays a message with the correct ticket price based on the input.
print("====")
active = True
while active:
    age = input("Please type in how old are you: \t")
    age = int(age)
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15
    print(f"Your ticket price is {price}")
    

# 7.6. Three exits. Prepare three different versions of exercise 7.4 or 7.5, each of which will perform the following tasks at least once:
# Using a conditional test in a while loop to stop its execution.
print("====")
topping = input("Topping: ")
while topping != 'end':   
    toppings.append(topping)
    print(f"We added {topping}")
    topping = input("Topping: ")

print(toppings)

print("====")
active = True
print("To finish adding toppings, Type in 'end'")
while active:
    age = input("Please type in how old are you: \t")
    if age == 'end':
        break
    age = int(age)
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15
    print(f"Your ticket price is {price}")
    

# Using an active variable to control how long the while loop runs.
print("====")
print("To finish adding toppings, Type in 'end'")
toppings =[]
active = True
while active:
    topping = input("Please type in the topping: ")
    if topping == 'end':
        active = False
    if len(toppings) > 5:
        active = False
    else:
        toppings.append(topping)
        print(f"We added {topping}")

print(toppings)

print("====")

active = True
print("To finish adding toppings, Type in 'end'")
viewers = 0
while active and viewers < 5:
    age = input("Please type in how old are you: \t")
    if age == 'end':
        break
    age = int(age)
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15
    viewers += 1
    print(f"Your ticket price is {price}")
    

# Using a break statement to exit the loop when the user types 'end'.
print("====")
active = True
print("To finish adding toppings, Type in 'end'")
while active:
    age = input("Please type in how old are you: \t")
    if age == 'end':
        break
    age = int(age)
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15
    print(f"Your ticket price is {price}")
    

print("====")

active = True
while active:
    age = input("Please type in how old are you: \t")
    if age == 'end':
        break
    age = int(age)
    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15
    print(f"Your ticket price is {price}")

# 7. Infinity. Create an infinite loop and run it. (To stop the loop, press Ctrl+C or close the terminal window displaying the program's output.)
print("====")
while True:
    print("This runs forever")
