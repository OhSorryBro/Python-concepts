from name_function import get_formatted_name

print("Type in 'q' to finish.")
while True:
    first = input("\n Type in first name: ")
    if first =='q':
        break
    last = input("\n Type in last name: ")
    if last =='q':
        break

    formatted_name = get_formatted_name(first,last)
    print(f"\t Nicely formatted full name is: {formatted_name}.")

