message = (input("Tell me something about yourself. I will print it at your screen."))
print(message)

name = input("Please type in your name: ")
print(f"Hello, {name}")

prompt = "If you tell us, who are you, we will personalise what you see on the screen."
prompt +="\n What is your name? "
name = input(prompt)
print(f"\n Welcome, {name}.")

age = input("How old are you? ")
print(age)
age = int(age) 
print(age >= 18)

height = input(" How tall in cm are you? ")
height = int(height)

if height>= 90:
    print("\n You are tall enough for a ride!")
else:
    print("\n You can ride, when you grow up a little")