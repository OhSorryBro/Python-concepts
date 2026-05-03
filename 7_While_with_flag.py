prompt = "Type in city names, which you wish to visit:"
prompt += "\n When you are finished, type 'End'\t"

while True:
    city = input(prompt)

    if city == 'End':
        break
    else:
        print(f"I would like to visit {city.title()}!")