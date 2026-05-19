print("Type in two numbers that will be divided.")
print("Type in 'q' to end.")

while True:
    first_number = input("\n First number: ")
    if first_number == 'q':
        break
    second_number = input("\n Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
