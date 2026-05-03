4 % 3
5 % 3
6 % 3
6 % 3

number = input("Type in number, to check either it is even or not: ")
number = int(number)

if number % 2 == 0:
    print(f"\n Number {number} is even")
else:
    print(f"\n Number {number} is not even")


# DO IT YOURSELF
# 7.1. Borrowing a car. Write a program that asks the user which car brand they would like to borrow. Then display the message, for example: "Just a moment, check if the Subaru is available."
print("===")
car = input("Type in car that you are intrested in: ")
print(f"Just a moment, check if {car.title()} is available")


# 7.2. Restaurant table booking. Write a program that asks the customer how many people they want to book a table for. 
# If they answer that the number is greater than 8, you should display a message that the customer needs to wait for a table. Otherwise, inform the customer that the table is ready.
print("===")

table = input("For how many people do you wish to book a table? ")
table = int(table)
if table > 8:
    print("Please wait for a moment.")
else:
    print("Your table is ready")


# 7.3. Multiples of ten. Ask the user to enter any number, then check if it is a multiple of 10.
print("===")
number_2 = input("Please enter number: ")
number_2 = int(number_2)
if number_2 % 10 == 0:
    print("Yes")
else:
    print("No")